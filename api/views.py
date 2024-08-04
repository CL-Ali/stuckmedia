from rest_framework import generics
from .models import ClientFeedback, Service, PricingPlan, SkillCategory, TeamMember
from .serializers import ClientFeedbackSerializer, ServiceSerializer, PricingPlanSerializer, SkillCategorySerializer, TeamMemberSerializer


class ClientFeedbackListCreate(generics.ListCreateAPIView):
    queryset = ClientFeedback.objects.all()
    serializer_class = ClientFeedbackSerializer

class ServiceListCreate(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class PricingPlanListCreate(generics.ListCreateAPIView):
    queryset = PricingPlan.objects.all()
    serializer_class = PricingPlanSerializer

class SkillCategoryListCreate(generics.ListCreateAPIView):
    queryset = SkillCategory.objects.all()
    serializer_class = SkillCategorySerializer

class TeamMemberListCreate(generics.ListCreateAPIView):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer

