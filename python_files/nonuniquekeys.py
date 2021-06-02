from parser import Parser
from Outputer import Outputer
from Hist import Hist
import matplotlib.pyplot as plt
"""
Didnt work
"""
def solve(filename):
  parser = Parser(filename)
  l = []
  parser.readData(l)
  hist = Hist()
  for x,y in l:
    for i in y:
      hist.insert(i)
  numbers = hist.getSortedKeys()#getSortedNonUniqueKeys()
  min_orders = calculate_orders(l)
  l_values = [numbers[0]]*parser.getPlayerCount()
  round_count = parser.getRoundCount()
  for i in range(len(l)):
    l[i] = (l[i][0],sorted(l[i][1],reverse=True))
  
  for num in numbers[1:]:
    #update with new num value
    m = parser.getRoundCount()
    for i in range(len(l)):
      j=0
      while j < round_count:
        if l[i][1][j] > num:
          l[i][1][j] = num
          j+=1
          continue
        break
      m = min(j,m)
    if m > 0:
      round_count -=m
      for i in range(parser.getPlayerCount()):
        for k in range(m):
          l[i][1].pop(0)
    #calculate min orders
    orders = calculate_orders(l)
    for i in range(parser.getPlayerCount()):
      if min(min_orders[i],orders[i]) != min_orders[i]:
        min_orders[i] = orders[i]
        l_values[i] = num
  l_count_pairs = hist.getSortedKeyValuePairs()
  y_values = [0]*len(l_count_pairs)
  x_values = []
  z_values = []
  j=0
  x1 = []
  x2 = []
  for x,y in l_count_pairs:
    x_values.append(x)
    z_values.append(y)
    for i in range(len(l_values)):
      if l_values[i] == x:
        y_values[j]+=1
        if not x in x1:
          x1.append(x)
          x2.append(y)
    
    j+=1
  plt.figure()
  plt.title("Importances")
  plt.bar(x_values,y_values)
  plt.figure()
  plt.title("Counts")
  plt.bar(x_values,z_values)
  plt.figure()
  plt.title("Counts of important ones")
  plt.bar(x1,x2)
  plt.show()
  return min_orders

def calculate_orders(l):
  sums = [(x[0],sum(x[1])) for x in l]
  sums = sorted(sums,key=lambda y: y[1],reverse=True)
  orders = [0]*len(l)
  o = len(l)
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
o = Outputer("./../outputs/output2.txt")
o.output(l)