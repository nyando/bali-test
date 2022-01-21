class ClassFile:
    classfile = None
    magic = 0
    minor = 0
    major = 0
    constpoolcount = 0
    constpool = []
    access = 0
    this = 0
    superclass = 0
    ifacecount = 0
    ifaces = []
    fieldcount = 0
    fields = []
    methodcount = 0
    methods = []
    attribcount = 0
    attribs = []

    def __init__(self, filename):
        with open(filename, 'rb') as file:
            self.classfile = file
            self.parse_classfile()

    def _read_u4(self):
        return int.from_bytes(self.classfile.read(4), byteorder='big')

    def _read_u2(self):
        return int.from_bytes(self.classfile.read(2), byteorder='big')

    def parse_classfile(self):
        self.magic = self._read_u4()
        self.minor = self._read_u2()
        self.major = self._read_u2()
        self.parse_cpinfo()
        self.access = self._read_u2()
        self.superclass = self._read_u2()
        self.ifacecount = self._read_u2()
        for _ in range(0, self.ifacecount):
            self.ifaces.append(self._read_u2())
        self.fieldcount = self._read_u2()
        for _ in range(0, self.fieldcount):
            self.fields.append(self.parse_info())
        self.methodcount = self._read_u2()
        for _ in range(0, self.methodcount):
            self.methods.append(self.parse_info())
        self.attribcount = self._read_u2()
        for _ in range(0, self.attribcount):
            self.attribs.append(self.parse_attribute_info())

    def parse_cpinfo(self):
        self.constpoolcount = self._read_u2()
        for _ in range(0, self.constpoolcount - 1):
            self.parse_constpool_info()

    def parse_constpool_info(self):
        tag = self.classfile.read(1)
        if tag == b'\x07':    # class tag
            self.constpool.append(('CLASS', self._read_u2()))
        elif tag == b'\x0a':  # method ref
            self.constpool.append(('METHOD', self._read_u2(), self._read_u2()))
        elif tag == b'\x03':  # integer ref
            self.constpool.append(('INT', self._read_u4()))
        elif tag == b'\x0c':  # NameAndType ref
            self.constpool.append(('NAMEANDTYPE', self._read_u2(), self._read_u2()))
        elif tag == b'\x01':  # utf8 ref
            self.constpool.append(self.parse_utf8_ref())

    def parse_utf8_ref(self):
        length = self._read_u2()
        return 'UTF8', length, bytes(self.classfile.read(length))

    def parse_info(self):
        access_flags = self._read_u2()
        name_index = self._read_u2()
        descriptor_index = self._read_u2()
        attr_count = self._read_u2()
        attributes = []
        for _ in range(0, attr_count):
            attributes.append(self.parse_attribute_info())
        return access_flags, name_index, descriptor_index, attr_count, attributes

    def parse_attribute_info(self):
        attr_name_index = self._read_u2()
        attr_length = self._read_u4()
        return attr_name_index, attr_length, bytes(self.classfile.read(attr_length))


cf = ClassFile('java/IntReverse.class')
for i, const in (enumerate(cf.constpool)):
    print(str(i + 1) + ': ' + str(const))

for attr in cf.fields:
    print(str(attr))
