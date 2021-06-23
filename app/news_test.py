import unittest
from models import news
News= news.News

class Newsest(unittest.TestCase):
        '''
        Test Class to test the behaviour of the News class
        '''

def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_new = News1234,'Python Must Be Crazy','A thrilling new Python Series','https://newsapi.org/v2/top-headlines?country=us&apiKey',8.5,129993)

def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))


if __name__ == '__main__':2
    unittest.main()