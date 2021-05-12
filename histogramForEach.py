from parser import Parser
from Outputer import Outputer
"""
Working
"""

def solve(filename):
  parser = Parser(filename)
  h = []
  s = set()
  h,s = parser.readDataHistogram(h,s)
  numbers = sorted(list(s),reverse = True)

  min_orders = calculate_orders(h)
  round_count = parser.getRoundCount()

  for num in numbers[1:]:
    #update with new num value
    m = parser.getRoundCount()

    for i in range(parser.getPlayerCount()):
      j=0
      totalChange = 0
      while j < len(h[i][1]):
        if h[i][1][j][0] > num:
          totalChange += h[i][1][j][1]
          h[i][1][j] = (num,h[i][1][j][1])
          if len(h[i][1]) > j+1 and h[i][1][j][0]==h[i][1][j+1][0]:
            temp = h[i][1].pop(j)
            h[i][1][j] = (h[i][1][j][0],h[i][1][j][1]+temp[1])
          j += 1
          continue
        break
      m = min(totalChange,m)
    
    if m > 0:
      round_count -=m
      for i in range(parser.getPlayerCount()):
        if h[i][1][0][1] > m:
          h[i][1][0]=(h[i][1][0][0],h[i][1][0][1]-m)
        else:
          h[i][1].pop(0)

    
    #calculate min orders
    orders = calculate_orders(h)
    for i in range(parser.getPlayerCount()):
      min_orders[i] = min(min_orders[i],orders[i])
  return min_orders

def getSum(h):
  s=0
  for x,y in h:
    s += x*y
  return s

def calculate_orders(l):
  sums = [(x[0],getSum(x[1])) for x in l]
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
      







l= solve("./Test Cases/baby_comp_4.txt")
o = Outputer("./output4.txt")
o.output(l)
