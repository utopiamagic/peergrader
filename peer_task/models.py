# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

class PeerReviewAssignmentArticleResponses(models.Model):
    submissionid = models.IntegerField(db_column='submissionID', primary_key=True, blank=True, null=False)  
    articleindex = models.IntegerField(db_column='articleIndex')  
    outline = models.TextField()  # This field type is a guess.
    response = models.TextField()  # This field type is a guess.

    class Meta:
        db_table = 'peer_review_assignment_article_responses'

class Assignments(models.Model):
    assignmentid = models.IntegerField(db_column='assignmentID', primary_key=True, blank=True, null=False)  
    name = models.CharField("Assignment Name", max_length=128)
    courseid = models.IntegerField(db_column='courseID')  
    displaypriority = models.IntegerField(db_column='displayPriority')  
    assignmenttype = models.CharField(db_column='assignmentType', max_length=64)  
    passwordmessage = models.TextField("Password Message", db_column='passwordMessage', blank=True, null=True)  
    password = models.CharField(max_length=255, blank=True, null=False)
    browsable = models.BooleanField("Visible to students", db_column='visibleToStudents')   # This field type is a guess.

    class Meta:
        db_table = 'assignments'
        
class AssignmentSubmissions(models.Model):
    submissionid = models.IntegerField(db_column='submissionID', primary_key=True, blank=True, null=False)  
    assignmentid = models.IntegerField(db_column='assignmentID')  
    authorid = models.IntegerField(db_column='authorID')  
    content = models.TextField()   # This field type is added by ng
    filepath = models.ImageField(upload_to='images/temp/', default = 'images/temp/no-img.png')
    nopublicuse = models.TextField(db_column='noPublicUse')   # This field type is a guess.
    submissiontimestamp = models.DateTimeField(db_column='submissionTimestamp')  

    class Meta:
        managed = False
        db_table = 'peer_review_assignment_submissions'
        unique_together = (('assignmentid', 'authorid'),)

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
    success = models.BooleanField()  # This field type is a guess.
    seen = models.BooleanField()  # This field type is a guess.
    summary = models.TextField()
    details = models.TextField()  # This field type is a guess.

    class Meta:
        db_table = 'job_notifications'


class Status(models.Model):
    value = models.TextField(primary_key=True, blank=True, null=False)

    class Meta:
        managed = False
        db_table = 'status'

class PeerReviewAssignmentDenied(models.Model):
    userid = models.IntegerField(db_column='userID', primary_key=True)  
    assignmentid = models.IntegerField(db_column='assignmentID', primary_key=True)  

    class Meta:
        db_table = 'peer_review_assignment_denied'
        unique_together = (('userid', 'assignmentid'),)


class PeerReviewAssignmentEssaySettings(models.Model):
    assignmentid = models.IntegerField(db_column='assignmentID', primary_key=True)  
    topicindex = models.IntegerField(db_column='topicIndex', primary_key=True)  
    topic = models.CharField(max_length=255)

    class Meta:
        db_table = 'peer_review_assignment_essay_settings'
        unique_together = (('assignmentid', 'topicindex'),)


class PeerReviewAssignmentEssays(models.Model):
    submissionid = models.IntegerField(db_column='submissionID', primary_key=True, blank=True, null=False)  
    text = models.TextField()  # This field type is a guess.
    topicindex = models.IntegerField(db_column='topicIndex', blank=True, null=False)  

    class Meta:
        db_table = 'peer_review_assignment_essays'


class PeerReviewAssignmentImages(models.Model):
    submissionid = models.IntegerField(db_column='submissionID', primary_key=True, blank=True, null=False)  
    imgwidth = models.IntegerField(db_column='imgWidth')  
    imgheight = models.IntegerField(db_column='imgHeight')  
    imgdata = models.TextField(db_column='imgData')   # This field type is a guess.
    text = models.TextField()

    class Meta:
        db_table = 'peer_review_assignment_images'


class PeerReviewAssignmentIndependent(models.Model):
    userid = models.IntegerField(db_column='userID', primary_key=True)  
    assignmentid = models.IntegerField(db_column='assignmentID', primary_key=True)  

    class Meta:
        db_table = 'peer_review_assignment_independent'
        unique_together = (('userid', 'assignmentid'),)

class PeerReviewAssignmentArticleResponseSettings(models.Model):
    assignmentid = models.IntegerField(db_column='assignmentID', primary_key=True)  
    articleindex = models.IntegerField(db_column='articleIndex', primary_key=True)  
    name = models.CharField(max_length=255)
    link = models.TextField()

    class Meta:
        db_table = 'peer_review_assignment_article_response_settings'
        unique_together = (('assignmentid', 'articleindex'),)
        
        
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

