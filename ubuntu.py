import os
import sys
import time

ubuntu_banner = """
 _   _ ____  _   _ _   _ _____ _   _ 
| | | | __ )| | | | \ | |_   _| | | |
| | | |  _ \| | | |  \| | | | | | | |
| |_| | |_) | |_| | |\  | | | | |_| |
 \___/|____/ \___/|_| \_| |_|  \___/
+===================================+
|  Author     : Farhan Abdurrahman  |
|  Contact    : www.fsecurity7.com  |
+++++++++++++++++++++++++++++++++++++

"""
def banner():
        print ubuntu_banner


print """
  \033[0;31mWelcome to Ubuntu Installation
 _   _ ____  _   _ _   _ _____ _   _
| | | | __ )| | | | \ | |_   _| | | |
| | | |  _ \| | | |  \| | | | | | | |
| |_| | |_) | |_| | |\  | | | | |_| |
 \___/|____/ \___/|_| \_| |_|  \___/
\033[0;32m+===================================+
|  Author     : Farhan Abdurrahman  |
|  Contact    : www.fsecurity7.com  |
+++++++++++++++++++++++++++++++++++++
"""

def main():
        print"  [01] Install"
        print"  \033[0;31m[02] Exit"
        han = raw_input("\033[0;36m\nHaN:~#\033[0m ")

        if han == "1" or han == "01":
            banner()
            os.system("cd")
            os.system("apt-get update -y")
            os.system("apt-get upgrade -y")
            os.system("apt-get install wget proot tar -y")
            os.system("cd && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Ubuntu/ubuntu.sh")
            os.system("cd && bash ubuntu.sh")
            os.system("./start-ubuntu.sh")
            os.system("wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/DesktopEnvironment/Apt/Xfce4/de-apt-xfce4.sh")
            os.system("bash de-apt-xfce4.sh")
            os.system("apt-get update")
            os.system("apt-get upgrade")
            os.system("apt-get install ruby && gem install lolcat")
            os.system("apt install neofetch")
            os.system("neofetch")

        elif han == "2" or han == "02":
            sys.exit()

        else:
            print"Salah Input !!!"
            sys.exit()

if __name__ == "__main__":
        main()
