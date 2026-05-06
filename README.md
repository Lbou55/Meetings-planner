!!!! Run these commands first !!!!
python -m venv my_env
.\my_env\Scripts\Activate
pip install django
pip install djangorestframework
pip freeze > requirements.txt

!!! If you want to run the server !!!
.\my_env\Scripts\Activate
python manage.py runserver

Plan a Meeting: Users can define:

The date of the meeting.
/The duration (length) of the meeting.
/Assign a room to the meeting (the application handles the relationship between meetings and rooms).

View Meetings: A list of planned meetings (e.g., "Seance 01," "Seance 02") is displayed on the home page.

Manage Data: An administrator can use a built-in Admin Panel to perform CRUD operations (Create, Read, Update, Delete) on meetings and rooms.

Room Management: The app includes a model for Room and defines an association (One-to-Many) where one room can have multiple meetings.

In short, it is a practical exercise to learn Django by building a functional tool that handles user requests, database relationships, templates, and forms.


