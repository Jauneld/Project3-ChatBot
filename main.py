import random #imports the library random

phases = ["That's cool." , "Wow, so stylish!", "Timeless.", "Trendy!", "Absolutely breathtaking!", "It's so good :]"]#creates a list of pharses to be used in the if statement
casualClothes = random.choice(["T-shirts" , "jeans", "sneakers" , "sweats" , "pj pants", "crocs"])#creates a list of casual clothes that will be chosen at random.
formal = random.choice(["suit" , "dress" , "Jacket and tie"])#creates a list of formal clothes that will be chosen at random.

fName = input("Hello user. What is your first name? ")#Ask user to put a name
print("Welcome to your fashion guru " + fName + ".")#Welcomes the user 


style = input("What is your style " + fName + "? Is it statement making, or casual? ")#Ask the user if they would like a casual or formal outfit. 



if style == "statement making" or style == "Statement Making" or style == "statement Making" or style == "Statement making" or style == "formal" or style == "Formal":
     styleChoice = style
     print(styleChoice + " is so in now. Let's get ready")
else:
     if style == "casual" or style == "chill" or style == "Casual" or style == "normal":
         styleChoice = style
         print(styleChoice + " is so cool. Let's get ready")



styleChoice = style
age = int(input("How old are you " + fName + "? "))#Age input

if age <= 12:
    print()
    print("Wow so young and already thinking about fashion. " + phases[random.randint(0,5)])
elif age >= 13 and age <= 18:
    print()
    print("This is your time to make your fashion make a mark in the world. ")
    print(phases[random.randint(0,5)])
elif age > 18 and age < 55:
    print()
    print("Keep doing your thing")
else:
    print("Its never to late to change it up.\n")
    print(phases[random.randint(0,5)])
    print()

if styleChoice == "casual" or styleChoice == "chill" or styleChoice == "Casual" or styleChoice == "normal":
    print()
    Option1 = input("I think a " + casualClothes + " would be a good fit. What do you think? ")
    if Option1 == "yes" or Option1 == "✓" or Option1 == "y" or Option1 == "Yes" or Option1 == "YES" :
        print()
        print("Great. Glad we're on the same page. What accessory do you want? ")
        acces = input("")
        print("A " + acces + " would be so cool.")
        yesShoes = input("What cool things will you put on your feet? ")
        print(fName + ", " + yesShoes + " will pair well with a " + acces + ".")
        print("You made an amazing outfit.")
        rateYes = int(input("Rate my service from 1 - 10. 10 being the best."))
        if rateYes >= 8:
            print("Wow! Thanks " + fName + " for such a high rating. See you soon. :)")
        elif rateYes < 8 and rateYes >= 5:
           print("Thanks for the feedback " + fName + ". Hope I can earn a better rating next time. Bye " + fName + ".")
        else:
            print("I thought I did a good job but I guess I didn't. Hope I will be better. Bye " + fName + ".")
    elif Option1 == "no" or Option1 == "x" or Option1 == "n" or Option1 == "No" or Option1 == "NO":
        print()
        print("Well then. You tell me what you want.")
        alt1 = input("")
        print(alt1 , "is a good subtitute.")
        anotherClothes = input("What accesories would you add " + fName + "?")
        print(phases[random.randint(0,5)])
        noShoes = input("What cool things will you put on your feet?")
        print(fName + " " + noShoes + " will pair well with " + anotherClothes + ".")
        print("You made an amazing outfit.")
        rateNo = int(input("Rate my service from 1 - 10. 10 being the best."))
        if rateNo >= 8:
            print("Wow! Thanks " + fName + " for such a high rating. See you soon. :)")
        elif rateNo < 8 and rateNo >= 5:
            print("Thanks for the feedback " + fName + ". Hope I can earn a better rating next time. Bye " + fName + ".")
        else:
            print("I thought I did a good job but I guess I didn't. Hope I will be better. Bye " + fName + ".")
    else:
        print("Lets move on to what you would like to add to the outfit " + fName + ".")
        unknownBottomClothes = input("What do you like for the bottom ?")
        print(unknownBottomClothes + " is good.")
        unknownAcces = input("What accessory do you want?")
        print(phases[random.randint(0,5)])
        unknownShoes = input("What cool things will you put on your feet?")
        print(fName + " " + unknownShoes + " will pair well with" + unknownAcces + ".")
        rateUnknown = int(input("Rate my service from 1 - 10. 10 being the best."))
        if rateUnknown >= 8:
            print("Wow! Thanks " + fName + " for such a high rating. See you soon. :)")
        elif rateUnknown < 8 and rateUnknown >= 5:
           print("Thanks for the feedback " + fName + ". Hope I can earn a better rating next time. Bye " + fName + ".")
        else:
            print("I thought I did a good job but I guess I didn't. Hope I will be better. Bye " + fName + ".")


if style == "statement making" or style == "Statement Making" or style == "statement Making" or style == "Statement making" or style == "formal" or style == "Formal":
    Option2 = input("I think a " + formal + " would be a good fit. What do you think? ")
    if Option2 == "yes" or Option2 == "✓" or Option2 == "y" or Option2 == "Yes" or Option2 == "YES" :
        print()
        print("Great. Glad we're on the same page. What accessory do you want?")
        accesFormYes = input("")
        print("A " + accesFormYes + " would be so cool.")
        formYesShoes = input("What cool things will you put on your feet?")
        print(fName + ", " + formYesShoes + " will pair well with a " + accesFormYes + ".")
        print("You made an amazing outfit.")
        formRateYes = int(input("Rate my service from 1 - 10. 10 being the best."))
        if formRateYes >= 8:
            print("Wow! Thanks " + fName + " for such a high rating. See you soon. :)")
        elif formRateYes < 8 and formRateYes >= 5:
           print("Thanks for the feedback " + fName + ". Hope I can earn a better rating next time. Bye " + fName + ".")
        else:
            print("I thought I did a good job but I guess I didn't. Hope I will be better. Bye " + fName + ".")
    elif Option2 == "no" or Option2 == "x" or Option2 == "n" or Option2 == "No" or Option2 == "NO":
        print()
        print("Well then. You tell me what you want.")
        alt1Form = input("")
        print("A " + alt1Form , "is a good subtitute.")
        anotherFormClothes = input("What accesories would you add " + fName + "? ")
        print(phases[random.randint(0,5)])
        noShoesForm = input("What cool things will you put on your feet?")
        print(fName + " " +  noShoesForm  + " will pair well with your " + anotherFormClothes + ".")
        print("You made an amazing outfit.")
        rateNoForm = int(input("Rate my service from 1 - 10. 10 being the best."))
        if rateNoForm >= 8:
            print("Wow! Thanks " + fName + " for such a high rating. See you soon. :)")
        elif rateNoForm < 8 and rateNoForm >= 5:
           print("Thanks for the feedback " + fName + ". Hope I can earn a better rating next time. Bye " + fName + ".")
        else:
            print("I thought I did a good job but I guess I didn't. Hope I will be better. Bye " + fName + ".")
    else:
        print("Lets move on to what you would like to add to the outfit " + fName + ".")
        unknownBottomClothesForm = input("What do you like for the bottom ?")
        print(unknownBottomClothesForm + " is good.")
        unknownAccesForm = input("What accessory do you want?")
        print(phases[random.randint(0,5)])
        unknownShoesForm = input("What cool things will you put on your feet?")
        print(fName + " " + unknownShoesForm + " will pair well with" + unknownAccesForm + ".")
        rateUnknownForm = int(input("Rate my service from 1 - 10. 10 being the best."))
        if rateUnknownForm >= 8:
            print("Wow! Thanks " + fName + " for such a high rating. See you soon. :)")
        elif rateUnknownForm < 8 and rateUnknownForm >= 5:
           print("Thanks for the feedback " + fName + ". Hope I can earn a better rating next time. Bye " + fName + ".")
        else:
            print("I thought I did a good job but I guess I didn't. Hope I will be better. Bye " + fName + ".")