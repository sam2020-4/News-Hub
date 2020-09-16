import unittest
from app.models import headlines

class headlinesTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the headlines class.
    '''

    def setUp(self):
        '''
        set up method that will run before every test
        '''

        self.new_headlines = headlines('')