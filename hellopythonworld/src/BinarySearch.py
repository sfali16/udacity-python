'''
Created on Jul 30, 2017

@author: Faraz
'''

class BinarySearch(object):
    '''
    This is a binary search class created to learn python
    '''
    def __init__(self, array):
        '''
        Constructor
        '''
        self.array = array
        
    def search(self, target):
        ''' search the given list for a particular target. return -1 if
        target element is not found in the list, or returns the index  in
        the list at which element is found'''
        self.array.sort()
        return self.binarySearch( 0, len(self.array)-1, target)
            
    def binarySearch(self, lo, high, target):
        pivot = (lo+high)/2
#         print("binarySearch called with low=" + str(lo) + ", high=" 
#               + str(high) + ", pivot= " + str(pivot))
        array = self.array
        if ( lo > high ):
            return -1
        if ( array[pivot] == target):
            return pivot
        elif ( array[pivot] < target ):
            return self.binarySearch( pivot+1, high, target)
        else:
            return self.binarySearch( lo, pivot, target)
            
            
