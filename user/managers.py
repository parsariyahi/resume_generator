from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username, full_name, email, phone_number, 
                    password=None, year_of_birth=None, address=None):
        if not username:
            raise ValueError('Username is Required')

        user = self.model(
            username=username,
            full_name=full_name,
            email=email,
            phone_number=phone_number,
            year_of_birth=year_of_birth,
            address=address,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, full_name, email, phone_number, password=None):
        user = self.create_user(
            username=username,
            full_name=full_name,
            email=email,
            phone_number=phone_number,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
