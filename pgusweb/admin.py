from django.contrib import admin
from cms.extensions import PageExtensionAdmin

from .models import ResolutionExtension


class ResolutionExtensionAdmin(PageExtensionAdmin):
    pass

admin.site.register(ResolutionExtension, ResolutionExtensionAdmin)
