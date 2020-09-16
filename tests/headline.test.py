import unittest
from app.models import headlines

class HeadlinesTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the headlines class.
    '''

    def setUp(self):
        '''
        set up method that will run before every test
        '''

        self.new_headlines=Headlines("BBC News",
                                        "Recovering from Covid-19:..",
                                        "Many patients are...",
                                        "http://www.bbc.co.uk/news/world-asia-india-54163109",
                                        "https://ichef.bbci.co.uk/news/1024/branded_news/AE68/production/_114384644_gettyimages-1228467467.jpg",
                                        "2020-09-16T02:07:23.6661058Z")

    def test_instance(self):
        
        '''
        Test to check creation of the new headline instance
        '''
        self.assertTrue(isinstance(self.new_headlines, Headlines))