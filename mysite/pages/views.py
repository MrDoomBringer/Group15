from django.http import HttpResponse
from .models import ToDoList
from .forms import CreateNewList
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import User, Task


def index(request):
    template_name = 'pages/home.html'
    return render(request, template_name)

def faq(request):
    return HttpResponse("FAQ")

def howto(request):
    return HttpResponse("How To")

def account(request):
    return HttpResponse("Account Page")

class CalendarView(generic.ListView):
    template_name = 'pages/tasks.html'
    context_object_name = 'tsk_list'

    def get_queryset(self):
        """Return the published tasks."""
        return Task.objects.filter(due_date__lte=timezone.now()).order_by('-due_date')

def tos(request):
    return HttpResponse("Terms of Service")

def create(response):
	if response.method == "POST":
		form = CreateNewList(response.POST)
		if form.is_valid():
			n = form.cleaned_data["name"]
			t = ToDoList(name=n)
			t.save()

		return HttpResponseRedirect("/%i" %t.id)
	else:
		form = CreateNewList()
	return render(response, "pages/create.html", {"form": form})
