from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# club --> User
# courses --> club details --> Profile


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # additional data for user:
    name = models.CharField(max_length=50, null=True)
    about = models.TextField(max_length=250, null=True)
    img = models.ImageField(verbose_name='profile image:', upload_to='profile', blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username



















class Clubs(models.Model):
    name= models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Courses(models.Model):
    subject= models.CharField(max_length=50)
    last_update= models.DateTimeField(auto_now_add=True)
    club = models.ForeignKey(Clubs, on_delete=models.CASCADE, related_name='courses', null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses', null=True)

    def __str__(self):
        return self.subject
