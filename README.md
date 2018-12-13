# Flask Tutorial
## Following a tutorial called Flask Mega-Tutorial - By Miguel Grinberg

[Tutorial Home Page](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

### Chapters:
- [x] ~~Chapter 1: Hello, World!~~
- [x] ~~Chapter 2: Templates~~
- [x] ~~Chapter 3: Web Forms~~
- [x] ~~Chapter 4: Database~~
- [x] ~~Chapter 5: User Logins~~
- [x] ~~Chapter 6: Profile Page and Avatars~~
- [x] ~~Chapter 7: Error Handling~~
- [x] ~~Chapter 8: Followers~~
- [x] ~~Chapter 9: Pagination~~
- [x] ~~Chapter 10: Email Support~~
- [x] ~~Chapter 11: Facelift~~
- [x] ~~Chapter 12: Dates and Times~~
- [x] ~~Chapter 13: I18n and L10n~~
- [x] ~~Chapter 14: Ajax~~
- [x] ~~Chapter 15: A Better Application Structure~~
- [ ] Chapter 16: Full-Text Search
- [ ] Chapter 17: Deployment on Linux
- [ ] Chapter 18: Deployment on Heroku
- [ ] Chapter 19: Deployment on Docker Containers
- [ ] Chapter 20: Some JavaScript Magic
- [ ] Chapter 21: User Notifications
- [ ] Chapter 22: Background Jobs
- [ ] Chapter 23: Application Programming Interfaces (APIs)

### Chapter 1: Hello, World!
- creating a package
- installing and importing flask
- instantiating flask
- creating routes
- running the basic server

*Note: Using virtual environment enables you to work with specific versions
 and packages on a project while having others in the global environment or other projects.*

### Chapter 2: Templates
- return HTML from index()
- use a template html file
- conditional statements in html renderer
- for loop in html renderer
- template inheritance and block content

### Chapter 3: Web Forms
- install flask-wtf via the project interpreter in PyCharm
- configuration, setting a secret key ([CSRF](https://en.wikipedia.org/wiki/Cross-site_request_forgery))
- create the user login page and functionality with **FlaskForm**
  - form templates
  - form views
  - receiving the data
- flashing messages
- field validation
- using url_for() to generate URLs

### Chapter 4: Database
- using flask-sqlalchey - an ORM and flask-migrate
- create the db model for user
  - \_\_repr\_\_ instead of \_\_str\_\_
- create the initial migration
  - flask db init (requires FLASK_APP to be set) - creates the migrations directory
  - flask db migrate -m "comment here" creates the db migration in versions
  - flask db upgrade - creates (or updates) the database
  - <i>flask db downgrad</i> to revert the previous
  - flask db history
- adding db model for post with a foreign key for user id
  - using utcnow to set timestamp in GMT
  - user_id relationship to the User table (foreign key)
  - define a db.relationship in User to get the list of posts. set lazy='dynamic' to have posts as a query rather
    than a list, so it can be customized during use
- running from the shell. using flask shell and adding shell_context_processor
  - db.session.add() and db.session.commit()
  - Object.query.all() for all the objects
  - Object.query.get(id) by id
  - Object.query.oder_by(Object.field.desc()).all() all objects sorted by field in descending order
  - @app.shell_context_processor

### Chapter 5: User Logins
- password hashing
- the WerkZeug library
- Flask-login - login, logout, redirect to login if current user is not authorized. redirect to next page after login
- user registration

### Chapter 6: Profile Page and Avatars
- profile page
- avatar with Gravatar
- sub-templates
- simple editor

### Chapter 7: Error Handling
- error handling in Flask
- working with debug mode
- creating error pages
- sending email on crash
- logging
- customizing a flask form to add special validations

### Chapter 8: Followers
- many to many - followers relation table
- define a relationship field with the helper table
- piping query operations like Obj.query.join().filter().order_by()
- unit testing
- implement following and followed relationships between users

### Chapter 9: Pagination
- implementing the post form and showing followed posts on home page
- implementing explore page and user links
- pagination
- relative time (mine):
  - older than a year - YYYY-MM-DD HH:mm:SS
  - 7 days to one year - Feb 07 HH:mm:SS
  - 1 to 7 days - Tue HH:mm:SS
  - 6 hr to one day - HH:mm:SS
  - 90 min to 6 hr - about <x> hours ago
  - 60 to 90 min - about an hour ago
  - 2 to 60 min - <x> minutes ago
  - <2 min - a moment ago
  
### Chapter 10: Email Support
Reset password through an emailed link
- Flask-Mail and JSON Web Tokens
- encoding/decoding with JWT
- sending and validating the token via email
- implementing the email request and reset password page
- asynchronous process with threading

### Chapter 11: Facelift
Improve the application look and feel
- CSS Frameworks - [Bootstrap](https://getbootstrap.com/docs/3.3/getting-started/#examples)
- derive base.html from bootstrap/base.html
- use bootstrap/wtf.html for automatic form builder
- update _post.html to look good under bootstrap
- rendering pagination links

### Chapter 12: Dates and Times
- converting UTC times to local TZ
- Moment.js and Flask-Moment

### Chapter 13: I18n and L10n
Internationalization and Localization
- Flask-Babel
- language and country codes
- localeselector decorator
- marking the text to translate
- extracting text to translate (.pot)
- adding translation to another language (.po)
- compile the translation and generate an (.mo)
- create flask commands with cli. Remember to export FLASK_APP=microblog.py in the env shell before calling these commands

### Chapter 14: Ajax
Server/Client side components - Translate posts contents
- Ajax - Asynchronous JavaScript and XML (today XML is mostly replaced by JSON)
- language identification [guess_language](https://pypi.org/project/guess_language-spirit/)
- add column to Post to store language. this way detection is run only once, when the post is submitted by the user
- add code in index() to detect language and store in db
- show a translate link if the detected language is different for the locale one
- 3<sup>rd</sup> party translator - Microsoft Azure - translator API. set key
- first implement server-side translation
- ajax from client

### Chapter 15: A Better Application Structure
Discuss ways to make the application more scalable, maintainable, and better organized.
- current structure is based on function - views, forms, templates, email, etc
- using blueprint, a factory to initiate application instances, with different configurations
- separate the application to blueprints for the different aspects of the application, authentication,
errors, and main. Each blueprint may contain views and forms and templates and is a package
- blueprints are dormant until registered with the application
- error handling have the errors package (and sub-dir) under app and an errors sub-dir under templates,
and in these have all the related files to error handling
- authentication blueprint
- main app blueprint
- improve unit testing
- environment variables
  - install python-dotenv
  - have all the environment variables set in .env
  - load_dotenv
- requirements file
  - pip freeze > requirements.txt
  - pip install -r requirements.txt
