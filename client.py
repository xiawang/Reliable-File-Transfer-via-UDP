import socket
import sys
import time
import pickle
import os
import ast

## 134.173.24.150

PACKETSIZE = 100
FILE = 'file.txt'
TIMEOUT = 0.4


def readChunks(file_object, chunk_size=1024):
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data

def main(address, portNum):
    TCP_IP = address
    TCP_PORT = int(portNum)
    BUFFER_SIZE = 1024345
    UDP_IP = address
    UDP_PORT = int(portNum)


    tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        tcpSocket.connect((TCP_IP, TCP_PORT))
    except:
        pass

    f = open(FILE)
    fileSize =  os.path.getsize(FILE)

    numPackets = None
    if fileSize % PACKETSIZE == 0:
        numPackets = fileSize / PACKETSIZE

    else:
        numPackets = fileSize / PACKETSIZE + 1


    packetDict = {}
    i = 0
    for piece in readChunks(f, PACKETSIZE):
        packetDict[i] = piece
        i += 1

    packetList = range(numPackets)

    tcpSocket.send(str(fileSize))
    tcpSocket.close()
    print fileSize
    while True:
        serverResponse = ""

        if packetList == []:
            break

        for packetNum in packetList:


            udpSocket = socket.socket(socket.AF_INET, # Internet
                                socket.SOCK_DGRAM) # UDP

            packet = {
                        str(packetNum): packetDict[packetNum]
                     }


            data = pickle.dumps(packet)

            udpSocket.sendto(data, (UDP_IP, UDP_PORT))


            if (packetNum == packetList[-1]):
                data = None
                tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                tcpSocket.connect((TCP_IP, TCP_PORT))
                print "Waiting on server response"
                while 1:
                    data = tcpSocket.recv(BUFFER_SIZE)
                    if type(data) == str:
                        print data
                        serverResponse += data
                    if data[-1] == ']': break
                print "response recieved"


        try:
            packetList = ast.literal_eval(serverResponse)
        except:
            print "OH NO, NO PACKETLIST"
            packetList = [0]


        tcpSocket.close()



if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])




