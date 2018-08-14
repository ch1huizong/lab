from django.contrib import admin
from bands.models import Band, Member


class BandAdmin(admin.ModelAdmin):

    list_display = ('name',)

    def __str__(self):
        return self.name


class MemberAdmin(admin.ModelAdmin):
    """Customize the look of the auto-generated admin for the Member model"""
    list_display = ('name', 'instrument')
    list_filter = ('band',)

admin.site.register(Band, BandAdmin)  # Use the default options
admin.site.register(Member, MemberAdmin)  # Use the customized options
