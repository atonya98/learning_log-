from django.shortcuts import render
from django.http import HttpResponse
from .models import Topic,Entry
from django.http import HttpResponseRedirect,Http404
from django.urls import reverse
from .forms import TopicForm,EntryForm 
from django.contrib.auth.decorators import login_required

# Home page
def index(request):
	return render(request, 'learning_logs/index.html')

# Page for all the topics
@login_required 
def topics(request):
	'''shows all topics '''
	topics = Topic.objects.filter(owner=request.user).order_by('date_added')
	# topics = Topic.objects.order_by('date_added')
	context = {'topics': topics}
	return render(request, 'learning_logs/topics.html', context)

#Page for viewing each topic individually
@login_required
def topic(request,topic_id):
	topic = Topic.objects.get(id = topic_id)
	# Make sure the topic belongs to the current user
	if topic.owner != request.user:
		raise Http404

	entries =  topic.entry_set.all().order_by('-date_added') # return entries in reverse order
	context = {'topic':topic, 'entries': entries}
	return render(request, 'learning_logs/topic.html',context)


	
# view for adding a new topic
@login_required 
def new_topic(request):
	'''add new topic'''
	if request.method != 'POST':
		# no data is submitted, return a blank form 
		form = TopicForm()
	else:
		#Post data submitted 
		form = TopicForm(request.POST)
		if form.is_valid():
			new_topic = form.save(commit=False)
			new_topic.owner = request.user
			new_topic.save()
			# form.save()
			return HttpResponseRedirect(reverse('topics'))

	context = {'form': form}
	return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request,topic_id):
	topic = Topic.objects.get(id = topic_id)
	# POST data not submitted , return a blank form 
	if request.method != 'POST':
		form  = EntryForm()
	else:
		# Post data submitted, Process data
		form = EntryForm(data = request.POST) 
		if form.is_valid():
			new_entry = form.save(commit = False)
			new_entry.topic = topic
			new_entry.save()
			return HttpResponseRedirect(reverse('topic',args=[topic_id]))
 
	context = {'topic': topic, 'form': form}
	return render(request, 'learning_logs/new_entry.html', context)


def edit_entry(request,entry_id):
	entry = Entry.objects.get(id = entry_id)
	topic = entry.topic

	if request.method != 'POST':
		#Initial request, prefill form with exixsting entry
		form = EntryForm(instance = entry)
	else:
		# POST data submitted , process data 
		form = EntryForm(instance = entry, data = request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('topic',args=[topic.id]))

	context = {'entry': entry, 'topic': topic, 'form': form}
	return render(request, 'learning_logs/edit_entry.html', context)


def delete_entry(request,entry_id):
	entry = Entry.objects.get(id = entry_id)
	topic = entry.topic
	context = {}
	if request.method == 'POST':
		entry.delete()
		return HttpResponseRedirect("/")
		


	return render(request, 'learning_logs/delete_entry.html',context)




