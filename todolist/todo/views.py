from django.shortcuts import render, get_object_or_404
from .models import To
from django.shortcuts import redirect

def todo_list(request):
	to = To.objects.all()
	return render(request, 'todo/todo_list.html', {'to': to})

# Create your views here.
