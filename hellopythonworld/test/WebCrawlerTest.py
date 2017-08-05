'''
Created on Jul 30, 2017

@author: Faraz
'''
import unittest
from WebCrawler import WebCrawler


class Test(unittest.TestCase):



    def setUp(self):
        self.crawler = WebCrawler()

    def testWebCrawler(self):
        page = ('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')
        self.crawler.findUrlsInPage(page)
        
        self.crawler.findUrlsInPage( '<a href="http://udacity.com">Hello world</a>')
        pass
    
    def testWebCrawlerFile(self):
#         filename = "/Users/faraz/eclipse/python_workspace/hellopythonworld/udacity-source.htm"
        filename = "../udacity-source.htm"
        self.crawler.findUrlsInFile( filename )

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()