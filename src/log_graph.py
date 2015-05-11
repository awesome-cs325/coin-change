import matplotlib.pyplot as plt
import numpy as np
import scipy as sc
import sys
import argparse

ns = [
        [
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            13,
            20,
            25,
            30,
            35,
            40],
        [
            4,
            5,
            6,
            7,
            8,
            9,
            10],
        [
            4,
            5,
            6,
            7,
            8,
            9,
            10]
        ];

times = [
        [
            14.336,
            14.350,
            14.617,
            14.281,
            14.107,
            14.125,
            13.998,
            13.895,
            13.867,
            13.931,
            13.877,
            14.001,
            13.873
            ],
        [
            0.020,
            0.013,
            0.011,
            0.009,
            0.008,
            0.007,
            0.007
            ],
        [
            168.257,
            57.118,
            18.659,
            6.385,
            2.223,
            0.743,
            0.245
            ]
        ];

timedict = {};
timedict["Brute Force, A=21"] = {
        "ns" : ns[2],
        "times" : times[2]
        };
timedict["Greedy, A=60000"] = {
        "ns" : ns[1],
        "times" : times[1]
        };
timedict["DP, A=6000"] = {
        "ns" : ns[0],
        "times" : times[0]
        };

def plot(silentFlag):
    for alg in timedict.keys():
        xs = timedict[alg]["ns"];
        ys = timedict[alg]["times"];
        plt.plot(xs,ys,label=alg)

    plt.xlabel('number of available coins')
    plt.ylabel('time')

    plt.legend()
    plt.title("Running Times of Various\nCoin Usage Algorithms")

    plt.savefig("../bin/testrun_log.eps",bbox_inches="tight")
    if not silentFlag:
        plt.show()


if __name__ == "__main__":
    silentFlag = False
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--silent", action="store_true")
    args = parser.parse_args()
    plot(args.silent)
