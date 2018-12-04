from django.contrib import admin
from .models import Chat, Source, File, Directory
# Register your models here.

admin.site.register(Chat)
admin.site.register(Source)
admin.site.register(File)
admin.site.register(Directory)