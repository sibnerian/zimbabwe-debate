from website.models import Member, Sponsor
from django.contrib import admin

class MemberAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields':['name', 'bio']}),
    ]
    list_display = ('name', 'bio')
    list_filter = ['name']
    search_fields = ['name']

class SponsorAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields':['name', 'url', 'image_url']}),
    ]
    list_display = ('name', 'url', 'image_url')
    list_filter = ['name']
    search_fields = ['name']

admin.site.register(Member, MemberAdmin)
admin.site.register(Sponsor, SponsorAdmin)