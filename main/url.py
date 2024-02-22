from django.urls import path
from.views import home_page_view,about_page_view,contact

urlpatterns=[
    path("",home_page_view,name="home" ),
    path('about/',about_page_view, name="about_page" ),
    path("contact/", contact, name="contact"),
]