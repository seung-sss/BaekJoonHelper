class TestCase(list):

  def __init__(self):
    self.addTestCase()

  def appendTest(self,testInput,testOutput):
    self.append((testInput,testOutput))
  
  def addTestCase(self):
    testInput = ['5 21\r\n5 6 7 8 9\r\n', '10 500\r\n93 181 245 214 315 36 185 138 216 295\r\n']
    testOutput = ['21\r\n', '497\r\n']
    for i in range(len(testInput)):
      self.appendTest(testInput=testInput[i],testOutput=testOutput[i])


