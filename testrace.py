import pytest,unittest
from racemapper import Racemapper
from drivermapper import Drivermapper
from race import Race
from driver import Driver

racemapper=Racemapper()
drivermapper=Drivermapper()
    
class testrace(unittest.TestCase):
<<<<<<< HEAD
    @pytest.mark.a
=======
  
>>>>>>> 136813301b374068555fb5743538b448565fbfcd
    def test_radd(self):
        race = Race("1000","2","3","4","5","6","7")
        racemapper.add(race)
        getrace=racemapper.getracebyId("1000")
        print(getrace)
<<<<<<< HEAD
        self.assertEqual(getrace[3] ,race.getname())

    @pytest.mark.b
=======
        self.assertEqual(getrace.getname() ,race.getname())

>>>>>>> 136813301b374068555fb5743538b448565fbfcd
    def test_dadd(self):
        driver=Driver("500","2","3","4","5","6","7")
        drivermapper.add(driver)
        getdriver=drivermapper.getdriverbyId("500")
<<<<<<< HEAD
        self.assertEqual(getdriver[5] ,driver.getdob())
    @pytest.mark.c
=======
        self.assertEqual(getdriver.getdob() ,driver.getdob())

>>>>>>> 136813301b374068555fb5743538b448565fbfcd
    def test_rupdate(self):
        #8 instaed of 7
        r=Race("1000","2","3","4","5","updated","7")
        racemapper.update(r)
        getnew=racemapper.getracebyId("1000")
<<<<<<< HEAD
        self.assertEqual( "updated",getnew[5])
    @pytest.mark.d
=======
        self.assertEqual( "updated",getnew.gettime())
    
>>>>>>> 136813301b374068555fb5743538b448565fbfcd
    def test_driverupdate(self):
        d=Driver("500","2","3","4","5","updated","7")
        drivermapper.update(d)
        getnew=drivermapper.getdriverbyId("500")
<<<<<<< HEAD
        self.assertEqual( "updated",getnew[5])
    @pytest.mark.e
=======
        self.assertEqual( "updated",getnew.getdob())
    
>>>>>>> 136813301b374068555fb5743538b448565fbfcd
    def test_rdelete(self):
        racemapper.delete("1000")
        getnew=racemapper.getracebyId("1000")
        print(getnew)
        self.assertEqual( None,getnew)
<<<<<<< HEAD
    @pytest.mark.f
=======

>>>>>>> 136813301b374068555fb5743538b448565fbfcd
    def test_driverdelete(self):
        drivermapper.delete("500")
        getnew=drivermapper.getdriverbyId("500")
        self.assertEqual( None,getnew)