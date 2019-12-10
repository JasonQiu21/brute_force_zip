import zipfile
import sys
import os

cwd = os.getcwd()

#get zip file
try:
    Zip = input("Zip file location:    ")
except FileNotFoundError:
    print("Error: can't open zip.")
    sys.exit()
if Zip.startswith("/"): 
    pass
else: 
    Zip = cwd + "/" + Zip
try:
    myZip = zipfile.ZipFile(Zip)
except zipfile.BadZipfile:
    print("Error: can't open zip.")
    sys.exit()

#get wordlist file
try:
    wordlist = input("Wordlist file location:    ")
    if wordlist.startswith("/"):
        pass
    else:
        wordlist = cwd + "/" + wordlist
    f = open(wordlist, mode = "r")
except:
    print("Error: can't open wordlist. Check spelling.")
    sys.exit()
    
passwds = f.readlines()

#cracking bit
for i, j in enumerate(passwds):
    password = str.encode(j.strip())
    try:
        myZip.extractall(pwd = password)
        print("Pass-protected password cracked.")
        print(f"Password: {j.strip()}")
        print(f"Files extracted to {cwd}")
        sys.exit()
    except Exception as e:
        if 'Bad password for file' in str(e):
            pass
        else:
            print(e)
print ("Password not in wordlist given.")