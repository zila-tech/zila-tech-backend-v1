from rest_framework import serializers
from .models import *


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonials
        fields = "__all__"


class AboutsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abouts
        fields = "__all__"


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"


class FirmLogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirmLogo
        fields = "__all__"


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ["contact", "email"]


class wrapperImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WrapperImage
        fields = "__all__"


class GallarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallary
        fields = [
            "file",
        ]


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brands
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = "__all__"


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = "__all__"


class ExperienceSerializer(serializers.ModelSerializer):
    works = WorkExperienceSerializer(source="work", many=True)

    class Meta:
        model = Experience
        fields = ["id", "year", "works"]


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class WorksSerializer(serializers.ModelSerializer):
    tags = TagsSerializer(source="tag", many=True)

    class Meta:
        model = Work
        fields = [
            "title",
            "description",
            "projectLink",
            "codeLink",
            "imageurl",
            "tags",
        ]
