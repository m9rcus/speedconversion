while True:

    conv = input("What would you like to do (1: MPH to KPH, 2: KPH to MPG, 3: MPG to Knots, 4: Knots to MPG, 5: KPH to Knots, 6: Knots to KPH): ")

    if conv == "1":
        mph1 = input("Enter a speed in Miles per hour: ")
        if not mph1.isnumeric():
            print("Enter a real number")
        else:
            mph1 = float(mph1)
            if mph1 < 0:
                print("Enter a number greater than 0")
            else:
                kph1 = mph1 * 1.609
                print("KPG:" , kph1)

    elif conv == "2":
        kph2 = input("Enter a speed in Kilometers per hour: ")
        if not kph2.isnumeric():
            print("Enter a real number")
        else:
            kph2 = float(kph2)
            if kph2 < 0:
                print("Enter a number greater than 0")
            else:
                mph2 = kph2 / 1.609
                print("MPH:" , mph2)

    elif conv == "3":
        mph3 = input("Enter a speed in Miles per hour: ")
        if not mph3.isnumeric():
            print("Enter a real number")
        else:
            mph3 = float(mph3)
            if mph3 < 0:
                print("Enter a number greater than 0")
            else:
                knots3 = mph3 / 1.151
                print("Knots:" , knots3)

    elif conv == "4":
        knots4 = input("Enter a speed in Knots: ")
        if not knots4.isnumeric():
            print("Enter a real number")
        else:
            knots4 = float(knots4)
            if knots4 < 0:
                print("Enter a number greater than 0")
            else:
                mph4 = knots4 * 1.151
                print("MPH:" , mph4)
        
    elif conv == "5":
        kph5 = input("Enter a speed in Kilometers per hour: ")
        if not kph5.isnumeric():
            print("Enter a real number")
        else:
            kph5 = float(kph5)
            if kph5 < 0:
                print("Enter a number greater than 0")
            else:
                knots5 = kph5 / 1.852
                print("Knots:" , knots5)

    elif conv == "6":
        knots6 = input("Enter a speed in Knots per hour: ")
        if not knots6.isnumeric():
            print("Enter a real number")
        else:
            knots6 = float(knots6)
            if knots6 < 0:
                print("Enter a number greater than 0")
            else:
                kph6 = knots6 * 1.852
                print("KPH:" , kph6)

    else:
        print("Enter a number from 1 to 6")
