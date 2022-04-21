from matplotlib import pyplot as plt
import csv
import math


def read_jvm_results(filename):
    results = {}
    with open(filename, 'r') as resfile:
        rdr = csv.reader(resfile, delimiter=';')
        next(rdr, None)
        baseline = math.floor(float(next(rdr, None)[3]))
        for row in rdr:
            progname = row[0]
            inputval = int(row[1])
            loopcount = int(row[2])
            exectime = math.floor(float(row[3]))
            if progname in results:
                if loopcount in results[progname]:
                    results[progname][loopcount].append((inputval, exectime - baseline))
                else:
                    results[progname][loopcount] = []
                    results[progname][loopcount].append((inputval, exectime - baseline))
            else:
                results[progname] = {}
                results[progname][loopcount] = []
                results[progname][loopcount].append((inputval, exectime - baseline))
    return results


def read_results(filename):
    results = {}
    with open(filename, 'r') as resfile:
        rdr = csv.reader(resfile, delimiter=';')
        next(rdr, None)
        for row in rdr:
            progname = row[0]
            inputval = int(row[1])
            loopcount = int(row[2])
            exectime = math.floor(float(row[3]))
            if progname in results:
                if loopcount in results[progname]:
                    results[progname][loopcount].append((inputval, exectime))
                else:
                    results[progname][loopcount] = []
                    results[progname][loopcount].append((inputval, exectime))
            else:
                results[progname] = {}
                results[progname][loopcount] = []
                results[progname][loopcount].append((inputval, exectime))
    return results


balidata = read_results('exectime.csv')
jvmdata = read_jvm_results('jvmexectime.csv')
prognames = ['IntReverse', 'TowersOfHanoi', 'QuickSort', 'RecursiveMath', 'PrimeSieve']

for progname in prognames:
    for loopcount in balidata[progname]:
        x = [i[0] for i in balidata[progname][loopcount]]
        bali_y = [i[1] for i in balidata[progname][loopcount]]
        jvm_y = [i[1] for i in jvmdata[progname][loopcount]]
        plt.scatter(x, bali_y, c='b', marker='o', label='Bali')
        plt.scatter(x, jvm_y, c='r', marker='o', label='JVM')
        plt.yscale('log')
        plt.legend(loc='upper left')
        plt.title('{} with {} Loops'.format(progname, loopcount))
        plt.show()
