from django.db import models
from apps.accounts.models import User
from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     EMPLOYER = 'employer'
#     WORKER = 'worker'
#     ADMIN = 'admin'
#     USER_TYPES = [
#         (EMPLOYER, 'Employer'),
#         (WORKER, 'Worker'),
#         (ADMIN, 'Admin'),
#     ]
#     type = models.CharField(max_length=10, choices=USER_TYPES, default=WORKER)

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category_images/')

    def __str__(self) -> str:
        return self.name


class Work(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='works')
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)

    PAYMENT_CHOICES = (
        ('cash', 'Cash'),
        ('card', 'Credit/Debit Card'),
    )
    payment_type = models.CharField(max_length=10, choices=PAYMENT_CHOICES, default='cash')

    def __str__(self):
        return f'{self.user.first_name} - {self.title}'


# Work Image Model
class WorkImage(models.Model):
    work = models.ForeignKey(Work, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='work_images')


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    work = models.ForeignKey(Work, on_delete=models.CASCADE, related_name='reviews')
    description = models.TextField()
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])

    def __str__(self) -> str:
        return f'{self.user.first_name} - {self.work.title}'
    
class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='portfolio_items')
    image = models.ImageField(upload_to='portfolio_images/')
    work = models.ForeignKey(Work, on_delete=models.CASCADE, related_name='portfolio_images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.user.first_name} - {self.work.title}'