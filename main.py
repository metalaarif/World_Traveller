#!/usr/bin/python3
import os

def main():
    header()
    name = input("Enter your name Traveller: ")
    total_countries = 196
    print("Mr {}, There are currently total of {} countries in the world".format(name, total_countries))
    print("\n.....Loading Countries.....\n")
    load_countries()
    countries = int(input("How many countries have you been Traveller: "))
    travel_percentage = percentageOfTravel(countries, total_countries)
    printOut(name, countries, travel_percentage)

def header():
    print("*" * 50)
    print("\t\t\t World Traveller")
    print("*" * 50)


def load_countries():
    with open("data.csv", "r") as fin:
        content = fin.read().splitlines()
        print(content,"\n")
        # for id, name in enumerate(fin.readlines()):
        #     print(id + 1, name)


def percentageOfTravel(data1, data2):
   percentage = (data1 * 100) // data2
   return percentage


def printOut(data1, data2, data3):
   print("Mr {}, there are 196 countries and you have travelled {} countries and you've seen only {}% of the entire world".format(data1, data2, data3))


if __name__ == "__main__":
    main()