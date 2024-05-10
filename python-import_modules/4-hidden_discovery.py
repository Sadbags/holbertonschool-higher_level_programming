#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    dirlist = dir(hidden_4)
    for i in range(0, len(dirlist)):
        if dirlist[i][1] != "_":
            print("{}".format(dirlist[i]))
