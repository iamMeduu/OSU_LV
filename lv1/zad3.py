lst_numbers= []
x= True
while True:
    print("Unesi broj ili Done za kraj: ")
    number = input()
    if(number=="Done"):
        break
    try:
        number = float(number)
        lst_numbers.append(number)
    except ValueError:
        print("Krivo uneseni broj!")
print ("Lenght: ", len(lst_numbers))
print("Min: ", min(lst_numbers))
print("Max: ", max(lst_numbers))
print("Average: ", sum(lst_numbers)/len(lst_numbers))
lst_numbers.sort()
print(lst_numbers)