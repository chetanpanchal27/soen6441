from flask import Flask, jsonify, request
import json
from race import Race
from driver import Driver
from racemapper import Racemapper
from drivermapper import Drivermapper
from collections import namedtuple

app = Flask(__name__)
racemapper=Racemapper()
drivermapper=Drivermapper()

@app.route('/')
def home():
    return render_template('home.html')

#races
@app.route("/getAllraces", methods = ["GET"])
def getallraces():
    print("get all")
    data = racemapper.getall()
    l=[]
    for i in range(len(data)):
        l.append(data[i])
    print(l)
    return render_template('indexrace.html', l=l)

@app.route("/srace" ,methods=['GET'])
def srace():
    return render_template('srace.html')

@app.route("/getBasedOnDriverId" , methods = ["GET"])
def getraces_driverid():
    print("request.args ==> ", request.args)
    args = request.args
    data = racemapper.getrace_driverid(args.get("driverid"))
    l=[]
    for i in range(len(data)):
        l.append(data[i])
    return render_template('racesofdriver.html', l=l)
   

@app.route("/rinsert" ,methods=['GET'])
def rinsert():
    return render_template('raceinsert.html')

@app.route("/insert" , methods = ["GET"])
def insert_race():
    result = request.get_json()
    print("result ==> ", result)
    race=Race(request.args.get("raceid"),request.args.get("year"),request.args.get("round"),request.args.get("name"),request.args.get("date"),request.args.get("time"),request.args.get("circuitid"))
    #race=Race(request.args.get("driverid"),request.args.get("driverref"),request.args.get("code"),request.args.get("forename"),request.args.get("surname"),request.args.get("dob"),request.args.get("nationality"))
    #driver = Driver(result["driverId"], result["driverRef"], result["code"], result["forename"], result["surname"], result["dob"], result["nationality"])
    racemapper.add(race)
    data = racemapper.getall()
    l=[]
    for i in range(len(data)):
        l.append(data[i])
    return render_template('indexrace.html', l=l)



@app.route("/rupdate" ,methods=['GET'])
def rupdate():
    return render_template('raceupdate.html')    

@app.route("/forupdaterace" , methods = ["GET"])
def rupdated():
    print("forupdaterace ==>", request.get_json())
    result = request.get_json()
    l=racemapper.getracebyId(request.args.get("raceid"))
    return render_template('forraceupdate.html',l=l)


@app.route("/updateRaceData" , methods = ["GET"])
def update_race():
    print("updateRaceData ==>", request.get_json())
    result = request.get_json()
    race=Race(request.args.get("raceid"),request.args.get("year"),request.args.get("round"),request.args.get("name"),request.args.get("date"),request.args.get("time"),request.args.get("circuitid"))
    #race = Race(result["raceId"], result["year"], result["round"], result["name"], result["date"], result["time"], result["circuitId"])
    racemapper.update(race)    
    data = racemapper.getall()
    l=[]
    for i in range(len(data)):
        l.append(data[i])
    return render_template('indexrace.html', l=l)
    
@app.route("/rdelete" ,methods=['GET'])
def rdelete():
    return render_template('racedelete.html')

@app.route("/deleteByRaceId" , methods = ["GET"])
def deleterace():
    # result = request.get_json()
    args = request.args
    racemapper.delete(args.get("raceid"))
    data = racemapper.getall()
    l=[]
    for i in range(len(data)):
        l.append(data[i])
    return render_template('indexrace.html', l=l)
    

#driver
from flask import Flask, redirect, url_for, render_template, request, flash

@app.route("/getAlldrivers", methods = ["GET"])
def getalldrivers():
    print("get all drivers")
    data = drivermapper.getall()
    l=[]
    for i in range(len(data)):
        l.append(data[i])
    print(l)
    
    return render_template('index.html', l=l)
    #return '{"msg" : "success", "data" : ' + json.dumps(data) + '}'

@app.route("/sdriver" ,methods=['GET'])
def sdriver():
    return render_template('sdriver.html')

@app.route("/getBasedOnRaceId" , methods = ["GET"])
def getdrivers_race():
    print("request.args ==> ", request.args)
    args = request.args
    data = drivermapper.getdrivers_raceid(args.get("raceid"))
    l=[]
    for i in range(len(data)):
        l.append(data[i])
    return render_template('driversofrace.html', l=l)
    

@app.route("/ginsert" ,methods=['GET'])
def ginsert():
    return render_template('insert.html')

@app.route("/insert/driver" , methods = ["GET"])
def inserdriver():
    result = request.get_json()
    print("result ==> ", result)
    driver=Driver(request.args.get("driverid"),request.args.get("driverref"),request.args.get("code"),request.args.get("forename"),request.args.get("surname"),request.args.get("dob"),request.args.get("nationality"))
    #driver = Driver(result["driverId"], result["driverRef"], result["code"], result["forename"], result["surname"], result["dob"], result["nationality"])
    drivermapper.add(driver)
    data = drivermapper.getall()
    l=[]
    for i in range(len(data)):
        l.append(data[i])
    return render_template('index.html',l=l)

@app.route("/gUpdateDriverId" ,methods=['GET'])
def gupdate():
    return render_template('update.html')

@app.route("/forupdatedriver" , methods = ["GET"])
def fupdated():
    print("forupdatedriver ==>", request.get_json())
    result = request.get_json()
    l=drivermapper.getdriverbyId(request.args.get("driverid"))
    return render_template('fordriverupdate.html',l=l)


@app.route("/updateDriiverData" , methods = ["GET"])
def updatedriver():
    print("updateDriverData ==>", request.get_json())
    result = request.get_json()
    print("id",request.args.get("driverid"))
    driver=Driver(request.args.get("driverid"),request.args.get("driverref"),request.args.get("code"),request.args.get("forename"),request.args.get("surname"),request.args.get("dob"),request.args.get("nationality"))
    #driver=Driver(result["driverId"], result["driverRef"], result["code"], result["forename"], result["surname"], result["dob"], result["nationality"])
    drivermapper.update(driver)    
    data = drivermapper.getall()
    l=[]
    for i in range(len(data)):
        l.append(data[i])
    return render_template('index.html',l=l)
    

@app.route("/gdeleteByDriverId" ,methods=['GET'])
def gdelte():
    return render_template('delete.html')


@app.route("/deleteByDriverId" , methods = ["GET"])
def deletedriver():
    #id=request.args.get("driverid")
    args = request.args
    print(args.get("driverid"))
    drivermapper.delete(request.args.get("driverid"))
    data = drivermapper.getall()
    l=[]
    for i in range(len(data)):
        l.append(data[i])
    return render_template('index.html',l=l)
    