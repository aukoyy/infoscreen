from django.contrib import admin

# Register your models here.

from .models import QuoteModel

admin.site.register(QuoteModel)

