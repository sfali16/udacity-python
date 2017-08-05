'''
Created on Jul 30, 2017

@author: Faraz
'''
from Carbon.Aliases import false

class Point(object):
    '''
    This is a class created by Faraz to learn how to use python. It
    represents a Point with an x and y coordinate
    '''


    def __init__(self, x=0, y=0):
        '''
        Constructor
        '''
        self.x = x
        self.y = y
    
    def __str__(self):
        return ( "x: " + str(self.x) + ", y: " + str( self.y ) ) 
        
    def __eq__(self, other):
        equal = (self.x == other.x) and (self.y == other.y)
        return equal
    
    def add(self, other):
        self.x += other.x
        self.y += other.y
        return self
    