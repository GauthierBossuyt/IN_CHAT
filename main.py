#REQUIRED IMPORTS TO MAKE THIS CODE RUN PROPERLY
import scripts.getInfo as info
import scripts.keyboard as kb
import socket
import logging
import time
from os import system, name
from emoji import demojize
from datetime import datetime


#REQUIRED VARIABLES TO LOGIN WITH TWITCH
server = "irc.chat.twitch.tv"
port = 6667
oauth = info.getCreds().get('OAuth')


#INPUT FROM USER
nickname = input("Enter your Twitch username: ")
system('cls')
print('The Twitch channel ID can be found at the end of the stream link: \nFor example: https://www.twitch.tv/{channelID}\n', end="\r")
channelID = input("Enter the Twitch channel ID: ")
system('cls')
channel = f"#{channelID}"





#DATA
lastKeyOut = ''
messages = []
counter = [0,0,0,0,0,0,0,0,0,0,0]





#CREATES CONNECTION WITH TWITCH SERVER
def createSocket():
    sock = socket.socket()
    sock.connect((server, port))
    sock.send(f"PASS {oauth}\n".encode('utf-8'))
    sock.send(f"NICK {nickname}\n".encode('utf-8'))
    sock.send(f"JOIN {channel}\n".encode('utf-8'))

    return sock


#CHECKS CONNECTION STATUS
def checkConnection(sock):
    connection = sock.recv(2048).decode('utf-8')
    if (f"JOIN {channel}" in connection):
        print(f"Connected to {channel}", end="\r")
        return True
    else:
        print(
            f"Connection to {channel} failed! Check if the name is spelled correctly.", end="\r"
        )
        return False


#CHECKS LOGIN STATUS
def checkLogin(sock):
    login = sock.recv(2048).decode('utf-8')
    if ("Welcome, GLHF!" in login):
        print(f"Logged In as {nickname}", end="\r")
        return True
    else:
        print(
            f"An error has occured while trying to login. Check your OAuth token and your username.\n Your OAuth: {oauth}\n Your username: {nickname}"
        )
        return False


#RECIEVES MESSAGES FROM CHAT
def recieveMsgs(sock):
    system('cls')

    while True:

        resp = sock.recv(2048).decode('utf-8')

        if resp.startswith('PING'):
            sock.send("PONG\n".encode('utf-8'))

        elif len(resp) > 0:
            x = resp.split(":")
            msg = x[2].splitlines()[0]
            user = x[1].split("!")[0]
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            
            saveMessage(msg,user,current_time)
            giveKeyOUT(msg)
            displayData()


#TRANSFORMS MESSAGES TO KEYBOARD OUTPUT
def giveKeyOUT(msg):
    global lastKeyOut
    msg = msg.lower()
    if "pepelaugh" in msg:
        kb.simulateKey(0x11)
        lastKeyOut = 'w'
        counter[0] +=1

    elif "lul" in msg:
        kb.simulateKey(0x1F)
        lastKeyOut = 's'
        counter[1] +=1

    elif "pausechamp" in msg:
        kb.simulateKey(0x1E)
        lastKeyOut = 'a'
        counter[2] +=1

    elif "kekw" in msg:
        kb.simulateKey(0x20)
        lastKeyOut = 'd'
        counter[3] +=1

    elif "kappa" in msg:
        kb.simulateKey(0x39)
        lastKeyOut = 'space'
        counter[4] +=1

    elif "ayaya" in msg:
        kb.simulateKey(0x48)
        lastKeyOut = 'up'
        counter[5] +=1

    elif "5head" in msg:
        kb.simulateKey(0x50)
        lastKeyOut = 'down'
        counter[6] +=1

    elif "pog" in msg:
        kb.simulateKey(0x4B)
        lastKeyOut = 'left'
        counter[7] +=1
        
    elif "catjam" in msg:
        kb.simulateKey(0x4D)
        lastKeyOut = 'right'
        counter[8] +=1

    elif "monkaw" in msg:
        kb.simulateKey(0x12)
        lastKeyOut = 'e'
        counter[9] +=1

    elif "nodders" in msg:
        kb.simulateKey(0x10)
        lastKeyOut = 'q'
        counter[10] +=1

def displayData():
    system('cls')
    messagelist = ''
    global lastKeyOut
    for i in range(len(messages)):
        messagelist += f"\n[{messages[i]['time']}] {messages[i]['user']}: {messages[i]['msg']}"

    print(f'PepeLaugh: {counter[0]}          LUL:     {counter[1]}          PauseChamp: {counter[2]} \nKEKW:      {counter[3]}          Kappa:   {counter[4]}          AYAYA:      {counter[5]} \n5Head:     {counter[6]}          POG:     {counter[7]}          catJAM:     {counter[8]} \nmonkaW:    {counter[9]}          NODDERS: {counter[10]} \n\nLatest Keyboard Output: {lastKeyOut} \n\nChat logs:{messagelist}')

def saveMessage(msg,user,time):
    data = {'user': user, 'msg': msg, 'time': time}
    messages.append(data)
    if len(messages) > 10:
        messages.pop(0)

def main():

    sock = createSocket()

    loginStatus = checkLogin(sock)
    connectionStatus = checkConnection(sock)

    if connectionStatus and loginStatus:
        recieveMsgs(sock)

    sock.close()




main()