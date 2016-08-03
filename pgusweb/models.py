from django.db import models

from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool


class ResolutionExtension(PageExtension):
    APPROVED = "APPROVED"
    NOT_APPROVED = "NOT APPROVED"
    PENDING = "PENDING"

    ACTION_CHOICES = (
        (APPROVED,  "Approved"),
        (NOT_APPROVED, "Not Approved"),
        (PENDING, "Pending"),
    )

    date = models.DateField()
    title = models.CharField(max_length=40)
    action = models.CharField(
        max_length = 12,
        choices = ACTION_CHOICES,
        default = PENDING,
    )
    resolution = models.TextField()
    vote_record = models.TextField()

extension_pool.register(ResolutionExtension)
