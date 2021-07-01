from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Coach(models.Model):
    """
    A coach model
    """

    class Meta:
        verbose_name_plural = "Coaches"

    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)    
    description = models.TextField()
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.first_name


class Comment(models.Model):
    """
    A comment model
    """
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateField(auto_now_add=True)
    stars = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return f"Comment about {self.coach.first_name} by {self.author}"
