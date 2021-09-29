# Goodbye Earth!

import random # random numbers (https://docs.python.org/3.3/library/random.html)
import sys # system stuff for exiting (https://docs.python.org/3/library/sys.html)

# top of the file are declarations and variables.
# Bottom are the main function and story where the program logic starts

#Player Description
player = {
    "name": "p1",
    "score": 0,
    "items": ["bag"],
    "friends": [],
    "location": "start"
}

rooms = {
    "room1": "Dying earth",
    "room2": "Elon's rocket to Mars",
    "room3": "in Elon's rocket",
    "room4": "land on Mars"
}

def printGraphic(name):
    if (name == "toiletpaper"): 
        print ('    .--""--.___.._   ')
        print ('   (  <__>  )     `-.')
        print ('   | --..-- |      <|')
        print ('   |       :|       /')
        print ('   |       :|--""-./ ')
        print ('   `.__  __;         ')
        print ('                     ')
        print ('   toilet paper      ')
    
    if (name == "elonsrocket"):
        print ('              /  \             ')
        print ('            /      \           ')
        print ('          /          \         ')
        print ('         |     /\     |        ')
        print ('         |    /  \    |        ')
        print ('         |   /    \   |        ')
        print ('         |  | (  ) |  |        ')
        print ('    /\   |  |      |  |   /\   ')
        print ('   /  \  |  |      |  |  /  \  ')
        print ('  |----| |  |      |  | |----| ')
        print ('  |    | | /|   .  |\ | |    | ')
        print ('  |    | /  |   .  |  \ |    | ')
        print ('  |    /    |   .  |    \    | ')
        print ('  |  /      |   .  |      \  | ')
        print ('  |/        |   .  |        \| ')
        print (' /   SPACE  |   .  |    X    \ ')
        print ('(          |      |           )')
        print (' |    | |--|      |--| |    |  ')
        print ('  /  \-----/  \/  \-----/  \   ')
        print ('  \///     \//\// /     \///   ')
        print ('   \/       \/  \/       \/    ')
        print ('                               ')
        print ('          Elon rocket          ')

    if (name == "elonmusk"):
        print ('   ////^///\    ')
        print ('   | ^   ^ |   ')
        print ('  @ (o) (o) @  ')
        print ('   |   <   |   ')
        print ('   |  ___  |   ')
        print ('    \_____/    ')
        print ('               ')
        print ('   Elon Musk   ')
    
    if (name == "flyingalien"):
        print ('             ,-"     "-.              ')
        print ('            / o       o \             ')
        print ('           /   \     /   \            ')
        print ('          /     )-"-(     \           ')
        print ('         /     ( 8 8 )     \          ')
        print ('        /       \ " /       \         ')
        print ('       /         )=(         \        ')
        print ('      /   o   .--"-"--.   o   \       ')
        print ('     /    I  /  -   -  \  I    \      ')
        print (' .--(    (_}y/\       /\y{_) )--.     ')
        print (' (    ".___l\/__\_____/__\/l___," )   ')
        print ('  \                              /    ')
        print ('   "-._    o O o O o O o    _,-"      ')
        print ('     `--Y--.___________.--Y--         ')
        print ('        |==.___________.==|           ')
        print ('                                      ')
        print ('            flying alien              ')
    
    if (name == "alienphone"):
        print ('    ___i   ')
        print ('   |---|   ')
        print ('   |[_]|   ')
        print ('   |:::|   ')
        print ('   |:::|   ')
        print ('   `\   \  ')
        print ('     \_=_\ ')
        print ('           ')
        print ('alien phone')

    if (name == "guardingstar"):
        print ('      \  :  /      ')
        print ('   `.____/ \____ . ')
        print ('  _ _\  (8)(8) /_ _')
        print ('     /___    ___\  ')
        print ('      .` \ /  `.   ')
        print ('       /  :  \     ')
        print ('                   ')
        print ('   guarding star   ')
    
    if (name == "compass"):
        print ('       = N =      ')
        print ('    =    |    =   ')
        print ('   W     |     E  ')
        print ('   =     0     =  ')
        print ('    =        =    ')
        print ('       = S =      ')
        print ('                  ')
        print ('      compass     ')
    
    if (name == "title"):
        print ('--------------------------------------------------------------------')
        print ('  _______  _______  _______  ______      ______            _______  ')
        print (' (  ____ \(  ___  )(  ___  )(  __  \    (  ___ \ |\     /|(  ____ \ ')
        print (' | (    \/| (   ) || (   ) || (  \  )   | (   ) )( \   / )| (    \/ ')
        print (' | |      | |   | || |   | || |   ) |   | (__/ /  \ (_) / | (__     ')
        print (' | | ____ | |   | || |   | || |   | |   |  __ (    \   /  |  __)    ')
        print (' | | \_  )| |   | || |   | || |   ) |   | (  \ \    ) (   | (       ')
        print (' | (___) || (___) || (___) || (__/  )   | )___) )   | |   | (____/\ ')
        print (' (_______)(_______)(_______)(______/    |/ \___/    \_/   (_______/ ')
        print ('                                                                    ')
        print ('  _______  _______  _______ _________           _                   ')
        print (' (  ____ \(  ___  )(  ____ )\__   __/|\     /| ( )                  ')
        print (' | (    \/| (   ) || (    )|   ) (   | )   ( | | |                  ')
        print (' | (__    | (___) || (____)|   | |   | (___) | | |                  ')
        print (' |  __)   |  ___  ||     __)   | |   |  ___  | | |                  ')
        print (' | (      | (   ) || (\ (      | |   | (   ) | (_)                  ')
        print (' | (____/\| )   ( || ) \ \__   | |   | )   ( |  _                   ')
        print (' (_______/|/     \||/   \__/   )_(   |/     \| (_)                  ')
        print ('--------------------------------------------------------------------')
    
    if (name == "mars"):
        print ('.         _  .          .          .    +     .          .          .      .')
        print ('      .(_)          .            .            .            .       :        ')
        print ('     .   .      .    .     .     .    .      .   .      . .  .  -+-        .')
        print ('       .           .   .        .           .          /         :  .       ')
        print ('     . .        .  .      /.   .      .    .     .    / .          .    .   ')
        print ('  .  +       .           /     .          .          /      .   .           ')
        print ('   .            .       /         .            .    *   .         .     .   ')
        print ('       .   .      .    *     .     .    .      .   .       .  .      .     .')
        print ('   .            .           .           .           .        .     +  .     ')
        print ('   . .        .  .       .   .      .    .     .     .    .      .   .      ')
        print (' .   +      .       ___/\_._/~~\_...__/\__.._._/~\        .         .   .   ')
        print ('      .      ___.--'                               '---._          .   .    ')
        print ('            /~~\/~\                                      `-/~\_         .   ')
        print (' .       .-'                                                   '-.          ')
        print ('                                                                            ')
        print ('                                Welcome to Mars!                            ')
                                                                         

                            
# Function of each variable 
def gameWon ():
    printGraphic("mars")
    print ("You won!")
    print ("name: " + player ["name"])
    print ("score: " + str(player["score"]))

def gameOver():
        
        printGraphic("elonmusk")

        print ("Game over! Rot on earth!")
        print ("name: " + player ["name"])
        print ("score: " + str(player["score"]))
        return
    
def dyingEarth():
    print ("Everyone on planet earth is panic buying.")
    print ("You have to fight for toilet paper before it runs out")
    print ("ready to fight for toilet paper?")
    printGraphic ("toiletpaper")
    PA = raw_input ("yes or no > ")

    if (PA == "no"):
        print ("would you like to go to Mars?")
        PA = raw_input ("rot on earth or go to mars >")
        if (PA == "rot on earth"):
            gameOver()
        elif (PA == "go to mars"):
            print ("Great! Looks like you get to live another day.")
            rockettoMars()
    if (PA == "yes"):
        print ("You are a fighter!")
        print ("Roll the dice to uncover your faith!")
        raw_input ("press enter> ")
        
        #roll dice to see if player makes it 
        #if dice more than or equal to 5 they win 
        dice = random.randint(1,6)
        print ("You rolled: " + str (dice) + " out of 6. ")

        #player wins, rolls more than 5 (fix this)
        if (dice >= 3 and dice < 6):
            print ("You won the toilet paper contest!")
            print ("People are starting to hate you because you collected 1000 toilet paper. Your life is now threatened.")
            printGraphic ("toiletpaper") 
            player["score"] = int(player["score"]) + 50 
            print ( "Your new score: " + str(player["score"]) ) 
        
        #next move
        PA = raw_input ("stay on earth or go to mars> ")

        #stay on earth
        if (PA == "stay on earth"):
            print ("Earth has officially died. Good bye.")
            gameOver()
        elif (PA == "go to mars"):
            print ("Good choice. You get to live another day!")
            rockettoMars()

        elif (dice < 3):
            print ("Looks like it is not your lucky day.")
            gameOver() 

        
               

# Option 2 to Mars
def rockettoMars():
    printGraphic ("elonsrocket")
    print ("Welcome to Elon's rocket. Looks like you don't have a ticket.")
    print ("Do you want to buy a ticket for $200,000 or steal from your annoying co-worker?")
    PA = raw_input ("buy or steal > ")

    if (PA == "buy"):
        print ("$200,000 is not present in your bank account")
        print ("You can either work for Elon for the rest of your life or steal a ticket")
        PA = raw_input ("work or steal > ")
        if (PA == "work"):
            print ("Elon accepts your offer!")
            print ("Now you and your future kids must work for him. You basically sold your soul to Elon.")
            print ("At least you get a compass. He gives a compass to every employee")
            printGraphic ("compass")
            player["items"].append("compass")
            player["score"] = int(player["score"]) + 50
            print ( "Your new score: " + str(player["score"]) ) 
        print ("Ready for your journey to mars?")
        PA = raw_input ("press enter> ")
        inRocket()

    elif (PA == "steal"):
        print ("Roll the dice to see if you managed to steal.")
        raw_input ("press enter> ")
        
        #roll dice 
        dice = random.randint(1,6)
        print ("You rolled: " + str (dice) + " out of 6. ")

        #player wins, rolls more than 4
        if (dice >= 4 and dice < 6):
            print ("You got a seat on Elon's Rocket!")
            print ("Elon gives every Mars passenger a compass")
            printGraphic ("compass")
            player["items"].append("compass")
            player["score"] = int(player["score"]) + 50
            print ( "Your new score: " + str(player["score"]) ) 
        #Introduce next journey
            print ("Ready for your journey to mars?")
            PA = raw_input ("press enter> ")
            inRocket()
        elif (dice < 4):
            print ("Looks like you failed.")
            gameOver() 
            


# In Elons Rocket
def inRocket():
    print ("You are a true Martian! Welcome to Elon's rocket.")
    print ("oh no, looks like you encountered a flying alien!")
    printGraphic ("flyingalien")
    print ("The flying alien tries to kidnap the passenger on your right.") 
    print ("You need to stop the flying alien!") 
    PA = raw_input ("talk to alien or offer compass> ")  
    if (PA == "talk to alien"):
        print ("The alien just wanted someone to talk to.Now you have a new friend!")
        print ("The alien offers you a phone so you can keep in touch.")
        printGraphic ("alienphone")
        player["items"].append("alienphone") 
        player["score"] = int(player["score"]) + 50 
        print ( "Your new score: " + str(player["score"]) ) 

        # Introduce next journey
        print ("You're about to land on mars")
        PA = raw_input ("press enter> ")
        onMars() 

    elif (PA == "offer compass"):
        print ("The alien throws your compass.")
        print ("Elon finds out you aren't a loyal Martian.")
        print ("He kicks you out of the rocket...")
        gameOver()
    
# Land on Mars
def onMars():
    print ("You are truly a trooper! You have landed on Mars.")
    print ("In order to enter the Mars city, you have to go through the guarding star!")
    printGraphic ("guardingstar")
    print ("You can only pass through if you have a friend.")
    PA = raw_input ("call alien friend or fight star> ")
    if (PA == "call alien friend"):
        print ("Your alien friend picks up!")
        print ("The gaurding star lets your cross over.")
        player["score"] = int(player["score"]) + 100 
        print ( "Your new score: " + str(player["score"]) ) 
        print ("Mars is truly utopian. Now your life truly begins...")
        gameWon()
    
    elif (PA == "fight star"):
        print ("The star has an army.")
        print ("There's no way you are winning. Goodbye " + player ["name"] + " ... ")
        gameOver()



# Story Starts 
def introStory():
    print ("Welcome to Goodbye Earth! What is your name?")
    player ["name"] = raw_input ("Please let us know your name > ")

    #story Intro
    print ("Welcome to Goodbye Earth " + player["name"] + "! ")
    print ("The year is 2021. Due to global warming, the earth is dying.")
    print ("We all knew this was coming but the only person that planned it well was Elon.")
    print ("Yes, Elon Musk. The billionaire that sold flamethrowers and Teslas.")
    print ("You can either stay on earth and die with it or move to Mars on Elon's rocket.")
    print ("Do you stay on earth or buy a ticket to mars?")

    PA = raw_input ("Please choose earth or mars > ")

    #player decide earth or mars
    if (PA == "earth"):
        print ("Good luck on earth. Now you have to fight for toilet paper to survive.")
        raw_input ("press enter > ")
        dyingEarth()
    elif (PA == "mars"):
        print ("Good choice! Get ready for the adventure to Mars.")
        raw_input ("press enter > ")
        rockettoMars()

# Game starts with this 
def main():
    printGraphic ("title")
    introStory()

main()
