from django.db import models

class AbstractDateTimeModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract=True 



class Task(AbstractDateTimeModel):
    assigned = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name = 'assigned', null=True)
    created_by = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name = 'created_by')
    description = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    money = models.DecimalField(max_digits=7, decimal_places=2, default=0)

    def __str__(self):
        return self.title


class MoneyLog(AbstractDateTimeModel):
    user = models.ForeignKey('users.User',on_delete=models.CASCADE)
    reason = models.CharField(max_length=255)
    debit = models.DecimalField(decimal_places=2,max_digits=7, default =0)
    credit = models.DecimalField(decimal_places=2,max_digits=7, default =0)
    money = models.DecimalField(decimal_places=2,max_digits=7, default =0)
    balance = models.DecimalField(decimal_places=2,max_digits=7, default =0)
    task = models.ForeignKey(Task,on_delete=models.CASCADE, default=None, null=True)


class TaskExpense(AbstractDateTimeModel):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    executor = models.ForeignKey('users.User', on_delete=models.CASCADE)
    money = models.DecimalField(max_digits=7, decimal_places=2)
