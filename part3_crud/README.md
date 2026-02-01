# Blogsite – Part 3 (Flask CRUD + SQLAlchemy + CKEditor)

This part turns the blog into a proper, REST-style web application. Instead of loading posts from an API, the app now manages its own SQLite database using SQLAlchemy. Each operation like creating, reading, updating, and deleting posts has its own route and uses the appropriate HTTP methods.

Users can add new posts, edit existing ones, or delete them entirely. Forms are built with WTForms and validated before saving. CKEditor provides a rich text editor for writing formatted blog content, and Bootstrap keeps the layout clean across all pages.

The homepage lists all posts from the database, each with links to view, edit, or delete. The “New Post” and “Edit Post” pages reuse the same form, with smart defaults based on the action. All changes are saved immediately to the SQLite database.

Skills learned: building REST-style CRUD routes, structuring SQLAlchemy models, validating user input with WTForms, integrating CKEditor for rich content editing, using Bootstrap for layout, and connecting all routes into a smooth workflow.