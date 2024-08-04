# forms.py
from django import forms
from .models import ClientFeedback, TeamMember
import base64

class ClientFeedbackForm(forms.ModelForm):
    image_file = forms.ImageField(required=False, label='Upload Image')

    class Meta:
        model = ClientFeedback
        fields = ['image_file', 'feedback', 'name', 'designation']

    def save(self, commit=True):
        instance = super().save(commit=False)
        
        # Handle Base64 encoding
        if 'image_file' in self.cleaned_data and self.cleaned_data['image_file']:
            image_file = self.cleaned_data['image_file']
            encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
            instance.image_base64 = encoded_image

        if commit:
            instance.save()
        return instance

class TeamMemberForm(forms.ModelForm):
    image_file = forms.ImageField(required=False, label='Upload Image')

    class Meta:
        model = TeamMember
        fields = ['name', 'role', 'image_file', 'facebook', 'twitter', 'instagram']

    def save(self, commit=True):
        instance = super().save(commit=False)
        
        # Handle Base64 encoding
        if 'image_file' in self.cleaned_data and self.cleaned_data['image_file']:
            image_file = self.cleaned_data['image_file']
            encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
            instance.image_base64 = encoded_image
        
        if commit:
            instance.save()
        return instance