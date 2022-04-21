import subprocess
import random
import os


def generate(inpath, paramset):
    content = ''
    with open(inpath, 'r') as inputfile:
        content = inputfile.read()
        for k, v in paramset.items():
            content = content.replace(k, v)
    return content


def get_jvm_exectime(prog, paramset):
    templatepath = './java/{}.jtmp'.format(prog)
    outpath = './java/{}.java'.format(prog)

    with open(outpath, 'w') as outputfile:
        outputfile.write(generate(templatepath, paramset))
    
    os.system('javac {}'.format(outpath))

    os.chdir('./java')

    timelist = []
    for _ in range(100):
        proc = subprocess.run(['perf', 'stat', '--event=cycles', 'java', '-Xint', prog], capture_output=True)
        cycles = parse_cycles(proc.stderr.decode('utf-8'))
        print(cycles)
        timelist.append(cycles)

    os.chdir('..')

    return sum(timelist) / len(timelist)


def parse_cycles(perfout):
    for line in perfout.splitlines():
        if 'cycles' in line:
            return int(line.split()[0].replace(',', ''))


def gen_random_array(length):
    arr = [i for i in range(length)]
    random.shuffle(arr)
    arrstring = str(arr).replace('[', '{').replace(']', '}')
    return arrstring


def intrev_jvmtime(i, j):
    return get_jvm_exectime('IntReverse', { '$REVERSE_INPUT$': str(i), '$LOOPCOUNT$': str(j) })


def sieve_jvmtime(i, j):
    return get_jvm_exectime('PrimeSieve', { '$SIEVE_INPUT$': str(i), '$LOOPCOUNT$': str(j) })


def towers_jvmtime(i, j):
    return get_jvm_exectime('TowersOfHanoi', { '$TOWERS_INPUT$': str(i), '$LOOPCOUNT$': str(j) })


def recursive_jvmtime(i, j):
    return get_jvm_exectime('RecursiveMath', { '$MATH_OP_1$': str(i), '$MATH_OP_2$': str(i), '$LOOPCOUNT$': str(j) })


def qsort_jvmtime(i, j):
    return get_jvm_exectime('QuickSort', { '$QSORT_INPUT_ARRAY$': gen_random_array(i), '$QSORT_INPUT_LEN$': str(i - 1), '$LOOPCOUNT$': str(j) })


def test_jvmtime():
    return get_jvm_exectime('BaselineTest', { })


random.seed(1)

intrev = [1, 12, 123, 1234, 12345]
sieve = [10, 20, 50, 100, 150, 200]
towers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
recursive = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
qsort = [10, 20, 50, 100]

csvoutput = []
csvoutput.append('program;input;exectime\n')

baseline = test_jvmtime()

for j in [1000, 2000, 3000, 4000, 5000]:
    for i in intrev:
        csvoutput.append('{};{};{};{}\n'.format('IntReverse', i, j, intrev_jvmtime(i, j)))
    for i in sieve:
        csvoutput.append('{};{};{};{}\n'.format('PrimeSieve', i, j, sieve_jvmtime(i, j)))
    for i in towers:
        csvoutput.append('{};{};{};{}\n'.format('TowersOfHanoi', i, j, towers_jvmtime(i, j)))
    for i in recursive:
        csvoutput.append('{};{};{};{}\n'.format('RecursiveMath', i, j, recursive_jvmtime(i, j)))
    for i in qsort:
        csvoutput.append('{};{};{};{}\n'.format('QuickSort', i, j, qsort_jvmtime(i, j)))

csvoutput.append('{};{};{}\n'.format('Test', 0, baseline))

with open('jvmexectime.csv', 'w') as csvout:
    csvout.writelines(csvoutput)
