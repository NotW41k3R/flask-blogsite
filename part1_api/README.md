# Blogsite - Part 1 (Flask + REST API Rendering)

A simple Flask application that fetches blog posts from an external JSON API and renders them as dynamic pages. The app retrieves data from a hosted REST endpoint, converts each entry into a `Post` object, and passes these objects into Jinja templates for display.

The homepage lists all posts with their titles and subtitles. Clicking a post loads a dedicated page showing the full content. Routing is handled using URL parameters, mapping each post’s ID to its detail page. This stage focuses on pulling structured data from an API, building a minimal backend, and connecting it cleanly to HTML templates.

Skills learned: consuming REST APIs with `requests`, parsing and structuring JSON data, building dynamic pages with Flask and Jinja, defining lightweight data models in Python, and setting up clean route-to-template rendering.
