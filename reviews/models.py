from django.db import models
from books.models import Book
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.
app_name = "reviews"

class Review(models.Model):
    book_id = models.ForeignKey(Book,on_delete=models.CASCADE,related_name="reviews")
    reviewer = models.ForeignKey(User,on_delete=models.CASCADE)
    ratings = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)])
    comments = models.TextField()
    
    class Meta:
        verbose_name = "Book Review"
    
    def __str__(self):
        return f"{self.book_id} --> {self.ratings}"