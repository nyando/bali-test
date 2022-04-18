import subprocess
import random


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


def get_fpga_exectime(prog, paramset):
    templatepath = './java/{}.jtmp'.format(prog)
    outpath = './java/{}.java'.format(prog)
    
    writejava(outpath, generate(templatepath, paramset))

    proc = subprocess.Popen(["just", "testbin", prog], stdout=subprocess.PIPE, text=True)

    try:
        out, _ = proc.communicate(timeout=30)
    except TimeoutExpired:
        proc.kill()
        out, _ = proc.communicate()
        return -1

    return int(out)


def gen_random_array(length):
    arr = [i for i in range(length)]
    random.shuffle(arr)
    arrstring = str(arr).replace('[', '{').replace(']', '}')
    return arrstring


def intrev_exectime(i):
    return get_fpga_exectime('IntReverse', { '$REVERSE_INPUT$': str(i) })


def sieve_exectime(i):
    return get_fpga_exectime('PrimeSieve', { '$SIEVE_INPUT$': str(i) })


def towers_exectime(i):
    return get_fpga_exectime('TowersOfHanoi', { '$TOWERS_INPUT$': str(i) })


def recursive_exectime(i):
    return get_fpga_exectime('RecursiveMath', { '$MATH_OP_1$': str(i), '$MATH_OP_2$': str(i) })


def qsort_exectime(i):
    return get_fpga_exectime('QuickSort', { '$QSORT_INPUT_ARRAY$': gen_random_array(i), '$QSORT_INPUT_LEN$': str(i - 1) })


random.seed(1)

intrev = [1, 12, 123, 1234, 12345]
sieve = [10, 20, 50, 100, 150, 200]
towers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
recursive = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
qsort = [10, 20, 50, 100, 150, 200]

csvoutput = []
csvoutput.append('program;input;exectime\n')

for i in intrev:
    csvoutput.append('{};{};{}\n'.format('IntReverse', i, intrev_exectime(i)))
for i in sieve:
    csvoutput.append('{};{};{}\n'.format('PrimeSieve', i, sieve_exectime(i)))
for i in towers:
    csvoutput.append('{};{};{}\n'.format('TowersOfHanoi', i, towers_exectime(i)))
for i in recursive:
    csvoutput.append('{};{};{}\n'.format('RecursiveMath', i, recursive_exectime(i)))
for i in qsort:
    csvoutput.append('{};{};{}\n'.format('QuickSort', i, qsort_exectime(i)))

with open('exectime.csv', 'w') as csvout:
    csvout.writelines(csvoutput)
