Modules
========
peer_auth:
-----------
+ Authentication system

peer_central:
--------------
+ pass

peer_home:
-----------
+ Home page

peer_review:
------------
+ Create/Edit peer reviews

peer_course:
------------
+ Create/Edit courses
		
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
## instructor
* change passwords {teaching-assistant, student}
* change roles {teaching-assistant, student}
## teaching-assistant | student
* update {password, name, Student ID}

Log
=======
* Nov, 24: 4 hrs
* Nov, 26: 1 hr
* Nov, 28: 4 hrs
