import util
import classificationMethod

class MostFrequentClassifier(classificationMethod.ClassificationMethod):
  """
  The MostFrequentClassifier is a very simple classifier: for
  every test instance presented to it, the classifier returns
  the label that was seen most often in the training data.
  """
  def __init__(self, legalLabels):
    self.guess = None
    self.type = "mostfrequent"
  
  def train(self, data, labels, validationData, validationLabels):
    """
    Find the most common label in the training data.
    """ 
    print " Inside the train function of MFC "
    counter = util.Counter()
    print " the counter is ", counter
    #print " data is ", len(data)
    #print " labels are ", labels,
    #print " validation data", len(validationData)
    #print " validation labels", validationLabels
    counter.incrementAll(labels, 1)
    print " after increment ", counter
    print " guess before is ",self.guess
    self.guess = counter.argMax()
    print " the guess after is ", self.guess
    print " the guess is ",counter.argMax()
  
  def classify(self, testData):
    """
    Classify all test data as the most common label.
    """
    print " Inside the classify function of the MFC "
    print " the test data is ", len(testData[0])
    return [self.guess for i in testData]
