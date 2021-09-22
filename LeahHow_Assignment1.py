#Assignment1

#Iphone 
isitApple = True
print (isitApple)

#Water Bottle
mybottlebrand = "SLM"
print (mybottlebrand)

#Cooking Utensils 
var1 = "fry"
var2 = "pan"
print(var1 + var2)

#Tshirts
myTshirts = {
"white": 3,
"black": 2, 
"pink": 1,
}
print (myTshirts)


# Assignment2 
myShoes = {
    "brand": "Adidas",
    "color": "beige",
    "size": "6us",
    "collection": "ultraboost",
    "pair": 1,
    "lightweight": True
}
print(myShoes)

# assignment3: this is my story maker
# interact with users
print ("Hello friends!")
print ("Asnwer questions to play")
print ("-----------------------------------")

# variables in your story
qualities = raw_input ("enter two qualities you value in a friendship: ")
name = raw_input ("What is your best friend's name?: ")
color = raw_input ("What is your best friend's favorite color?: ")
occupation = raw_input ("What is their occupation?: ")
activity = raw_input ("Favorite activity to do with your best friend (verb+ing): ")
location = raw_input ("Favorite place to go to do that activity: ")
celebrity = raw_input ("Favorite celebrity: ")
reason = raw_input ("What do you like about that celebrity?: ")


# this is your friendship story. it consist of strings, and variables.
# at the end of the story, you will understand how much you value your friendship

myStory = "Frienships are everything. I believe that frienships needs to have " + qualities + " in order to work. " \
"My best friend is " + name + "," "they love the color " + color + " and is a " + occupation + ". " \
"We spend most of our time at the " + activity + " at "+ location +" . " \
"I love my bestfriend but if I could trade them with anyone it would be " + celebrity + " . "\
"Well because " + reason + " and I will do anything for " + celebrity + " . " \
"So I guess my frienship is not that important to me because I will always choose " + celebrity + " over anybody. "

#This is your story about frienship
print (myStory)

