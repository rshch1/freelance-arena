from rest_framework.routers import DefaultRouter 
from .views import ExecutorViewSet, CustomerViewSet, TaskViewSet, RegisterUsersView, UserLoginView
from django.urls import path, include


router = DefaultRouter()
router.register('executors', ExecutorViewSet, 'executors' )
router.register('customers', CustomerViewSet, 'customers' )
router.register('tasks', TaskViewSet, 'tasks' )

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/login', UserLoginView.as_view()),
    path('v1/register', RegisterUsersView.as_view())
]
