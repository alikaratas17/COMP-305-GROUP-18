class Hist:
  def __init__(self):
    self.keys = dict()
  def insert(self,value):
    if value in self.keys:
      self.keys[value] +=1
    else:
      self.keys[value] = 1
  def getSortedNonUniqueKeys(self):
    s = []
    for value,count in self.keys.items():
      if count > 1:
        s.append(count)
    return sorted(s,reverse = True)
  def getSortedKeys(self):
    return sorted(list(self.keys.keys()),reverse=True)
  def getSortedKeyValuePairs(self):
    return sorted(list(self.keys.items()),reverse=True)
  def getCount(self,num):
    return self.keys[num]
