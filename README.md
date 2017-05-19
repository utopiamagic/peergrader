Questions
=========
* allow stu to quit a course?

Modules
========
peer_auth:
-----------
+ Authentication system

peer_task:
--------------
+ tasks yet-to-be-solved in a course

peer_panel:
-----------
* Home page displays the title. get started button, home and courses links, and log in and signup buttons.  
TODO: It should not display a list of courses.
* Title: the next-generation mechanical TA
* "Get Started" button directs users to the signup page.
* Courses page:  Currently it directs me to log in if I am not logged in.  
TODO: If I am not logged in, this should display a list of course names, without any other information about the courses.  The top right corner should have the log in and sign up buttons.  


peer_review:
------------
+ Create/Edit peer reviews

peer_course:
------------
+ Create/Edit courses
+ User information: student ID, email, first name, last name.  Edit button.
TODO: For an instructor, display "user ID" rather than "student ID".
TODO?: Do we need to show whether you are an instructor, a TA, or a student?
TODO?: A person could have different roles in different courses.   a TA in one course and a student in another course.  Do we want to allow this?

+ admin: Use this to distinguish admin (superuser) from other users.  Every instructor is an admin, meaning that they are born with the superior ability to access the admin page.
+ Instructor: admin = True
+ Everyone else: admin = False
+ staff in the user table is Django's functionality.
TODO: Remove "staff" from the UI because it is not being used right now.  Set staff = False for everyone. 

+ CourseMember table: manages the relationship between a user and a course.  We can use this table to keep track of whether someone is a student or a TA in this course.

+ Edit (user info) page:
TODO: Display a form, which shows the current information and also allows the person to update the information.
 	Fields to be displayed:
 	Student:
    Student ID (not modifiable)
    First name (modifiable)
    Last name (modifiable)
    Email (modifiable)
    Do not display staff or admin.
	Instructor: 
  	Only display the following information.  Do not allow them to be modified. 
  	User ID
		First name
		Last name
		Email
		Do not display staff or admin.
		
+ Create a course:
TODO (Alice and Heddy): Need to figure out what "browsable" and "archived" mean.  

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
