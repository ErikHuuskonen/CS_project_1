#from django.shortcuts import render, redirect
#from django.http import HttpResponse
#from .models import MyUser

#fixed:
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.http import HttpResponse
from .models import MyUser
from django.utils.html import escape

#-------------------------------------- flaw 1:

# OWASP A03: Injection (SQL Injection)
# Vulnerability: Directly adding user input to SQL queries allows for potential malicious SQL statements.
# Fix: Use Django's ORM filtering system instead.
def search_user(request):
    if not request.GET.get('username'): return render(request, 'search.html')
    username = request.GET.get('username')
    result = MyUser.objects.raw(f"SELECT * FROM {MyUser._meta.db_table} WHERE username = '{username}'")
    if not request.GET.get('username'): return render(request, 'search.html')
    return render(request, 'results.html', {'users': result})

#fixed:
#def search_user(request):
    #username = request.GET.get('username')
    #Fixed: Using Django ORM to prevent SQL injection.
    #result = MyUser.objects.filter(username=username)
    #if not request.GET.get('username'): return render(request, 'search.html')
    #return render(request, 'results.html', {'users': result})


#-------------------------------------- flaw 2:

# OWASP A07: Identification and Authentication Failures
# Vulnerability: Passwords should not be handled in plain text. Also, the login implementation is missing.
# Fix: Use Django's built-in authentication system.
def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if MyUser.objects.filter(username=username).exists():
            # Log in (This part should be implemented with Django's auth system)
            return HttpResponse("Tervetuloa, {}!".format(username))
        else:
            return HttpResponse("Virheellinen käyttäjänimi tai salasana.")
    return render(request, 'login.html')

#fixed:
#def login(request):
    #if request.method == "POST":
        #username = request.POST.get('username')
        #password = request.POST.get('password')
        # Fixed: Using Django's built-in authentication system.
        #user = authenticate(request, username=username, password=password)
        #if user is not None:
            #django_login(request, user)
            #return HttpResponse("Welcome, {}!".format(escape(username)))
        #else:
            #return HttpResponse("Invalid username or password.")
    #return render(request, 'login.html')

#-------------------------------------- flaw 3:

# OWASP A01: Broken Access Control
# Vulnerability: This function allows any user to view the details of all users in the system.
def show_users(request):
    users = MyUser.objects.all()
    return render(request, 'users.html', {'users': users})
    
# Fix: Implement access control checks to ensure only authorized users (e.g., administrators) can view all user details.
#if not request.user.is_authenticated or not request.user.is_staff:
#return HttpResponse("Ei oikeutta näyttää kaikkia käyttäjiä.")
#fixed:
# Fixed: Added access control so only staff can view all user details.
#def show_users(request):
    #if not request.user.is_authenticated or not request.user.is_staff:
        #return HttpResponse("No permission to view all users.")
    #users = MyUser.objects.all()
    #return render(request, 'users.html', {'users': users})

#-------------------------------------- flaw 4:

# OWASP A01: Broken Access Control (IDOR)
# Vulnerability: Any user can open any profile by changing user_id in the URL.
def view_profile(request, user_id):
    user = MyUser.objects.get(pk=user_id)
    return render(request, 'profile.html', {'user': user})

#fixed:
#def view_profile(request, user_id):
    #if not request.user.is_authenticated:
        #return HttpResponse("Please log in.", status=401)
    #if request.user.id != user_id and not request.user.is_staff:
        #return HttpResponse("No permission.", status=403)
    #user = MyUser.objects.get(pk=user_id)
    #safe_data = {
    #'username': user.username,
    #'first_name': user.first_name,
    #'last_name': user.last_name,
    #}
    #return render(request, 'profile.html', {'user': safe_data})

#-------------------------------------- flaw 5:

# OWASP A03: Injection (Stored Cross-Site Scripting)
# Vulnerability: Comments are stored and rendered unsafely without escaping.
def comment(request):
    if request.method == "POST":
        user_comment = request.POST.get('comment')
        user = MyUser.objects.first()
        if user:
            user.comment = user_comment
            user.save()
    all_comments = MyUser.objects.exclude(comment__isnull=True).exclude(comment__exact='')
    return render(request, 'comment.html', {'comments': all_comments})

#fixed:
#def comment(request):
    #if request.method == "POST":
        #user_comment = request.POST.get('comment')
        #user = MyUser.objects.first()
        #if user:
            #user.comment = escape(user_comment)
            #user.save()
    #all_comments = MyUser.objects.exclude(comment__isnull=True).exclude(comment__exact='')
    #return render(request, 'comment.html', {'comments': all_comments})
