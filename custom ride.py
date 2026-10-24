print("============================================")
print("WELCOME TO THE CUSTOM RIDE TRANSPORT SYSTEM")
print("============================================")
user_vehicle=int(input("choose your vehicle: bike or car write 1 for bike and 2 for car"))
if user_vehicle==1:
    print('you chose bike')
    print('now you can choose the type of bike')
    print("if you chose scooty you can on drive in roads and the top speed is 60km/h")
    print("if you chose rockrider you can drive up hill on rocks and the road top speed 40km/h")
    bike_choice=int(input("1 for scooty and 2 for rockrider"))
    if bike_choice==1:
        print("You chose scooty!!")
    else:
        print("You chose rockrider")
elif user_vehicle==2:
    print('you chose car')
    print('now you can choose the type of car')
    print("if you choose BMW you can drive faster than trains and the speed is 200km/h")
    print("if you choose lambo you willget all the respect but not speed and the speed is 150km/h")
    car_choice=int(input('for BMW 1 and lambo 2'))
    if car_choice==1:
         print("You chose BMW!!")
    else:
        print("You chose lambo")
else:
    print("Soory, wrong input")