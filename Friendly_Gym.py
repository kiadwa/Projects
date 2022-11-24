'''
Language: Python 3

Description

Application will ask for user information and later display a list of training for user to choose from
'''

import math
#function for calculate reps and mins of ages over 60 
def reduce_repmin (age,reps):
    '''calculate reps and mins for ages equal to and over 60'''
    if age >= 60 and age < 65: 
        x = age - 60
        reps = reps - reps*(0.01*x)
    if age >=65 and age < 75: 
        x = age -65 
        reps = reps- reps*(0.05 + 0.02*x)
    if age >= 75 and age < 80: 
        x = age - 75
        reps = reps - reps*(0.25 + 0.03*x)
    if age >= 80 and age <= 110: 
        x = age - 80 
        if x <= 10: 
            reps = reps - reps*(0.4+ 0.04*x)
        else: 
            reps = reps - reps*(0.8)
    return math.ceil(reps)
#function for name checking
def name_veri(x):
    ''' Function to validate user's name value with only letters and spaces'''
    i=0
    a = True
    if x =='':
        a = False  #function will return False if blank string is entered
    while i < len(x):
        if x.startswith(' ') or x.endswith(' '):
            a = False
            break
        elif x[i].isalpha() or x[i].isspace() : 
            i+=1
        else: 
            a= False
            break
    return a 

##########
#creating variables for reps and mins
rep_15 = 15
rep_20 = 20
rep_18 = 18
rep_10 = 10 
rep_12  = 12
mins_2 = 2
mins_3 = 3
mins_10 = 10
mins_15 = 15

#creating variables for each excercise, storing excercise info
fat_loss = f"Gym workout for fat loss\n\nPlate thrusters ({rep_15} reps x 3 sets)\nMountain climbers ({rep_20} reps x 3 sets)\nBox jumps ({rep_10} reps x 3 sets)\nLunges ({rep_10} reps x 3 sets)\nRenegade rows ({rep_10} reps x 3 sets)\nPress ups ({rep_15} reps x 3 sets)\nTreadmill ({rep_10} mins x 3 sets)\nSupermans ({rep_10} reps x 3 sets)\nCrunches ({rep_10} reps x 3 sets)"
str_rl = f"Gym workout for stretch and relax\n\nQuad stretchs ({mins_2} mins x 3 sets)\nHamstring stretchs ({mins_2} mins x 3 sets)\nChest and shoulder stretchs ({mins_2} mins x 2 sets)\nUpper back stretchs ({mins_3} mins x 2 sets)\nBiceps stretchs ({mins_2} mins x 2 sets)\nTriceps stretchs ({mins_2} mins x 3 sets)\nHip flexors ({mins_2} mins x 3 sets)\nCalf stretchs ({mins_2} mins x 3 sets)\nLower back stretchs ({mins_2} mins x 3 sets)"
hiit = f"Gym workout for high-intensity exercises\n\nJumping jacks ({rep_20} reps x 4 sets)\nSprints ({rep_20} reps x 3 sets)\nMountain climbers ({rep_20} reps x 4 sets)\nSquat jumps ({rep_20} reps x 4 sets)\nLunges ({rep_20} reps x 3 sets)\nCrunches ({rep_20} reps x 3 sets)\nTreadmill ({rep_15} mins x 2 sets)\nSide planks ({rep_15} reps x 3 sets)\nBurpees ({rep_15} reps x 3 sets)"
legs = f"Gym workout for strong legs\n\nBack squats ({rep_10} reps x 5 sets)\nHip thrusts ({rep_12} reps x 3 sets)\nOverhead presses ({rep_10} reps x 5 sets)\nRack pulls ({rep_10} reps x 5 sets)\nSquats ({rep_10} reps x 4 sets)\nDumbbell lunges ({rep_10} reps x 3 sets)\nLeg curls ({rep_15} reps x 3 sets)\nStanding calf raises ({rep_20} reps x 2 sets)"
abs_ex = f"Gym workout for strong ABS\n\nCross crunchs ({rep_12} reps x 3 sets)\nKnee ups ({rep_15} reps x 5 sets)\nHip thrusts ({rep_15} reps x 3 sets)\nMountain climbers ({rep_15} reps x 3 sets)\nVertical hip thrusts ({rep_12} reps x 3 sets)\nBicycles ({mins_15} mins x 2 sets)\nFront planks ({mins_15} mins x 3 sets)\nDragon flags ({rep_12} reps x 4 sets)\nReverse crunches ({rep_10} reps x 3 sets)"
sho_arm = f"Gym workout for strong shoulder and arms\n\nBench presses ({rep_10} reps x 5 sets)\nTriceps dips ({rep_10} reps x 5 sets)\nIncline dumbbell presses ({rep_12} reps x 3 sets)\ndumbbell flyes ({rep_15} reps x 3 sets)\nTriceps extensions ({rep_15} reps x 3 sets)\nPull ups ({rep_10} reps x 5 sets)\nTreadmill ({mins_15} mins x 2 sets)\nBent over rows ({rep_10} reps x 5 sets)\nChin ups ({rep_10} reps x 3 sets)"
mchild_ex =f"Gym workout for a male younger than 18 years old\n\nHigh knees ({rep_20} reps x 3 sets)\nSquats ({rep_10} reps x 3 sets)\nCalf raises ({rep_10} reps x 3 sets)\nScissor jumps ({rep_12} reps x 3 sets)\nBurpees ({rep_10} reps x 3 sets)\nTreadmill ({mins_10} mins x 2 sets)"
fchild_ex = f"Gym workout for a female younger than 18 years old\n\nSquats ({rep_10} reps x 3 sets)\nCrunches ({rep_10} reps x 2 sets)\nJumping jacks ({rep_10} reps x 3 sets)\nPush ups ({rep_10} reps x 2 sets)\nBurpees ({rep_10} reps x 3 sets)\nTreadmill ({mins_10} mins x 2 sets)"
madult_ex = f"Gym workout for a male at least 18 years old\n\nStanding biceps curls ({rep_20} reps x 3 sets)\nSeated incline curls ({rep_18} reps x 3 sets)\nSeated dumbbell presses ({rep_12} reps x 3 sets)\nLeg presses ({rep_15} reps x 3 sets)\nBench presses ({rep_10} reps x 4 sets)\nTricep kickbacks ({rep_15} reps x 3 sets)\nHip thrusts ({rep_12} reps x 3 sets)\nSeated rows ({rep_10} reps x 4 sets)"
fadult_ex = f"Gym workout for a female at least 18 years old\n\nLateral raises ({rep_15} reps x 3 sets)\nReverse flyes ({rep_12} reps x 3 sets)\nHip thrusts ({rep_12} reps x 3 sets)\nIncline dumbbell presses ({rep_15} reps x 3 sets)\nSquats ({rep_10} reps x 4 sets)\nDumbbell lunges ({rep_10} reps x 3 sets)\nLeg presses ({rep_12} reps x 3 sets)\nDumbbell presses ({rep_10} reps x 4 sets)"


#different lists for each 2 genders
ftraining_list = ["fat_loss","str_rl","hiit","legs","abs_ex","sho_arm","fchild_ex","fadult_ex"]
mtraining_list = ["fat_loss","str_rl","hiit","legs","abs_ex","sho_arm","mchild_ex","madult_ex"]
#create dictionaries for better data referencing later in conditional loops

train_num_dict = {1:fat_loss,2:str_rl,3:hiit,4:legs,5:abs_ex,6:sho_arm}
dictadult = {"male":madult_ex,"female":fadult_ex}
dictchild = {"male":mchild_ex,"female":fchild_ex}


#probing user for information 

name = input("Please enter your name: ") 
#validation for user information entry 
while name_veri(name) == False:
    print("Error: Only accept alphabetical characters and spaces for name")
    print('')
    name = input("Please enter your name: ")


print('')
    


age = int(input("Please enter your age: "))
#validation for user information entry 
while type(age) == int and age not in range(1,111):
    print("Error: The age is a number between 0 to 110")
    print('')
    age = int(input("Please enter your age: "))


    
print('')


sex = input("Please enter your biological sex (female/male): ")
#validation for user information entry 
while sex != "female" and sex != "male":
    print("Error: Please enter valid input")
    print('')
    sex = input("Please enter your biological sex (female/male): ")
    

print('')


train = int(input("What do you want to get out of your training? \n    1. Your goal is losing weight\n    2. Your goal is to staying calm and relax\n    3. Your goal is increasing your heart rate\n    4. Your goal is having stronger legs\n    5. Your goal is having stronger ABS\n    6. Your goal is having stronger shoulders and arms\nChoose a number between 1 to 6: "))
#validation for user information entry 
while train not in range(1,7):
    print("Error - It can only be a number between 1 to 6")
    print('')
    train = int(input("What do you want to get out of your training? \n    1. Your goal is losing weight\n    2. Your goal is to staying calm and relax\n    3. Your goal is increasing your heart rate\n    4. Your goal is having stronger legs\n    5. Your goal is having stronger ABS\n    6. Your goal is having stronger shoulders and arms\nChoose a number between 1 to 6: "))
    
print('')

day_train = int(input("How many days per week you can train: "))
#validation for user information entry 
while day_train not in range(1,8):
    print("Error: It can only be a number between 1 to 7")
    print('')
    day_train = int(input("How many days per week you can train: "))
    
print('')


#identify and provide training program base on user information: 
print(f"Hello {name}! Here is your training:")

if age >= 18 and age < 60:
   
    i=0
    while i < day_train:
        print("-------------------------------------------------------------------------------------")
        print(f"Day {i+1}")
        if (i+1) %2 == 0: 
            print(f"{dictadult[sex]}")
        else:
            print(f"{train_num_dict[train]}")
        i+=1
              
elif age < 18:
    
    i=0
    while i < day_train:
        print("-------------------------------------------------------------------------------------")
        print(f"Day {i+1}")
        if (i+1) %2 == 0: 
            print(f"{dictchild[sex]}")
        else:
            print(f"{train_num_dict[train]}")
        i+=1


    
#fixing reps for people of age over 60:


elif age >= 60:
    rep_10 = reduce_repmin(age,rep_10)
    rep_12 = reduce_repmin(age,rep_12)
    rep_15 = reduce_repmin(age,rep_15)
    rep_20 = reduce_repmin(age,rep_20)
    rep_18 = reduce_repmin(age,rep_18)
    mins_2 = reduce_repmin(age,mins_2)
    mins_3 = reduce_repmin(age,mins_3)
    mins_10 = reduce_repmin(age,mins_10)
    mins_15 = reduce_repmin(age,mins_15)
    fat_loss = f"Gym workout for fat loss\n\nPlate thrusters ({rep_15} reps x 3 sets)\nMountain climbers ({rep_20} reps x 3 sets)\nBox jumps ({rep_10} reps x 3 sets)\nLunges ({rep_10} reps x 3 sets)\nRenegade rows ({rep_10} reps x 3 sets)\nPress ups ({rep_15} reps x 3 sets)\nTreadmill ({rep_10} mins x 3 sets)\nSupermans ({rep_10} reps x 3 sets)\nCrunches ({rep_10} reps x 3 sets)"
    str_rl = f"Gym workout for stretch and relax\n\nQuad stretchs ({mins_2} mins x 3 sets)\nHamstring stretchs ({mins_2} mins x 3 sets)\nChest and shoulder stretchs ({mins_2} mins x 2 sets)\nUpper back stretchs ({mins_3} mins x 2 sets)\nBiceps stretchs ({mins_2} mins x 2 sets)\nTriceps stretchs ({mins_2} mins x 3 sets)\nHip flexors ({mins_2} mins x 3 sets)\nCalf stretchs ({mins_2} mins x 3 sets)\nLower back stretchs ({mins_2} mins x 3 sets)"
    hiit = f"Gym workout for high-intensity exercises\n\nJumping jacks ({rep_20} reps x 4 sets)\nSprints ({rep_20} reps x 3 sets)\nMountain climbers ({rep_20} reps x 4 sets)\nSquat jumps ({rep_20} reps x 4 sets)\nLunges ({rep_20} reps x 3 sets)\nCrunches ({rep_20} reps x 3 sets)\nTreadmill ({rep_15} mins x 2 sets)\nSide planks ({rep_15} reps x 3 sets)\nBurpees ({rep_15} reps x 3 sets)"
    legs = f"Gym workout for strong legs\n\nBack squats ({rep_10} reps x 5 sets)\nHip thrusts ({rep_12} reps x 3 sets)\nOverhead presses ({rep_10} reps x 5 sets)\nRack pulls ({rep_10} reps x 5 sets)\nSquats ({rep_10} reps x 4 sets)\nDumbbell lunges ({rep_10} reps x 3 sets)\nLeg curls ({rep_15} reps x 3 sets)\nStanding calf raises ({rep_20} reps x 2 sets)"
    abs_ex = f"Gym workout for strong ABS\n\nCross crunchs ({rep_12} reps x 3 sets)\nKnee ups ({rep_15} reps x 5 sets)\nHip thrusts ({rep_15} reps x 3 sets)\nMountain climbers ({rep_15} reps x 3 sets)\nVertical hip thrusts ({rep_12} reps x 3 sets)\nBicycles ({mins_15} mins x 2 sets)\nFront planks ({mins_15} mins x 3 sets)\nDragon flags ({rep_12} reps x 4 sets)\nReverse crunches ({rep_10} reps x 3 sets)"
    sho_arm = f"Gym workout for strong shoulder and arms\n\nBench presses ({rep_10} reps x 5 sets)\nTriceps dips ({rep_10} reps x 5 sets)\nIncline dumbbell presses ({rep_12} reps x 3 sets)\ndumbbell flyes ({rep_15} reps x 3 sets)\nTriceps extensions ({rep_15} reps x 3 sets)\nPull ups ({rep_10} reps x 5 sets)\nTreadmill ({mins_15} mins x 2 sets)\nBent over rows ({rep_10} reps x 5 sets)\nChin ups ({rep_10} reps x 3 sets)"
    mchild_ex =f"Gym workout for a male younger than 18 years old\n\nHigh knees ({rep_20} reps x 3 sets)\nSquats ({rep_10} reps x 3 sets)\nCalf raises ({rep_10} reps x 3 sets)\nScissor jumps ({rep_12} reps x 3 sets)\nBurpees ({rep_10} reps x 3 sets)\nTreadmill ({mins_10} mins x 2 sets)"
    fchild_ex = f"Gym workout for a female younger than 18 years old\n\nSquats ({rep_10} reps x 3 sets)\nCrunches ({rep_10} reps x 2 sets)\nJumping jacks ({rep_10} reps x 3 sets)\nPush ups ({rep_10} reps x 2 sets)\nBurpees ({rep_10} reps x 3 sets)\nTreadmill ({mins_10} mins x 2 sets)"
    madult_ex = f"Gym workout for a male at least 18 years old\n\nStanding biceps curls ({rep_20} reps x 3 sets)\nSeated incline curls ({rep_18} reps x 3 sets)\nSeated dumbbell presses ({rep_12} reps x 3 sets)\nLeg presses ({rep_15} reps x 3 sets)\nBench presses ({rep_10} reps x 4 sets)\nTricep kickbacks ({rep_15} reps x 3 sets)\nHip thrusts ({rep_12} reps x 3 sets)\nSeated rows ({rep_10} reps x 4 sets)"
    fadult_ex = f"Gym workout for a female at least 18 years old\n\nLateral raises ({rep_15} reps x 3 sets)\nReverse flyes ({rep_12} reps x 3 sets)\nHip thrusts ({rep_12} reps x 3 sets)\nIncline dumbbell presses ({rep_15} reps x 3 sets)\nSquats ({rep_10} reps x 4 sets)\nDumbbell lunges ({rep_10} reps x 3 sets)\nLeg presses ({rep_12} reps x 3 sets)\nDumbbell presses ({rep_10} reps x 4 sets)"


#different lists for each 2 genders
    ftraining_list = ["fat_loss","str_rl","hiit","legs","abs_ex","sho_arm","fchild_ex","fadult_ex"]
    mtraining_list = ["fat_loss","str_rl","hiit","legs","abs_ex","sho_arm","mchild_ex","madult_ex"]
#create dictionaries for better data referencing later in conditional loops

    train_num_dict = {1:fat_loss,2:str_rl,3:hiit,4:legs,5:abs_ex,6:sho_arm}
    dictadult = {"male":madult_ex,"female":fadult_ex}
    i=0
    while i < day_train:
        print("-------------------------------------------------------------------------------------")
        print(f"Day {i+1}")
        if (i+1) %2 == 0: 
            print(f"{dictadult[sex]}")
        else:
            print(f"{train_num_dict[train]}")
        i+=1





print("-------------------------------------------------------------------------------------\n")
print(f"Bye {name}.")

