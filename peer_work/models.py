# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Appealtype(models.Model):
    value = models.TextField(primary_key=True, blank=True, null=False)

    class Meta:
        db_table = 'appealType'


class AppealAssignment(models.Model):
    submissionid = models.IntegerField(db_column='submissionID', primary_key=True, blank=True, null=False)  
    markerid = models.IntegerField(db_column='markerID')  

    class Meta:
        db_table = 'appeal_assignment'


class AssignmentPasswordEntered(models.Model):
    userid = models.IntegerField(db_column='userID', primary_key=True)  
    assignmentid = models.IntegerField(db_column='assignmentID', primary_key=True)  

    class Meta:
        db_table = 'assignment_password_entered'
        unique_together = (('userid', 'assignmentid'),)


class Assignments(models.Model):
    assignmentid = models.IntegerField(db_column='assignmentID', primary_key=True, blank=True, null=False)  
    name = models.CharField(max_length=128)
    courseid = models.IntegerField(db_column='courseID')  
    displaypriority = models.IntegerField(db_column='displayPriority')  
    assignmenttype = models.CharField(db_column='assignmentType', max_length=64)  
    passwordmessage = models.TextField(db_column='passwordMessage', blank=True, null=False)  
    password = models.CharField(max_length=255, blank=True, null=False)
    visibletostudents = models.TextField(db_column='visibleToStudents')   # This field type is a guess.

    class Meta:
        db_table = 'assignments'


class Calibrationstate(models.Model):
    value = models.TextField(primary_key=True, blank=True, null=False)

    class Meta:
        db_table = 'calibrationState'




class GroupPickerAssignment(models.Model):
    assignmentid = models.IntegerField(db_column='assignmentID', primary_key=True, blank=True, null=False)  
    startdate = models.DateTimeField(db_column='startDate')  
    stopdate = models.DateTimeField(db_column='stopDate')  

    class Meta:
        db_table = 'group_picker_assignment'


class GroupPickerAssignmentGroups(models.Model):
    assignmentid = models.IntegerField(db_column='assignmentID', primary_key=True)  
    groupindex = models.IntegerField(db_column='groupIndex', primary_key=True)  
    grouptext = models.TextField(db_column='groupText')  

    class Meta:
        db_table = 'group_picker_assignment_groups'
        unique_together = (('assignmentid', 'groupindex'),)


class GroupPickerAssignmentSelections(models.Model):
    selectionid = models.IntegerField(db_column='selectionID', primary_key=True, blank=True, null=False)  
    assignmentid = models.IntegerField(db_column='assignmentID')  
    userid = models.IntegerField(db_column='userID')  
    groupindex = models.IntegerField(db_column='groupIndex')  

    class Meta:
        db_table = 'group_picker_assignment_selections'
        unique_together = (('assignmentid', 'userid'),)


class JobNotifications(models.Model):
    notificationid = models.IntegerField(db_column='notificationID', primary_key=True, blank=True, null=False)  
    courseid = models.IntegerField(db_column='courseID')  
    assignmentid = models.IntegerField(db_column='assignmentID')  
    job = models.TextField()
    dateran = models.DateTimeField(db_column='dateRan')  
    success = models.TextField()  # This field type is a guess.
    seen = models.TextField()  # This field type is a guess.
    summary = models.TextField()
    details = models.TextField()  # This field type is a guess.

    class Meta:
        db_table = 'job_notifications'


class Status(models.Model):
    value = models.TextField(primary_key=True, blank=True, null=False)

    class Meta:
        managed = False
        db_table = 'status'


