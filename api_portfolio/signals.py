import os, sys
from django.db.models.signals import post_delete, pre_save, pre_delete
from django.dispatch import receiver

from deploy_dj.utility import delete_old_files
from .models import Work, WrapperImage, Gallary, Testimonials, Abouts, Brands, Skills


@receiver(pre_save, sender=WrapperImage)
def pre_save_image(sender, instance, **kwargs):
    delete_old_files(
        sender, instance, field_names=["lgImg", "mdImg", "smImg"], pre_save=True
    )


@receiver(post_delete, sender=WrapperImage)
def post_delete_image(sender, instance, **kwargs):
    delete_old_files(
        sender, instance, field_names=["lgImg", "mdImg", "smImg"], post_delete=True
    )


@receiver(pre_save, sender=Gallary)
def pre_save_image(sender, instance, **kwargs):
    delete_old_files(sender, instance, field_names=["file"], pre_save=True)


@receiver(post_delete, sender=Gallary)
def post_delete_image(sender, instance, **kwargs):
    delete_old_files(sender, instance, field_names=["file"], post_delete=True)


@receiver(pre_save, sender=Testimonials)
def pre_save_image(sender, instance, **kwargs):
    delete_old_files(sender, instance, field_names=["imageurl"], pre_save=True)


@receiver(post_delete, sender=Testimonials)
def post_delete_image(sender, instance, **kwargs):
    delete_old_files(sender, instance, field_names=["imageurl"], post_delete=True)


@receiver(pre_save, sender=Abouts)
def pre_save_image(sender, instance, *args, **kwarg):
    print(sender)
    print(instance)
    delete_old_files(sender, instance, field_names=["imageurl"], pre_save=True)


@receiver(post_delete, sender=Abouts)
def post_delete_image(sender, instance, *args, **kwarg):
    print(sender)
    print(instance)
    delete_old_files(sender, instance, field_names=["imageurl"], post_delete=True)


@receiver(pre_save, sender=Brands)
def pre_save_image(sender, instance, *args, **kwarg):
    delete_old_files(sender, instance, field_names=["imageurl"], pre_save=True)


@receiver(post_delete, sender=Brands)
def post_delete_image(sender, instance, **kwargs):
    delete_old_files(sender, instance, field_names=["imageurl"], post_delete=True)


@receiver(pre_save, sender=Skills)
def pre_save_image(sender, instance, **kwargs):
    delete_old_files(sender, instance, field_names=["icon"], pre_save=True)


@receiver(post_delete, sender=Skills)
def post_delete_image(sender, instance, **kwargs):
    delete_old_files(sender, instance, field_names=["icon"], post_delete=True)


@receiver(pre_save, sender=Work)
def pre_save_image(sender, instance, **kwargs):
    delete_old_files(sender, instance, field_names=["imageurl"], pre_save=True)


@receiver(post_delete, sender=Work)
def post_delete_image(sender, instance, **kwargs):
    delete_old_files(sender, instance, field_names=["imageurl"], post_delete=True)
