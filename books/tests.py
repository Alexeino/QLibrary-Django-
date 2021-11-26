from django.test import TestCase
from .models import Book,Author
# Create your tests here.
class BookModelTestCase(TestCase):
    def setUp(self):
        self.book_a = Book.objects.create(title = "Demo Title",short_desc = "Life is good",book_id="demo_id")
        
        
    def test_active_timestamp(self):
        active_timestamp = self.book_a.active_timestamp
        print(active_timestamp)
        self.assertTrue(active_timestamp)
        
    def test_deactive_remove_timestamp(self):
        self.book_a.is_active = False
        self.book_a.save()
        print(self.book_a.is_active)
        self.assertEqual(self.book_a.active_timestamp,None)        