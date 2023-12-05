from django.db import models

# Create your models here.


class StudentDetail(models.Model):
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    class Meta:
        db_table = 'Student'

    def __str__(self) -> str:
        return self.email
