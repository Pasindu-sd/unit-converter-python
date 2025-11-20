def convert_km_to_m(km):
    return km * 1000

def convert_m_to_cm(m):
    return m * 100

def convert_cm_to_m(cm):
    return cm / 100

def convert_m_to_km(m):
    return m / 1000

def convert_kg_to_g(kg):
    return kg * 1000

def convert_g_to_kg(g):
    return g / 1000

def convert_hours_to_minutes(hours):
    return hours * 60

def convert_minutes_to_hours(minutes):
    return minutes / 60

def convert_liters_to_ml(liters):
    return liters * 1000

def convert_ml_to_liters(ml):
    return ml / 1000

def main():
    print("~ UNIT CONVERTER ~")
    print("------------------")
    print("1. kilometers --> Meters")
    print("2. Meters --> Centimeters")
    print("3. Centimeters --> Meters")
    print("4. Meters --> Kilometers")
    print("5. Kilograms --> Grams")
    print("6. Grams --> Kilograms")
    print("7. Hours --> Minutes")
    print("8. Minutes --> Hours")
    print("9. Liters --> Milliliters")
    print("10. Milliliters --> Liters")

    choice = input("Choose what to convert (1-10): ")

    if choice == "1":
        km = float(input("Enter kilometers: "))
        print("Meters: ", convert_km_to_m(km))

    elif choice == "2":
        m = float(input("Enter meters: "))
        print("Centemeters: ", convert_m_to_cm(m))
    
    elif choice == "3":
        cm = float(input("Enter centimeters: "))
        print("Meters:", convert_cm_to_m(cm))

    elif choice == "4":
        m = float(input("Enter meters: "))
        print("Kilometers:", convert_m_to_km(m))

    elif choice == "5":
        kg = float(input("Enter kilograms: "))
        print("Grams:", convert_kg_to_g(kg))

    elif choice == "6":
        g = float(input("Enter grams: "))
        print("Kilograms:", convert_g_to_kg(g))

    elif choice == "7":
        hours = float(input("Enter hours: "))
        print("Minutes:", convert_hours_to_minutes(hours))

    elif choice == "8":
        minutes = float(input("Enter minutes: "))
        print("Hours:", convert_minutes_to_hours(minutes))

    elif choice == "9":
        liters = float(input("Enter liters: "))
        print("Milliliters:", convert_liters_to_ml(liters))

    elif choice == "10":
        ml = float(input("Enter milliliters: "))
        print("Liters:", convert_ml_to_liters(ml))

    else:
        print("Invalid option.Try Again!!!")

if __name__ == "__main__":
    main()
