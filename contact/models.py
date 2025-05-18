import re

from django.core.exceptions import ValidationError
from django.db import models
from django.conf import settings


class ContactInquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='contact_inquiries_updated'
    )
    is_resolved = models.BooleanField(default=False)

    def clean(self):
        # Validate mobile number format (e.g., +1234567890 or 1234567890)
        if self.mobile_number:
            if not re.match(r'^\+?\d{9,15}$', self.mobile_number):
                raise ValidationError(
                    {'mobile_number': 'Enter a valid mobile number (e.g., +1234567890 or 1234567890)'})

    def save(self, *args, **kwargs):
        # Run validation before saving
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.email}"
