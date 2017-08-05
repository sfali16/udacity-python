'''
Created on Jul 30, 2017

@author: Faraz
'''
import unittest
from PointFile import Point


class PointTest(unittest.TestCase):

    def testEquals(self):
        p1 = Point(1,3)
        p2 = Point(1,3)
        print( p1 )
        print( "p2={0}".format(p2))
        self.assertFalse( p1 is p2, "p1 is not p2, so this should be false")
        self.assertEqual( p1, p2, "p1 and p2 should be equal" )
        pass

    def testAdd(self):
        p1 = Point(1,2)
        p2 = Point(3,4)
        self.assertEquals( Point(4,6), p1.add(p2), "Not adding the two points " + p1 + p2)
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()