from matplotlib import pyplot as plt
import csv


def read_results(filename):
    results = {}
    with open(filename, 'r') as resfile:
        rdr = csv.reader(resfile, delimiter=';')
        next(rdr, None)
        for row in rdr:
            progname = row[0]
            inputval = int(row[1])
            exectime = int(row[2])
            if progname in results:
                results[progname].append((inputval, exectime))
            else:
                results[progname] = []
                results[progname].append((inputval, exectime))
    return results


balidata = read_results('exectime.csv')
jvmdata = read_results('jvmexectime.csv')
prognames = ['IntReverse', 'TowersOfHanoi', 'QuickSort', 'RecursiveMath', 'PrimeSieve']

for progname in prognames:
    x = [i[0] for i in balidata[progname]]
    bali_y = [i[1] * 10 for i in balidata[progname]]
    jvm_y = [i[1] for i in jvmdata[progname]]
    plt.scatter(x, bali_y, c='b', marker='o', label='Bali')
    plt.scatter(x, jvm_y, c='r', marker='o', label='JVM')
    plt.yscale('log')
    plt.legend(loc='upper left')
    plt.title(progname)
    plt.show()
