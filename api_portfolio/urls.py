from django.urls import path
from .views import *

urlpatterns = [
    path("", Home, name="home"),
    path("testimonials/", testimonial_list_create_view, name="testimonial"),
    path("skills/", skill_list_create_view, name="skills"),
    path("abouts/", about_list_create_view, name="abouts"),
    path("gallary/", gallary_list_create_view, name="gallary"),
    path("notes/", notes_list_create_view, name="notes"),
    path("info/", info_list_create_view, name="info"),
    path("wrapperImages/", wrapperImage_list_create_view, name="wrapperImages"),
    path("work_experiences/", workexperience_list_create_view, name="work-experiences"),
    path("experiences/", experience_list_create_view, name="experiences"),
    path("contacts/", contact_list_create_view, name="contacts"),
    path("firmLogos/", firmLogos_list_create_view, name="firmLogos"),
    path("brands/", brand_list_create_view, name="brands"),
    path("works/", work_list_create_view, name="works"),
    path("tags/", tag_list_create_view, name="tags"),
]
