
from django.db import models

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')  # Specify the directory for uploaded files
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Optional: timestamp of upload

    def __str__(self):
        return self.file.name
