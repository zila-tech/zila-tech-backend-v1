from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *
from django.shortcuts import redirect, render

# Create your views here.


def Home(request):
    return HttpResponse("Hello worldWelcome to my potfolio")


class ExperienceListCreateView(generics.ListCreateAPIView):
    queryset = Experience.objects.filter(use=True)
    serializer_class = ExperienceSerializer


experience_list_create_view = ExperienceListCreateView.as_view()


class SkillListCreateView(generics.ListCreateAPIView):
    queryset = Skills.objects.filter(use=True)
    serializer_class = SkillsSerializer


skill_list_create_view = SkillListCreateView.as_view()


class WorkExperienceListCreateView(generics.ListCreateAPIView):
    queryset = WorkExperience.objects.filter(use=True)
    serializer_class = WorkExperienceSerializer


workexperience_list_create_view = WorkExperienceListCreateView.as_view()


class ContactListCreateView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


contact_list_create_view = ContactListCreateView.as_view()


class BrandListCreateView(generics.ListCreateAPIView):
    queryset = Brands.objects.filter(use=True)
    serializer_class = BrandSerializer


brand_list_create_view = BrandListCreateView.as_view()


class AboutListCreateView(generics.ListCreateAPIView):
    queryset = Abouts.objects.filter(use=True)
    serializer_class = AboutsSerializer


about_list_create_view = AboutListCreateView.as_view()


class GalleryListCreateView(generics.ListCreateAPIView):
    queryset = Gallary.objects.filter(use=True)
    serializer_class = GallarySerializer


gallary_list_create_view = GalleryListCreateView.as_view()


class NoteListCreateView(generics.ListCreateAPIView):
    queryset = Note.objects.filter(use=True)
    serializer_class = NoteSerializer


notes_list_create_view = NoteListCreateView.as_view()


class InfoListCreateView(generics.ListCreateAPIView):
    queryset = Info.objects.filter(use=True)
    serializer_class = InfoSerializer


info_list_create_view = InfoListCreateView.as_view()


class FirmLogoListCreateView(generics.ListCreateAPIView):
    queryset = FirmLogo.objects.filter(use=True)
    serializer_class = FirmLogoSerializer


firmLogos_list_create_view = FirmLogoListCreateView.as_view()


class WrapperImageListCreateView(generics.ListCreateAPIView):
    queryset = WrapperImage.objects.filter(use=True)
    serializer_class = wrapperImageSerializer


wrapperImage_list_create_view = WrapperImageListCreateView.as_view()


class TestimonialListCreateView(generics.ListCreateAPIView):
    queryset = Testimonials.objects.filter(use=True)
    serializer_class = TestimonialSerializer


testimonial_list_create_view = TestimonialListCreateView.as_view()


class WorkListCreateView(generics.ListCreateAPIView):
    queryset = Work.objects.filter(use=True)
    serializer_class = WorksSerializer


work_list_create_view = WorkListCreateView.as_view()


class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.filter(use=True)
    serializer_class = TagsSerializer


tag_list_create_view = TagListCreateView.as_view()
