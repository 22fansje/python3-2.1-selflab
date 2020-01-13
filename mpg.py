#!/usr/bin/env python3

#importing a csv file
import csv

def main():
    # display a welcome message 
     more = "y"
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()
                                 
        mpg = round((miles_driven / gallons_used), 2)
        print("Miles Per Gallon:\t" + str(mpg))
        print()
        
        more = input("More entries? (y or n): ")
   
    L.append([miles_driven,gallons_used,mpg])
    print(L)
    with open ("trips.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(L)
        print(L)
    print("The Miles Per Gallon application")
    print()
    L = ["miles_driven","gallons_used","mpg",]
    print(L)
    

   


    def read_trips():
        with open("trips.csv", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                trips.append(row)
        

    def list_trips(trips):
        print("Distance\t Gallons\t MPG")
        print()
        for trips in trips:
            print(str(trip[0]) + "\t\t" + str(trip[1]) + "\t\t" + str(trip[2]))

def get_miles_driven():
    while True:
        miles_driven = float(input("Enter miles driven :     "))                    
        if miles_driven > 0:       
            return miles_driven
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue
    
def get_gallons_used():
    while True:
        gallons_used = float(input("Enter gallons of gas:     "))                    
        if gallons_used > 0:       
            return gallons_used
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue



    print("Bye")

if __name__ == "__main__":
    main()
