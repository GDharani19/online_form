from django.urls import path
from feedback import views

urlpatterns=[
    path('home/',views.createfeed,name="home"),
    path('read/',views.readfeed,name="read"),
    path('update/<pk>',views.updatefeed,name="update"),
    path('delete/<pk>',views.deletefeed,name="delete")
]
