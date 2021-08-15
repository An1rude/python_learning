print("Fermat's Last Theorem says that there are no positive integers a, b and c such that : ")
print("a^n + b^n = c^n for all n > 2")
print("Pick any 4 positive integers a,b,c and n to check.")

def check_int(s):
    if '-' in s:
        return False
    else:
        return s.isdigit()

def check_fermat():
    a = input("a=")  
    b = input("b=")
    c = input("c=")
    n = input("n=")
    if check_int(a) and check_int(b) and check_int(c) and check_int(n):
        a = int(a)
        b = int(b)
        c = int(c)
        n = int(n)
        if n < 3:
            print("n must be greater than 2")
            n = int(input("n="))
        if a**n + b**n == c**n and n > 2:
            print("Holly smokes, Fermat was wrong")
        if a**n + b**n != c**n and n > 2:
            print(a**n + b**n, "is not equal to",  c**n)
            print("Fermat is correct afterall")
    else:
        print("Please note a, b, c and n have to be positive integers")
        check_fermat()


check_fermat()
print("success")
