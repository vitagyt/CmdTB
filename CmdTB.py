import os, sys, random, webbrowser

youtube="https://rebrand.ly/VitagYouTube"
website="https://vitagyt.tk"
twitter="https://rebrand.ly/VitagTwitter"
discord="https://rebrand.ly/VitagDiscord"

make=[youtube, website, twitter, discord]

a=1

os.system('@echo off')
os.system('title CmdTB - © Vitag')

def CmdTB():
    print("-> Github Repository : https://github.com/vitagyt/CmdTB <-")
    print("--------")
    print("About me")
    print("YouTube:",youtube)
    print("Website:",website)
    print("Twitter:",twitter)
    print("Discord:",discord)
    print("--------")
    print("Command Prompt : 0")
    print("Regedit : 1")
    print("PowerShell : 2")
    print("Msinfo32 : 3")
    print("Exit : 4")
    print("Press [ENTER] when you answered")
    print("--------")
    
    ask=int(input("Make your choice : "))
    
    if ask==0:
        os.system('start cmd')
                  
    if ask==1:
        os.system('start regedit')
                  
    if ask==2:
        os.system('start powershell')
                  
    if ask==3:
        os.system('msinfo32')
                  
    if ask==4:
        sys.exit(0)
            
    webbrowser.open(random.choice(make))
    os.system('cls')

while a==1:
    CmdTB()
