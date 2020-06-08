from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to="user_images")

    male = 'ml'
    female = 'fm'
    any = 'an'
    sex_choises = [
        (male, 'Мужской пол'),
        (female, 'Женский пол'),
        (any, 'Любой другой пол'),

    ]
    sex = models.CharField(
        max_length=2,
        choices=sex_choises,
        default=any,
    )
    notice = models.BooleanField(blank=True, null=False, default=False)

    def __str__(self):
        return f"Профиль пользователя {self.user.username}"

    def save(self, *args, **kwargs):
        """changes picture size if it too big"""
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 256 or img.width > 256:
            resize = (256, 256)
            img.thumbnail(resize)
            img.save(self.image.path)
