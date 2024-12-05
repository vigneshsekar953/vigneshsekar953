from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models.signals import post_save
from django.dispatch import receiver
from django import forms

# category

class Category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    img_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
    
# class Post(models.Model):
#     title=models.CharField(max_length=100)
#     content=models.TextField()
#     img_url=models.URLField(blank=True)
#     created_at=models.DateTimeField(auto_now_add=True)
#     slug=models.SlugField(unique=True)
#     category=models.ForeignKey(Category,on_delete=models.CASCADE)

#     def save(self,*args,**kwargs):
#         if not self.slug:
#             self.slug=slugify(self.title)
#             super().save(*args,**kwargs)
#     def __str__(self):
#         return self.title
    
class Aboutus(models.Model):
    content=models.TextField()
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

all_posts = Post.objects.all().order_by('-created_at')
paginator = Paginator(all_posts, 5)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    def __str__(self):
        return self.user.username
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Message from {self.name} ({self.email})"
