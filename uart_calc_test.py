import serial


ser = serial.Serial(port='COM4',
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1)

IINC, IADD, ISUB, IAND, IOR, IXOR, INEG, ISHL, ISHR = 0b0000, 0b0001, 0b0010, 0b0110, 0b0111, 0b01000, 0b1001, 0b1010, 0b1011

ser.isOpen()

a  = 0xd3ad_b33f
b  = 0xc4fe_b4b3
ops = [IINC, IADD, ISUB, IAND, IOR, IXOR, INEG, ISHL, ISHR]

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
