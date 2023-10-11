from datetime import timezone
from django.db import models
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from PIL import Image
import sys
from django.db.models.signals import pre_save, post_delete

from deploy_dj.utility import delete_old_files

def upload_to(instance, filename):
    model_name = instance.__class__.__name__.lower()
    return f"{model_name}/{filename}"


def compress_images(uploadedImage, width=200, height=200, format="JPEG"):
    lower_format = str(format).lower()
    try:
        imageTemproary = Image.open(uploadedImage)
        imageTemproary = imageTemproary.resize((width, height))
        if format in ["JPEG", "jpeg", "Jpeg", "JPG", "Jpg", "jpg"]:
            imageTemproary = imageTemproary.convert("RGB")
        outputIoStream = BytesIO()
        outputIoStream.seek(0)
        imageTemproary.save(outputIoStream, format=f"{format}", quality=95)
        uploadedImage = InMemoryUploadedFile(
            outputIoStream,
            "ImageField",
            f'{uploadedImage.name.split(".")[0]}.{lower_format}',
            f"image/{lower_format}",
            sys.getsizeof(outputIoStream),
            None,
        )
    except:
        uploadedImage = uploadedImage
    return uploadedImage


class WrapperImage(models.Model):
    bgImg = models.ImageField(_("Big Image"), upload_to=upload_to)
    mdImg = models.ImageField(_("Normal Image"), upload_to=upload_to)
    smImg = models.ImageField(_("Small Image"), upload_to=upload_to)
    use = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Wrapper Image"
        verbose_name_plural = "Wrapper Images"


class Gallary(models.Model):
    file = models.ImageField(_("Image"), upload_to=upload_to)
    use = models.BooleanField(default=True)

    class Meta:
        """Meta definition for Gallary."""

        verbose_name = "Gallary"
        verbose_name_plural = "Gallary"


class FirmLogo(models.Model):
    title = models.CharField(max_length=100)
    logo = models.ImageField(upload_to=upload_to)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    use = models.BooleanField()

    def save(self, *args, **kwargs):
        if self.use:
            FirmLogo.objects.exclude(pk=self.pk).filter(use=True).update(use=False)
        super(FirmLogo, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Note(models.Model):
    welcome = models.CharField(max_length=50)
    detail = models.CharField(max_length=100)
    note = models.TextField(
        _("nate"),
        default="Zilla Tech: Where Innovation Meets Success. Join us on the journey!",
    )
    use = models.BooleanField(default=True)

    class Meta:
        """Meta definition for Note."""

        verbose_name = "Note"
        verbose_name_plural = "Notes"

    def __str__(self):
        return self.welcome


class Info(models.Model):
    contact = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    use = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        # Check if this instance is becoming active
        if self.use:
            # Deactivate all other active banners
            Info.objects.exclude(pk=self.pk).filter(use=True).update(use=False)

        super(Info, self).save(*args, **kwargs)

    def __str__(self):
        return self.contact


class Testimonials(models.Model):
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    imageurl = models.ImageField(_("Image"), upload_to=upload_to)
    feedback = models.CharField(max_length=200)
    use = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Testimonials"
        verbose_name_plural = "Testimonials"

    def save(self, *args, **kwargs):
        self.imageurl = compress_images(self.imageurl)
        super(Testimonials, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Abouts(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    imageurl = models.ImageField(_("Image"), upload_to=upload_to)
    use = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.imageurl = compress_images(self.imageurl)
        super(Abouts, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Abouts"
        verbose_name_plural = "Abouts"

    def __str__(self):
        return self.title


class Brands(models.Model):
    name = models.CharField(max_length=150)
    imageurl = models.ImageField(_("Image"), upload_to=upload_to)
    use = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Brands"
        verbose_name_plural = "Brands"

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    message = models.TextField()

    def __str__(self):
        return self.name


class Experience(models.Model):
    year = models.CharField(blank=True, max_length=50)
    work = models.ManyToManyField(
        "WorkExperience", blank=True, related_name="experiences"
    )
    use = models.BooleanField(default=True)

    def __str__(self):
        return self.year


class Skills(models.Model):
    name = models.CharField(max_length=150)
    bgColor = models.CharField(blank=True, max_length=100)
    icon = models.ImageField(_("Icon"), upload_to=upload_to)
    use = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Skills")
        verbose_name_plural = _("Skills")

    def __str__(self):
        return self.name


class WorkExperience(models.Model):
    name = models.CharField(max_length=150)
    company = models.CharField(max_length=150)
    desc = models.CharField(max_length=150)
    use = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Work(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    projectLink = models.CharField(max_length=150)
    codeLink = models.CharField(max_length=150)
    imageurl = models.ImageField(_("Image"), upload_to=upload_to)
    tag = models.ManyToManyField("Tag", blank=True, related_name="works")
    use = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.imageurl = compress_images(self.imageurl)
        super(Work, self).save(*args, **kwargs)


class Tag(models.Model):
    tag = models.CharField(max_length=150)
    use = models.BooleanField(default=True)

    def __str__(self):
        return self.tag
