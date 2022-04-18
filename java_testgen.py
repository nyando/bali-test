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


def get_jvm_exectime(prog, paramset):
    templatepath = './javasw/{}.jtmp'.format(prog)
    outpath = './javasw/{}.java'.format(prog)
    
    writejava(outpath, generate(templatepath, paramset))

    proc = subprocess.Popen(['java', '-Xint', '-XX:-TieredCompilation', './javasw/{}.java'.format(prog)], stdout=subprocess.PIPE, text=True)

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


def intrev_jvmtime(i):
    return get_jvm_exectime('IntReverse', { '$REVERSE_INPUT$': str(i) })


def sieve_jvmtime(i):
    return get_jvm_exectime('PrimeSieve', { '$SIEVE_INPUT$': str(i) })


def towers_jvmtime(i):
    return get_jvm_exectime('TowersOfHanoi', { '$TOWERS_INPUT$': str(i) })


def recursive_jvmtime(i):
    return get_jvm_exectime('RecursiveMath', { '$MATH_OP_1$': str(i), '$MATH_OP_2$': str(i) })


def qsort_jvmtime(i):
    return get_jvm_exectime('QuickSort', { '$QSORT_INPUT_ARRAY$': gen_random_array(i), '$QSORT_INPUT_LEN$': str(i - 1) })


random.seed(1)

intrev = [1, 12, 123, 1234, 12345]
sieve = [10, 20, 50, 100, 150, 200]
towers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
recursive = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
qsort = [10, 20, 50, 100, 150, 200]

csvoutput = []
csvoutput.append('program;input;exectime\n')

for i in intrev:
    csvoutput.append('{};{};{}\n'.format('IntReverse', i, intrev_jvmtime(i)))
for i in sieve:
    csvoutput.append('{};{};{}\n'.format('PrimeSieve', i, sieve_jvmtime(i)))
for i in towers:
    csvoutput.append('{};{};{}\n'.format('TowersOfHanoi', i, towers_jvmtime(i)))
for i in recursive:
    csvoutput.append('{};{};{}\n'.format('RecursiveMath', i, recursive_jvmtime(i)))
for i in qsort:
    csvoutput.append('{};{};{}\n'.format('QuickSort', i, qsort_jvmtime(i)))

with open('jvmexectime.csv', 'w') as csvout:
    csvout.writelines(csvoutput)
