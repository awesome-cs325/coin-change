#!python3

import ast
import bisect
import os
import sys

# ALGORITHM 1
def changeslow(coinValues, amount):
    coinCounts = [0] * len(coinValues)
    coinTotal = 0
    index = bisect.bisect_left(coinValues, amount)
    if index != len(coinValues) and coinValues[index] == amount:
        coinCounts[index] += 1
        coinTotal = 1
    else:
        minCoins1 = []
        minCoins2 = []
        for i in range(1, amount):
            (coins1, total1) = changeslow(coinValues, i)
            (coins2, total2) = changeslow(coinValues, amount - i)
            if total1 + total2 < coinTotal or coinTotal == 0:
                coinTotal = total1 + total2
                minCoins1 = coins1
                minCoins2 = coins2
                coinCounts = [x + y for x, y in zip(minCoins1, minCoins2)]
    return (coinCounts, coinTotal);
    

# ALGORITHM 2
def changegreedy(coinValues, amount):
    coinCounts = [0] * len(coinValues)
    k = len(coinValues) - 1
    while k >= 0:
        if (coinValues[k] == amount):
            coinCounts[k] += 1
            return (coinCounts, 1)
        if (coinValues[k] > amount):
            k -= 1;
        if (coinValues[k] < amount):
            sum2 = amount - coinValues[k]
            (coinlist, totalcoins) = changegreedy(coinValues, sum2)
            coinlist[k] += 1
            totalcoins += 1
            return (coinlist, totalcoins)


# ALGORITHM 3            
# The list of coins that the dp table is built for
coinListAlg3 = []
# The coin table storing optimal sets of coins for a given amount
coinTableAlg3 = []

def changedpHelper(coinValues, amount):
    global coinTableAlg3
    if not coinTableAlg3[amount]:
        index = bisect.bisect_left(coinValues, amount)
        if index != len(coinValues) and coinValues[index] == amount:
            coinIndices = [0] * len(coinValues)
            coinIndices[index] = 1
            coinTableAlg3[amount] = (coinIndices, 1)
        else:
            coinTotal = 0
            minCoins1 = []
            minCoins2 = []
            for i in range(1, amount):
                (coins1, total1) = changedpHelper(coinValues, i)
                (coins2, total2) = changedpHelper(coinValues, amount - i)
                if total1 + total2 < coinTotal or coinTotal == 0:
                    coinTotal = total1 + total2
                    minCoins1 = coins1
                    minCoins2 = coins2
            coinTableAlg3[amount] = ([x + y for x, y in zip(minCoins1, minCoins2)], coinTotal)
    return coinTableAlg3[amount]

def changedp(coinValues, amount):
    global coinListAlg3
    coinListAlg3 = coinValues
    global coinTableAlg3
    coinTableAlg3 = [0] * (amount + 1)
    return changedpHelper(coinValues, amount)

# test for arguments
if len(sys.argv) != 2:
    print('Usage: Project2 input_file')
    sys.exit(0)

inputfile = sys.argv[1]

# test that filename in argument exists
if not os.path.isfile(inputfile):
    print('Error: file does not exist')
    sys.exit(1)
    
# create output file name
base, ext = os.path.splitext(inputfile)
base = base + 'change'
outputfile = base + ext

# read input file, creating problem list from lines read
# WE ARE ASSUMING THAT THE COIN LIST IS ALREADY SORTED

coinList = []
sumList = []

fileobj = open(inputfile, "r")

line = fileobj.readlines()
for line_num, i in enumerate(line):
    if (i != '') and (i != '\n'):
        if (line_num % 2 == 1):
            sumList.append(i)
        else:
            coinList.append(ast.literal_eval(i))

fileobj.close()

of = open(outputfile, "w")

# 
#   SOLVE WITH ALGORITHM 1
#

of.write("SOLVING WITH ALGORITHM #1:\n\n")

j = 0
for i in coinList:
    coins = coinList[j]
    sum = int(sumList[j])
    (cList, cTot) = changeslow(coins, sum)
    
    of.write(str(cList))
    of.write("\n")
    of.write(str(cTot))
    of.write("\n")
    j += 1


#
#   SOLVE WITH ALGORITHM 2
#

of.write("\n\nSOLVING WITH ALGORITHM #2:\n\n")

j = 0
for i in coinList:
    coins = coinList[j]
    sum = int(sumList[j])
    (cList, cTot) = changegreedy(coins, sum)
    
    of.write(str(cList))
    of.write("\n")
    of.write(str(cTot))
    of.write("\n")
    j += 1


#
#   SOLVE WITH ALGORITHM 3
#

of.write("\n\nSOLVING WITH ALGORITHM #3:\n\n")

j = 0
for i in coinList:
    
    coins = coinList[j]
    sum = int(sumList[j])
    (cList, cTot) = changedp(coins, sum)
    
    of.write(str(cList))
    of.write("\n")
    of.write(str(cTot))
    of.write("\n")
    j += 1

of.close()