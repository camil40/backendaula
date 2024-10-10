from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings
 
class Task(models.Model):
    CATEGORY_NAME = (
        ('I', 'Inicializado'),
        ('E', 'Em Andamento'),
        ('F', 'Finalizado'),
    )
 
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    start_date = models.DateField(null=True, blank=True)
    # data de vencimento da tarefa
    due_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.CharField(max_length=1, choices=CATEGORY_NAME, default='I', null=False, blank=False)
 
    def __str__(self):
        return self.title
 
class Tag(models.Model):
    tag_name = models.CharField(max_length=70)
    tasks = models.ManyToManyField(Task, related_name='tags')
 
    def __str__(self):
        return self.tag_name
   
class Comment(models.Model):
    comment_text = models.TextField(blank=True, null=True)
    fk_task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    fk_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.comment_text

class Notification(models.Model):
    title = models.CharField(max_length = 255,blank = True, null = True)
    description = models.TextField(blank=False, null=False)
    date = models.DateField(blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class FileUpload(models.Model):
    file = models.FileField(blank = True, null = True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(blank = True, null = True)


class UsuarioManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('O campo usuário deve ser preenchido')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=255)
    birthdate= models.DateField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True, unique=True)
    cpf = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username