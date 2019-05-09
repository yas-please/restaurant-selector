#this will be the main file for my restaurant selector tool. 

#first, I want to create a dictionary that contains a list of restaurants organised by restaurant "type".
#the "type" is just going to be the word I use to describe whatever food I'm in the mood for (so may not be consistent).

restaurant_list = {"sushi":["Izaka-ya","Yanagi","Fusion","Oki Doki","369"],"halal":["Halal Guys","Gyro Lab","Chicken Maison"],"fast food":["McDonalds","Wendys","Chick fil a"],
"healthy":["Tocaya Organica","home cooking"]}

#I can always add to the restaurant_list dictionary later, or if I decide I'd prefer to import a file that tags restaurants with different dictionary entries I can change it.

user_choice = input("What would you like to eat ?   ")

if "sushi" in user_choice: 
	print("you said you'd like sushi.")