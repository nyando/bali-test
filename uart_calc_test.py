import serial


ser = serial.Serial(port='COM4',
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1)

IADD, ISUB, INEG, ISHL, ISHR, IAND, IOR, IXOR, IINC = 0b0000, 0b0001, 0b0101, 0b1100, 0b1101, 0b1111, 0b1000, 0b1001, 0b1010

ser.isOpen()

a  = 0xd3ad_b33f
b  = 0xc4fe_b4b3
ops = [IADD, ISUB, INEG, ISHL, ISHR, IAND, IOR, IXOR, IINC]

for op in ops:
    ser.write(a.to_bytes(4, 'little'))
    ser.write(b.to_bytes(4, 'little'))
    ser.write(op.to_bytes(4, 'little'))

    if op == IINC:
        assert int.from_bytes(ser.read(4), 'little') == a + 1
    elif op == IADD:
        assert int.from_bytes(ser.read(4), 'little') == (a + b) & 0xffff_ffff
    elif op == ISUB:
        assert int.from_bytes(ser.read(4), 'little') == a - b
    elif op == IAND:
        assert int.from_bytes(ser.read(4), 'little') == a & b
    elif op == IOR:
        assert int.from_bytes(ser.read(4), 'little') == a | b
    elif op == IXOR:
        assert int.from_bytes(ser.read(4), 'little') == a ^ b
    elif op == INEG:
        assert int.from_bytes(ser.read(4), 'little') == a ^ 0xffff_ffff
    elif op == ISHL:
        assert int.from_bytes(ser.read(4), 'little') == (a << 1) & 0xffff_ffff
    elif op == ISHR:
        assert int.from_bytes(ser.read(4), 'little') == a >> 1
