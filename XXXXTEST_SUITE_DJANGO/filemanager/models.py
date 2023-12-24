from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.


class UserFile(models.Model):
    file = models.FileField(
        upload_to="user_files",
        validators=[FileExtensionValidator(["pdf", "png", "jpg"])],
    )
