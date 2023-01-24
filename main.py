import colorama

def osszeadás():
    b = 0
    while True:
        a = input("Mennyi: ")

        if a == "=":
            break

        try:
            a = int(a)
            b = b + a

        except:
            ossze()

def kivonás():
    b = 0
    while True:
        a = input("Mennyi: ")

        if a == "=":
            break

        try:
            a = int(a)
            b = b - a

        except:
            kivonás()

def szorzás():
    b = int(input("Mennyi: "))
    while True:
        a = input("Mennyi: ")

        if a == "=":
            break

        try:
            a = int(a)
            b = b * a

        except:
            szorzás()

def osztás():
    b = int(input("Mennyi: "))
    while True:
        a = input("Mennyi: ")

        if a == "=":
            break

        try:
            a = int(a)
            b = b / a

        except:
            osztás()

def osztás2():
    b = int(input("Mennyi: "))
    while True:
        a = input("Mennyi: ")

        if a == "=":
            break

        try:
            a = int(a)
            b = b % a

        except:
            osztás2()

def user_input():

    print("""
    
    1. Összeadás
    2. Kivonás
    3. Szorzás
    4. Osztás
    5. Egés osztás
    
    """)

    a = input("Írd be a művelet számát: ")

    if a == "1":
        osszeadás()

    elif a == "2":
        kivonás()

    elif a == "3":
        szorzás()

    elif a == "4":
        osztás()

    elif a == "5":
        osztás2()

    else:
        print("Rossz az input.")
        user_input()
        r
user_input()
