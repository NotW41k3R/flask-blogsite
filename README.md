# **Blogsite - Project (Parts 1-4 Combined Overview)**

This repository contains a four-part capstone project that evolves from a simple blog viewer into a fully functional blogging platform with authentication, database storage, commenting, admin controls, and clean Bootstrap styling. Each part builds upon the previous one, introducing new backend concepts, tools, and real-world web development patterns.

---

# Project Progression

## Part 1 - Flask + REST API Rendering

The project starts with a simple Flask application that retrieves blog data from a remote JSON API. Each post is turned into a small Python object and rendered through Jinja templates. The homepage displays all posts, and each one links to its own detail page using dynamic routing.

**Skills learned:**

* Making API requests with `requests`
* Converting JSON into clean Python structures
* Dynamic routing with URL parameters
* Displaying data using Jinja templates

---

## Part 2 - Jinja Layouts + Bootstrap Styling

The second version improves the UI and structure of the site. Bootstrap is added to style the layout and make the pages responsive. Jinja template inheritance is used to organize repeated HTML elements like navigation bars and footers.

The app still fetches posts from the same JSON API, but everything now looks and feels more like a real website.

**Skills learned:**

* Using Bootstrap for responsive styling
* Building reusable Jinja layouts
* Creating multi-page navigation (About, Contact, Posts)
* Structuring clean HTML templates without duplication

---

## Part 3 - CRUD Application with SQLAlchemy + CKEditor

Here the project transforms from an API-based viewer into a real content management system. An SQLite database is introduced via SQLAlchemy, and the app now stores and manages its own posts. Users can create, update, and delete posts, each backed by real database operations.

WTForms handles validation, and CKEditor enables rich text formatting for blog content.

**Skills learned:**

* Designing SQLAlchemy models and relationships
* Implementing full CRUD routes
* Using WTForms for form handling and validation
* Integrating CKEditor for formatted text
* Applying REST-style patterns for clean backend design

---

## Part 4 - User Authentication + Comments + Admin Access

The final stage adds proper user accounts and security. Visitors can register, log in, and log out. Passwords are hashed safely using Werkzeug, and user sessions are handled via `Flask-Login`.

Only authenticated users can comment on posts, and only the admin (user ID = 1) can create, edit, or delete posts. Comments are stored in their own table and linked to both users and posts via SQLAlchemy relationships.

This part ties everything together and turns the project into a fully functional blogging platform.

**Skills learned:**

* Implementing authentication with Flask-Login
* Securing routes with decorators (`login_required`, `admin_only`)
* Hashing and verifying passwords
* Creating many-to-one relationships (Users ⇄ Comments ⇄ Posts)
* Handling user sessions and role-based access
* Using flash messages for clean UX feedback

---

# Final Features of the Complete Blogsite

By the end of Part 4, the blogsite includes:

### Public Features

* View all posts on the homepage
* Read full posts
* View comments under each post

### User Features

* Register a new account
* Log in and log out
* Comment on any post

### Admin Features

* Create new posts
* Edit existing posts
* Delete posts
* Access restricted routes

### Technical Features

* SQLAlchemy models with relationships
* WTForms validation
* CKEditor rich text editing
* Secure sessions with Flask-Login
* Decorator-based access control
* Clean Bootstrap UI layout

---

# Tools & Technologies Used

* Flask - core backend framework
* SQLAlchemy - ORM for database management
* WTForms - form validation
* CKEditor - rich text editor
* Flask-Login - user authentication
* Bootstrap 5 - responsive frontend styling
* Jinja2 - templating engine
* SQLite - lightweight embedded database

---

### Create a virtual environment
python -m venv venv

### Activate the virtual environment (Windows)
venv\Scripts\activate

### Install dependencies
pip install -r requirements.txt

### Run the application
python main.py
