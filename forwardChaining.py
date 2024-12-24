database = ["Croaks", "Eat Flies", "Shrimps", "Sings"]
knowbase = ["Frog", "Canary", "Green", "Yellow"]
def display():
    print("\n X is:")
    print("1. Croaks")
    print("2. Eat Flies")
    print("3. Shrimps")
    print("4. Sings")
    print("\nSelect one option:")
def main():
    print("Forward Chaining")
    display()  
    x = int(input())
    if x == 1 or x == 2:
        print("Chance of Frog")
    elif x == 3 or x == 4:
        print("Chance of Canary")
    else:
        print("Invalid Option Selected")
        return  
    if 1 <= x <= 4:
        print("\n X is:", database[x - 1])
        print("Color options:")
        print("1. Green")
        print("2. Yellow")
        print("\nSelect color option:")
        k = int(input())
        if k == 1 and (x == 1 or x == 2):  # Frog and green
            print("Yes, it is", knowbase[0], "and the color is", knowbase[2])
        elif k == 2 and (x == 3 or x == 4):  # Canary and yellow
            print("Yes, it is", knowbase[1], "and the color is", knowbase[3])
        else:
            print("Invalid Knowledge Database")
if __name__ == "__main__":
    main()
