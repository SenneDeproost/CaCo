from time import gmtime, strftime

counter = 1


def log(msg, agent):
    global counter
    time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    string = "[" + time + "] (" + agent.upper() + ") |" + str(counter) + "| " + msg
    counter = counter + 1
   # print(string)
