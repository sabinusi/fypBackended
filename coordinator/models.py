from django.db import models

class Coordinator(models.Model):
    employee_id=models.CharField(primary_key=True,max_length=100)
    name=models.CharField(max_length=300)
    email=models.CharField(max_length=200,blank=True,null=True)
    login=models.BooleanField(default=False)
    role=models.CharField(default='cordinaor',max_length=20)
    profile_picture=models.ImageField(blank=True,null=True,upload_to='cordinator_profile_pics')
    def __str__(self):
        return self.name
class CoordinatorAnaucements(models.Model):
    coordinator_employee_id=models.ForeignKey(Coordinator,max_length=100,on_delete=models.PROTECT)
    title=models.CharField(max_length=55)
    creted_at=models.DateTimeField(auto_now_add=True)
    description=models.TextField()
    def __str__(self):
        return self.title
    

