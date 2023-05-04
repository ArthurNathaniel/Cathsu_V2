# # from django.http.response import HttpResponse, HttpResponseRedirect
# # from django.shortcuts import render
# # from django.contrib.auth import authenticate, login, logout
# # from django.urls import reverse 
# # from django.contrib import messages
# # from django.contrib.auth.views import LoginView
# # from django.contrib.auth.decorators import login_required

# # Create your views here.


# # def render_login(request):
# #     return render(request, 'login.html')




# # def perform_login(request):
# #     if request.method != "POST":
# #         return HttResponse("Method is not allowed")
# #     else:
# #         username = request.POST.get("username")
# #         password = request.POST.get("password")
# #         user_obj = authenticate(request, username=username, password=password)
# #         if user_obj is not None:
# #             login(request, user_obj)
# #             return HttpResponseRedirect(reverse("admin_dashboard"))
# #         else:
# #             messages.error(request, "Username or Password is Invalid")
# #             return HttpResponseRedirect("/")


# # def admin_dashboard(request):
# #     return render(request, "admin_dashboard.html")


# # def perform_logout(request):
# #     logout(request)
# #     return HttpResponseRedirect("/")


# # from django.http.response import HttpResponse, HttpResponseRedirect
# # from django.shortcuts import render
# # from django.contrib.auth import authenticate, login, logout
# # from django.urls import reverse
# # from django.contrib import messages
# # from django.contrib.auth.views import LoginView
# # # import the login_required decorator
# # from django.contrib.auth.decorators import login_required


# # def render_login(request):
# #     return render(request, 'login.html')


# # def perform_login(request):
# #     if request.method != "POST":
# #         return HttpResponse("Method is not allowed")
# #     else:
# #         username = request.POST.get("username")
# #         password = request.POST.get("password")
# #         user_obj = authenticate(request, username=username, password=password)
# #         if user_obj is not None:
# #             login(request, user_obj)
# #             return HttpResponseRedirect(reverse("admin_dashboard"))
# #         else:
# #             messages.error(request, "Username or Password is Invalid")
# #             return HttpResponseRedirect("/")


# # add the login_required decorator to restrict access to authenticated users only
# # @login_required
# # def admin_dashboard(request):
# #     return render(request, "admin_dashboard.html")


# # def perform_logout(request):
# #     logout(request)
# #     return HttpResponseRedirect("/")


# from django.http.response import HttpResponse, HttpResponseRedirect
# from django.shortcuts import render
# from django.contrib.auth import authenticate, login, logout
# from django.urls import reverse
# from django.contrib import messages
# from django.contrib.auth.views import LoginView


# def render_login(request):
#     return render(request, 'login.html')


# def perform_login(request):
#     if request.method != "POST":
#         return HttResponse("Method is not allowed")
#     else:
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         user_obj = authenticate(request, username=username, password=password)
#         if user_obj is not None:
#             login(request, user_obj)
#             next_url = request.GET.get('next', reverse('admin_dashboard'))
#             return HttpResponseRedirect(next_url)
#         else:
#             messages.error(request, "Username or Password is Invalid")
#             return HttpResponseRedirect(reverse('render_login') + "?next=" + request.GET.get('next', ''))


# def admin_dashboard(request):
#     if not request.user.is_authenticated:
#         messages.error(request, "Please login first to access this page.")
#         return HttpResponseRedirect(reverse('render_login') + "?next=" + request.path)
#     else:
#         return render(request, "admin_dashboard.html")


# def perform_logout(request):
#     logout(request)
#     return HttpResponseRedirect("/")

from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.views import LoginView


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


# def admin_dashboard(request):
#     if not request.user.is_authenticated:
#         messages.error(request, "Please login first to access this page.",
#                        extra_tags='alert alert-danger')
#         return HttpResponseRedirect(reverse('render_login') + "?next=" + request.path)
#     else:
#         return render(request, "admin_dashboard.html")

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
