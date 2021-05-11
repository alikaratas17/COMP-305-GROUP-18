"""
A simple parser class
"""
class Parser:
  def __init__(self,filename):
    self.__filename = filename
    self.__playerCount = 0
    self.__roundCount = 0

  def getPlayerCount(self):
    return self.__playerCount

  def getRoundCount(self):
    return self.__roundCount

  def readData(self,l=[]):
    with open(self.__filename,"r") as file:
      info = file.readline().split()
      self.__playerCount = int(info[0])
      self.__roundCount = int(info[1])
      for i in range(self.__playerCount):
        current = file.readline().split()
        player = (i,[int(num) for num in current])
        l.append(player)
    return l
