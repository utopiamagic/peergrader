Modules
========
peer_auth:
-----------
+ Authentication system

peer_quest:
--------------
+ tasks yet-to-be-solved in a course

peer_panel:
-----------
+ Home page

peer_review:
------------
+ Create/Edit peer reviews

peer_course:
------------
+ Create/Edit courses
+ Models.py
		* numreviews | Number of reviews | 3
		* calibrationbias | 1
		* users | different types 
		* course code |
		
Next Step
=========
* Finish user_update()
* Restore mysql

Roles
======
* superuser
* instructor
* teaching-assistant
* student

Sign up Fields
===============
* Student ID (unique)
* E-mail (unique)
* Firstname Lastname
* Password

Permissions
===========
## superuser
* change passwords {instructor, teaching-assistant, student}
* change roles {instructor, teaching-assistant, student}
* change courses {instructor, name, teaching-assistant, student}
* add courses
## instructor
* change passwords {teaching-assistant, student}
* change roles {teaching-assistant, student}
* add
* add/edit courses
## teaching-assistant | student
* update {password, name, Student ID}

Log
=======
* Nov, 24: 4 hrs
* Nov, 26: 2 hrs
* Nov, 28: 4 hrs
* Nov, 29: 3 hrs
* Dec, 19: 5 hrs
