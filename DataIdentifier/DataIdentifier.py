import os

monthExt = ['January','February','March','April','May','June','July','August','September','October','November','December'] 
day = 0
month = 0
verifYear = 0
year = 0

year=(int(input("Enter with the year: ")))

if(year % 4 == 0):

    if(year%100==0):
     verifYear=year%400    

month=(int(input("Enter with the month: ")))

if(month<1 or month>12):
    while True:
        month=(int(input("Enter again with the month: ")))
        if not(month<1 or month>12):
            break

day=(int(input("Enter with the day: ")))

if(day<1 or day>31):
    while True:
        day=(int(input("Enter again with the day: ")))
        if not (day<1 or day>31):
            break

if(verifYear==0 and month==2):
    if(day>29):
        while True:
            day=(int(input("Enter again with the day: ")))
            if not (day>29):
                break
else:
     if(verifYear!=0 and month==2):
         if(day>28):
             while True:
                 day=(int(input("Enter again with the day: ")))
                 if not (day>28):
                    break
if(month==4 or month==6 or month==7 or month==11 and day>30):
        while True:
            day=(int(input("Enter again with the day: ")))
            if not (month==4 or month==6 or month==7 or month==11 and day>30):
                break

cls=lambda: os.system('cls')
cls()

print("Day: ", day)
print("Month: ", monthExt[month-1])
print("Year: ", year)










