def is_triangle(side1, side2, side3):
    if side1 + side2 >= side3:
        if side3 + side2 >= side1:
            if side1 + side3 >= side2:
                print("These lengths would make a triangle.")
    else:
        print("These lengths would not make a triangle. ")



def main():
    a = int(input("Please enter a side length."))
    b = int(input("Please enter a second side length."))
    c = int(input("Please enter the final side length."))
    print(is_triangle(a,b,c))


if __name__ == '__main__':
    main()
