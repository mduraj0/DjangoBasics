# Django Course

This repository contains the projects and materials for a comprehensive Django course. The course covers the following topics:

- Introduction to Django framework
- HTTP protocol and its role in web development
- Understanding the MVT (Model-View-Template) and MVC (Model-View-Controller) patterns
- Dockerizing applications for easy deployment
- Deployment strategies for Django projects
- Test-driven development (TDD) and testing Django applications
- Application and user security, including password security best practices
- File upload functionality in Django
- Working with databases and data models
- Field types and dynamic attributes in Django models
- Relationships between different models
- User migrations and automated migrations
- Object managers and building queries
- Data aggregation in Django
- Class-based views
- Introduction to REST APIs
- Data serialization in Django
- Extending Django templates
- Working with CSRF tokens
- And much more!

## Projects

The course includes two main projects:

1. Blog: A Django-based blog application that allows users to create, read, update, and delete blog posts. It demonstrates core concepts of Django such as models, views, forms, and templates.

2. Library: A Django application that manages a library's book collection. It showcases more advanced Django features like user authentication, database relationships, and data aggregation.

## Installation

To run the projects and follow along with the course, make sure you have Python and Django installed. You can set up a virtual environment and install the required dependencies using the following commands:

```bash
# Create and activate a virtual environment
python3 -m venv myenv
source myenv/bin/activate

# Install Django
pip install django

# Clone the repository
git clone https://github.com/mduraj0/DjangoBasics.git

# Navigate to the project directory
cd firstDjango

# Run migrations
python manage.py migrate

# Start the development server
python manage.py runserver
