import socket
import time
import cryptography
from cryptography.fernet import Fernet
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
def load_key():
    return open("key.key", "rb").read()
 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    host = "127.0.0.1"
    port = 8002
    status_connect = s.connect_ex((host, port))
    while status_connect == 0: 
        write_key()
        msg = input("Enter your messager : ").encode('utf-8') 
        f = Fernet( load_key())
        s.sendall(f.encrypt(msg)) 
        print("client recv : ",f.decrypt(s.recv(300)).decode('utf-8')) 
        time.sleep(1)