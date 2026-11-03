from django.db import models


class Employee(models.Model):
    DEPARTMENT_CHOICES = [
        ('HR', 'HR'),
        ('Developer', 'Developer'),
        ('Manager', 'Manager'),
        ('Designer', 'Designer'),
        ('Finance', 'Finance'),
        ('Marketing', 'Marketing'),
        ('Sales', 'Sales'),
        ('IT', 'IT'),
        ('Operations', 'Operations'),
    ]

    name = models.CharField(max_length=100)
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES)
    age = models.PositiveIntegerField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
