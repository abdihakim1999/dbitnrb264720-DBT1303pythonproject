#NEIGHBORHOOD MOVEMENT MANAGEMENT SOFTWARE BY ABDIRASHID ABDI ALI DBITNRB264720

#My project below is to manage routes within the neighbourhood ..visitors are asingned route

''' step1 (get input from visitors)'''

name =input("Please key in your name:")
print("Hi there " + name +", where are you headed?:")
destination = input (" enter house to visit: ")
print(" Please wait as we confirm with " + destination + " we will advise you shortly")

#HOST

host =input(" do you wish to be visited by" + name + " at your home!(true or False):")
is_visit =True
print(" Your geust" + name +"will be allocated a route to "+ destination + "!:")
is_visit =False
print(" We shall notify "+ name +"that you arent available ")

print("visitor not allowed ")

#this responds now takes us to generating timings for the  route allocation

#step 3

#use of time calculation time
time_in = float
time_arrive = float
time_in = input("please enter start time (use dots)")
time_arrive = input(" enter expected time of arrival to host(use dots)")

result = float(time_arrive) - float(time_in)

#the system will print out estimated time of arrival
print(result)

print("have a lovely day ahead" + name +"Walk safe!" )

#the visitor proceeds to route