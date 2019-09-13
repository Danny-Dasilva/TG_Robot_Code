import serial
import time

class Brooklyn:
    def __init__(self, port='/dev/ttyACM0'):
        self.port = port
        self.ser = serial.Serial(port=self.port,baudrate=1000000,writeTimeout=0.05)
        self.connect()
        self.ready = False
    def connect(self):
        self.ser.write(bytearray([170]))
        time.sleep(2)
        if ord(self.ser.read()) == 170:
            self.ready = True

    def send_cmd(self, cmd, cid, data):
        packetsize = len(data)
        checksum1 = packetsize ^ cid ^ cmd
        for byte in data:
            checksum1 = checksum1 ^ byte
        checksum1 = checksum1 & 0xFE
        checksum2 = (~checksum1) & 0xFE
        packet = ([0xFF, 0xFF, cmd, cid, packetsize])
        for byte in data:
            packet.append(byte)
        packet.append(checksum1)
        packet.append(checksum2)
        self.ser.write(packet)
        #data = []
        #for i in range(9):
        #    data.append(ord(self.readBytes(self.ser, 1)[0]))

    def readBytes(self,serial, numbytes):
        data = list()
        for i in range(0, numbytes):
            data.append(serial.read())
        return data

    def setSpeed(self, motor, val):
        motor -= 1
        dir = 0
        val = int(val * 255)
        if(val > 0):
            dir = 1
        elif(val < 0):
            dir = 0
        val = abs(val)
        self.send_cmd(0x00, motor, [val, dir])
    def close(self):
        self.ser.write(bytearray([255,255,255]))
        print("UH")
