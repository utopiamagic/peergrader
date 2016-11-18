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
    value = models.TextField(primary_key=True, blank=True, null=True)

    class Meta:
        db_table = 'appealType'


class AppealAssignment(models.Model):
    submissionid = models.IntegerField(db_column='submissionID', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    markerid = models.IntegerField(db_column='markerID')  # Field name made lowercase.

    class Meta:
        db_table = 'appeal_assignment'


class AssignmentPasswordEntered(models.Model):
    userid = models.IntegerField(db_column='userID', primary_key=True)  # Field name made lowercase.
    assignmentid = models.IntegerField(db_column='assignmentID', primary_key=True)  # Field name made lowercase.

    class Meta:
        db_table = 'assignment_password_entered'
        unique_together = (('userid', 'assignmentid'),)


class Assignments(models.Model):
    assignmentid = models.IntegerField(db_column='assignmentID', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=128)
    courseid = models.IntegerField(db_column='courseID')  # Field name made lowercase.
    displaypriority = models.IntegerField(db_column='displayPriority')  # Field name made lowercase.
    assignmenttype = models.CharField(db_column='assignmentType', max_length=64)  # Field name made lowercase.
    passwordmessage = models.TextField(db_column='passwordMessage', blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(max_length=255, blank=True, null=True)
    visibletostudents = models.TextField(db_column='visibleToStudents')  # Field name made lowercase. This field type is a guess.

    class Meta:
        db_table = 'assignments'


class Calibrationstate(models.Model):
    value = models.TextField(primary_key=True, blank=True, null=True)

    class Meta:
        db_table = 'calibrationState'


class Course(models.Model):
    courseid = models.IntegerField(db_column='courseID', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(unique=True, max_length=64)
    displayname = models.CharField(db_column='displayName', max_length=128)  # Field name made lowercase.
    authtype = models.CharField(db_column='authType', max_length=128)  # Field name made lowercase.
    registrationtype = models.CharField(db_column='registrationType', max_length=128)  # Field name made lowercase.
    browsable = models.TextField()  # This field type is a guess.
    archived = models.TextField()  # This field type is a guess.

    class Meta:
        db_table = 'course'


class CourseConfiguration(models.Model):
    courseid = models.IntegerField(db_column='courseID', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    windowsize = models.IntegerField(db_column='windowSize')  # Field name made lowercase.
    numreviews = models.IntegerField(db_column='numReviews')  # Field name made lowercase.
    scorenoise = models.TextField(db_column='scoreNoise')  # Field name made lowercase. This field type is a guess.
    maxattempts = models.IntegerField(db_column='maxAttempts')  # Field name made lowercase.
    numcovertcalibrations = models.IntegerField(db_column='numCovertCalibrations')  # Field name made lowercase.
    exhaustedcondition = models.TextField(db_column='exhaustedCondition')  # Field name made lowercase.
    minreviews = models.IntegerField(db_column='minReviews')  # Field name made lowercase.
    spotcheckprob = models.TextField(db_column='spotCheckProb')  # Field name made lowercase. This field type is a guess.
    highmarkthreshold = models.TextField(db_column='highMarkThreshold')  # Field name made lowercase. This field type is a guess.
    highmarkbias = models.TextField(db_column='highMarkBias')  # Field name made lowercase. This field type is a guess.
    calibrationthreshold = models.TextField(db_column='calibrationThreshold')  # Field name made lowercase. This field type is a guess.
    calibrationbias = models.TextField(db_column='calibrationBias')  # Field name made lowercase. This field type is a guess.
    scorewindowsize = models.IntegerField(db_column='scoreWindowSize')  # Field name made lowercase.
    scorethreshold = models.TextField(db_column='scoreThreshold')  # Field name made lowercase. This field type is a guess.
    disqualifywindowsize = models.IntegerField(db_column='disqualifyWindowSize')  # Field name made lowercase.
    disqualifythreshold = models.TextField(db_column='disqualifyThreshold')  # Field name made lowercase. This field type is a guess.

    class Meta:
        db_table = 'course_configuration'


class GroupPickerAssignment(models.Model):
    assignmentid = models.IntegerField(db_column='assignmentID', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='startDate')  # Field name made lowercase.
    stopdate = models.DateTimeField(db_column='stopDate')  # Field name made lowercase.

    class Meta:
        db_table = 'group_picker_assignment'


class GroupPickerAssignmentGroups(models.Model):
    assignmentid = models.IntegerField(db_column='assignmentID', primary_key=True)  # Field name made lowercase.
    groupindex = models.IntegerField(db_column='groupIndex', primary_key=True)  # Field name made lowercase.
    grouptext = models.TextField(db_column='groupText')  # Field name made lowercase.

    class Meta:
        db_table = 'group_picker_assignment_groups'
        unique_together = (('assignmentid', 'groupindex'),)


class GroupPickerAssignmentSelections(models.Model):
    selectionid = models.IntegerField(db_column='selectionID', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    assignmentid = models.IntegerField(db_column='assignmentID')  # Field name made lowercase.
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    groupindex = models.IntegerField(db_column='groupIndex')  # Field name made lowercase.

    class Meta:
        db_table = 'group_picker_assignment_selections'
        unique_together = (('assignmentid', 'userid'),)


class JobNotifications(models.Model):
    notificationid = models.IntegerField(db_column='notificationID', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    courseid = models.IntegerField(db_column='courseID')  # Field name made lowercase.
    assignmentid = models.IntegerField(db_column='assignmentID')  # Field name made lowercase.
    job = models.TextField()
    dateran = models.DateTimeField(db_column='dateRan')  # Field name made lowercase.
    success = models.TextField()  # This field type is a guess.
    seen = models.TextField()  # This field type is a guess.
    summary = models.TextField()
    details = models.TextField()  # This field type is a guess.

    class Meta:
        db_table = 'job_notifications'


class PeerReviewAssignment(models.Model):
    assignmentid = models.IntegerField(db_column='assignmentID', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    submissionquestion = models.TextField(db_column='submissionQuestion')  # Field name made lowercase. This field type is a guess.
    submissiontype = models.CharField(db_column='submissionType', max_length=64)  # Field name made lowercase.
    submissionstartdate = models.DateTimeField(db_column='submissionStartDate')  # Field name made lowercase.
    submissionstopdate = models.DateTimeField(db_column='submissionStopDate')  # Field name made lowercase.
    reviewstartdate = models.DateTimeField(db_column='reviewStartDate')  # Field name made lowercase.
    reviewstopdate = models.DateTimeField(db_column='reviewStopDate')  # Field name made lowercase.
    markpostdate = models.DateTimeField(db_column='markPostDate')  # Field name made lowercase.
    maxsubmissionscore = models.TextField(db_column='maxSubmissionScore')  # Field name made lowercase. This field type is a guess.
    maxreviewscore = models.TextField(db_column='maxReviewScore')  # Field name made lowercase. This field type is a guess.
    defaultnumberofreviews = models.IntegerField(db_column='defaultNumberOfReviews')  # Field name made lowercase.
    allowrequestofreviews = models.TextField(db_column='allowRequestOfReviews')  # Field name made lowercase. This field type is a guess.
    showmarksforreviewsreceived = models.TextField(db_column='showMarksForReviewsReceived')  # Field name made lowercase. This field type is a guess.
    showotherreviewsbystudents = models.TextField(db_column='showOtherReviewsByStudents')  # Field name made lowercase. This field type is a guess.
    showotherreviewsbyinstructors = models.TextField(db_column='showOtherReviewsByInstructors')  # Field name made lowercase. This field type is a guess.
    showmarksforotherreviews = models.TextField(db_column='showMarksForOtherReviews')  # Field name made lowercase. This field type is a guess.
    showmarksforreviewedsubmissions = models.TextField(db_column='showMarksForReviewedSubmissions')  # Field name made lowercase. This field type is a guess.
    appealstopdate = models.DateTimeField(db_column='appealStopDate')  # Field name made lowercase.
    showpoolstatus = models.TextField(db_column='showPoolStatus')  # Field name made lowercase. This field type is a guess.
    calibrationmincount = models.IntegerField(db_column='calibrationMinCount')  # Field name made lowercase.
    calibrationmaxscore = models.IntegerField(db_column='calibrationMaxScore')  # Field name made lowercase.
    calibrationthresholdmse = models.TextField(db_column='calibrationThresholdMSE')  # Field name made lowercase. This field type is a guess.
    calibrationthresholdscore = models.TextField(db_column='calibrationThresholdScore')  # Field name made lowercase. This field type is a guess.
    autoassignessaytopic = models.TextField(db_column='autoAssignEssayTopic')  # Field name made lowercase. This field type is a guess.
    extracalibrations = models.IntegerField(db_column='extraCalibrations', blank=True, null=True)  # Field name made lowercase.
    essaywordlimit = models.IntegerField(db_column='essayWordLimit')  # Field name made lowercase.
    calibrationstartdate = models.DateTimeField(db_column='calibrationStartDate')  # Field name made lowercase.
    calibrationstopdate = models.DateTimeField(db_column='calibrationStopDate')  # Field name made lowercase.

    class Meta:
        db_table = 'peer_review_assignment'


class PeerReviewAssignmentAppealMessages(models.Model):
    appealmessageid = models.IntegerField(db_column='appealMessageID', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    appealtype = models.TextField(db_column='appealType')  # Field name made lowercase.
    matchid = models.IntegerField(db_column='matchID')  # Field name made lowercase.
    authorid = models.IntegerField(db_column='authorID')  # Field name made lowercase.
    viewedbystudent = models.TextField(db_column='viewedByStudent')  # Field name made lowercase. This field type is a guess.
    text = models.TextField()

    class Meta:
        db_table = 'peer_review_assignment_appeal_messages'


class PeerReviewAssignmentArticleResponseSettings(models.Model):
    assignmentid = models.IntegerField(db_column='assignmentID', primary_key=True)  # Field name made lowercase.
    articleindex = models.IntegerField(db_column='articleIndex', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=255)
    link = models.TextField()

    class Meta:
        db_table = 'peer_review_assignment_article_response_settings'
        unique_together = (('assignmentid', 'articleindex'),)


class PeerReviewAssignmentArticleResponses(models.Model):
    submissionid = models.IntegerField(db_column='submissionID', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    articleindex = models.IntegerField(db_column='articleIndex')  # Field name made lowercase.
    outline = models.TextField()  # This field type is a guess.
    response = models.TextField()  # This field type is a guess.

    class Meta:
        db_table = 'peer_review_assignment_article_responses'


class PeerReviewAssignmentCalibrationMatches(models.Model):
    matchid = models.IntegerField(db_column='matchID', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    assignmentid = models.IntegerField(db_column='assignmentID')  # Field name made lowercase.
    required = models.TextField()  # This field type is a guess.

    class Meta:
        db_table = 'peer_review_assignment_calibration_matches'


class PeerReviewAssignmentCalibrationPools(models.Model):
    assignmentid = models.IntegerField(db_column='assignmentID', primary_key=True)  # Field name made lowercase.
    poolassignmentid = models.IntegerField(db_column='poolAssignmentID', primary_key=True)  # Field name made lowercase.

    class Meta:
        db_table = 'peer_review_assignment_calibration_pools'
        unique_together = (('assignmentid', 'poolassignmentid'),)


class PeerReviewAssignmentCode(models.Model):
    submissionid = models.IntegerField(db_column='submissionID', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    code = models.TextField()  # This field type is a guess.

    class Meta:
        db_table = 'peer_review_assignment_code'


class PeerReviewAssignmentCodeSettings(models.Model):
    assignmentid = models.IntegerField(db_column='assignmentID', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    codelanguage = models.CharField(db_column='codeLanguage', max_length=255)  # Field name made lowercase.
    codeextension = models.CharField(db_column='codeExtension', max_length=10)  # Field name made lowercase.
    uploadonly = models.TextField(db_column='uploadOnly')  # Field name made lowercase. This field type is a guess.

    class Meta:
        db_table = 'peer_review_assignment_code_settings'


class PeerReviewAssignmentDemotionLog(models.Model):
    userid = models.IntegerField(db_column='userID', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    demotiondate = models.DateTimeField(db_column='demotionDate')  # Field name made lowercase.
    demotionthreshold = models.TextField(db_column='demotionThreshold')  # Field name made lowercase. This field type is a guess.

    class Meta:
        db_table = 'peer_review_assignment_demotion_log'


class PeerReviewAssignmentDenied(models.Model):
    userid = models.IntegerField(db_column='userID', primary_key=True)  # Field name made lowercase.
    assignmentid = models.IntegerField(db_column='assignmentID', primary_key=True)  # Field name made lowercase.

    class Meta:
        db_table = 'peer_review_assignment_denied'
        unique_together = (('userid', 'assignmentid'),)


class PeerReviewAssignmentEssaySettings(models.Model):
    assignmentid = models.IntegerField(db_column='assignmentID', primary_key=True)  # Field name made lowercase.
    topicindex = models.IntegerField(db_column='topicIndex', primary_key=True)  # Field name made lowercase.
    topic = models.CharField(max_length=255)

    class Meta:
        db_table = 'peer_review_assignment_essay_settings'
        unique_together = (('assignmentid', 'topicindex'),)


class PeerReviewAssignmentEssays(models.Model):
    submissionid = models.IntegerField(db_column='submissionID', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    text = models.TextField()  # This field type is a guess.
    topicindex = models.IntegerField(db_column='topicIndex', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'peer_review_assignment_essays'


class PeerReviewAssignmentImages(models.Model):
    submissionid = models.IntegerField(db_column='submissionID', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    imgwidth = models.IntegerField(db_column='imgWidth')  # Field name made lowercase.
    imgheight = models.IntegerField(db_column='imgHeight')  # Field name made lowercase.
    imgdata = models.TextField(db_column='imgData')  # Field name made lowercase. This field type is a guess.
    text = models.TextField()

    class Meta:
        db_table = 'peer_review_assignment_images'


class PeerReviewAssignmentIndependent(models.Model):
    userid = models.IntegerField(db_column='userID', primary_key=True)  # Field name made lowercase.
    assignmentid = models.IntegerField(db_column='assignmentID', primary_key=True)  # Field name made lowercase.

    class Meta:
        db_table = 'peer_review_assignment_independent'
        unique_together = (('userid', 'assignmentid'),)


class PeerReviewAssignmentInstructorReviewTouchTimes(models.Model):
    submissionid = models.IntegerField(db_column='submissionID', primary_key=True)  # Field name made lowercase.
    instructorid = models.IntegerField(db_column='instructorID', primary_key=True)  # Field name made lowercase.
    timestamp = models.DateTimeField()

    class Meta:
        db_table = 'peer_review_assignment_instructor_review_touch_times'
        unique_together = (('submissionid', 'instructorid'),)


class PeerReviewAssignmentMatches(models.Model):
    matchid = models.IntegerField(db_column='matchID', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    submissionid = models.IntegerField(db_column='submissionID')  # Field name made lowercase.
    reviewerid = models.IntegerField(db_column='reviewerID')  # Field name made lowercase.
    instructorforced = models.TextField(db_column='instructorForced')  # Field name made lowercase. This field type is a guess.
    calibrationstate = models.TextField(db_column='calibrationState')  # Field name made lowercase.

    class Meta:
        db_table = 'peer_review_assignment_matches'
        unique_together = (('submissionid', 'reviewerid'),)


class PeerReviewAssignmentQuestions(models.Model):
    questionid = models.IntegerField(db_column='questionID', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    assignmentid = models.IntegerField(db_column='assignmentID')  # Field name made lowercase.
    questionname = models.CharField(db_column='questionName', max_length=128)  # Field name made lowercase.
    questiontext = models.TextField(db_column='questionText')  # Field name made lowercase.
    questiontype = models.CharField(db_column='questionType', max_length=64)  # Field name made lowercase.
    hidden = models.TextField()  # This field type is a guess.
    displaypriority = models.IntegerField(db_column='displayPriority')  # Field name made lowercase.

    class Meta:
        db_table = 'peer_review_assignment_questions'


class PeerReviewAssignmentRadioOptions(models.Model):
    questionid = models.IntegerField(db_column='questionID', primary_key=True)  # Field name made lowercase.
    index = models.IntegerField(primary_key=True)
    label = models.CharField(max_length=1024)
    score = models.TextField()  # This field type is a guess.

    class Meta:
        db_table = 'peer_review_assignment_radio_options'
        unique_together = (('questionid', 'index'),)


class PeerReviewAssignmentReviewAnswers(models.Model):
    matchid = models.IntegerField(db_column='matchID', primary_key=True)  # Field name made lowercase.
    questionid = models.IntegerField(db_column='questionID', primary_key=True)  # Field name made lowercase.
    answerint = models.IntegerField(db_column='answerInt', blank=True, null=True)  # Field name made lowercase.
    answertext = models.TextField(db_column='answerText', blank=True, null=True)  # Field name made lowercase.
    reviewtimestamp = models.DateTimeField(db_column='reviewTimestamp')  # Field name made lowercase.

    class Meta:
        db_table = 'peer_review_assignment_review_answers'
        unique_together = (('matchid', 'questionid'),)


class PeerReviewAssignmentReviewAnswersDrafts(models.Model):
    matchid = models.IntegerField(db_column='matchID', primary_key=True)  # Field name made lowercase.
    questionid = models.IntegerField(db_column='questionID', primary_key=True)  # Field name made lowercase.
    answerint = models.IntegerField(db_column='answerInt', blank=True, null=True)  # Field name made lowercase.
    answertext = models.TextField(db_column='answerText', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'peer_review_assignment_review_answers_drafts'
        unique_together = (('matchid', 'questionid'),)


class PeerReviewAssignmentReviewMarks(models.Model):
    matchid = models.IntegerField(db_column='matchID', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    score = models.TextField()  # This field type is a guess.
    comments = models.TextField(blank=True, null=True)
    automatic = models.TextField()  # This field type is a guess.
    reviewpoints = models.TextField(db_column='reviewPoints')  # Field name made lowercase. This field type is a guess.
    reviewmarktimestamp = models.DateTimeField(db_column='reviewMarkTimestamp')  # Field name made lowercase.

    class Meta:
        db_table = 'peer_review_assignment_review_marks'


class PeerReviewAssignmentSpotChecks(models.Model):
    submissionid = models.IntegerField(db_column='submissionID', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    checkerid = models.IntegerField(db_column='checkerID')  # Field name made lowercase.
    status = models.TextField()

    class Meta:
        db_table = 'peer_review_assignment_spot_checks'


class PeerReviewAssignmentSubmissionMarks(models.Model):
    submissionid = models.IntegerField(db_column='submissionID', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    score = models.TextField()  # This field type is a guess.
    comments = models.TextField(blank=True, null=True)
    automatic = models.TextField()  # This field type is a guess.
    submissionmarktimestamp = models.DateTimeField(db_column='submissionMarkTimestamp')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'peer_review_assignment_submission_marks'


class PeerReviewAssignmentSubmissions(models.Model):
    submissionid = models.IntegerField(db_column='submissionID', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    assignmentid = models.IntegerField(db_column='assignmentID')  # Field name made lowercase.
    authorid = models.IntegerField(db_column='authorID')  # Field name made lowercase.
    nopublicuse = models.TextField(db_column='noPublicUse')  # Field name made lowercase. This field type is a guess.
    submissiontimestamp = models.DateTimeField(db_column='submissionTimestamp')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'peer_review_assignment_submissions'
        unique_together = (('assignmentid', 'authorid'),)


class PeerReviewAssignmentTextOptions(models.Model):
    questionid = models.IntegerField(db_column='questionID', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    minlength = models.IntegerField(db_column='minLength')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'peer_review_assignment_text_options'


class Status(models.Model):
    value = models.TextField(primary_key=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'status'


class Usertype(models.Model):
    value = models.TextField(primary_key=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userType'


class UserPasswords(models.Model):
    username = models.CharField(primary_key=True, max_length=64, blank=True, null=True)
    passwordhash = models.CharField(db_column='passwordHash', max_length=128)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_passwords'


class Users(models.Model):
    userid = models.IntegerField(db_column='userID', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    usertype = models.TextField(db_column='userType')  # Field name made lowercase.
    courseid = models.IntegerField(db_column='courseID')  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=128)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=128)  # Field name made lowercase.
    username = models.CharField(max_length=64)
    studentid = models.IntegerField(db_column='studentID')  # Field name made lowercase.
    alias = models.CharField(max_length=64, blank=True, null=True)
    markingload = models.TextField(db_column='markingLoad')  # Field name made lowercase. This field type is a guess.
    dropped = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'users'
        unique_together = (('courseid', 'username'),)
