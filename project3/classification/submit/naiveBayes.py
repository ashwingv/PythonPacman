import util
import classificationMethod
import math

class NaiveBayesClassifier(classificationMethod.ClassificationMethod):
  """
  See the project description for the specifications of the Naive Bayes classifier.
 
  Note that the variable 'datum' in this code refers to a counter of features
  (not to a raw samples.Datum).
  """
  cpt0={}
  cpt1={}
  cpt2={}
  cpt3={}
  cpt4={}
  cpt5={}
  cpt6={}
  cpt7={}
  cpt8={}
  cpt9={}
  labelIndexes={}
  bestK=-1
  def __init__(self, legalLabels):
    self.legalLabels = legalLabels
    self.type = "naivebayes"
    self.k = 1 # this is the smoothing parameter, ** use it in your train method **
    self.automaticTuning = False # Look at this flag to decide whether to choose k automatically ** use this in your train method **
   
  def setSmoothing(self, k):
    """
    This is used by the main method to change the smoothing parameter before training.
    Do not modify this method.
    """
    self.k = k

  def train(self, trainingData, trainingLabels, validationData, validationLabels):
    """
    Outside shell to call your method. Do not modify this method.
    """ 
     
    self.features = trainingData[0].keys() # this could be useful for your code later...
   
    if (self.automaticTuning):
        kgrid = [0.001, 0.01, 0.05, 0.1, 0.5, 1, 5, 10, 20, 50]
    else:
        kgrid = [self.k]
       
    self.trainAndTune(trainingData, trainingLabels, validationData, validationLabels, kgrid)
     
  def trainAndTune(self, trainingData, trainingLabels, validationData, validationLabels, kgrid):
    """
    Trains the classifier by collecting counts over the training data, and
    stores the Laplace smoothed estimates so that they can be used to classify.
    Evaluate each value of k in kgrid to choose the smoothing parameter
    that gives the best accuracy on the held-out validationData.
   
    trainingData and validationData are lists of feature Counters.  The corresponding
    label lists contain the correct label for each datum.
   
    To get the list of all possible features or labels, use self.features and
    self.legalLabels.
    """
    #print " features are ",self.features
    #print " lenght of features are ",len(self.features)
    #print " legal labels are ", self.legalLabels
    #print " training data is ", trainingData[99]   
    #print " the training lables 99 is ",trainingLabels[99]
    trainingLabelCounters=util.Counter()
    trainingLabelCounters.incrementAll(trainingLabels,1)
    #print "TRDATA",trainingLabelCounters
    vLabel=util.Counter()
    vLabel.incrementAll(trainingLabels,1)
    #print"VDATA",vLabel
    #print "The count f the legal labels in the training labels are ", trainingLabelCounters
    trainingLabelProp={}
    for i in trainingLabelCounters:
      trainingLabelProp.update({i:round((float(trainingLabelCounters[i])/100),2)})
    #print "The probabilites of the legal lables ",trainingLabelProp
    #print "______________________________________________________________"
    #print trainingLabels
    index0=[]
    index1=[]
    index2=[]
    index3=[]
    index4=[]
    index5=[]
    index6=[]
    index7=[]
    index8=[]
    index9=[]
    for i in range(100):
      if trainingLabels[i]==0:
        index0.append(i)
        NaiveBayesClassifier.labelIndexes.update({0:index0})		# GETTING THE INDEX POSITION OF 0 FEATURES
      if trainingLabels[i]==1:
        index1.append(i)
        NaiveBayesClassifier.labelIndexes.update({1:index1})		# GETTING THE INDEX POSITION OF 1 FEATURES
      if trainingLabels[i]==2:
        index2.append(i)
        NaiveBayesClassifier.labelIndexes.update({2:index2})		# GETTING THE INDEX POSITION OF 2 FEATURES
      if trainingLabels[i]==3:
        index3.append(i)
        NaiveBayesClassifier.labelIndexes.update({3:index3})		# GETTING THE INDEX POSITION OF 3 FEATURES
      if trainingLabels[i]==4:
        index4.append(i)
        NaiveBayesClassifier.labelIndexes.update({4:index4})		# GETTING THE INDEX POSITION OF 4 FEATURES
      if trainingLabels[i]==5:
        index5.append(i)
        NaiveBayesClassifier.labelIndexes.update({5:index5})		# GETTING THE INDEX POSITION OF 5 FEATURES
      if trainingLabels[i]==6:
        index6.append(i)
        NaiveBayesClassifier.labelIndexes.update({6:index6})		# GETTING THE INDEX POSITION OF 6 FEATURES
      if trainingLabels[i]==7:
        index7.append(i)
        NaiveBayesClassifier.labelIndexes.update({7:index7})		# GETTING THE INDEX POSITION OF 7 FEATURES
      if trainingLabels[i]==8:
        index8.append(i)
        NaiveBayesClassifier.labelIndexes.update({8:index8})		# GETTING THE INDEX POSITION OF 8 FEATURES
      if trainingLabels[i]==9:
        index9.append(i)
        NaiveBayesClassifier.labelIndexes.update({9:index9})		# GETTING THE INDEX POSITION OF 9 FEATURES
    """for i in labelIndexes:
      print labelIndexes[i]"""
    for i in NaiveBayesClassifier.labelIndexes:
      #print "computing CPTs for label :",i
      imagesIndexes=NaiveBayesClassifier.labelIndexes[i]        # MCGS GETTING THE LIST OF INDEX OF THE IMAGES OF THE GIVEN NUMBER
      imageKeys=trainingData[imagesIndexes[0]].keys()    		# GETTING THE KEYS FOR THE GIVEN NUMBER
      #print len(imageKeys)
      for key in imageKeys:
        zeros=0
        for j in imagesIndexes:
          if(trainingData[j][key]==0):
             zeros=zeros+1
        if(i==0):
          NaiveBayesClassifier.cpt0.update({key:zeros}) 	# CALCULATING THE COUNTS OF 0 OVER ALL THE FEATURES
        if(i==1):
          NaiveBayesClassifier.cpt1.update({key:zeros})		# CALCULATING THE COUNTS OF 1 OVER ALL THE FEATURES
        if(i==2):
          NaiveBayesClassifier.cpt2.update({key:zeros})		# CALCULATING THE COUNTS OF 2 OVER ALL THE FEATURES
        if(i==3):
          NaiveBayesClassifier.cpt3.update({key:zeros})		# CALCULATING THE COUNTS OF 3 OVER ALL THE FEATURES
        if(i==4):
          NaiveBayesClassifier.cpt4.update({key:zeros})		# CALCULATING THE COUNTS OF 4 OVER ALL THE FEATURES
        if(i==5):
          NaiveBayesClassifier.cpt5.update({key:zeros})		# CALCULATING THE COUNTS OF 5 OVER ALL THE FEATURES
        if(i==6):
          NaiveBayesClassifier.cpt6.update({key:zeros})		# CALCULATING THE COUNTS OF 6 OVER ALL THE FEATURES
        if(i==7):
          NaiveBayesClassifier.cpt7.update({key:zeros})		# CALCULATING THE COUNTS OF 7 OVER ALL THE FEATURES
        if(i==8):
          NaiveBayesClassifier.cpt8.update({key:zeros})		# CALCULATING THE COUNTS OF 8 OVER ALL THE FEATURES
        if(i==9):
          NaiveBayesClassifier.cpt9.update({key:zeros})		# CALCULATING THE COUNTS OF 9 OVER ALL THE FEATURES
   

    #util.raiseNotDefined()
       
  def classify(self, testData):
    """
    Classify the data based on the posterior distribution over labels.
   
    You shouldn't modify this method.
    """
    guesses = []
    self.posteriors = [] # Log posteriors are stored for later data analysis (autograder).
    for datum in testData:
      posterior = self.calculateLogJointProbabilities(datum)
      guesses.append(posterior.argMax())
      self.posteriors.append(posterior)
    return guesses
     
  def calculateLogJointProbabilities(self, datum):
    """
    Returns the log-joint distribution over legal labels and the datum.
    Each log-probability should be stored in the log-joint counter, e.g.   
    logJoint[3] = <Estimate of log( P(Label = 3, datum) )>
    """
    logJoint = util.Counter()
    #print logJoint
    "*** YOUR CODE HERE ***"
    """if(NaiveBayesClassifier.bestK<0):
      print "Calculating the log joint probabilites for validating "
    else:"""
     
    #util.raiseNotDefined()
   
    return logJoint
 
  def findHighOddsFeatures(self, label1, label2):
    """
    Returns the 100 best features for the odds ratio:
            P(feature=1 | label1)/P(feature=1 | label2)
    """
    featuresOdds = []
       
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

    return featuresOdds
