from django.db import models

# Create your models here.
class Expense(models.Model):        
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    #category choice fields
    CATEGORY_CHOICES = (
        ('food', 'Food'),
        ('transportation', 'Transportation'),
        ('utilities', 'Utilities'),
        ('entertainment', 'Entertainment'),
        ('other', 'Other'),
    )   
    #category = models.ForeignKey('Category', on_delete=models.CASCADE)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    
    def __str__(self):
        return f"{self.description} - {self.amount}"