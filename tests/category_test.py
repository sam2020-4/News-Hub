import unittest
from app.models import Category

class CategoryTest(unittest.TestCase):
    """
    Test class to test the behavior of the category class
    """

    def setUp(self):
        """
        Set up method that will run before every test
        """
        self.new_category = Category("n-tv NACHRICHTEN", 
                            "Grenke-Aktienkurs bricht ...",
                            "Fraser Perring ..",
                            "https://www.n-tv.de/wirtschaft/MDax-Konzern-im-Visier-des-Wirecard-Jaegers-article22038427.html",
                            "https://bilder1.n-tv.de/img/incoming/crop22038460/6591327788-cImg_16_9-w1200/135584362.jpg",
                            "2020-09-15T15:09:36Z")

    def test_instance(self):
        
        self.assertTrue(isinstance(self.new_category, Category))
