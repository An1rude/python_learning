boolean = True
num = 345
negative_num = -90
zero = 0
floater = 1.9
zero_zero = 0.0
string = "abc"
empty = ""
none_string = None
print(boolean)
print(int(boolean))
print(bool(num))
print(bool(negative_num))
print(bool(zero))
print(bool(floater))
print(bool(zero_zero))
print(bool(string))
print(bool(empty))
print(bool(none_string))

def test(a):
    print("number:", a)
    if( a >= 6):
        return True
    else:
        return False

if test(f) or test(k):
    print("all true")
else:
    print("all false")

def count_down(a):
    while a > 1:
        print (a)
        if(a%2 == 0):
            a = a/2
        else:
            a = 3*a + 1
    print(a)

count_down(3**65)