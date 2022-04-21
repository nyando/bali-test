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


def writejava(outpath, content):
    with open(outpath, 'w') as outputfile:
        outputfile.write(content)


def compilejava(outpath):
    os.system('javac {}'.format(outpath))


def get_jvm_exectime(prog, paramset):
    templatepath = './javasw/{}.jtmp'.format(prog)
    outpath = './javasw/{}.java'.format(prog)

    writejava(outpath, generate(templatepath, paramset))
    
    compilejava(outpath)

    os.chdir('./javasw')

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


def intrev_jvmtime(i):
    return get_jvm_exectime('IntReverse', { '$REVERSE_INPUT$': str(i), '$LOOPCOUNT$': '2000' })


def sieve_jvmtime(i):
    return get_jvm_exectime('PrimeSieve', { '$SIEVE_INPUT$': str(i), '$LOOPCOUNT$': '2000' })


def towers_jvmtime(i):
    return get_jvm_exectime('TowersOfHanoi', { '$TOWERS_INPUT$': str(i), '$LOOPCOUNT$': '2000' })


def recursive_jvmtime(i):
    return get_jvm_exectime('RecursiveMath', { '$MATH_OP_1$': str(i), '$MATH_OP_2$': str(i), '$LOOPCOUNT$': '2000' })


def qsort_jvmtime(i):
    return get_jvm_exectime('QuickSort', { '$QSORT_INPUT_ARRAY$': gen_random_array(i), '$QSORT_INPUT_LEN$': str(i - 1), '$LOOPCOUNT$': '2000' })


def test_jvmtime():
    return get_jvm_exectime('Test', { })


random.seed(1)

intrev = [1, 12, 123, 1234, 12345]
sieve = [10, 20, 50, 100, 150, 200]
towers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
recursive = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
qsort = [10, 20, 50, 100]

csvoutput = []
csvoutput.append('program;input;exectime\n')

baseline = test_jvmtime()

for i in intrev:
    csvoutput.append('{};{};{}\n'.format('IntReverse', i, intrev_jvmtime(i) - baseline))
    test_jvmtime()
for i in sieve:
    csvoutput.append('{};{};{}\n'.format('PrimeSieve', i, sieve_jvmtime(i) - baseline))
    test_jvmtime()
for i in towers:
    csvoutput.append('{};{};{}\n'.format('TowersOfHanoi', i, towers_jvmtime(i) - baseline))
    test_jvmtime()
for i in recursive:
    csvoutput.append('{};{};{}\n'.format('RecursiveMath', i, recursive_jvmtime(i) - baseline))
    test_jvmtime()
for i in qsort:
    csvoutput.append('{};{};{}\n'.format('QuickSort', i, qsort_jvmtime(i) - baseline))
    test_jvmtime()

csvoutput.append('{};{};{}\n'.format('Test', 0, baseline))

with open('jvmexectime.csv', 'w') as csvout:
    csvout.writelines(csvoutput)
