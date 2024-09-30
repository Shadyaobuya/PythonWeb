# Create your models here.

from django.db import models
from django.utils import timezone


class ModificationTrackingModel(models.Model):
    created_by = models.CharField(
        null=True, blank=True, help_text="User who created record", max_length=30
    )
    modified_by = models.CharField(
        null=True, blank=True, help_text="User who modified record", max_length=30
    )
    created_at = models.DateTimeField(
        # auto_now_add=True,
        help_text="Time record was created",
        max_length=30,
        default=timezone.now,
        null=True,
    )
    modified_at = models.DateTimeField(
        # auto_now=True,
        help_text="Time record was modified",
        max_length=30,
        default=timezone.now,
        null=True,
    )
