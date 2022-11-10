
from driver import Driver
from race import Race
from drivermapper import Drivermapper
from racemapper import Racemapper

print("1. Add a driver: add")
print("2. Update a driver: update")
print("3. Delete a driver: delete")
print("4. Get all drivers: getall")
print("5. Other details: other")
print("6. Exit: exit")

while(input("Enter your choice(continue or exit): ")!="exit"):
    operation=input("Enter the operation: ")
    #singletone
    drivermapper=Drivermapper()
    racemapper=Racemapper()

    if operation=="add":
        table=input("Enter the table name(driver,race): ")
        if table=="driver":
            driverId=input("Enter the driverId: ")
            driverRef=input("Enter the driverRef: ")
            code=input("Enter the code: ")
            forename=input("Enter the forename: ")
            surname=input("Enter the surname: ")
            dob=input("Enter the dob: ")
            nationality=input("Enter naitonality: ")
            
            driver = Driver(driverId,driverRef,code, forename, surname,dob,nationality)
            drivermapper.add(driver)
            print("Driver Added(P)")
        elif table=="race":
            raceId=input("Enter the raceId: ")
            year=input("Enter the year: ")
            round=input("Enter the round: ")
            circuitId=input("Enter the circuitId: ")
            name=input("Enter the name: ")
            date=input("Enter the date: ")
            time=input("Enter the time: ")
            race=Race(raceId,year,round,circuitId,name,date,time)
            racemapper.add(race)
            print("Race added(P)")

    elif operation=="update":
        table=input("Enter the table name(driver,race): ")
        if table=="driver":
            id=input("Enter the driverId: ")
            driver=drivermapper.getdriverbyId(id)
            print("Driver details: ",driver)
            driverId=input("Enter the driverId: ")
            driverRef=input("Enter the driverRef: ")
            code=input("Enter the code: ")
            forename=input("Enter the forename: ")
            surname=input("Enter the surname: ")
            dob=input("Enter the dob: ")
            nationality=input("Enter naitonality: ")
            driver=Driver(driverId,driverRef,code, forename, surname,dob,nationality)
            drivermapper.update(driver)
            print("Driver updated(P)")
        elif table=="race" :
            id=input("Enter the raceId: ")
            race=racemapper.getracebyId(id)
            print("Real Details: ",race)
            raceId=input("Enter the raceId: ")
            year=input("Enter the year: ")
            round=input("Enter the round: ")
            circuitId=input("Enter the circuitId: ")
            name=input("Enter the name: ")
            date=input("Enter the date: ")
            time=input("Enter the time: ")
            nrace=Race(raceId,year,round,circuitId,name,date,time)
            racemapper.update(nrace)
            print("Race updated(P)")

    elif operation=="delete":
        table=input("Enter the table name(driver,race): ")
        if table=="driver":
            deleteId=input("Enter the driverId: ")
            drivermapper.delete(deleteId)
            print("Driver deleted(P)")
        elif table=="race":
            raceId=input("Enter the raceId: ")
            racemapper.delete(raceId)
            print("Race Deleted(P)")

    elif operation=="getall":
        table=input("Enter the table name(driver,race): ")
        if table=="driver":
            alldrivers=drivermapper.getall()
            for i in range(len(alldrivers)):
                print(alldrivers[i])
        else:
            all_races=racemapper.getall()
            for i in range(len(all_races)):
                print(all_races[i])

    elif operation=="other":
        print("For all drivers of particular race: Enter 1")
        print("For all races of particular driver: Enter 2")
        op=input("Enter your operation: ")
        if op=="1":
            raceId=input("Enter the raceId: ")
            drivers=drivermapper.getdrivers_raceid(raceId)
            print("NAme of all drivers in raceid: "+raceId)
            print(len(drivers))
            for i in range(len(drivers)):
                print(drivers[i][0]+" "+drivers[i][1])
        elif op=="2":
            driverId=input("Enter the driverId: ")
            races=racemapper.getrace_driverid(driverId)
            print("Names of all races by driverId: "+driverId)
            for i in range(len(races)):
                print(races[i][0])



#all races by driver

# driverId=input("Enter the driverId: ")
# driverRef=input("Enter the driverRef: ")
# code=input("Enter the code: ")
# forename=input("Enter the forename: ")
# surname=input("Enter the surname: ")
# dob=input("Enter the dob: ")
# nationality=input("Enter Nationality: ")
# driver.add(driverId,driverRef,code, forename, surname,dob,nationality)
# print("Driver Added Successfully")

# update_id=input("Enter the driverId to update: ")
# driver.update(update_id)

# delete_id=input("Enter the driverId to delete: ")
# driver.delete(delete_id)

# alldrivers=driver.getall()
# for i in range(len(alldrivers)):
#     print(alldrivers[i])


##RACE

# raceId=input("Enter the raceId: ")
# year=input("Enter the year: ")
# round=input("Enter the round: ")
# circuitId=input("Enter the circuitId: ")
# name=input("Enter the name: ")
# date=input("Enter the date: ")
# time=input("Enter the time: ")
# race.add(raceId,year,round,circuitId,name,date,time)
# print("Race added(P)")

# update_id=input("Enter the raceId to update: ")
# race.update(update_id)

# delete_id=input("Enter the raceId to delete: ")
# race.delete(delete_id)

# all_races=race.getall()
# for i in range(len(all_races)):
#     print(all_races[i])

#all drivers of race
# raceId=input("Enter the raceId: ")
# drivers=driver.getdrivers_race(raceId)
# print("NAme of all drivers in raceid: "+raceId)
# print(len(drivers))
# for i in range(len(drivers)):
#     print(drivers[i][0]+" "+drivers[i][1])

#all races by driver
# driverId=input("Enter the driverId: ")
# races=race.getraces_driver(driverId)
# print("Names of all races by driverId: "+driverId)
# for i in range(len(races)):
#     print(races[i][0])
