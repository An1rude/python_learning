print("Fermat's Last Theorem says that there are no positive integers a, b and c such that : ")
print("a^n + b^n = c^n for all n > 2")
print("Pick any 4 positive integers a,b,c and n to check.")

def check_int(s):
    if '-' in s:
        return False
    else:
        return s.isdigit()

def inpt_a():
    a = input("a=")
    if check_int(a):
         a = int(a)
         return int(a)
    else:
        print("a must be a positive integer")
        inpt_a()

    
def inpt_b():
    b = input("b=")
    if check_int(b):
        b = int(b)
        return int(b)
    else:
        print("b must be a positive integer")
        inpt_b()



def inpt_c():
    c = input("c=")
    if check_int(c):
     c = int(c)
     return int(c)
    else:
        print("c must be a positive integer")
        inpt_c()



def inpt_n():
    n = input("n=")
    if check_int(n):
        n = int(n)
        if n<3:
            print("n must be greater than 2")
            inpt_n()
        return int(n)
    else:
        print("n must be a positive integer")
        inpt_n()
          
             
def check_fermat():
    a = inpt_a()
    b = inpt_b()
    c = inpt_c()
    n = inpt_n()
    if a**n + b**n == c**n:
        print("Holy smokes! Fermat was wrong !!!")
    else:
        print(a**n + b**n, "is not equal to",  c**n)
        print("Fermat is correct afterall")

check_fermat()