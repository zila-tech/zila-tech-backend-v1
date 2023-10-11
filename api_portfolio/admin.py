from django.contrib import admin

import admin_thumbnails
from django.http import HttpResponse
from django.urls import reverse
from django.utils.html import format_html
from django.template import loader
from .models import (
    Abouts,
    Brands,
    Contact,
    Experience,
    FirmLogo,
    Gallary,
    Info,
    Note,
    Skills,
    Tag,
    Testimonials,
    Work,
    WorkExperience,
    WrapperImage,
)

# Register your models here.

admin.site.site_header = "ZILA TECH administration"


class BaseUse:
    def check_selected(self, request, queryset):
        queryset.update(use=True)

    check_selected.short_description = "Check selected items"

    # Define a custom admin action to uncheck all selected records.
    def uncheck_selected(self, request, queryset):
        queryset.update(use=False)

    uncheck_selected.short_description = "Uncheck selected items"


@admin.register(Testimonials)
@admin_thumbnails.thumbnail("imageurl")
class TestimonialsAdmin(admin.ModelAdmin, BaseUse):
    list_display = ("name", "company", "imageurl_thumbnail", "feedback", "use")
    search_fields = ("name", "company", "imageurl_thumbnail", "feedback")
    list_filter = ("name", "use")
    list_editable = ("use",)
    actions = ["check_selected", "uncheck_selected"]


@admin_thumbnails.thumbnail("imageurl")
@admin.register(Abouts)
class AboutsAdmin(admin.ModelAdmin, BaseUse):
    list_display = ("title", "description", "imageurl_thumbnail", "use")
    search_fields = ("title", "description", "imageurl_thumbnail")
    list_filter = ("title", "use")
    list_editable = ("use",)
    actions = ["check_selected", "uncheck_selected"]


@admin.register(Brands)
@admin_thumbnails.thumbnail("imageurl")
class BrandsAdmin(admin.ModelAdmin, BaseUse):
    list_display = ("name", "imageurl_thumbnail", "use")
    search_fields = ("name",)
    list_filter = ("name", "use")
    list_editable = ("use",)
    actions = ["check_selected", "uncheck_selected"]


@admin.register(Skills)
@admin_thumbnails.thumbnail("icon")
class SkillsAdmin(admin.ModelAdmin, BaseUse):
    list_display = ("name", "bgColor", "icon_thumbnail", "use")
    search_fields = ("name",)
    list_filter = ("name", "use")
    list_editable = ("use",)
    actions = ["check_selected", "uncheck_selected"]


@admin.register(Gallary)
@admin_thumbnails.thumbnail("file")
class GallaryAdmin(admin.ModelAdmin, BaseUse):
    list_display = ("file_thumbnail", "use")
    list_filter = ("use",)
    list_editable = ("use",)

    actions = ["check_selected", "uncheck_selected"]


@admin.register(WrapperImage)
@admin_thumbnails.thumbnail("bgImg", "Big Image")
@admin_thumbnails.thumbnail("mdImg", "Normal Image")
@admin_thumbnails.thumbnail("smImg", "Small Image")
class WrapperImageAdmin(admin.ModelAdmin, BaseUse):
    list_display = ("bgImg_thumbnail", "mdImg_thumbnail", "smImg_thumbnail", "use")
    list_filter = ("use",)
    list_editable = ("use",)
    actions = ["check_selected", "uncheck_selected"]


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "short_message",
    )  # Add 'short_message' to the list_display
    search_fields = ("name", "email", "message")
    list_filter = ("name",)

    # Define a function to get a truncated version of the message
    def short_message(self, obj):
        return obj.message[:50] + "..." if len(obj.message) > 50 else obj.message

    short_message.short_description = "Message"  # Set a user-friendly column name


admin.site.register(Contact, ContactAdmin)


@admin.register(Info)
class InfoAdmin(admin.ModelAdmin, BaseUse):
    list_display = ("contact", "email", "use")
    search_fields = ("contact", "email")
    list_filter = ("use", "contact", "email")
    list_editable = ("use",)
    actions = ["check_selected", "uncheck_selected"]


@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin, BaseUse):
    list_display = ("name", "company", "desc", "use")
    search_fields = ("name", "company", "desc")
    list_filter = ("name", "company", "use")
    list_editable = ("use",)
    actions = ["check_selected", "uncheck_selected"]


@admin.register(FirmLogo)
@admin_thumbnails.thumbnail("logo", "Firm Logo")
class FirmLogoAdmin(admin.ModelAdmin, BaseUse):
    list_display = ("title", "logo_thumbnail", "date_created", "use")
    search_fields = ("title", "date_created")
    list_filter = ("title", "date_created", "use")
    list_editable = ("use",)


@admin.register(Work)
@admin_thumbnails.thumbnail("imageurl")
class WorkAdmin(admin.ModelAdmin, BaseUse):
    list_display = (
        "title",
        "description",
        "projectLink",
        "codeLink",
        "imageurl_thumbnail",
        "use",
    )
    search_fields = (
        "title",
        "description",
    )
    list_editable = ("use",)
    actions = ["check_selected", "uncheck_selected"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin, BaseUse):
    list_display = ("tag", "use")
    search_fields = ("tag",)
    list_filter = ("tag", "use")
    list_editable = ("use",)
    actions = ["check_selected", "uncheck_selected"]


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin, BaseUse):
    list_display = ("year", "use")
    list_filter = ("year", "use")
    list_editable = ("use",)
    actions = ["check_selected", "uncheck_selected"]


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin, BaseUse):
    list_display = ("welcome", "detail", "use")
    search_fields = ("welcome", "detail", "use")
    list_filter = ("welcome", "detail", "use")
    list_editable = ("use",)

    # Define a custom admin action to check all selected records.

    def print_selected_items(self, request, queryset):
        # Load the template for the preview page
        template = loader.get_template("notes_preview.html")

        # Prepare the context with the selected notes
        context = {
            "notes": queryset,
        }

        # Render the template to HTML
        preview_content = template.render(context)

        # Create a response with the preview HTML content
        response = HttpResponse(preview_content, content_type="text/html")
        return response

    print_selected_items.short_description = "Preview Selected Items"

    actions = ["check_selected", "uncheck_selected", print_selected_items]
