def max(a,b):
    if a > b:
        return a
    else:
        return b
def is_divisible(num1,num2):
    if int(num1) % int(num2) == 0:
        return True
    else:
        return False
def main():
    num = input("Please enter a number to check")
    check = input("Please enter a number to divide by")
    if is_divisible(num,check):
        print(num, "is divisible by", check)
    else:
        print(num, "is not divisible by", check)

if __name__ == '__main__':
    main()
