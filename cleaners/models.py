from django.db import models

class Cleaner(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    document = models.CharField(max_length=100)
    cv = models.TextField()
    picture = models.ImageField(upload_to='cleaner_pictures/')
    work_experience = models.PositiveIntegerField()
    comments = models.TextField(blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


