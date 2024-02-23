from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    content = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    # Add fields for extra information (e.g., link to a specific object)
    link_object_type = models.CharField(max_length=50, blank=True, null=True)
    link_object_id = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} - {self.content}'

    def mark_as_read(self):
        """
        Mark the notification as read.
        """
        self.is_read = True
        self.save()

    def get_link_object(self):
        """
        Get the linked object (if any) associated with the notification.
        Implement this method based on your application's structure.
        """
        if self.link_object_type and self.link_object_id:
            # Assuming you have a function to get the linked object based on type and id
            return get_linked_object(self.link_object_type, self.link_object_id)
        return None
