from django.urls import path
from . import views

urlpatterns = [
    path('client-feedback/', views.ClientFeedbackListCreate.as_view(), name='clientfeedback-list-create'),
    path('services/', views.ServiceListCreate.as_view(), name='service-list-create'),
    path('pricing-plans/', views.PricingPlanListCreate.as_view(), name='pricingplan-list-create'),
    path('skill-categories/', views.SkillCategoryListCreate.as_view(), name='skillcategory-list-create'),
    path('team-members/', views.TeamMemberListCreate.as_view(), name='teammember-list-create'),
]

