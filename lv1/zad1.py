def total_euro(work_hours,hourly_pay):
    return f"Ukupno: {work_hours*hourly_pay} eura"
print("Radni sati: ")
work_hours=int(input())
while(work_hours<0):
    print("Krivi unos! Pokusajte ponovno: ")
    work_hours=int(input())
print("eura/h: ")
hourly_wage=float(input())
while(hourly_wage<0):
    print("Krivi unos! Pokusajte ponovno: ")
    hourly_wage=float(input())
print(total_euro(work_hours,hourly_wage))