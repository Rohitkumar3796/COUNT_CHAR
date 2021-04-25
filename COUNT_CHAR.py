# THE OUTPUT OF THIS CODE IS HOW MANY TIMES IN PERCENTAGE A CHARACTER USE IN THIS TEXT
# HERE WE OPEN A FILE AND WRITE SOMETHING
name=input('enter the file name:')
with open(name,"w") as f:
    f.write('''The second approach in the above example takes care of all the exceptions
            but using the with statement makes the code compact and much more readable. 
            Thus, with statement help shown above and with Locks, sockets, subprocesses and telnets etc''')
    f.close()
# FUNCTION DEFINE OF COUNT CHAR
def char_count(text,char):
    count=0
    for i in text:
        if i==char:
            count=count+1
    return count

# HERE WE READ A FILE
file=input("enter the file name want to read:")
with open(file) as f:
    text=f.read()

# HERE WE CALL FUNCTION 
for char in "abcdefghijklmnopqrstuvwxyz":
    percentage=100 * char_count(text,char) / len(text)
    print("{}-{}%".format(char,round(percentage,2)))
