from django.db import models

class EmailMessage(models.Model):
    content = models.TextField()
    receiver_email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message sent to {self.receiver_email} at {self.created_at}"
