def bonus(l,s):
    if l > 5:
        b =1.05*s
    if l <= 5:
        b = s

    return b
def main():
    l = int(input("How long have you been working at your current company?"))
    s = int(input("What is your salary?"))
    print("Your total salary is :",bonus(l,s))

if __name__ == '__main__':
    main()
