# enter yaer and find that the number is leap year or not

# year div 4 then it's leap year
#  but year is div by 100 then it's not leap year
# year div 4 then it's leap year but year is not div by 100 then  leap year
# year div 4 then it's leap year but year is div by 100 then it's not leap yaar but if year is div by 400 then it's leap year
 

year = int(input("Please enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:

        if year % 400 == 0:
            print("it's a leap year")
        else:
            print("it's not a leap year")

    else:
        print("it's a leap year")

else:
    print("it's not a leap year") 