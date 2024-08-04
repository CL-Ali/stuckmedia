from django.contrib import admin
from .models import ClientFeedback, Service, PricingPlan, SkillCategory, TeamMember
from .forms import ClientFeedbackForm, TeamMemberForm

@admin.register(ClientFeedback)
class ClientFeedbackAdmin(admin.ModelAdmin):
    form = ClientFeedbackForm
    list_display = ('name', 'designation', 'feedback')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'link')  # Update this line


@admin.register(PricingPlan)
class PricingPlanAdmin(admin.ModelAdmin):
    list_display = ('service', 'type', 'price')

@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    form =  TeamMemberForm
    list_display = ('name', 'role',  'facebook', 'twitter', 'instagram')  # Update fields here

