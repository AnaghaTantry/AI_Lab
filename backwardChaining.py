database = ["Croaks", "Eat Flies", "Shrimps", "Sings"]
knowbase = ["Frog", "Canary"]
color = ["Green", "Yellow"]
def display():
    print("\nX is")
    print("1. Frog")
    print("2. Canary")
    print("\nSelect one option:")
def main():
    print("Backward Chaining ")
    display()
    x = int(input())
    if x == 1:
        print("Chance of eating flies")
    elif x == 2:
        print("Chance of shrimping")
    else:
        print("Invalid Option Selected")
        return  
    if 1 <= x <= 2:
        print("\nX is:", knowbase[x - 1])
        print("Color options:")
        print("1. Green")
        print("2. Yellow")
        print("\nSelect color option:")
        k = int(input())
        if k == 1 and x == 1:  
            print("Yes, it is in", color[0], "color and will", database[0])
        elif k == 2 and x == 2:  
            print("Yes, it is in", color[1], "color and will", database[2])
        else:
            print("Invalid Knowledge Database")
if __name__ == "__main__":
    main()
