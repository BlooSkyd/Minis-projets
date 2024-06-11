#encoding: utf-8

def syracuse(n: int) -> int :
    print(n)
    if n == 1:
        print("Fini!")
    elif n%2 == 0: # n pair
        syracuse(int(n/2))
    else:
        syracuse((n*3)+1)

syracuse(int(input("Saisissez un nombre : ")))