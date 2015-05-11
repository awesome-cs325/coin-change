import matplotlib.pyplot as plt
import numpy as np
import scipy as sc
import sys
import argparse

import timings
import log_graph

def plot(timedict, silentFlag):
    xs = timedict.pop("ns")
    for alg, times in timedict.items():
        ys = ([np.sum(ts) for ts in times])

        plt.plot(xs,ys,label=alg)
    plt.xlabel('amount')
    plt.ylabel('time')

    plt.legend()
    plt.title("Running Times of Various\nCoin Usage Algorithms")

    plt.savefig("../bin/testrun.eps",bbox_inches="tight")
    if not silentFlag:
        plt.show()


if __name__ == "__main__":
    silentFlag = False
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--silent", action="store_true")
    args = parser.parse_args()
    log_graph.plot(args.silent)
    plot(timings.timefuncs(), args.silent)
