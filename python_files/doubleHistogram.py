from parser import Parser
from Outputer import Outputer
from Hist import Hist
import math
"""
Works
"""

def solve(filename):
  parser = Parser(filename)

  h1 = []
  h2 = Hist()
  parser.readDataDoubleHistogram(h1,h2)
  #print(h1)
  players = [(x[0],x[1].getSortedKeyValuePairs()) for x in h1]
  l_values = h2.getSortedKeyValuePairs()
  min_orders = calculate_orders(players)
  l_pair = l_values.pop(0)
  toBeUpdated = l_pair[1]
  number = l_pair[0]

  while len(l_values) > 0:
    #Update with new num
    m = math.inf
    updated = 0
    for i in range(len(players)):
      n = 0
      j = 0
      while j < len(players[i][1]):
        if players[i][1][j][0] > number:
          players[i][1][j] = (number,players[i][1][j][1])
          n += players[i][1][j][1]
          updated+= players[i][1][j][1]
        if j+1 < len(players[i][1]) and players[i][1][j][0]==players[i][1][j+1][0]:
          c = players[i][1].pop(j)[1]
          players[i][1][j] = players[i][1][j][0],players[i][1][j][1]+c
        if toBeUpdated == updated:
          break
        j+=1
      
      m = min(m,n)
      if toBeUpdated == updated:
          break



    #Remove sum values
    i = 0
    c = m
    while i < len(players):
      if players[i][1][0][1] > c:
        players[i][1][0] = players[i][1][0][0],players[i][1][0][1] - c
        i +=1
        c = m
      else:
        c -= players[i][1].pop(0)[1]

    # Update l and toBeUpdated
    toBeUpdated -= m
    l_pair = l_values.pop(0)
    number = l_pair[0]
    toBeUpdated +=l_pair[1]

    #Recalculate orders
    orders = calculate_orders(players)
    for i in range(len(orders)):
      min_orders[i] = min(min_orders[i],orders[i])
  return min_orders

def getSum(values):
  s = 0
  for x,y in values:
    s+=x*y
  return s


def calculate_orders(players):
  sums = [(player[0],getSum(player[1])) for player in players]
  sums = sorted(sums,key=lambda y: y[1],reverse=True)
  orders = [0]*len(players)
  o = len(players)
  orders[sums[0][0]] = o
  o -=1
  for i in range(1,len(sums)):
    if sums[i][1] < sums[i-1][1]:
     orders[sums[i][0]] = o
    else:
      orders[sums[i][0]] = orders[sums[i-1][0]]
    o -=1
  return orders
      
l= solve("./../inputs/baby_comp_4.txt")
o = Outputer("./../outputs/output5.txt")
o.output(l)
