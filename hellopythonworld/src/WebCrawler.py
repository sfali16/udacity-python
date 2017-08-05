'''
Created on Jul 30, 2017

@author: Faraz
'''

class WebCrawler(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        
    def findUrlsInPage(self, page):
        lastIndex = 0
        urlList = []
        while ( page.find("<a href=", lastIndex) != -1):
            print( "lastIndex=" + str(lastIndex))
            urlIndex = page.find( "<a href=", lastIndex) + 9
            endIndex = page.find('\"', urlIndex)
            url = page[ urlIndex: endIndex ]
#             print("SFA_DEBUG url=" + url)
            urlList.append( url )
            lastIndex = (endIndex+1)
        
        print( urlList )
        
    def findUrlsInFile(self, filename):
        fileObj = open( filename, 'r')
        self.findUrlsInPage( fileObj.read() )
        