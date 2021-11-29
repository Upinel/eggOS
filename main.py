#!/usr/bin/env python3
"""
Name:   Nova Altesse Chow
Email:  nv@bu.edu
File:   eggos.py
Desc:   Enterprise Giftcard Generate Operating System (eggOS)
"""
import string, random, os
from shutil import copy
import time
​
timestamp = time.strftime("%Y%m%d-%H%M%S")
eggos_ver = "v.0.9"
​
​
class Code:
    def __init__(self, event="Default Event", prefix="GCC", length=9):
        self.__event = str(event)
        self.__prefix = str(prefix).replace(" ","").upper()
        self.__length = int(length)
        self.file = str(event).replace(" ", "").upper() #define the file name from the event name
        self.code = [] #init the code array
        self.read() #read the code if same the event already there
​
    def create(self, qty): #Create new codes by input qty
        for i in range(qty):
            #Generate code by random sample with ASCII uppercase, and replace some char with __swapcode
            newstr = self.__prefix + self.__swapcode(
                "".join(random.sample(string.ascii_uppercase, self.__length))
            )
            #adding new line symbol \n in order to write the file with newlines correctly
            self.code.append(newstr + "\n")
            #print the code generate process to the screen in case it is a large volume of code and cannot know the progress
            print(str(i + 1).zfill(int(len(str(qty)))) + "/" + str(qty) + ": " + newstr)
​
        #Show generate report
        print(f"Status: Created Codes: {str(qty)}")
        print(f"Status: Total Codes: {str(len(self.code))}")
        #Check if any of the code repeated
        if self.check_unique():
            print(f"Status: Unique Check OK")
        else:
            print("Status: ALERT - Check Unique Failed!!!!! Please DO NOT SAVE")
​
    def reload(self): #Reload the file without saving it
        self.code = []
        self.code = self.read()
​
    def __swapcode(self, inp):  #This function is to replace confusing chars in printed Giftcard: I&L&1, O&0, U&V&W
        return (
            inp.replace("I", "3")
            .replace("J", "4")
            .replace("L", "5")
            .replace("O", "6")
            .replace("U", "7")
            .replace("V", "8")
            .replace("W", "9")
        )
​
    def check_unique(self): #The quickest way to know if there are any repeated code is by comparing the unique list.
        return len(self.code) == len(set(self.code))
​
    def save(self): #Save the code file, also backup before save
        self.__before_save()
        filesave(self.code, self.file)
        return True
​
    def read(self): #read the file if event already existed
        try:
            f = open(self.file + ".txt")
            tmp = f.readlines()[:]
            f.close()
            return tmp
        except:
            pass
​
    def __before_save(self): #Backup the file before make any changes on it
        filebackup(self.file + ".txt")
​
    def count(self): #Show how many codes in the memory
        return int(len(self.code))
​
    def name(self): #expose the private var to public
        return str(self.__event)
​
    def __repr__(self):  #When call the value directly, display the code list
        return ",".join(self.code).replace("\n", "")
​
​
def init():  #Create the necessary folders if not exists
    try:
        os.makedirs("./Backup")
        print("Status: Backup folder - Created")
    except:
        print("Status: Backup folder - Found")
​
​
def filesave(inputarray, targetfile):  # Create output file
    f = open(targetfile + ".txt", "w")
    f.writelines(inputarray)
    f.close()
​
​
def filebackup(targetfile):  # Create Backup file before everything happen
    try:
        copy(targetfile, "./Backup/" + targetfile + "-" + timestamp + ".backup.txt")
        print(f"Status: Original File Backed Up: {targetfile}-{timestamp}.backup.txt")
    except:
        print(f"Status: New Event, file name {targetfile}")
​
​
def menu(event): #This is the user step-by-step menu when execute this py directly
    print()
    print("eggOS Main Menu")
    print(f"Project: {event.name()}, Code Qty: {event.count()}")
    print("=================================")
    print("1. Display all code")
    print("2. Create addition codes")
    print("3. Save document")
    print("4. Reload document without save")
    print("5. Exit (without save)")
    inp = input("Please select option (1,2,3,4): ")
    print()
    if inp == "1":
        print(f"Status: The codes are: {event}")
    elif inp == "2":
        inp_sub = input("How many code you need to add: ")
        event.create(int(inp_sub))
    elif inp == "3":
​
        if event.check_unique():
            if event.save():
                print("Status: File saved successfully")
        else:
            inp_sub = input(
                "The file may have repeated code, are you sure to save? (Y/N): "
            )
            if inp_sub.upper() == "Y":
                if event.save():
                    print("Status: File saved successfully")
            else:
                print("Status: Save operation aborted.")
​
    elif inp == "4":
        event.reload()
    elif inp == "5":
        exit()
    else:
        print("Status: Wrong input, please try again")
​
​
def main(): #This is the step by step wizard on create event when execute this py directly
    print(f"Welcome to eggOS ({eggos_ver}), Please follow the intrustion to create your project")
    print("============================================================================")
    #inp_event = input("Your event name: ")
    inp_prefix = input("Please define the Prefix: ")
    inp_length = int(input("How long is the code: "))
    event = Code(inp_prefix, inp_prefix, inp_length) #Create a event with Code class
    while True: #Loop the menu infinitely
        menu(event)
​
​
if __name__ == "__main__":
    init()
    main()
