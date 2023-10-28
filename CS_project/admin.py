from django.contrib import admin
from .models import MyUser  # vaihda tämä jos nimesit mallisi eri tavalla

admin.site.register(MyUser)
