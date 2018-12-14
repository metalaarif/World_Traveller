#!/usr/bin/python3
def main():
    header()
    name = input("Enter your name Traveller: ")
    total_countries = 195
    countries = int(input("How many countries have you been Traveller: "))
    travel_percentage = percentageOfTravel(countries, total_countries)
    printOut(name, countries, travel_percentage)

def header():
    print("*" * 50)
    print("\t\t\t World Traveller")
    print("*" * 50)


def percentageOfTravel(data1, data2):
    percentage = (data1 * 100) // data2
    return percentage


def printOut(data1, data2, data3):
    print("Mr {}, there are 195 countries and you have travelled {} countries and you've seen only {}% of the entire world".format(data1, data2, data3))


if __name__ == "__main__":
    main()