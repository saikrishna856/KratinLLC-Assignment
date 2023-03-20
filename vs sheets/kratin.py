class Sunita_Sharma:
    def __init__(self,patient,age,blood_group,blood_pressure,sugar):
        self.patient=patient
        for i in self.patient:
            if(i.isdigit()):
                raise NameError
        self.age=age 
        self.blood_group=blood_group[:-1]
        self.sign=blood_group[-1]
        self.s=""
        if(self.sign=="+"):
            self.s="Positive"
        else:
            self.s="Negative"
        self.blood_pressure=blood_pressure 
        self.sugar=sugar
        if(not(65<=self.age<=100) or len(str(self.blood_pressure))>3 or len(str(self.sugar))>3):
            raise ValueError
    def details(self):
        return("""patient  : {}
Age(should be 65 to 100 only):{}
blood group(A or B or O or AB): {}    Sign:{}  
Blood pressure(BP) : {}
Diabetes           : {}""".format(self.patient,self.age,self.blood_group,self.s,self.blood_pressure,self.sugar))
    def bp_Checking(self):
        if(self.blood_pressure>110)and(self.blood_pressure<=140):
            print("""Blood pressure Result:-This is normal. 
------------------------------------------------------------------
** please do this bellow Precations.
---------------------------------------------------------------------------------------
Precations:-
------------
1.As a general goal, aim for at least 30 minutes 
of moderate physical activity every day.
2.Exercise can also help keep elevated blood pressure
from turning into high blood pressure (hypertension). 
3.For those who have hypertension,
regular physical activity can bring blood pressure down to safer levels.""")
        elif(self.blood_pressure<=110):
            print("""Blood pressure Result:- This is Low Blood blood pressure. 
---------------------------------------------------------------------------------------
** If you want to over come this problem please do this bellow Precations.
---------------------------------------------------------------------------------------
Precations :-
-----------
1.Eat more salt. Contrary to popular advice, 
low-sodium diets are not good for everyone with blood pressure problems. ...
2.Avoid alcoholic beverages. ...
3.Discuss medications with a doctor. ...
4.Cross legs while sitting. ...
5.Drink water. ...
6.Eat small meals frequently. ...
7.Wear compression stockings. ...
8.Avoid sudden position changes.""") 
        
        elif(self.blood_pressure >140)and(self.blood_pressure<=180):
            print("""Blood pressure Result:-This is symptom for getting blood pressure. 
----------------------------------------------------------------------
** If you want to over come this problem please do this bellow Precations.
---------------------------------------------------------------------------------------
Precations:-
------------
1.Lose extra pounds and watch your waistline. 
2.Blood pressure often increases as weight increases. 
3.Exercise regularly. 
4.Eat a healthy diet. 
5.Reduce salt (sodium) in your diet. 
6.Limit alcohol. 
7.Get a good night's sleep. 
8.Reduce stress. 
9.Monitor your blood pressure at home and get regular checkups.""")
        else:
            print("""Blood pressure Result:-It means you have high blood pressure.
 -----------------------------------------------------------------------------
 **If you want to over come this problem please do this bellow Precations.
---------------------------------------------------------------------------------------
TREATMENT:
----------
1.Eating a heart-healthy diet with less salt.
2.Getting regular physical activity.
3.Maintaining a healthy weight or losing weight.
4.Limiting alcohol.
5.Not smoking.
6.Getting 7 to 9 hours of sleep daily.
7.immidiatly consult doctore for medicine.""")
    def sugar_checking(self):
        if(self.sugar<=140):
            print("""Blood sugar result:- This is normal keep maiatain like this
-----------------------------------------------------------------
Precations:-
------------
1.Lose extra weight. Losing weight reduces the risk of diabetes. ...
2.Be more physically active. There are many benefits to regular physical activity. ...
3.Eat healthy plant foods. Plants provide vitamins, minerals and carbohydrates in your diet. ...
4.Eat healthy fats. ...
5.Skip fad diets and make healthier choices.""")
        elif(self.sugar>140)and(self.sugar<=200):
            print("""Blood sugar result:- Due to this, symptoms of blood sugar 
---------------------------------------------------------------------
Precations:-
------------
1.Keep track of your blood sugar levels to see what makes them go up or down.
2.Eat at regular times, and don't skip meals.
3.Choose foods lower in calories, saturated fat, trans fat, sugar, and salt.
4.Track your food, drink, and physical activity.
5.Drink water instead of juice or soda.""")
        else:
            print("""Blood sugar result:- It means High amount of suger in your blood
---------------------------------------------------------------------------------------
Precations:-
---------------------------------------------------------------------------------------
1.Exercise regularly. ...
2.Manage your carb intake. ...
3.Eat more fiber. ...
4.Drink water and stay hydrated. ...
5.Implement portion control. ...
6.Choose foods with a low glycemic index. ...
7.Try to manage your stress levels. ...
8.Monitor your blood sugar levels.""")
#-----------------------------------------------------------------------------
# i am taking sugar in blood and bp(blood pressure if this is normal then this peoples are good in health i feel like this. so that's why i wrote a code for these things.        
       
try:        
    name=input("Enter Name: ")
    a=int(input("Enter Your Age: "))
    b=input("Enter Your Blood Group: ")
    blood_pressure=int(input("Enter Your Blood Pressure(As per Test result): "))
    sugar=int(input("Enter Your Sger Leves(As per Test Result): "))
    obj=Sunita_Sharma(name,a,b,blood_pressure,sugar)
    print(obj.details())
    print("*"*70)
    obj.bp_Checking()
    print("*"*70)
    obj.sugar_checking()
    print("*"*70)
except ValueError:
    print("Please check your age or bp or suger values are may be incorrect....")
except NameError:
    print("please provide correct name or blood group ...")
except:
    print("information not correct please check once....")
finally:
    print("""           ------------------------------------------
              ** Thanks for this opportunity **
          -------------------------------------------""")