"""
Author:Samarth Kanubhai Patel

this code is written for made selection for items and rides and after that making bill of items and rides
"""

rides={"Behemoth":15,
       "The Fly":25
       ,"Krachenwagen":30
       ,"Psyclone":17
       ,"Time Warp":36} #this is dic of rides
menu={"Burger":5,
      "Pizza":8,
      "Coffee":3,
      "Hot Chocolate":2,
      "Ice cream":4}  #this is dic of food menu

rides_price=[15,25,30,17,36]   #it is ride price list

food_price=[5,8,3,2,4]   #it is food price list

food_name=["Burger","Pizza","Coffee","Hot Chocolate","Ice cream"]   #it is food name list

rides_name=["Behemoth","The Fly","Krachenwagen","Psyclone","Time Warp"]  #it is ride name list

print("Welcome to Wonderland! Available rides:")

i=0
for name,value in rides.items():   #this for loop use for print rides options for user 
    i+=1
    print(f"{i}. {name}- {value}$")
    
print("\n\nFood menu:")  
k=0
for name,value in menu.items():    #this for loop use for print food options for user
    k+=1
    print(f"{k}. {name}- {value}$")

friend_name=[]  #empty list for user input friend name
l=1
while l<6:                          #this loop is used for taking input of 5 friend's name 
    friend=input(f"\nEnter the name of Friend {l}:")
    l+=1
    friend_name.append(friend)

ride_selection = [] #empty list to add selection of rides name

ride_selected_price = [] #empty list to add selected ride price

for o in range(2):      #it is asking two times to user input number 
    print("\nAvailable Rides:")
    c=0
    while c<1  :
            k=0
            for name,value in rides.items(): #it is print available rides
                k+=1
                print(f"{k}. {name}- {value}$")
            c+=1
            selected_rides=int(input("Enter the number of ride you want to go:"))  #taking input for rides
            ride_selected_price.append(rides_price[selected_rides-1])  #add into list items price that selected
            ride_selection.append(rides_name[selected_rides-1]) #add into list items price that selected
           


food_selection = []
food_selected_price=[]
for p in range(2):
    print("\nFood menu:")
    b=0
    while b<1  :
            w=0
            for name,value in menu.items(): #it is print available menu
                w+=1
                print(f"{w}. {name}- {value}$")
            b+=1
            selected_choice=int(input("Enter the number forfood you want to eat:"))   #taking input for 
            food_selected_price.append(food_price[selected_choice-1])  #add into list items price that selected
            food_selection.append(food_name[selected_choice-1])  #add into list items price that selected
            
            

print("\n\nSelected Rides:") 

for items in ride_selection:  #print Selected Rides names
     print(items)

print("\nSelected Food")

for foods in food_selection:    #print Selected foods names
     print(foods)

           
cost_food = sum(food_selected_price)                        #Total of food cost that were selected
print(f"\n\nTotal food cost : $ {cost_food}")

cost_rides = sum(ride_selected_price)                   #Total of ride cost that were selected
print(f"Total ride cost : $ {cost_rides}")

total_cost=cost_food+cost_rides                        #Total of food cost and ride cost
print(f"Total cost : $ {total_cost}")

if total_cost>0: #if totat is greater than 0 then print this line 
    print("\n\nCongratulations! You are eligible for a prize.")

import random   #import random 
random_name=random.choice(friend_name)  #select one random name among the five friends
print("\n\nThe Lucky Winner of the price is:",random_name)

print("Enjoy your day at wonderland and have fun!")

