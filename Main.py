print("Enter temperatures of all days")
sat = input("Saturday: ")
sun = input("Sunday: ")
mon = input("Monday: ")
tue = input("Tuesday: ")
wed = input("Wednesday: ")
thu = input("Thursday: ")
fri = input("Friday: ")

days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
temperatures = [sat, sun, mon, tue, wed, thu, fri]


def corres_clothing(temp):
    temp = int(temp)
    if temp <= 0:
        return"Remember to wear your winter coat, hat, gloves and boots"
    elif 0 <= temp <= 30:
        return "You can just wear a coat and a scarf"
    elif 30 <= temp <= 60:
        return "Wear a hoodie"
    elif 30 <= temp <= 90:
        return "Wear whatever you want"
    else:
        return "Dayum it's hot"


for i in range(len(days)):
    print(corres_clothing(temperatures[i]) + " on " + days[i])