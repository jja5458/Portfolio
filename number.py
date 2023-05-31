def main():
    x = getint()
    print(f"x is {x}")

def getint():
    while True:
        try:
            return int(input("what's x?"))
        
        except ValueError:
            pass

        
main()