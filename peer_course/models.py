from django.db import models
from django.contrib.auth.models import User
#   * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.

class CourseList(models.Model):
    courseid = models.AutoField(db_column='courseID', primary_key=True, blank=True, null=False)  
    name = models.CharField(unique=False, max_length=64) # do not use it
    displayname = models.CharField(db_column='displayName', max_length=128)  
    authtype = models.CharField(db_column='authType', max_length=128)  # do not use it
    registrationtype = models.CharField(db_column='registrationType', max_length=128)    # do not use it
    browsable = models.BooleanField()
    archived = models.BooleanField()  # This field type is a guess.  / do not use it
    stucode = models.CharField(max_length=128, null=True) # student enter the auto-generated course code to gain access to the course page
    tascode = models.CharField(max_length=128, null=True) # ta enter the course code to gain access to the course page

    class Meta:
        db_table = 'course'
        
    def __str__(self) :
        return str(self.courseid)

#class CourseCode(models.Model):
#    courseid = models.IntegerField(blank=True, null=False)
#    code = models.CharField(max_length=128)
#    usertype = models.CharField(max_length=128)
#    class Meta:
#        db_table = 'course_code'
        
class CourseMember(models.Model):
    courseid = models.IntegerField(blank=True, null=False)
    userid = models.IntegerField(null=False)
    usertype = models.CharField(max_length=128)
    markingload = models.FloatField(db_column='markingload', null=True)
    class Meta:
        db_table = 'course_member'
        
    def __str__(self) :
        return str(self.usertype)

class CourseConfiguration(models.Model):
    courseid = models.IntegerField(db_column='courseID', primary_key=True, blank=True, null=False)  
    windowsize = models.IntegerField("Window Size", db_column='windowSize')  
    numreviews = models.IntegerField(db_column='numReviews')  # show it
    scorenoise = models.FloatField(db_column='scoreNoise')   # This field type is a guess.
    maxattempts = models.IntegerField(db_column='maxAttempts')  
    numcovertcalibrations = models.IntegerField(db_column='numCovertCalibrations')  
    exhaustedcondition = models.TextField(db_column='exhaustedCondition')  
    minreviews = models.IntegerField(db_column='minReviews')  
    spotcheckprob = models.FloatField(db_column='spotCheckProb')   # show it, what factions of reviews are checked by TAs This field type is a guess.
    highmarkthreshold = models.FloatField(db_column='highMarkThreshold')   # 1, This field type is a guess.
    highmarkbias = models.FloatField(db_column='highMarkBias')   # 1, This field type is a guess.
    calibrationthreshold = models.FloatField(db_column='calibrationThreshold')   # This field type is a guess.
    calibrationbias = models.FloatField(db_column='calibrationBias')   # This field type is a guess.
    scorewindowsize = models.IntegerField(db_column='scoreWindowSize')  
    scorethreshold = models.FloatField(db_column='scoreThreshold',)   # This field type is a guess.
    disqualifywindowsize = models.IntegerField(db_column='disqualifyWindowSize',)  
    disqualifythreshold = models.FloatField(db_column='disqualifyThreshold',)   # This field type is a guess.

    class Meta:
        db_table = 'course_configuration'

