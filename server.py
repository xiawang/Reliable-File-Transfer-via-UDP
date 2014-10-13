import socket
import ast
import sys
import os
import StringIO
import pickle
import urllib2

TIMEOUT = .5
PACKETSIZE = 100
FILE = 'out.txt'

def main(address, portNum):


    UDP_IP = address
    UDP_PORT = int(portNum)
    TCP_IP = address

    TCP_PORT = int(portNum)
    BUFFER_SIZE =  10244564 # Normally 1024, but we want fast response

    tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpSocket.bind((TCP_IP, TCP_PORT))
    tcpSocket.listen(1)

    udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    udpSocket.bind((UDP_IP, UDP_PORT))
    udpSocket.settimeout(5 * TIMEOUT)

    tcpConn, tcpAddr = tcpSocket.accept()
    tcpData = tcpConn.recv(BUFFER_SIZE)

    fileSize = int(tcpData)


    numPackets = None
    if fileSize % PACKETSIZE == 0:
        numPackets = fileSize / PACKETSIZE
    else:
        numPackets = fileSize / PACKETSIZE + 1

    packetDict = {}
    for i in range(numPackets):
        packetDict[i] = None
        i += 1


    while True:

        try:
            udpData, udpAddr = udpSocket.recvfrom(1024) # buffer size is 1024 bytes
            udpData = pickle.loads(udpData)

            seenPercent = []

            for key in udpData:

                percent =  int((100* (int(key) + 1) / numPackets))
                print percent
                packetDict[int(key)] = udpData[key]

        except:
            print "accepting tcpSocket"
            tcpConn, tcpAddr = tcpSocket.accept()
            droppedPacketList = []

            tmpList = []

            for i in droppedPacketList:
                if packetDict[i] == None:
                     tmpList += [i]
            droppedPacketList = tmpList


            print "sending packetList"
            tcpConn.sendall(str(droppedPacketList))
            print "sent packetList"

            if (droppedPacketList == []):

                with open(FILE, 'wb') as fp:
                    for key in packetDict:
                        fp.write(packetDict[key])


                tcpConn.close()
                return