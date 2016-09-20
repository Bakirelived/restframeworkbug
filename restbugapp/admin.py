from django.contrib import admin

# Register your models here.
from restbugapp.models import *

admin.site.register([Book, Author, Publisher])