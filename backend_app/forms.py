from django import forms
from backend_app.models import UserRole, PgUserDetail


class UserRoleForm(forms.ModelForm):
    class Meta:
        model = UserRole
        exclude = ['role_id', 'role_name']


class PgUserDetailForm(forms.ModelForm):
    class Meta:
        model = PgUserDetail
        exclude = ['role', 'name', 'email', 'password', 'gender', 'address', 'mobile', 'otp', 'otp_time', 'verify_link', 'is_active']
