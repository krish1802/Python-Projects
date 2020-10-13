import string
import random
import subprocess

if __name__ == "__main__":
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation
    username = input("Enter the username\n")
    plen = int(input("Enter Password Length\n"))

    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
  
    # random.shuffle(s)
    print("Your Passwordfor " + username + " is")
    print("".join(random.sample(s, plen)))
    # print("".join(s[0:plen]))

    print("You can copy this to notepad")
    print("Type 'y' if you want to open, else write anything")
    x = input("Should I open Notepad to copy:   ")
    
    if 'y' in x:
        subprocess.getoutput("start notepad")
    else:
        print("Okay.")

