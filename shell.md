from books.models import Book,Author

book1 = Book.objects.get(is_active = False)