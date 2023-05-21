
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.views import LoginView
from .models import Document


def render_login(request):
    return render(request, 'login.html')


def perform_login(request):
    if request.method != "POST":
        return HttResponse("Method is not allowed")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user_obj = authenticate(request, username=username, password=password)
        if user_obj is not None:
            login(request, user_obj)
            next_url = request.GET.get('next', reverse('admin_dashboard'))
            return HttpResponseRedirect(next_url)
        else:
            messages.error(request, "Invalid username or password",
                           extra_tags='alert alert-danger')
            return HttpResponseRedirect(reverse('render_login') + "?next=" + request.GET.get('next', ''))


@login_required
def admin_dashboard(request):
    if not request.user.is_authenticated:
        messages.error(request, "Please login first to access this page.")
        return HttpResponseRedirect(reverse('render_login') + "?next=" + request.path)
    else:
        username = request.user.username
        return render(request, "admin_dashboard.html", {'username': username})


def perform_logout(request):
    logout(request)
    return HttpResponseRedirect("/")


def all_members(request):
    return render(request, 'all_members.html')


def add_member(request):
    return render(request, 'add_member.html')


def executive(request):
    return render(request, 'executive.html')


def active_members(request):
    return render(request, 'active_members.html')


def affiliate_members(request):
    return render(request, 'affiliate_members.html')


def patrons(request):
    return render(request, 'patrons.html')

# def document(request):
#     if request.method == 'POST':
#         document = Document()
#         document.name = request.POST['document_name']
#         document.image = request.FILES['document_image']
#        document = Document(document_name=document_name, document_image=document_image)
#         document.save()
#         return redirect('document')
#     return render(request, 'document.html')


def document(request):
    success_message = None
    
    if request.method == 'POST':
        document_name = request.POST['document_name']
        document_image = request.FILES['document_image']
        
        document = Document(document_name=document_name, document_image=document_image)
        document.save()

        success_message = 'Document saved successfully.'

    return render(request, 'document.html', {'success_message': success_message})
