from freelance_arena.users.models import User

def user_validate(object):
    if len(object.get('password')) > 6:
        if "@" in object.get('email'):
            if object.get('user_type') == 1 or object.get('user_type') == 2:
                try:
                    User.objects.get(username=object.get('username'))
                except User.DoesNotExist:
                        return True
    return False