#Coded by:Sanz
#Youtube:SANZ SOEKAMTI
#GitHub:https://github.com/B4N954N2-ID
#Note:Jangan di ubah ya nanti bisa error
import os
import sys
import time
import random

def kntl():
    load = [
     '\033[1;31m[\033[1;37m#################\033[1;31m]  \033[1;37m0% ', '\033[1;31m[\033[1;34m#####\033[1;37m############\033[1;31m] \033[1;37m40% ', '\033[1;31m[\033[1;34m##########\033[1;37m#######\033[1;31m] \033[1;37m60% ', '\033[1;31m[\033[1;34m###########\033[1;37m######\033[1;31m] \033[1;37m70% ', '\033[1;31m[\033[1;34m#############\033[1;37m####\033[1;31m] \033[1;37m80% ', '\033[1;31m[\033[1;34m###############\033[1;37m##\033[1;31m] \033[1;37m90% ', '\033[1;31m[\033[1;34m#################\033[1;31m] \033[1;37m100% ', '\033[1;31m[\033[1;37m     SUCCESS     \033[1;31m] \033[1;37m100% ', '\033[1;31m[\033[1;37m                 \033[1;31m] \033[1;37m100% ', '\033[1;31m[\033[1;37m     SUCCESS     \033[1;31m] \033[1;37m100% ', '\033[1;31m[\033[1;37m                 \033[1;31m] \033[1;37m100% ', '\033[1;31m[\033[1;37m     SUCCESS     \033[1;31m] \033[1;37m100% ', '\033[1;31m[\033[1;37m                 \033[1;31m] \033[1;37m100% ', '\033[1;31m[\033[1;37m     SUCCESS     \033[1;31m] \033[1;37m100% ', '\033[1;31m[\033[1;37m                 \033[1;31m] \033[1;37m100% ', '\033[1;31m[\033[1;37m     SUCCESS     \033[1;31m] \033[1;37m100% ', '\033[1;31m[\033[1;37m                 \033[1;31m] \033[1;37m100% ', '\033[1;31m[\033[1;37m     SUCCESS     \033[1;31m] \033[1;37m100% ', '\033[1;31m[\033[1;37m                 \033[1;31m] \033[1;37m100% ', '\033[1;31m[\033[1;37m     SUCCESS     \033[1;31m] \033[1;37m100% ', '\033[1;31m[\033[1;34m#################\033[1;31m] \033[1;37m100% ']
    for o in load:
        print '\r\x1b[1;37m    [\033[1;32m+\033[1;37m] \x1b[1;92mLoading \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(0.3)
kntl()