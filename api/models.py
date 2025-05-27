from django.db.models import Model, CharField
from django.db.models.fields import DateTimeField, BooleanField


class Task(Model):
    title = CharField(max_length=255)
    description = CharField(max_length=255)
    is_completed = BooleanField(default=False)
    created_at = DateTimeField()
    updated_at = DateTimeField()
