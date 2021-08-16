import os, sys
import socket
import subprocess
from cryptography.fernet import Fernet
#---SETUP----
HOST = '192.168.1.117'#--Set HOST here--
PORT = 443


#Start socket and connect, send stratup message
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect((HOST,PORT))
#s.send('Connection Established!\n')
#//-----------------INPUT MSG HERE----------------------
message = "The secret password is killbill3232"
key = Fernet.generate_key()
#Fernet class instance with the key
fernet = Fernet(key)


print("Using Fernet key: ")
print( key)
print("Sending Encrypted MSG:")
print( message)
encMessage = fernet.encrypt(message.encode())
print("Encrypted message: ")
print(encMessage)
decMessage = fernet.decrypt(encMessage).decode()

print("Decrypted message: ")
print(decMessage)


#s.send(encryptedString)
#s.close()


