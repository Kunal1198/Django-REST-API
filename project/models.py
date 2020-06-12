from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Student(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    marks =  models.IntegerField()
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    #owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name