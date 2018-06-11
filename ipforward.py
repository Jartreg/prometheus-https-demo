import subprocess
import os

option = None
ipv4command = "sysctl -w net.ipv4.ip_forward=1"
ipv6Command = "sysctl -w net.ipv6.conf.all.forwarding=1"
ipv4commandTwo = "sysctl -w net.ipv4.ip_forward=0"
ipv6CommandTwo = "sysctl -w net.ipv6.conf.all.forwarding=0"
option1 = False
option2 = False
option3 = False
option4 = False
option5 = False
option6 = False
switchPage = False
page = 1

endlessrun = True
while endlessrun == True:
    if page == 1:
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
        print("N) To go to next page")
        if option1 == True:
            print("Succesfully enabled ipv4 forwarding")
            option1 = False
        elif option2 == True:
            print("Succesfully enabled ipv6 forwarding")
            option2 = False
        elif option3 == True:
            print("Wrong parameter")
            option3 = False
        print("")
        optioninput = input()
        option = str(optioninput)
        if option == "1":
            output = subprocess.check_output(['bash', '-c', ipv4command])
            option1 = True
            page = 1
        elif option == "2":
            output = subprocess.check_output(['bash', '-c', ipv6Command])
            option2 = True
            page = 1
        elif option == 'q' or option == 'Q':
            os.system("clear")
            exit()
        elif option == 'n' or option == 'N':
            page = 2
        else:
            option3 = True
    elif page == 2:
        os.system("clear")
        print("   ___________      ______                               _ _             ")
        print("  |_   _| ___ \     |  ___|                             | (_)            ")
        print("    | | | |_/ /_____| |_ ___  _ ____      ____ _ _ __ __| |_ _ __   __ _ ")
        print("    | | |  __/______|  _/ _ \| '__\ \ /\ / / _` | '__/ _` | | '_ \ / _` |")
        print("   _| |_| |         | || (_) | |   \ V  V / (_| | | | (_| | | | | | (_| |")
        print("   \___/\_|         \_| \___/|_|    \_/\_/ \__,_|_|  \__,_|_|_| |_|\__, |")
        print("                                                                    __/ |")
        print("                                                                   |___/ ")
        print("Which IP-Version do you want to undo?")
        print("1) IPV4")
        print("2) IPV6")
        print("")
        print("Q) To exit the programm")
        print("P) To go to previous page")
        if option4 == True:
            print("Succesfully disabled ipv4 forwarding")
            option4 = False
        elif option5 == True:
            print("Succesfully disabled ipv6 forwarding")
            option5 = False
        elif option6 == True:
            print("Wrong parameter")
            option6 = False
        print("")
        optioninput = input()
        option = str(optioninput)
        if option == "1":
            output = subprocess.check_output(['bash', '-c', ipv4commandTwo])
            option4 = True
            page = 2
        elif option == "2":
            output = subprocess.check_output(['bash', '-c', ipv6CommandTwo])
            option5 = True
            page = 2
        elif option == 'q' or option == 'Q':
            os.system("clear")
            exit()
        elif option == 'p' or option == 'P':
            page = 1
        else:
            option6 = True

