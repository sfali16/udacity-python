'''
Created on Aug 2, 2017

@author: Faraz
'''


def classify(features_train, labels_train):   
    ### import the sklearn module for GaussianNB
    ### create classifier
    ### fit the classifier on the training features and labels
    ### return the fit classifier
    ### your code goes here!
    
    from sklearn import naive_bayes
    clf = naive_bayes.GaussianNB()
    clf.fit( features_train, labels_train )
    return clf
