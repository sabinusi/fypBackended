from django.db import models

class Login(models.Model):
    user_id=models.CharField(primary_key=True,max_length=100)
    password=models.CharField(max_length=150)
    role=models.CharField(max_length=100)
    def __str__(self):
        return '%s   %s' % (self.user_id,self.role)
class PastProjects(models.Model):
    title=models.CharField(max_length=2000)
    conceptNote=models.FileField(upload_to='pastprojects/%y/%m/%d')
    year=models.CharField(max_length=100)
    def __str__(self):
        return self.year

class SysteamControl(models.Model):
    submitConceptNote=models.BooleanField(default=True)
    sem1progress=models.BooleanField(default=False)
    sem1final=models.BooleanField(default=False)
    sem2progress=models.BooleanField(default=False)
    sem2final=models.BooleanField(default=False)
    def __str__(self):
        return 'system_controls_status'

