# Main SETUP script for Pi
from time import sleep
import os
import sys
import shutil


#Set Node ID Here, to change files
NODE_ID = "Enter node ID here"
NODE_NAME = "Enter node name here"
HOSTNAME = "fittongreen"
RASPI_CONFIG_TEMPLATE = "raspberry-pi-config.txt"


# ML algorithm checks for accessible spots or ignores them
ACCESSIBLE_SPOTS = 0 # 1 or 0 

# For copying latest version repository to pi
GITHUB_CLI_KEY = "Enter key here"

# SYS_PASSWORD = sys.argv[1]

# Default Install options
INSTALL_PACKAGES = 1
SET_CONFIG_FILE = 1
GET_GIT_REPOS = 1
SET_CERTIFICATES = 1
ENABLE_AUTO_START = 1
GENERATE_CONFIG_FILE = 1


#Commands and Packages to be executed
APT_UPDATE = "apt-get update"
PIP_UPGRADE = "pip3 install --upgrade pip"
PI_CONFIG_FILE_DIR = "/boot/config.txt"
PROJECT_DIRECTORY = "/home/pi"

APT_PACKAGES = [
    "python3-pip",
    "tflite-runtime",
    "libcblas-dev",
    "libhdf5-dev",
    "libhdf5-serial-dev",
    "libatlas-base-dev",
    "libjasper-dev",
    "libqtgui4",
    "libqt4-test"
    "python3-opencv"
]
PIP3_PACKAGES = [
    "numpy",
    "power-api"
]

GIT_CLONE_COMMAND = "gh repo clone"
GIT_REPOS = [
    ["KB4YG/iot", PROJECT_DIRECTORY],
    ["KB4YG/ml", PROJECT_DIRECTORY + "/iot"],
]

def installPackages():
    # Install system packages
    print(" <==== Starting Installing Linux Packes ====>") 
    os.system(APT_UPDATE)
    for package in APT_PACKAGES:
        print(" <==== Installing " + package + " ====>")
        os.system("sudo apt-get -y install " + package)

    # Install Python specific packages
    os.system(PIP_UPGRADE)
    for package in PIP3_PACKAGES:
        print(" <==== Installing " + package + " ====>") 
        os.system("yes | sudo pip3 install " + package)

    return


def setConfigFile():
    configFile = os.getcwd() + "/" + RASPI_CONFIG_TEMPLATE
    print(configFile)
    
    # replace Pi config file with template
    try:
        shutil.copy(configFile, PI_CONFIG_FILE_DIR)
        print("File copied successfully.")
    except shutil.SameFileError:
        print("Parameters are the same as template.")
    except PermissionError:
        print("Permission denied.")
    except:
        print("Error occurred while copying config file.")
    return


    # TODO Edit hostname
    return
    
def getGitRepos():
    # TODO Authenticate & Establish connection to GitHub repos
    
    # Navigate to directory and pull repo
    for repo in GIT_REPOS:
        print(" <==== Cloning repo " + repo[0] + " ====>") 
        os.system("cd " + repo[1])
        os.system(GIT_CLONE_COMMAND + " " + repo[0])
    return

def setCertificates():
    # TODO create certificates folder
    # TODO create certificates files needed for communicating with backend
    return

def enableAutoStart():
    # Set the Python main python script to start automatically
    startupCommand = "python3 " + PROJECT_DIRECTORY + "/src/main.py"
    # TODO Modify the ./rc.local file with the startup command 

def rebootPi():
    print("Rebooting Pi to apply new configuration settings")
    sleep(3)
    os.system("sudo reboot")
    return

def generateConfigFile():
    # TODO create a config file with constants for main.py to use with settings like NODE ID, NODE NAME, etc.
    return

def main():

    print("Proceeding to set up this Raspberry Pi with the following configuration in 10 seconds: ")
    print("NODE ID:             " + NODE_ID)
    print("NODE NAME:           " + NODE_NAME)
    print("ACCESSIBLE SPOTS:    " + str(ACCESSIBLE_SPOTS))
    print("GITHUB CLI KEY:      " + GITHUB_CLI_KEY)
    sleep(10)

    # TODO get command line arguments to see which to skip 
    if INSTALL_PACKAGES:        installPackages()
    if SET_CONFIG_FILE:         setConfigFile()
    if GET_GIT_REPOS:           getGitRepos()
    if SET_CERTIFICATES:        setCertificates()
    if ENABLE_AUTO_START:       enableAutoStart()
    if GENERATE_CONFIG_FILE:    generateConfigFile()

    rebootPi()

if __name__ == '__main__':
    # installPackages()
    main()
