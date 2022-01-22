OPCODES = {
    0x00: 'nop',
    0x01: 'aconst_null',
    0x02: 'iconst_m1',
    0x03: 'iconst_0',
    0x04: 'iconst_1',
    0x05: 'iconst_2',
    0x06: 'iconst_3',
    0x07: 'iconst_4',
    0x08: 'iconst_5',
    0x10: 'bipush',
    0x11: 'sipush',
    0x12: 'ldc',
    0x15: 'iload',
    0x19: 'aload',
    0x1a: 'iload_0',
    0x1b: 'iload_1',
    0x1c: 'iload_2',
    0x1d: 'iload_3',
    0x2a: 'aload_0',
    0x2b: 'aload_1',
    0x2c: 'aload_2',
    0x2d: 'aload_3',
    0x2e: 'iaload',
    0x32: 'aaload',
    0x33: 'baload',
    0x34: 'caload',
    0x35: 'saload',
    0x36: 'istore',
    0x3a: 'astore',
    0x3b: 'istore_0',
    0x3c: 'istore_1',
    0x3d: 'istore_2',
    0x3e: 'istore_3',
    0x4b: 'astore_0',
    0x4c: 'astore_1',
    0x4d: 'astore_2',
    0x4e: 'astore_3',
    0x4f: 'iastore',
    0x53: 'aastore',
    0x54: 'bastore',
    0x55: 'castore',
    0x56: 'sastore',
    0x57: 'pop',
    0x59: 'dup',
    0x5f: 'swap',
    0x60: 'iadd',
    0x64: 'isub',
    0x68: 'imul',
    0x6c: 'idiv',
    0x70: 'irem',
    0x74: 'ineg',
    0x78: 'ishl',
    0x7a: 'ishr',
    0x7c: 'iushr',
    0x7e: 'iand',
    0x80: 'ior',
    0x82: 'ixor',
    0x84: 'iinc',
    0x99: 'ifeq',
    0x9a: 'ifne',
    0x9b: 'iflt',
    0x9c: 'ifge',
    0x9d: 'ifgt',
    0x9e: 'ifle',
    0x9f: 'if_icmpeq',
    0xa0: 'if_icmpne',
    0xa1: 'if_icmplt',
    0xa2: 'if_icmpge',
    0xa3: 'if_icmpgt',
    0xa4: 'if_icmple',
    0xa7: 'goto',
    0xac: 'ireturn',
    0xb0: 'areturn',
    0xb1: 'return',
    0xb7: 'invokespecial',
    0xb8: 'invokestatic',
    0xbc: 'newarray'
}

OPCODE_ARG_COUNT = {
    0x00: 0,
    0x01: 0,
    0x02: 0,
    0x03: 0,
    0x04: 0,
    0x05: 0,
    0x06: 0,
    0x07: 0,
    0x08: 0,
    0x10: 1,
    0x11: 2,
    0x12: 1,
    0x15: 1,
    0x19: 1,
    0x1a: 0,
    0x1b: 0,
    0x1c: 0,
    0x1d: 0,
    0x2a: 0,
    0x2b: 0,
    0x2c: 0,
    0x2d: 0,
    0x2e: 0,
    0x32: 0,
    0x33: 0,
    0x34: 0,
    0x35: 0,
    0x36: 1,
    0x3a: 1,
    0x3b: 0,
    0x3c: 0,
    0x3d: 0,
    0x3e: 0,
    0x4b: 0,
    0x4c: 0,
    0x4d: 0,
    0x4e: 0,
    0x4f: 0,
    0x53: 0,
    0x54: 0,
    0x55: 0,
    0x56: 0,
    0x57: 0,
    0x59: 0,
    0x5f: 0,
    0x60: 0,
    0x64: 0,
    0x68: 0,
    0x6c: 0,
    0x70: 0,
    0x74: 0,
    0x78: 0,
    0x7a: 0,
    0x7c: 0,
    0x7e: 0,
    0x80: 0,
    0x82: 0,
    0x84: 0,
    0x99: 2,
    0x9a: 2,
    0x9b: 2,
    0x9c: 2,
    0x9d: 2,
    0x9e: 2,
    0x9f: 2,
    0xa0: 2,
    0xa1: 2,
    0xa2: 2,
    0xa3: 2,
    0xa4: 2,
    0xa7: 2,
    0xac: 0,
    0xb0: 0,
    0xb1: 0,
    0xb7: 2,
    0xb8: 2,
    0xbc: 1
}


class MethodCode:
    def __init__(self, name, max_stack, max_local, code_segment):
        self.name = name
        self.max_stack = max_stack
        self.max_local = max_local
        self.code = code_segment

    def get_name(self):
        return self.name

    def get_stack(self):
        return self.max_stack

    def get_local(self):
        return self.max_local

    def get_code(self):
        return self.code


class ClassFile:
    class_file = None
    magic = 0
    minor = 0
    major = 0
    const_count = 0
    const_pool = []
    utf8_consts = {}
    access = 0
    this = 0
    superclass = 0
    interface_count = 0
    interfaces = []
    field_count = 0
    fields = []
    method_count = 0
    methods = []
    attr_count = 0
    attribs = []
    code_segments = []

    def __init__(self, filename):
        with open(filename, 'rb') as file:
            self.class_file = file
            self.parse_class_file()

    def _read_u4(self):
        return int.from_bytes(self.class_file.read(4), byteorder='big')

    def _read_u2(self):
        return int.from_bytes(self.class_file.read(2), byteorder='big')

    def parse_class_file(self):
        self.magic = self._read_u4()
        self.minor = self._read_u2()
        self.major = self._read_u2()
        self.parse_const_pool()
        for index, value in enumerate(self.const_pool):
            if value[0] == 'UTF8':
                self.utf8_consts[index + 1] = value[2].decode('UTF-8')
        self.access = self._read_u2()
        self.superclass = self._read_u2()
        self.interface_count = self._read_u2()
        for _ in range(0, self.interface_count):
            self.interfaces.append(self._read_u2())
        self.field_count = self._read_u2()
        for _ in range(0, self.field_count):
            self.fields.append(self.parse_info())
        self.method_count = self._read_u2()
        for _ in range(0, self.method_count):
            self.methods.append(self.parse_info())
        self.attr_count = self._read_u2()
        for _ in range(0, self.attr_count):
            self.attribs.append(self.parse_attribute_info(''))

    def parse_const_pool(self):
        self.const_count = self._read_u2()
        for _ in range(0, self.const_count - 1):
            self.parse_const_pool_info()

    def parse_const_pool_info(self):
        tag = self.class_file.read(1)
        if tag == b'\x07':    # class tag
            self.const_pool.append(('CLASS', self._read_u2()))
        elif tag == b'\x0a':  # method ref
            self.const_pool.append(('METHOD', self._read_u2(), self._read_u2()))
        elif tag == b'\x03':  # integer ref
            self.const_pool.append(('INT', self._read_u4()))
        elif tag == b'\x0c':  # NameAndType ref
            self.const_pool.append(('NAMEANDTYPE', self._read_u2(), self._read_u2()))
        elif tag == b'\x01':  # utf8 ref
            self.const_pool.append(self.parse_utf8_ref())

    def parse_utf8_ref(self):
        length = self._read_u2()
        return 'UTF8', length, bytes(self.class_file.read(length))

    def parse_info(self):
        access_flags = self._read_u2()
        name_index = self._read_u2()
        descriptor_index = self._read_u2()
        attr_count = self._read_u2()
        attributes = []
        name = ''
        if name_index in self.utf8_consts:
            name = self.utf8_consts[name_index]
        for _ in range(0, attr_count):
            attributes.append(self.parse_attribute_info(name))
        return access_flags, name_index, descriptor_index, attr_count, attributes

    def parse_attribute_info(self, name):
        attr_name_index = self._read_u2()
        attr_length = self._read_u4()
        if attr_name_index in self.utf8_consts and self.utf8_consts[attr_name_index] == 'Code':
            return self.parse_code_segment(name)
        else:
            return attr_name_index, attr_length, bytes(self.class_file.read(attr_length))

    def parse_code_segment(self, name):
        max_stack = self._read_u2()
        max_locals = self._read_u2()
        code_len = self._read_u4()
        code = bytes(self.class_file.read(code_len))
        self.code_segments.append(MethodCode(name, max_stack, max_locals, code))
        exception_table_len = self._read_u2()
        exception_table = []
        for _ in range(exception_table_len):
            exception_table.append((self._read_u2(), self._read_u2(), self._read_u2(), self._read_u2()))
        attr_count = self._read_u2()
        for _ in range(attr_count):
            self.parse_attribute_info(name)

    def get_methods(self):
        return self.code_segments


class ClassOutput:
    def __init__(self, class_file):
        self.class_file = class_file

    def print_const_pool(self):
        for const_index, const in (enumerate(self.class_file.const_pool)):
            print(str(const_index + 1) + ': ' + str(const))

    def print_methods(self):
        for method in self.class_file.get_methods():
            print(method.get_name())
            print(method.get_stack())
            print(method.get_local())
            code = method.get_code()

            i = 0
            while i < len(code):
                if code[i] in OPCODES:
                    argc = OPCODE_ARG_COUNT[code[i]]
                    print(str(i) + ': ' + OPCODES[code[i]] + str([code[i + j] for j in range(1, argc + 1)]))
                    i += argc + 1
                else:
                    print(str(code[i]) + ' is not a valid opcode')
                    i += 1


cf = ClassFile('java/RecursiveMath.class')
out = ClassOutput(cf)
out.print_const_pool()
out.print_methods()
