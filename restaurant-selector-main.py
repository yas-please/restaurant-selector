#this will be the main file for my restaurant selector tool. 

import random

#now, let's establish the different categories of food.
#I can do this by creating lists of restaurants that satisfy each category of food.
#restaurants can fill more than one category, so I might double-dip some names.

sushi = ["Fusion", "IzakaYa", "OkiDoki"];
pizza = ["Dominos", "PapaGuidos"]
fastfood = ["McDonalds", "ChickFilA", "Chipotle", "InNOut"]
halal = ["Cava", "HalalGuys", "HalalEurope"]
chicken = ["WingStop", "BuffaloWildWings"]
anything = [sushi, pizza, fastfood, halal, chicken]
genre = ["sushi", "pizza", "fastfood", "halal", "chicken", "anything"]

#I can add more restaurants later; right now I want to try to make this work.

#now I'd like to ask the user what type of food they'd like.

mood_input = input("What type of food would you like ? ")

#if this input corresponds to a category where I have restaurants tagged, then I'm good to go ! 
#if the input doesn't correspond to a category that exists, then I'll output a note listing the categories and urging the user to select an existing category.

#to make my life easier, I'm going to set up some default strings as responses and input prompts.
offer_1 = "You might enjoy "
offer_2 = "Sorry about that.  Here are all the restaurants that might satisfy your craving: "
offer_3 = "Sorry about that.  Perhaps you'd prefer "
good_job = "Excellent choice !  Enjoy your meal =)"
good_job2 = "Enjoy your meal =)"
bad_job = "I'm sorry I couldn't suggest a good idea.  Hopefully you've narrowed down your options !"
end = "     "

if "pizza" in mood_input: 
	response_1 = raw_input(offer_1 + str(random.choice(pizza)) + end)
	if "y" in response_1:
		print(good_job)		
	else: 
		response_2 = input(offer_2 + str(pizza) + end)				
		if "y" in response_2 or "ok" in response_2:
			print(good_job2)
		else:
			print(bad_job)
elif "halal" in mood_input:
	response_1 = input(offer_1 + str(random.choice(halal)) + end)
	if "y" in response_1:
		print(good_job)		
	else: 
		response_2 = input(offer_3 + str(random.choice(halal)) + end)				
		if "y" in response_2 or "ok" in response_2:
			print(good_job)
		else:
			response_3 = input(offer_2 + str(halal) + end)
			if "y" in response_3 or "ok" in response_3:
				print(good_job2)
			else: 
				print(bad_job)
elif "chicken" in mood_input:
	response_1 = input(offer_1 + str(random.choice(chicken)) + end)
	if "y" in response_1:
		print(good_job)		
	else:
		response_3 = input(offer_2 + str(chicken) + end)
		if "y" in response_3 or "ok" in response_3:
			print(good_job2)
		else: 
			print(bad_job)
elif "fastfood" in mood_input:
	response_1 = input(offer_1 + str(random.choice(fastfood)) + end)
	if "y" in response_1:
		print(good_job)		
	else: 
		response_2 = input(offer_3 + str(random.choice(fastfood)) + end)				
		if "y" in response_2 or "ok" in response_2:
			print(good_job)
		else:
			response_3 = input(offer_2 + str(fastfood) + end)
			if "y" in response_3 or "ok" in response_3:
				print(good_job2)
			else: 
				print(bad_job)
elif "sushi" in mood_input:
	response_1 = input(offer_1 + str(random.choice(sushi)) + end)
	if "y" in response_1:
		print(good_job)		
	else: 
		response_2 = input(offer_3 + str(random.choice(sushi)) + end)				
		if "y" in response_2 or "ok" in response_2:
			print(good_job)
		else:
			response_3 = input(offer_2 + str(sushi) + end)
			if "y" in response_3 or "ok" in response_3:
				print(good_job2)
			else: 
				print(bad_job)
elif "anything" in mood_input: 
	response_1 = input(offer_1 + str(random.choice(random.choice(anything))) + end)
	if "y" in response_1:
		print(good_job)		
	else: 
		response_2 = input(offer_3 + str(random.choice(random.choice(anything))) + end)				
		if "y" in response_2 or "ok" in response_2:
			print(good_job)
		else:
			print(bad_job)
elif mood_input not in anything and mood_input != "anything":
	print([str(n) for n in genre])