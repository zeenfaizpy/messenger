from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    """ """

    def create_user(self, username, password, email, name):
        """Creates and saves a User with the given email and password."""
        if username is None:
            raise TypeError('Users must have a username.')
        if password is None:
            raise TypeError('Users must have a password.')
        if email is None:
            raise TypeError('Users must have a email.')
        if name is None:
            raise TypeError('Users must have a name.')

        user = self.model(username=username, email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, email, name):
        """Creates and saves a User with the given email and password and
        makes the user as super user."""
        if username is None:
            raise TypeError('Superusers must have a username.')
        if password is None:
            raise TypeError('Superusers must have a password.')
        if email is None:
            raise TypeError('Superusers must have a email.')
        if name is None:
            raise TypeError('Superusers must have a name.')

        user = self.create_user(username, password, email, name)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user
