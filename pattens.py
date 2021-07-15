def main():
    n = int(input("Enter height of pyramid: "))
    draw(n)


def draw(n):
    for i in range(n):
        for j in range(i):
            print("#", end="")
        print()
    print("-------------------------")
    for i in range(n):
        for j in range(n-i):
            print("#", end="")
        print()


main()
