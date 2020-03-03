from django import forms
from backend_app.models import UserRole,PgUserDetail


class UserRoleForm(forms.ModelForm):
    class Meta:
        Model = UserRole
        exclude = ['role_id', 'role_name']


class PgUserDetailForm(forms.ModelForm):
    class Meta:
        Model = PgUserDetail
        exclude = ['role', 'name', 'email', 'password', 'gender', 'address', 'mobile', 'otp', 'otp_time', 'verify_link', 'is_active']