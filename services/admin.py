from django.contrib import admin
from .models import Service
from .models import Article
from .models import FeedbackMessage

# Register your models here.

admin.site.register(Service)
admin.site.register(Article)
admin.site.register(FeedbackMessage)
