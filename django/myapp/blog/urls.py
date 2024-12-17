from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path("",views.index, name="index"),
    path("post/<str:slug>",views.detail,name="detail"),
    path("old_url", views.old_url_view, name="old_url"),
    path("new_url/<int:post_id>", views.new_url_view, name="new_url_path"),
    path("contact", views.contact_view, name="contact"),
    path("about", views.about_view, name="about"),
]