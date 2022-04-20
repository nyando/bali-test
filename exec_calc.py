import csv
import math

exectimes = {}

with open('jvmexectime.csv', 'r') as jvmexec:
    rdr = csv.reader(jvmexec, delimiter=';')
    rdr.__next__()
    for entry in rdr:
        if entry[0] in exectimes:
            exectimes[entry[0]].append((entry[1], entry[2]))
        else:
            exectimes[entry[0]] = [(entry[1], entry[2])]

baseline = exectimes['Test'][0][1]
print('baseline exec cycle count: {}'.format(baseline))

for progname in exectimes.keys():
    for entry in exectimes[progname]:
        print('{}: Input {}, Cycles {}'.format(progname, entry[0], math.floor(float(entry[1]) - float(baseline))))
