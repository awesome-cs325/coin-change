#!python3

import time
import random
import pprint

import ast
import bisect
import os
import sys

from numba import jit

# ALGORITHM 1
def changeslow(coinValues, amount):
    #pprint.pprint(amount)
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

def timefunc(func,args,moreargs):

    startTime = time.time()
    func(args,moreargs)
    elapsedTime = time.time() - startTime

    return elapsedTime

def timegen(func,cvs,alist,loops):
    times = []
    #for each size n...
    for a in alist:
        #calculate the time for each of the amounts
        #pprint.pprint(a)
        #pprint.pprint(cvs)
        times.append([timefunc(func,cvs,a) for i in range(loops)])

    return times

def timefuncs():
    coin_vals = list(range(2,31,2))
    coin_vals.insert(0,1);
    a_list = list(range(20,30,1))
    loop_cnt = [1,1000,1]
    algs = [changeslow,changegreedy,changedp]
    timedict = {}
    #generate dictionaries for ease of labels in graphing
    for i in range(0,2):
        timedict[str(algs[i].__name__)] = timegen(algs[i],coin_vals,a_list,loop_cnt[i])

    timedict["ns"] = a_list
    return timedict

def main():
    timedict = timefuncs()
    pprint.pprint(timedict)
