'''
Created on Jul 30, 2017

@author: Faraz
'''
f = open('/Users/Faraz/eclipse/pyjs-pyjs-07f54ad/examples/HelloWorld', 'r')
print( f )
for line in f:
    print( line.rstrip())
f.close()