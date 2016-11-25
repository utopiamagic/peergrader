from django.db import models

#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

class Usertype(models.Model):
	value = models.TextField(primary_key=True, blank=True, null=False)

	class Meta:
		managed = False
		db_table = 'userType'


class UserPasswords(models.Model):
	username = models.CharField(primary_key=True, max_length=64, blank=True, null=False)
	passwordhash = models.CharField(db_column='passwordHash', max_length=128)  

	class Meta:
		managed = False
		db_table = 'user_passwords'


class Users(models.Model):
	userid = models.IntegerField(db_column='userID', primary_key=True, blank=True, null=False)  
	usertype = models.TextField(db_column='userType')  
	courseid = models.IntegerField(db_column='courseID')  
	firstname = models.CharField(db_column='firstName', max_length=128)  
	lastname = models.CharField(db_column='lastName', max_length=128)  
	username = models.CharField(max_length=64)
	studentid = models.IntegerField(db_column='studentID')  
	alias = models.CharField(max_length=64, blank=True, null=False)
	markingload = models.TextField(db_column='markingLoad')   # This field type is a guess.
	dropped = models.TextField()  # This field type is a guess.

	class Meta:
		managed = False
		db_table = 'users'
		unique_together = (('courseid', 'username'),)
