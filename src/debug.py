from time import gmtime, strftime
import time

counter = 1

name = "../logs/" + str(round(time.time())) + ".log"
open(name, 'w+').close()
print("--------------------")
print(name)
print("--------------------")

def log(msg, agent):
    global counter
    time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    string = "[" + time + "] (" + agent.upper() + ") |" + str(counter) + "| " + msg
    counter = counter + 1
    f = open(name, "a+")
    f.write(string)
    f.write("\n")
    f.close()
