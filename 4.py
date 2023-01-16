history = []

def celsius_to_farenheit(temp):
    return (temp * 9/5) + 32

def celsius_to_kelvin(temp):
    return 273 + temp

def kelvin_to_celsius(temp):
    return temp - 273

def farenheit_to_celsius(temp):
    return (temp-32)*5/9

while True:
    #menu
    print("1. From Celsius To Farenhiet?")
    print("2. From Farenhiet To Celsius?")
    print("3. From Celsius To Kelvin?")
    print("4. From kelvin To Celsius?")
    print("5. From Farenheit To Kelvin")
    print("6. From Kelvin To Farenheit")
    print("7. History")
    print("8. Exit")
    choice = int(input("Enter choice"))
    if choice == 8:
        exit()
    if choice == 7:
        print(history)
        continue
    temp = int(input("Enter temperature"))
    if choice == 1:
        conv = celsius_to_farenheit(temp)
    if choice == 2:
        conv = farenheit_to_celsius(temp)
    if choice == 3:
        conv = celsius_to_kelvin(temp)
    if choice == 4:
        conv = kelvin_to_celsius(temp)
    if choice == 5:
        conv = celsius_to_kelvin(farenheit_to_celsius(temp))
    if choice == 6:
        conv = celsius_to_farenheit(kelvin_to_celsius(temp))
    print(conv)
    conversion = (temp, conv) 
    history.append(conversion)