from time import gmtime, strftime


def log(msg):
    time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    string = "[" + time + "] " + msg
    print(string)
