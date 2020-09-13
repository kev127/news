import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = news(,'Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))
