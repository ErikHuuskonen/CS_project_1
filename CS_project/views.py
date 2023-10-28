#from django.shortcuts import render, redirect
#from django.http import HttpResponse
#from .models import MyUser

#fixed:
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.http import HttpResponse
from .models import MyUser
from django.utils.html import escape


#def search_user(request):
    #username = request.GET.get('username')
    # OWASP: SQL Injection
    # Vulnerability: Directly adding user input to SQL queries allows for potential malicious SQL statements.
    # Fix: Use Django's ORM filtering system instead.
    #result = MyUser.objects.raw('SELECT * FROM user WHERE username = ' + username)
    #return render(request, 'results.html', {'users': result})
#fixed:
def search_user(request):
    username = request.GET.get('username')
    # Fixed: Using Django ORM to prevent SQL injection.
    result = MyUser.objects.filter(username=username)
    return render(request, 'results.html', {'users': result})



#def login(request):
    #if request.method == "POST":
        #username = request.POST.get('username')
        #password = request.POST.get('password')
        # OWASP: Broken Authentication
        # Vulnerability: Passwords should not be handled in plain text. Also, the login implementation is missing.
        # Fix: Use Django's built-in authentication system.
        #if MyUser.objects.filter(username=username).exists():
            # Log in (This part should be implemented with Django's auth system)
            #return HttpResponse("Tervetuloa, {}!".format(username))
        #else:
            #return HttpResponse("Virheellinen käyttäjänimi tai salasana.")
    #return render(request, 'login.html')
#fixed:
def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Fixed: Using Django's built-in authentication system.
        user = authenticate(request, username=username, password=password)
        if user is not None:
            django_login(request, user)
            return HttpResponse("Welcome, {}!".format(escape(username)))
        else:
            return HttpResponse("Invalid username or password.")
    return render(request, 'login.html')



#def show_users(request):
    # OWASP: Broken Access Control
    # Vulnerability: This function allows any user to view the details of all users in the system.
    #users = MyUser.objects.all()
    #return render(request, 'users.html', {'users': users})
    # Fix: Implement access control checks to ensure only authorized users (e.g., administrators) can view all user details.
    #if not request.user.is_authenticated or not request.user.is_staff:
    #return HttpResponse("Ei oikeutta näyttää kaikkia käyttäjiä.")
#fixed:
def show_users(request):
    # Fixed: Added access control so only staff can view all user details.
    if not request.user.is_authenticated or not request.user.is_staff:
        return HttpResponse("No permission to view all users.")
    users = MyUser.objects.all()
    return render(request, 'users.html', {'users': users})



#def view_profile(request, user_id):
    # OWASP: Sensitive Data Exposure
    # Vulnerability: Depending on the MyUser model, this could potentially expose sensitive data.
    # Fix: Only show necessary user data, and ensure sensitive data like passwords are never exposed.
    #user = MyUser.objects.get(pk=user_id)
    #return render(request, 'profile.html', {'user': user})
#fixed:
def view_profile(request, user_id):
    # Assuming that the MyUser model does not contain sensitive information like plaintext passwords.
    # It's crucial here to ensure only necessary details are shown.
    user = MyUser.objects.get(pk=user_id)
    return render(request, 'profile.html', {'user': user})



#def comment(request):
    #if request.method == "POST":
        #user_comment = request.POST.get('comment')
        # OWASP: Cross-Site Scripting (XSS)
        # Vulnerability: Without proper validation and escaping, user-provided data can lead to script execution.
        # Fix: Ensure any user-provided data is properly sanitized before displaying it back on a page.
        # Save the comment to the database (implementation missing)
        # Display comments (implementation missing)
        #return HttpResponse("Kommenttisi on tallennettu!")
    #return render(request, 'comment.html')
#fixed:
def comment(request):
    if request.method == "POST":
        user_comment = request.POST.get('comment')
        # Fixed: Preventing possible XSS vulnerability with code execution.
        sanitized_comment = escape(user_comment)
        # At this point, the comment would be saved to the database and shown to the user.
        return HttpResponse("Your comment has been saved!")
    return render(request, 'comment.html')

