from django.db import models

# Create your models here.
# آقسام الدورات
class Category(models.Model):
    name = models.CharField(max_length=100)

    # الدورة

class Course(models.Model):
    name = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

# ال
class Review(models.Model):
    course = models.ForeignKey(Course, related_name='reviews', on_delete=models.CASCADE)