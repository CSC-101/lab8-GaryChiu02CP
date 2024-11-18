import sys

def file():
    try:
        f = open(sys.argv[1])
        sum = 0
        array = f.read().split()
        for i in array:
            try:
                sum += float(i)
            except:
                print("Error, skipping to next line")
    except:
        print("Error. Exiting now.")
        exit()
    return sum

if __name__ == "__main__":
    print(file())