from rest_framework import serializers
from .models import ClientFeedback, Service, PricingPlan, SkillCategory, TeamMember
import base64
from rest_framework import serializers
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from PIL import Image

class ClientFeedbackSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(write_only=True, required=False)

    class Meta:
        model = ClientFeedback
        fields = ['image', 'image_base64', 'feedback', 'name', 'designation']

    def create(self, validated_data):
        # Extract image file if present
        image = validated_data.pop('image', None)
        if image:
            # Convert image to Base64 string
            buffered = BytesIO()
            img = Image.open(image)
            img.save(buffered, format=img.format)
            img_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')

            validated_data['image_base64'] = img_base64

        return super().create(validated_data)


class TeamMemberSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(write_only=True, required=False)

    class Meta:
        model = ClientFeedback
        fields = ['image', 'image_base64', 'role', 'name', 'facebook', 'twitter', 'instagram']

    def create(self, validated_data):
        # Extract image file if present
        image = validated_data.pop('image', None)
        if image:
            # Convert image to Base64 string
            buffered = BytesIO()
            img = Image.open(image)
            img.save(buffered, format=img.format)
            img_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')

            validated_data['image_base64'] = img_base64

        return super().create(validated_data)

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class PricingPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = PricingPlan
        fields = '__all__'

class SkillCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillCategory
        fields = '__all__'
