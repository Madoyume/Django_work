from django.db import models

class Test1(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField(max_length=200)
    gender = models.BooleanField()
    age = models.IntegerField(default=0)
    birthday = models.DateField()
    
    def __str__(self):
        return f'<Test1:id={str(self.id)}, {self.name}({self.age})>'
