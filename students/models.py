from django.db import models

class StudentGroups(models.Model):
    group_id=models.IntegerField(primary_key=True,auto_created=True)
    first_member_reg_no=models.CharField(max_length=100,unique=True)
    second_member_reg_no=models.CharField(max_length=100,blank=True,null=True,unique=False)
    third_member_reg_no=models.CharField(max_length=100,blank=True,null=True,unique=False)
    proposed_supervisor = models.CharField(max_length=100)
    supervisor_employee_id = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return  '%s'% (self.group_id)

class Student(models.Model):
    student_reg_no=models.CharField(max_length=100,primary_key=True)
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    profile_picture=models.ImageField(null=True,blank=True,upload_to='students_profile_pictures/%Y/%m/%d')
    studentgroup=models.ForeignKey(StudentGroups,related_name='student',on_delete=models.SET_NULL,null=True,blank=True)
    email=models.CharField(max_length=200,null=True,blank=True)
    login=models.BooleanField(default=False)
    role=models.CharField(max_length=20, default='student')
    course=models.CharField(max_length=100,default='bsc in comp science')

    def __str__(self):
        return '%s %s ' % (self.student_reg_no,self.lastname)
class GroupsProject(models.Model):
    group_id=models.OneToOneField(StudentGroups,on_delete=models.CASCADE,primary_key=True,related_name='group_title',auto_created=True)
    semister1_progress=models.FileField(blank=True,null=True,upload_to='Student_GroupsProject_Semister1_Progress/%Y/%m/%d')
    semister1_final=models.FileField(blank=True,null=True,upload_to='Student_GroupsProject_Semister1_Final/%Y/%m/%d')
    semister2_progress=models.FileField(blank=True,null=True,upload_to='Student_GroupsProject_Semister2_Progress/%Y/%m/%d')
    semister2_Final=models.FileField(blank=True,null=True,upload_to='Student_GroupsProject_Semister2_Final/%Y/%m/%d')
    title=models.TextField(null=True)
    concept_note=models.FileField(blank=True,null=True,upload_to='Students_groups_projects_ConceptNotes/%Y/%m/%d')
    semister1_progress_grades=models.IntegerField(default=0)
    semister1_final_grades=models.IntegerField(default=0)
    semister2_progress_grades=models.IntegerField(default=0)
    semister2_Final_grades=models.IntegerField(default=0)
    def __str__(self):
        return 'group_id = %s' % (self.group_id)
class Message(models.Model):
    student_group_id=models.ForeignKey(StudentGroups,max_length=100,on_delete=models.CASCADE,null=True,blank=True)
    message_from_supervisor=models.TextField(null=True,blank=True)

    creted_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return 'messages from student'

class MessageFromCoordinator(models.Model):
    student_group_id = models.ForeignKey(StudentGroups, max_length=100, on_delete=models.CASCADE, null=True, blank=True)
    message_from_cordinator = models.TextField(null=True, blank=True)
    creted_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.message_from_cordinator

