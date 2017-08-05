'''
Created on Jul 30, 2017

@author: Faraz
'''
import unittest
from BinarySearch import BinarySearch

class BinarySearchTest(unittest.TestCase):

    def searchForTarget(self, target, expectedIndex):
        self.searchArrayForTarget(None, target, expectedIndex)
        
    def searchArrayForTarget(self, list1, target, expectedIndex):
        """
        Test the search function by searching the list provided for the target
        and ensure that the expectedIndex is what the search returns
        """
        if ( list1 is not None ):
                self.testObject = BinarySearch(list1)
        self.assertEquals(expectedIndex, self.testObject.search(target))

    def testSearch(self):
        self.searchArrayForTarget([1, 2, 3], 3, 2)
        self.searchForTarget(4, -1)
        self.searchForTarget(2, 1)
        self.searchArrayForTarget([1], 3, -1)
        self.searchForTarget(1, 0)
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()