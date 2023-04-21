class UserManager(BaseUserManager):
    def create_user(self, email,username=None,password=None,is_admin=True,is_staff=True,is_active=True):
        if not email:
            raise ValueError("user must have an email")
        if not password:
            raise ValueError("user must have an password")
        
        user=self.model(
            email=self.normalize_email(email)
        )
        user.username(username)
        user.set_password(password)
        user.admin=is_active
        user.staff=is_active
        user.active=is_active
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email,username=None,password=None,**extra_fields):
         if not email:
            raise ValueError("user must have an email")
         if not password:
            raise ValueError("user must have an password")

         user=self.model(
            email=self.normalize_email(email)
         )
         user.username(username)
         user.set_password(password)
         user.admin=True
         user.staff=True
         user.active=True
         user.save(using=self._db)
         return user