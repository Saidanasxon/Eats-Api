from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Food(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    recept = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    text = models.TextField()
    user = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
