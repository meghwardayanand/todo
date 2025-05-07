from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


# Create your models here.
class TodoItem(models.Model):
    class Status(models.TextChoices):
        CREATED = 'C', _('Created')
        IN_PROGRESS = 'I', _('In Progress')
        FINISHED = 'F', _('Finished')


    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=Status.choices, default=Status.CREATED.value)

    # defined without requirements for better flavor
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} | {self.title} | {self.owner}"

    class Meta:
        db_table = 'todo_item'
