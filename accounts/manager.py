from django.contrib.auth.base_user import BaseUserManager
class UserManager(BaseUserManager):
    use_in_migrations = True

    def create(self, phone, password=None, **extra_fields):
        if not phone:
            raise ValueError('Phone number is required')
            user = self.model(phone=phone, **extra_fields)