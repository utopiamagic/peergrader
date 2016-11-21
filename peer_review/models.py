from django.db import models

#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

class PeerReviewAssignment(models.Model):
    assignmentid = models.IntegerField(db_column='assignmentID', primary_key=True, blank=True, null=False)   
    submissionquestion = models.TextField(db_column='submissionQuestion')   # This field type is a guess.
    submissiontype = models.CharField(db_column='submissionType', max_length=64)  
    submissionstartdate = models.DateTimeField(db_column='submissionStartDate')  
    submissionstopdate = models.DateTimeField(db_column='submissionStopDate')  
    reviewstartdate = models.DateTimeField(db_column='reviewStartDate')  
    reviewstopdate = models.DateTimeField(db_column='reviewStopDate')  
    markpostdate = models.DateTimeField(db_column='markPostDate')  
    maxsubmissionscore = models.TextField(db_column='maxSubmissionScore')   # This field type is a guess.
    maxreviewscore = models.TextField(db_column='maxReviewScore')   # This field type is a guess.
    defaultnumberofreviews = models.IntegerField(db_column='defaultNumberOfReviews')  
    allowrequestofreviews = models.TextField(db_column='allowRequestOfReviews')   # This field type is a guess.
    showmarksforreviewsreceived = models.TextField(db_column='showMarksForReviewsReceived')   # This field type is a guess.
    showotherreviewsbystudents = models.TextField(db_column='showOtherReviewsByStudents')   # This field type is a guess.
    showotherreviewsbyinstructors = models.TextField(db_column='showOtherReviewsByInstructors')   # This field type is a guess.
    showmarksforotherreviews = models.TextField(db_column='showMarksForOtherReviews')   # This field type is a guess.
    showmarksforreviewedsubmissions = models.TextField(db_column='showMarksForReviewedSubmissions')   # This field type is a guess.
    appealstopdate = models.DateTimeField(db_column='appealStopDate')  
    showpoolstatus = models.TextField(db_column='showPoolStatus')   # This field type is a guess.
    calibrationmincount = models.IntegerField(db_column='calibrationMinCount')  
    calibrationmaxscore = models.IntegerField(db_column='calibrationMaxScore')  
    calibrationthresholdmse = models.TextField(db_column='calibrationThresholdMSE')   # This field type is a guess.
    calibrationthresholdscore = models.TextField(db_column='calibrationThresholdScore')   # This field type is a guess.
    autoassignessaytopic = models.TextField(db_column='autoAssignEssayTopic')   # This field type is a guess.
    extracalibrations = models.IntegerField(db_column='extraCalibrations', blank=True, null=False)  
    essaywordlimit = models.IntegerField(db_column='essayWordLimit')  
    calibrationstartdate = models.DateTimeField(db_column='calibrationStartDate')  
    calibrationstopdate = models.DateTimeField(db_column='calibrationStopDate')  

    class Meta:
        db_table = 'peer_review_assignment'


class PeerReviewAssignmentAppealMessages(models.Model):
    appealmessageid = models.IntegerField(db_column='appealMessageID', primary_key=True, blank=True, null=False)  
    appealtype = models.TextField(db_column='appealType')  
    matchid = models.IntegerField(db_column='matchID')  
    authorid = models.IntegerField(db_column='authorID')  
    viewedbystudent = models.TextField(db_column='viewedByStudent')   # This field type is a guess.
    text = models.TextField()

    class Meta:
        db_table = 'peer_review_assignment_appeal_messages'


class PeerReviewAssignmentArticleResponseSettings(models.Model):
    assignmentid = models.IntegerField(db_column='assignmentID', primary_key=True)  
    articleindex = models.IntegerField(db_column='articleIndex', primary_key=True)  
    name = models.CharField(max_length=255)
    link = models.TextField()

    class Meta:
        db_table = 'peer_review_assignment_article_response_settings'
        unique_together = (('assignmentid', 'articleindex'),)


class PeerReviewAssignmentArticleResponses(models.Model):
    submissionid = models.IntegerField(db_column='submissionID', primary_key=True, blank=True, null=False)  
    articleindex = models.IntegerField(db_column='articleIndex')  
    outline = models.TextField()  # This field type is a guess.
    response = models.TextField()  # This field type is a guess.

    class Meta:
        db_table = 'peer_review_assignment_article_responses'


class PeerReviewAssignmentCalibrationMatches(models.Model):
    matchid = models.IntegerField(db_column='matchID', primary_key=True, blank=True, null=False)  
    assignmentid = models.IntegerField(db_column='assignmentID')  
    required = models.TextField()  # This field type is a guess.

    class Meta:
        db_table = 'peer_review_assignment_calibration_matches'


class PeerReviewAssignmentCalibrationPools(models.Model):
    assignmentid = models.IntegerField(db_column='assignmentID', primary_key=True)  
    poolassignmentid = models.IntegerField(db_column='poolAssignmentID', primary_key=True)  

    class Meta:
        db_table = 'peer_review_assignment_calibration_pools'
        unique_together = (('assignmentid', 'poolassignmentid'),)


class PeerReviewAssignmentCode(models.Model):
    submissionid = models.IntegerField(db_column='submissionID', primary_key=True, blank=True, null=False)  
    code = models.TextField()  # This field type is a guess.

    class Meta:
        db_table = 'peer_review_assignment_code'


class PeerReviewAssignmentCodeSettings(models.Model):
    assignmentid = models.IntegerField(db_column='assignmentID', primary_key=True, blank=True, null=False)  
    codelanguage = models.CharField(db_column='codeLanguage', max_length=255)  
    codeextension = models.CharField(db_column='codeExtension', max_length=10)  
    uploadonly = models.TextField(db_column='uploadOnly')   # This field type is a guess.

    class Meta:
        db_table = 'peer_review_assignment_code_settings'


class PeerReviewAssignmentDemotionLog(models.Model):
    userid = models.IntegerField(db_column='userID', primary_key=True, blank=True, null=False)  
    demotiondate = models.DateTimeField(db_column='demotionDate')  
    demotionthreshold = models.TextField(db_column='demotionThreshold')   # This field type is a guess.

    class Meta:
        db_table = 'peer_review_assignment_demotion_log'


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


class PeerReviewAssignmentInstructorReviewTouchTimes(models.Model):
    submissionid = models.IntegerField(db_column='submissionID', primary_key=True)  
    instructorid = models.IntegerField(db_column='instructorID', primary_key=True)  
    timestamp = models.DateTimeField()

    class Meta:
        db_table = 'peer_review_assignment_instructor_review_touch_times'
        unique_together = (('submissionid', 'instructorid'),)


class PeerReviewAssignmentMatches(models.Model):
    matchid = models.IntegerField(db_column='matchID', primary_key=True, blank=True, null=False)  
    submissionid = models.IntegerField(db_column='submissionID')  
    reviewerid = models.IntegerField(db_column='reviewerID')  
    instructorforced = models.TextField(db_column='instructorForced')   # This field type is a guess.
    calibrationstate = models.TextField(db_column='calibrationState')  

    class Meta:
        db_table = 'peer_review_assignment_matches'
        unique_together = (('submissionid', 'reviewerid'),)


class PeerReviewAssignmentQuestions(models.Model):
    questionid = models.IntegerField(db_column='questionID', primary_key=True, blank=True, null=False)  
    assignmentid = models.IntegerField(db_column='assignmentID')  
    questionname = models.CharField(db_column='questionName', max_length=128)  
    questiontext = models.TextField(db_column='questionText')  
    questiontype = models.CharField(db_column='questionType', max_length=64)  
    hidden = models.TextField()  # This field type is a guess.
    displaypriority = models.IntegerField(db_column='displayPriority')  

    class Meta:
        db_table = 'peer_review_assignment_questions'


class PeerReviewAssignmentRadioOptions(models.Model):
    questionid = models.IntegerField(db_column='questionID', primary_key=True)  
    index = models.IntegerField(primary_key=True)
    label = models.CharField(max_length=1024)
    score = models.TextField()  # This field type is a guess.

    class Meta:
        db_table = 'peer_review_assignment_radio_options'
        unique_together = (('questionid', 'index'),)


class PeerReviewAssignmentReviewAnswers(models.Model):
    matchid = models.IntegerField(db_column='matchID', primary_key=True)  
    questionid = models.IntegerField(db_column='questionID', primary_key=True)  
    answerint = models.IntegerField(db_column='answerInt', blank=True, null=False)  
    answertext = models.TextField(db_column='answerText', blank=True, null=False)  
    reviewtimestamp = models.DateTimeField(db_column='reviewTimestamp')  

    class Meta:
        db_table = 'peer_review_assignment_review_answers'
        unique_together = (('matchid', 'questionid'),)


class PeerReviewAssignmentReviewAnswersDrafts(models.Model):
    matchid = models.IntegerField(db_column='matchID', primary_key=True)  
    questionid = models.IntegerField(db_column='questionID', primary_key=True)  
    answerint = models.IntegerField(db_column='answerInt', blank=True, null=False)  
    answertext = models.TextField(db_column='answerText', blank=True, null=False)  

    class Meta:
        db_table = 'peer_review_assignment_review_answers_drafts'
        unique_together = (('matchid', 'questionid'),)


class PeerReviewAssignmentReviewMarks(models.Model):
    matchid = models.IntegerField(db_column='matchID', primary_key=True, blank=True, null=False)  
    score = models.TextField()  # This field type is a guess.
    comments = models.TextField(blank=True, null=False)
    automatic = models.TextField()  # This field type is a guess.
    reviewpoints = models.TextField(db_column='reviewPoints')   # This field type is a guess.
    reviewmarktimestamp = models.DateTimeField(db_column='reviewMarkTimestamp')  

    class Meta:
        db_table = 'peer_review_assignment_review_marks'


class PeerReviewAssignmentSpotChecks(models.Model):
    submissionid = models.IntegerField(db_column='submissionID', primary_key=True, blank=True, null=False)  
    checkerid = models.IntegerField(db_column='checkerID')  
    status = models.TextField()

    class Meta:
        db_table = 'peer_review_assignment_spot_checks'


class PeerReviewAssignmentSubmissionMarks(models.Model):
    submissionid = models.IntegerField(db_column='submissionID', primary_key=True, blank=True, null=False)  
    score = models.TextField()  # This field type is a guess.
    comments = models.TextField(blank=True, null=False)
    automatic = models.TextField()  # This field type is a guess.
    submissionmarktimestamp = models.DateTimeField(db_column='submissionMarkTimestamp')  

    class Meta:
        managed = False
        db_table = 'peer_review_assignment_submission_marks'


class PeerReviewAssignmentSubmissions(models.Model):
    submissionid = models.IntegerField(db_column='submissionID', primary_key=True, blank=True, null=False)  
    assignmentid = models.IntegerField(db_column='assignmentID')  
    authorid = models.IntegerField(db_column='authorID')  
    nopublicuse = models.TextField(db_column='noPublicUse')   # This field type is a guess.
    submissiontimestamp = models.DateTimeField(db_column='submissionTimestamp')  

    class Meta:
        managed = False
        db_table = 'peer_review_assignment_submissions'
        unique_together = (('assignmentid', 'authorid'),)


class PeerReviewAssignmentTextOptions(models.Model):
    questionid = models.IntegerField(db_column='questionID', primary_key=True, blank=True, null=False)  
    minlength = models.IntegerField(db_column='minLength')  

    class Meta:
        managed = False
        db_table = 'peer_review_assignment_text_options'

