from django.db import models


class UserRole(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=255, default="", blank=True, null=True)

    def __str__(self):
        return self.role_name





