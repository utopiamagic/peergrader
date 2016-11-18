from django.db import models

#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

class Course(models.Model):
    courseid = models.IntegerField(db_column='courseID', primary_key=True, blank=True, null=True)  
    name = models.CharField(unique=True, max_length=64)
    displayname = models.CharField(db_column='displayName', max_length=128)  
    authtype = models.CharField(db_column='authType', max_length=128)  
    registrationtype = models.CharField(db_column='registrationType', max_length=128)  
    browsable = models.TextField()  # # This field type is a guess.
    archived = models.TextField()  # # This field type is a guess.

    class Meta:
        db_table = 'course'


class CourseConfiguration(models.Model):
    courseid = models.IntegerField(db_column='courseID', primary_key=True, blank=True, null=True)  
    windowsize = models.IntegerField(db_column='windowSize')  
    numreviews = models.IntegerField(db_column='numReviews')  
    scorenoise = models.TextField(db_column='scoreNoise')   # This field type is a guess.
    maxattempts = models.IntegerField(db_column='maxAttempts')  
    numcovertcalibrations = models.IntegerField(db_column='numCovertCalibrations')  
    exhaustedcondition = models.TextField(db_column='exhaustedCondition')  
    minreviews = models.IntegerField(db_column='minReviews')  
    spotcheckprob = models.TextField(db_column='spotCheckProb')   # This field type is a guess.
    highmarkthreshold = models.TextField(db_column='highMarkThreshold')   # This field type is a guess.
    highmarkbias = models.TextField(db_column='highMarkBias')   # This field type is a guess.
    calibrationthreshold = models.TextField(db_column='calibrationThreshold')   # This field type is a guess.
    calibrationbias = models.TextField(db_column='calibrationBias')   # This field type is a guess.
    scorewindowsize = models.IntegerField(db_column='scoreWindowSize')  
    scorethreshold = models.TextField(db_column='scoreThreshold')   # This field type is a guess.
    disqualifywindowsize = models.IntegerField(db_column='disqualifyWindowSize')  
    disqualifythreshold = models.TextField(db_column='disqualifyThreshold')   # This field type is a guess.

    class Meta:
        db_table = 'course_configuration'

