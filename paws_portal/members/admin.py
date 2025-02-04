from django.contrib import admin
from members.models import Member

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'joined_date')
    prepopulated_fields = {'slug': ('first_name', 'last_name')}

admin.site.register(Member, MemberAdmin)
