import unittest
from models import sources
sources = sources.sources

class Test(unittest.TestCase):
    '''
    Test Class to test the behaviour of the sources class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = sources(,"News, analysis from the Middle East and worldwide, multimedia and interactives, opinions, documentaries, podcasts, long reads and broadcast schedule.",)

    def test_instance(self):
        self.assertTrue(isinstance(self.news_source,Sources))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_source.id,"al-jazeera-english")
        self.assertEquals(self.new_source.name,"Al Jazeera English")
        self.assertEquals(self.new_source.description,"News, analysis from the Middle East and worldwide, multimedia and interactives, opinions, documentaries, podcasts, long reads and broadcast schedule.",)
        self.assertEquals(self.new_source.url, "http://www.aljazeera.com")
        self.assertEquals(self.new_source.category,"general")
        self.assertEquals(self.new_source.country,"us")
        self.assertEquals(self.new_source.language,"en")

class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles('Al Jazeera ','Al Jazeera','Toyota Launches $800M Fund To Boost ‘Mobility’ And AI-Focused Companies')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_article.id,'Al Jazeera ')
        self.assertEquals(self.new_article.author,'Al Jazeera')
        self.assertEquals(self.new_article.title,'innovation')
        self.assertEquals(self.new_article.description,'Toyota Launches $800M Fund To Boost ‘Mobility’ And AI-Focused Companies')
        self.assertEquals(self.new_article.url,'forbes.com')


