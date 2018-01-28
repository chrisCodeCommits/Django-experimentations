from django.contrib import admin

# Here, register models.
from .models import Posts

admin.site.register(Posts)
