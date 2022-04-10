import serial
import time

ser = serial.Serial(port='/dev/ttyUSB1',
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1)

ser.isOpen()

for i in range(0, 0x0F):
    ser.write(i.to_bytes(1, 'little'))
    print('wrote {}, read response {}'.format(i.to_bytes(1, 'little'), ser.read(1)))
    time.sleep(1)

