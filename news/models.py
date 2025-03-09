from django.db import models
from django.utils import timezone

class News(models.Model):
    headline = models.CharField(max_length=200)
    body = models.TextField()
    published_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.headline

    def formatted_published_date(self):
        return self.published_date.strftime('%B %d, %Y')  # Formato: 'May 21, 2021'
