from django.db import models


class UserRole(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=255, default="", blank=True, null=True)

    def __str__(self):
        return self.role_name


class PgUserDetail(models.Model):
    role = models.ForeignKey(UserRole, on_delete=models.PROTECT)
    name = models.CharField(max_length=255, default="", blank=True, null=True)
    email = models.EmailField(max_length=255, primary_key=True, default="")
    password = models.CharField(max_length=255, default="", blank=True, null=True)
    gender = models.CharField(max_length=255, default="", blank=True, null=True)
    address = models.CharField(max_length=255, default="", blank=True, null=True)
    mobile = models.BigIntegerField(default="", blank=True, null=True)
    otp = models.CharField(max_length=255, default="", null=True, blank=True)
    otp_time = models.CharField(max_length=255, null=True, blank=True, default="")
    verify_link = models.CharField(max_length=255, default="", null=True, blank=True)
    is_active = models.NullBooleanField(default=0)

    def __str__(self):
        return self.email
