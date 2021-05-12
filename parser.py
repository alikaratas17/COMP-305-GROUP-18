from Hist import Hist
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
  def readDataHistogram(self,h = [],s = set()):
    with open(self.__filename,"r") as file:
      info = file.readline().split()
      self.__playerCount = int(info[0])
      self.__roundCount = int(info[1])
      for x in range(self.__playerCount):
        current = file.readline().split()
        numbers = sorted([int(num) for num in current],reverse = True)
        counts = [(numbers[0],1)]
        j = 1
        for n in numbers:
          s.add(n)
        for i in range(1,self.__roundCount):
          if numbers[i]==numbers[i-1]:
            counts[j-1] = (counts[j-1][0],counts[j-1][1]+1)
          else:
            counts.append((numbers[i],1))
            j +=1
        h.append((x,counts))
    return h,s

  def readDataDoubleHistogram(self,hListPlayers=[],hNumbers=Hist()):
    with open(self.__filename,"r") as file:
      info = file.readline().split()
      self.__playerCount = int(info[0])
      self.__roundCount = int(info[1])
      for i in range(self.__playerCount):
        hListPlayers.append((i,Hist()))
      for x in range(self.__playerCount):
        current = file.readline().split()
        numbers = sorted([int(num) for num in current],reverse = True)
        for num in numbers:
          hListPlayers[x][1].insert(num)
          hNumbers.insert(num)
    return hListPlayers,hNumbers
