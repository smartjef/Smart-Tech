from django.contrib import admin
from accounts.models import user_profile, Contact, main_app_details,Subscribe,Site_Contacts;
# Register your models here.

class SiteContactInline(admin.StackedInline):
    model = Site_Contacts
    extra = 0

class MainAppAdmin(admin.ModelAdmin):
    list_display=('name', 'description', 'logo')
    fieldsets=[
        (None, {
            'fields':['name']
        }),
        ('Site Description', {
            'fields':['description'], 'classes':['collapse']
        }),
    ]
    inlines = [SiteContactInline]

class ContactAdmin(admin.ModelAdmin):
    list_display=('name', 'email', 'feedback')
    list_filter=['email']
    list_per_page=20
    search_fields = ['name', 'email']

class SubscribeAdmin(admin.ModelAdmin):
    list_display=('name', 'email')
    list_filter=['email']
    list_per_page=20
    search_fields = ['name', 'email']

class UserProfileAdmin(admin.ModelAdmin):
    list_display=('user', 'bio','phone', 'user_type')
    list_filter=['user_type']
    list_per_page=20
    search_fields = ['user', 'phone']
    ordering=['user_type']

admin.site.register(main_app_details, MainAppAdmin)
admin.site.register(user_profile, UserProfileAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Subscribe, SubscribeAdmin)
