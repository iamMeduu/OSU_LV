while True:
    print("Unesite broj: ")
    try:
        number=float(input())
        break
    except:
        print("Niste unijeli broj!")

def get_grade(number):
    match number:
        case _ if number<0.6:
            print("F")
        case _ if number<0.7 and number>=0.6:
            print("D")
        case _ if number<0.8 and number>=0.7:
            print("C")
        case _ if number<0.9 and number>=0.8:
            print("B")
        case _ if number<= 1.0 and number>=0.9:
            print("A")
        case  _:
            print("Broj izvan intervala!")
print(get_grade(number))
