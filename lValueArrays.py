from parser import Parser
from Outputer import Outputer
"""
Current Best
Worst case complexity: O(n*m*n*m)
"""
# Array of length player count [(index, sum)]*player_count
#   sums

# For each player keep:
#   numbers array (sorted)
#   index of last unchanged value (before it all are equal to l value)

# l values in sorted list(set())

# min_orders array

# calculate dl and update sum using that value dl = li - li-1

def main():
  filename = "./Test Cases/baby_comp_2.txt"
  #filename = "./random_test_case.txt"
  parser = Parser(filename)
  players = []
  parser.readDataNew(players)
  playerCount = parser.getPlayerCount()
  roundCount = parser.getRoundCount()
  for i in range(playerCount):
    players[i] = sorted(players[i],reverse=True)
  s = set()
  for y in players:
    for i in y:
      s.add(i)
  l_values = sorted(list(s),reverse = True)
  sums = [sum(player) for player in players]
  min_orders = calculate_orders(sums)
  #print(sums)
  #print(min_orders)
  k = [0]*playerCount
  old_l_value = l_values.pop(0)
  for l_value in l_values:
    for i in range(playerCount):
      current = players[i]
      sums[i] += (k[i] * (l_value - old_l_value))
      dv = 0
      if k[i] < roundCount:
        while current[k[i]] >= l_value:
          dv -= (current[k[i]] - l_value)
          k[i]+=1
          if k[i]==roundCount:
            break
      sums[i] += dv
    orders = calculate_orders(sums)
    #print(sums)
    #print(orders)
    for i in range(playerCount):
      min_orders[i] = min(min_orders[i],orders[i])
    old_l_value = l_value
  outputer = Outputer("./output6.txt")
  outputer.output(min_orders)


      





def calculate_orders(s):
  sums = [(i,s[i]) for i in range(len(s))]
  sums = sorted(sums,key=lambda y: y[1],reverse=True)
  orders = [0]*len(sums)
  o = len(sums)
  orders[sums[0][0]] = o
  o -=1
  for i in range(1,len(sums)):
    if sums[i][1] < sums[i-1][1]:
     orders[sums[i][0]] = o
    else:
      orders[sums[i][0]] = orders[sums[i-1][0]]
    o -=1
  return orders



main()