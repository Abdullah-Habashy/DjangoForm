from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.users, name='users'),
    path('signup/', views.signup, name='signup'),
]

# path: the link after app to show this view
# view.index : refer to the function (view) rendered when request the link main/apppath/viewpath/
