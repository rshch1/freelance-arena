from freelance_arena.users.models import User

def user_validate(object):
    if len(object.get('password')) > 6:
        if "@" in object.get('email'):
            try:
                User.objects.get(username=object.get('username'))
            except User.DoesNotExist:
                return True
    return False