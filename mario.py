def main():
    getsqauresize()
    print_square(3)

def getsqauresize():
   return int(input("What size sqaure do you want?"))
    
        
def print_square(size):
    #for each row in a square 
    for i in range(size):
        #for each brick in a row 
        for j in range(size):
            #print brick
            print("#", end="")
        print()

main()