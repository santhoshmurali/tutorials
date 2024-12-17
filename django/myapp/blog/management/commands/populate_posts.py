from typing import Any
from django.core.management.base import BaseCommand
from blog.models import Post, Category
import random

class Command(BaseCommand):
    help = "This will inserts post data in Database"

    def handle(self, *args, **options):
        # Delete Existing data
        Post.objects.all().delete()

        # # Blog Titles
        titles = [
            "Understanding Django: A Beginner's Guide",
            "10 Tips for Writing Clean Python Code",
            "How to Build a Blog with Django Framework",
            "Deploying Your Django App to the Cloud",
            "Top 5 Features of Django Every Developer Should Know",
            "Optimizing Your Django Queries for Performance",
            "Django vs Flask: Which Framework to Choose?",
            "Introduction to Django Rest Framework",
            "Handling Forms in Django Like a Pro",
            "Building a Portfolio Website Using Django",
            "Mastering Django Templates for Dynamic Web Pages",
            "Django Signals: Connecting Your Application Events",
            "Using Class-Based Views vs Function-Based Views in Django",
            "A Step-by-Step Guide to Setting Up Django with PostgreSQL",
            "Creating a Search Functionality in Your Django App",
            "Django Middleware: What It Is and How to Use It",
            "Authentication and Authorization in Django Made Simple",
            "Integrating Third-Party Libraries in Django Projects",
            "How to Test Your Django Application Effectively",
            "The Ultimate Guide to Django Settings and Configurations"    
        ]

        # Blog Content
        contents = [
            """Django is a high-level Python web framework that enables rapid development of secure and maintainable websites. 
            This guide walks you through the basics of Django, from installation to creating your first project.""",

            """Writing clean Python code is not just about aesthetics but also about maintainability and readability. 
            This article shares 10 practical tips to help you write better Python code, including naming conventions, 
            avoiding code repetition, and leveraging Python's built-in features.""",

            """Creating a blog is one of the best ways to get started with Django. In this tutorial, we'll show you how to 
            set up your Django project, create models, and build views and templates for your blog application.""",

            """Deploying your Django app to the cloud can seem intimidating at first, but it's easier than you think. 
            Learn how to use platforms like Heroku, AWS, or Google Cloud to deploy your Django project and make it accessible to the world.""",

            """Django offers a wide range of features that make it stand out as one of the most popular web frameworks. 
            In this blog post, we'll explore five of the most useful features, including the admin interface, ORM, and form handling.""",

            """Django's ORM is powerful but can sometimes lead to performance bottlenecks if not used correctly. 
            This article dives into query optimization techniques like select_related, prefetch_related, and using raw SQL in Django.""",

            """Choosing between Django and Flask depends on your project's needs. This blog post compares the two frameworks, 
            highlighting their strengths, weaknesses, and ideal use cases.""",

            """Django Rest Framework (DRF) is a powerful tool for building APIs with Django. In this article, we cover the 
            basics of DRF, including serializers, views, and routing.""",

            """Handling forms is an essential part of any web application. Learn how to create, process, and validate forms in Django, 
            and use Django's built-in form classes to streamline the process.""",

            """A portfolio website is a great way to showcase your work. Follow this step-by-step guide to build your own 
            portfolio site using Django, including tips for styling and adding interactive elements.""",

            """Django templates are incredibly powerful for building dynamic web pages. In this blog post, 
            we explore how to use Django's templating language effectively, including template inheritance, 
            filters, and context rendering.""",

            """Django signals are a powerful tool for decoupling components in your application. Learn how 
            to use signals to connect events like user registrations, data updates, and more.""",

            """Class-Based Views (CBVs) and Function-Based Views (FBVs) are two ways to handle requests in Django. 
            This post compares their usage, pros, and cons, and provides examples to help you choose the right approach.""",

            """PostgreSQL is a popular database for Django projects. This guide walks you through configuring Django 
            to use PostgreSQL, including installation, settings adjustments, and basic query operations.""",

            """Adding a search feature to your Django app can enhance user experience. In this blog, we show you how 
            to implement search functionality using Django's ORM and build a clean user interface.""",

            """Middleware in Django allows you to process requests and responses globally. Discover how middleware works, 
            how to create custom middleware, and some common use cases like authentication and logging.""",

            """Django provides robust tools for managing authentication and authorization. This blog post explains how to 
            implement user login, logout, permissions, and group management in your application.""",

            """Django projects often require integrating third-party libraries for additional functionality. Learn how 
            to use libraries like `django-allauth` for social authentication, `django-cors-headers` for CORS handling, and more.""",

            """Testing is essential for building reliable applications. This post introduces Django's testing framework, 
            including unit tests, integration tests, and best practices for test-driven development.""",

            """Django settings are at the core of any project configuration. Learn how to manage settings for different environments, 
            use environment variables, and organize your settings file effectively."""    
        ]

        image_urls = ["https://picsum.photos/id/1/800/400",
                    "https://picsum.photos/id/2/800/400",
                    "https://picsum.photos/id/3/800/400",
                    "https://picsum.photos/id/4/800/400",
                    "https://picsum.photos/id/5/800/400",
                    "https://picsum.photos/id/6/800/400",
                    "https://picsum.photos/id/7/800/400",
                    "https://picsum.photos/id/8/800/400",
                    "https://picsum.photos/id/9/800/400",
                    "https://picsum.photos/id/10/800/400",
                    "https://picsum.photos/id/11/800/400",
                    "https://picsum.photos/id/12/800/400",
                    "https://picsum.photos/id/13/800/400",
                    "https://picsum.photos/id/14/800/400",
                    "https://picsum.photos/id/15/800/400",
                    "https://picsum.photos/id/16/800/400",
                    "https://picsum.photos/id/17/800/400",
                    "https://picsum.photos/id/18/800/400",
                    "https://picsum.photos/id/19/800/400",
                    "https://picsum.photos/id/20/800/400"]

        categories = Category.objects.all()

        for title,content,image_url in zip(titles,contents,image_urls):
            category = random.choice(categories)
            Post.objects.create(title=title,content=content,image_url=image_url, category=category)

        self.stdout.write(self.style.SUCCESS("Complted Inserting Data!"))

