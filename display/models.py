from django.conf import settings
from django.db import models


class QuoteModel(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=120, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 null=True, blank=True, on_delete=models.SET_NULL)

    # TODO: This is not working. fix or remove
    def save_model(self, request, obj, form, change):
        if not obj.added_by.id:
            obj.added_by = request.user
        obj.updated = request.user
        obj.save()

    def __str__(self):
        return self.quote
