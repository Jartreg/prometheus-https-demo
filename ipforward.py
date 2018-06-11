import subprocess
import os

option = None
ipv4command = "sysctl -w net.ipv4.ip_forward=1"
ipv6Command = "sysctl -w net.ipv6.conf.all.forwarding=1"
option1 = False
option2 = False

endlessrun = True
while endlessrun == True:
    os.system("clear")
    print("   ___________      ______                               _ _             ")
    print("  |_   _| ___ \     |  ___|                             | (_)            ")
    print("    | | | |_/ /_____| |_ ___  _ ____      ____ _ _ __ __| |_ _ __   __ _ ")
    print("    | | |  __/______|  _/ _ \| '__\ \ /\ / / _` | '__/ _` | | '_ \ / _` |")
    print("   _| |_| |         | || (_) | |   \ V  V / (_| | | | (_| | | | | | (_| |")
    print("   \___/\_|         \_| \___/|_|    \_/\_/ \__,_|_|  \__,_|_|_| |_|\__, |")
    print("                                                                    __/ |")
    print("                                                                   |___/ ")

    print("Which IP-Version do you want to port forward?")
    print("1) IPV4")
    print("2) IPV6")
    print("")
    print("Q) To exit the programm")
    if option1 == True:
        print("Succesfully enabled ipv4 forwarding")
        option1 = False
    elif option2 == True:
        print("Succesfully enabled ipv6 forwarding")
        option2 = False
    print("")
    optioninput = input()
    option = str(optioninput)
    if option == "1":
        output = subprocess.check_output(['bash', '-c', ipv4command])
        option1 = True
    elif option == "2":
        output = subprocess.check_output(['bash', '-c', ipv6Command])
        option2 = True
    elif option == "q" or option == "Q":
        os.system("clear")
        exit()
