from django.urls import path
# from . import views
from .views import (
    ClientFeedbackListCreate,
    ServiceListCreate,
    PricingPlanListCreate,
    SkillCategoryListCreate,
    TeamMemberListCreate
)
urlpatterns = [
    path('client-feedback/', ClientFeedbackListCreate.as_view(), name='clientfeedback-list-create'),
    path('services/', ServiceListCreate.as_view(), name='service-list-create'),
    path('pricing-plans/', PricingPlanListCreate.as_view(), name='pricingplan-list-create'),
    path('skill-categories/', SkillCategoryListCreate.as_view(), name='skillcategory-list-create'),
    path('team-members/', TeamMemberListCreate.as_view(), name='teammember-list-create'),
]

