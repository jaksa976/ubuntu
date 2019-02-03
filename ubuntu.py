import os
import time
import sys
from sys import platform

ubuntu_banner = """
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
        print"  [01] OS"
        print"  [02] DE"
        print"  \033[0;31m[03] Exit"
        han = raw_input("\033[0;36m\nHaN:~#\033[0m ")

        if han == "1" or han == "01":
            banner()
            os.system("cd")
            os.system("apt-get update -y")
            os.system("apt-get upgrade -y")
            os.system("apt-get install wget proot tar -y")
            os.system("cd && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Ubuntu/ubuntu.sh")
            os.system("cd && bash ubuntu.sh")
            os.system("cd /$HOME")
            os.system("cd && bash start-ubuntu.sh")

        elif han == "2" or han == "02":
            banner()
            os.system("apt-get update -y")
            os.system("apt-get upgrade -y")
            os.system("apt-get install ruby -y && gem install lolcat")
            os.system("apt install neofetch -y")
            os.system("neofetch")
            os.system("cd && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/DesktopEnvironment/Apt/Xfce4/de-apt-xfce4.sh")
            os.system("cd && bash de-apt-xfce4.sh")
        
        elif han == "3" or han == "03":
            print"Exit...."
            sys.exit()

        else:
            print"Salah Input !!!"
            sys.exit()

if __name__ == "__main__":
        main()
