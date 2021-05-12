from parser import Parser
from Outputer import Outputer
import matplotlib.pyplot as plt
def solve(filename):
  parser = Parser(filename)
  l = []
  parser.readData(l)
  s = set()
  for x,y in l:
    for i in y:
      s.add(i)
  numbers = sorted(list(s),reverse = True)
  min_orders = calculate_orders(l)
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
      min_orders[i] = min(min_orders[i],orders[i])
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
      
def calculate_mean(player):
  return sum(player[1])/len(player[1])
def calculate_variance(p,m):
  v= 0
  for x in p[1]:
    v += (m-x)**2
  return v/(len(p[1])-1)


filename ="./Test Cases/baby_comp_4.txt"

s= solve(filename)
parser = Parser(filename)
l = []
parser.readData(l)
x = []
y= []
z = []
for i in range(len(l)):
  player = l[i]
  m = calculate_mean(player)
  v = calculate_variance(player,m)
  z.append(v)
  x.append(m)
  y.append(s[i])
plt.figure()
plt.title("means")
plt.bar(y,x)
plt.figure()
plt.title("variances")
plt.bar(y,z)
plt.show()