'''URL Patterns for Learning_logs app'''
from django.urls import path
from . import views

urlpatterns = [
 	# Home page
 	path('contacts/', views.IndexView.as_view(), name='index'),
 	#The topics page 
 	path('contacts/<int:pk>/', views.ContactDetailView.as_view(), name='detail'),
 	# Viewing individual topic entries 
 	path('contacts/edit/<int:pk>/', views.edit, name='edit'),
 	# Adding a new topic 
 	 path('contacts/create/', views.create, name='create'),
 	# url for adding a new entry about a given topic 
 	path('contacts/delete/<int:pk>/', views.delete, name='delete'),
 	

	]
