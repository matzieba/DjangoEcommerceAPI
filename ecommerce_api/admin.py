from django import forms
from django.contrib import admin

from ecommerce_api.models import User


# Register your models here.


class UserAdminForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'



class UserAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
    )

    form = UserAdminForm

    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"


admin.site.register(User, UserAdmin)

