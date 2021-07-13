
from time import sleep
import os

from time import perf_counter
from datetime import datetime
from pywinauto.application import Application
import pywinauto.base_wrapper as ceva
import pyautogui
import psutil
import warnings
import tkinter as tk

def findWindow():
    print("find window")
    return 0

def getCSGOPID():
    process_name = "csgo"
    pid = None
    for proc in psutil.process_iter():
        if process_name in proc.name():
            pid = proc.pid  
    return pid


def restoreCSGOWindow(pid):
    app=Application().connect(process=pid)
    app_dialog = app.top_window()
    app_dialog.minimize()
    app_dialog.restore()

def printPID(pid):
    if pid == None:
        print("\nOpen CS:GO first")
    else:
        print("\nCS:GO pid: ", pid)

#Step 1 find if in main menu or not
#Step 2 Enter or not the main menu
#Step 3 Press on Go button
#Step 4 Press on Accept button
#Step 5 wait for accept to dissapear

if __name__ == "__main__":
    warnings.simplefilter("ignore")
    window = tk.Tk()
    greeting = tk.Label(text="Hello, Tkinter")
    greeting.pack()
    print("************************ CS:GO Autoaccept script started ************************", end="\n")
    print("***********************          Rosca Roberto           ************************")
    print("***********************    roscaroberto21@gmail.com      ************************")
    cwd = os.getcwd()
    start=perf_counter()
    print("Running from : ", cwd)
    print("*** Script started ***\n*** "+str(datetime.now().time())+" ***\n")
    pid = getCSGOPID()
    printPID(pid)
    sleep(1)
    playPressed = False
    initialization = False
    while True:
        sleep(3)
        pid = getCSGOPID()
        if(pid == None):
            print("\nOpen CS:GO first !")
            continue
        if initialization == False:
            app=Application().connect(process=pid)
            app_dialog = app.top_window()
            initialization = True
            continue
        app_dialog.restore()
        goButton = pyautogui.locateOnScreen("./elements/gobtn.png", confidence=0.85)
        acceptButton = pyautogui.locateOnScreen("./elements/acceptbtn.png", confidence=0.89)
        if goButton == None:
            if acceptButton == None:
                print("\nMain menu or waiting for game...")
            else:
                pyautogui.doubleClick(acceptButton)
                print("\nMatch Accepted!")
               
