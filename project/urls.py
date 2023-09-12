from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', StudentList.as_view(), name='home'),
    path('detail/<int:id>', StudentDetails.as_view(), name='detail'),
    path('delete/<int:pk>', StudentDelete.as_view(), name='delete'),
    path('create/', StudentCreate.as_view(), name='add'),
    path('update/<int:pk>', StudentUpdate.as_view(), name='update'),
    path('signup/', Signup.as_view(), name='signup')
]
