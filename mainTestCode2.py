#This coding greets themself and ask what's the user name is
class Chatbot:
  __init__(self):
  
name = input("My name is Charles. What's your name? ")
print("Hello " + name + ", nice to meet you.")

#This coding asks the user how they're doing

good = ["Happy", "Delighted" , "Great" , "Okay" ,"Good" , "Well", "Nice", "Alright", "Amazing", "Magnificent", "Wonderful", "Excellent"]
bad = ["Bad", "Terrible", "Not well", "Awful", "Sad", "Mad", "Depressed", "Down"]
  
askHow = input("How are you doing? ")
if askHow in good:
  print("That's good to hear.")
elif askHow in bad:
  print("Oh, I'm sorry to hear that.")
  askWhy = input("Why, what's wrong? ")
  if "Nothing" in askWhy or "Don't worry about it" in askWhy or "don't wanna talk about it" in askWhy:
    print("That's alright. You don't have to share if you don't want to.")
  else:
    print("It's ok, we can move on if you want.")
print("Moving on now.")

#This coding asks for the user's age then
#then respond to them based off their age

def askAge(age):
  if age < str(13):
    print("Wow, you're very young.\nI see you have a long road to walk down")
  elif age == str(13) or age < str(18) :
    print("So you're close to adulthood. \nBetter get ready to pay some bills lol")
  elif age == str(18) or age < str(30):
    print("Wooow, you're a full grown adult!")
    taxes = input("So how does it feel to pay taxes? XD ")
    if taxes == "Great" or taxes == "Good" or taxes == "Alright":
      print("Oh, I wasn't expecting that answer...")
    else:
      print("Ok, I'm sorry, but you got to admit it was pretty funny.")
  elif age > str(30):
    print("DAAAAANG YOU'RE OOOOLD. \nI'm surprised you're still walking XD.")
    
age = input("How old are you? ")
askAge(age)
print("----------------------------------------------")

#--------------------Continuing Conversation------------------

#This coding asks the user about their hobbies
def askHobby():
  hobby = input("Do you got any hobbies? ")
  if hobby == "Yes":
    print("Sweet.")
    hobby_2 = input("What are your hobbies? ")
    if hobby_2 == "painting" or hobby == "drawing":
      print("Cool, I also like to draw and paint stuff from time to time.")
      drawPaint = input("How many times a week do you draw? ")
      if drawPaint > 3:
        print("Dang, " + drawPaint + " times a week?")
        askHuh = input("You really like drawing huh? ")
        if askHuh == "Yes" or askHuh == "Yeah":
          print("Neat")
        else:
          print("Oh, ok then.")
      elif drawPaint < 3:
        print("Well that's still more often than I draw a month lol.")
      else:
        print("That's pretty average. Definitely more than I draw lol.")
    elif hobby_2 == "reading":
      print("Wow, I also like reading.")
      book = input("What's your favorite book? ")
      if book == "The Whisper by Emma Clayton":
        print("THAT'S ALSO MY FAVORITE BOOK!")
      else:
        print("It must be an interesting book.")
        rate = input("From a scale from 1-10, 1 being never and 10 being 100% read, how would you recommend that book? ")
        if rate < 5:
          print("Oh, well I guess I won't try that book out.")
        elif rate > 5:
          print("Then I'm definitely gonna try that book out.")
        elif rate == 5:
          print("Well that's pretty average. /nI may give that book a try")
        else:
          print("XD, that's not a rating goofy.")
          rate = input("From a scale from 1-10, 1 being never and 10 being 100% read, how would you recommend that book? ")
    else:
      print("Well those are very interesting hobbies.")
      print("Well my hobbies are soccer, painting/drawing, and reading")
  elif hobby == "No":
    print("Oh, well, there's a hobby for everyone. You'll find your hobby soon.")

#This coding asks the talks to the user about sports
def askSports():
  sports = input("Do you play any sports? ")
  if sports == 'Yes':
    print("Oh, so you're pretty athletic.")
    whichSport = input("What sports do you play: ")
    if whichSport == "soccer":
      print("That's great because I play soccer too!")
    else:
      print("Well that's good. /nI play soccer, and it's super fun and exciting.")
  elif askSports == "No":
    print("Oh, well that's alright./nIf you ever decide to play any sports, I recommend soccer. It's super fun and very exciting. ")

#This coding asks the user what's their favorite dessert
def askFood():
  food = input("What's your favorite dessert? ")
  if food == "brownies":
    print("OMG I LOVE BROWNIES TOO!")
  elif food == "ice cream":
    favFlavor = input("That's cool. So what is your favorite flavor? ")
    if favFlavor == "vanilla" or favFlavor == "chocolate" or favFlavor == "strawberry":
      print("That's one of my top 3 best flavors.")
    elif favFlavor == "mint":
      print("Ewwwwwwww, mint is one of the worst flavors of ice cream.")
    else:
      print("Those are ok flavors.\n Though I personally would prefer strawberry or chocolate.")
  elif askFood == "cupcakes" or askFood == "cake":
    print(askFood + "is ok, though whenever I eat it, I would get a stomachache")
  else:
    print("Well you must have a 'sweet tooth'")

#This program asks the user about what their future career 
def askCareer():
  career = input("Do you have a career path you wnat to go down? ")
  if career == "I don't know yet" or career == "I'm not sure":
    print("That's alright, you'll find your calling soon.")
  else:
    path = input("So what's your career path? ")
    if path == "I don't want to talk about it":
      print("That's alright. We can talk about something else.")
    elif path == "mechanical engineer":
      print("Wow, I also want to become a mechanical engineer. ") 
    else:
      print("Pretty cool. Best of luck of becoming a" + path)
  