from django.db import models
import uuid
from django.contrib.auth.models import User


def generate_uuid():
    return uuid.uuid4().hex

# Create your models here.


class BaseModel(models.Model):
    reference_id = models.CharField(
        max_length=32, unique=True, primary_key=True, default=generate_uuid)
    is_delete = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="+")
    created_at = models.DateTimeField()
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    updated_at = models.DateTimeField(null=True)

    class Meta:
        abstract = True


class StudentDetail(BaseModel):
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    class Meta:
        db_table = 'Student'

    def __str__(self) -> str:
        return self.email
