'''URL Patterns for Learning_logs app'''
from django.urls import path
from . import views

urlpatterns = [
 	# Home page
 	path('', views.index, name='index'),
 	#The topics page 
 	path('topics/', views.topics , name = 'topics'),
 	# Viewing individual topic entries 
 	path('topic/<int:topic_id>', views.topic, name='topic'),
 	# Adding a new topic 
 	path('new_topic/', views.new_topic, name = 'new_topic'),
 	# url for adding a new entry about a given topic 
 	path('new_entry/<int:topic_id>', views.new_entry, name='new_entry'),
 	# page for edititng an entry 
 	path('edit_entry/<int:entry_id>',views.edit_entry, name = 'edit_entry'),


	]
