from django.test import TestCase

from genres.models import Genre
from .models import Series
from django.utils import timezone
# Create your tests here.

class SeriesModelTestCase(TestCase):
    def setUp(self):
        series_1 = Series.objects.create(title="Series Title")
        series_2 = Series.objects.create(title="Series Title",genre= Genre.objects.first())
        self.series_1 = series_1
        self.series_2 = series_2
        
# To Test that series id is generated and contains title inside itself.
    def test_series_id(self):
        series_id = self.series_1.series_id
        print("Title : ",self.series_1.title)
        print("Series id : ",series_id)
        contain_title = self.series_1.title[0:6].lower() in series_id
        self.assertTrue(contain_title)
        
    def test_active_timestamp(self):
        active_timestamp = self.series_1.active_timestamp
        self.assertTrue(active_timestamp is not None)
        self.assertTrue(active_timestamp <= timezone.now())
        print(active_timestamp)
    
    def test_series_genre(self):
        s2_genre = self.series_2.genre
        ff = Genre.objects.first()
        self.assertEqual(s2_genre,ff)