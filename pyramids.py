def main():
    return runGame()

def runGame():
    number = int(input("Choose the size of your pyramid!\n"))
    # rows = int(input("Choose the number of rows:\n"))

    for i in range(0, number-1):
        print()
        print("*", end="")
        for y in range (i, i*2):
            print("*", end="")

    for i in range(0, number):
            print()
            print("*", end="")
            for y in range (i, number-1):
                print("*", end="")
        
    print()
    
    # for i in range(0, rows)

if __name__ == "__main__":
    main() 