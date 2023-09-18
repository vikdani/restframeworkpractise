
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.Studentlist.as_view()),
    #path('studentapi/', views.Studentcreate.as_view()),
    #path('studentapi/<int:pk>', views.Studentretrieve.as_view()),
    # path('studentapi/<int:pk>', views.Studentupdate.as_view()),
    path('studentapi/<int:pk>', views.Studentdestroy.as_view()),




]
