from django.db import models

class ATAcontent(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.uploaded_at} - {self.title}"