import os, sys, time


def installing():
    os.system('cls' if os.name == 'nt' else 'clear')
    SlowType('Installing', 0.04)

def SlowType(text:str, speed:float, newLine=True):
    for i in text:
        print(i, end="", flush=True)
        time.sleep(speed)
    if newLine:
        print()

def error_handle():
    print("Check your internet connection and try again.")
    sys.stdout.write("\r| [Error] took too long to connect to the server!")
    time.sleep(0.5)
    sys.stdout.write("\r| [     ] took too long to connect to the server!")
    time.sleep(0.5)
    sys.stdout.write("\r| [Error] took too long to connect to the server!")
    time.sleep(0.5)
    sys.stdout.write("\r| [     ] took too long to connect to the server!")
    time.sleep(0.5)
    sys.stdout.write("\r| [Error] took too long to connect to the server!")
    time.sleep(0.5)

    user = input("\n\n\n\nPress ENTER to exit\n\n")
    if user != "":
        exit()



def modules():
    try:
        version = sys.version
        major = version[0]
        minor = version[2:4]
        micro = version[5]

        if int(major) >= 3:
            pass

        else:
            print("--> ")
            SlowType(f"Your python version is {major}.{minor}.{micro}\n performing upgrade to new version!")
            os.system('py -m pip install --upgrade pip')

    except ConnectionError or ConnectionAbortedError or ConnectionRefusedError:
        error_handle()
        

    try:
        import PIL
    except ModuleNotFoundError or ConnectionAbortedError or ConnectionRefusedError:
        error = ('pillow')
        installing()
        os.system(f'py -m pip install {error}')

    except ConnectionError:
        error_handle()

    try:
        import pyperclip
    except ModuleNotFoundError or ConnectionAbortedError or ConnectionRefusedError:
        error = ('pyperclip')
        installing()
        os.system(f'py -m pip install {error}')

    except ConnectionError:
        error_handle()

    try:
        import customtkinter
    except ModuleNotFoundError or ConnectionAbortedError or ConnectionRefusedError:
        error = ('tkinter GUI')
        installing()
        os.system(f'py -m pip install {error}')

    except ConnectionError:
        error_handle()

    try:
        import PIL, customtkinter, pyperclip
    except:
        def installmodules():
            try:
                os.system(f'py -m pip install pillow customtkinter pyperclip')
            except ModuleNotFoundError or ConnectionError:
                print("\n| [Error] try again!")
        installmodules()


modules()