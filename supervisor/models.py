from django.db import models

class Supervisor(models.Model):
    name=models.CharField(max_length= 200)
    employee_id=models.CharField(max_length=100,primary_key=True)
    email=models.CharField(max_length=200)
    phone_number=models.CharField(max_length=50)
    role=models.CharField(default='supervisor',max_length=20)
    experties=models.CharField(max_length=500)
    ofice_number=models.CharField(max_length=50)
    login=models.BooleanField(default=False)
    profile_picture=models.ImageField(upload_to='supervisors_profile_pics/%Y/%m/%d',null=True,blank=True)
    def __str__(self):
        return self.name
class MessageFromSudents(models.Model):
    employee_id=models.ForeignKey(Supervisor,max_length=100,on_delete=models.CASCADE)
    student_title=models.TextField()
    message_from_student=models.TextField()
    group_id=models.CharField(max_length=100,null=True,blank=True)
    readed=models.BooleanField(default=False)
    student_names=models.CharField(max_length=200)
    def __str__(self):
        return self.student_names

class SudentGroup(models.Model):
    group_id=models.IntegerField()
    supervisor_employee_id=models.CharField(Supervisor,max_length=100)
    def __str__(self):
        return self.group_id
class StudentSingleGroup(models.Model):
    student_single_project_id=models.IntegerField()
    supervisor_employee_id=models.ForeignKey(Supervisor,max_length=100,on_delete=models.PROTECT)
    def __str__(self):
        return self.student_single_project_id

class ReceivedConcept(models.Model):
    group_id=models.IntegerField(primary_key=True,unique=True)
    supervisor_employee_id=models.ForeignKey(Supervisor,max_length=100,on_delete=models.PROTECT)
    recomandation=models.CharField(max_length=100,default='waiting')
    reasons=models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.recomandation
class Panel(models.Model):
    panel_id=models.IntegerField(primary_key=True,auto_created=True)
    first_supervisor=models.CharField(max_length=100,null=True,blank=True)
    second_supervisor=models.CharField(max_length=100,null=True,blank=True)
    third_supervisor=models.CharField(max_length=100,null=True,blank=True)
    fourth_supervisor=models.CharField(max_length=100,null=True,blank=True)
    fifth_supervisor=models.CharField(max_length=100,null=True,blank=True)
    six_supervisor=models.CharField(max_length=100,null=True,blank=True)
    seven_supervisor=models.CharField(max_length=100,null=True,blank=True)
    eight_supervisor=models.CharField(max_length=100,null=True,blank=True)
    first_groupid=models.IntegerField(null=True,blank=True)
    second_groupid=models.IntegerField(null=True,blank=True)
    third_groupid=models.IntegerField(null=True,blank=True)
    fourth_groupid=models.IntegerField(null=True,blank=True)
    fifth_groupid=models.IntegerField(null=True,blank=True)
    six_groupid=models.IntegerField(null=True,blank=True)
    seven_groupid=models.IntegerField(null=True,blank=True)
    eight_groupid=models.IntegerField(null=True,blank=True)
    nine_groupid=models.IntegerField(null=True,blank=True)
    ten_groupid=models.IntegerField(null=True,blank=True)



