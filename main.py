import string
import random
import time
player_hp = 100
mr_j_hp = 500
left = ["left", "l", "Left"]
right = ["right", "Right", "r"]
wrench = ["pickup wrench", "wrench", "Wrench", "Pickup Wrench"]
shop = ["shop", "Shop", "You see the shop as your next destination", "You stumble across to the shop",]
tower = ["Tower", "tower", "go to tower"]
burger = ["burger", "take burger", "take it", "yes", "Yes"]
john_cena = ["John cena", "John Cena", "john cena"]
spronken = ["spronken", "Spronken", "Walk to spronken", "walk to spronken"]
john_cena_burger = ["give", "burger", "give burger", "Give", "Burger"]
spronken_wrench = ["give", "give wrench", "yes", "Yes"]
right_talk = ["You come to see a garden with a towe at the centre. There is a wrench on the ground, and a you can see a small shop next to one of the trees in the garden."
              , "You pickup the wrench.", "After you pickup the wrench you walk over to the mysterious shop. It seems to be a hamburger shop.", "You take the burger.",
              "You walk over to the mysterious shop. It seems to be a hamburger shop.",
              "Once you decide to go down the alley way that was adjacent to the burger shop. It leads you down a long and dark path, soon coming to a building with a security guard outside."
              , "You come to realize that the securtiy guard is actually the John Cena.", "There is also a bearded spronken laying on the ground, infront of a tall gate"
              , "You walk over to John Cena.", "What's up small fry, Bing chilling, quo ou yaoh bing chilling?", "looks like he wants a burger if you want to pass."
              , "Thanks for the Ham burger, bing chilling pass.", "You go into the buildiing guarded by John Cena.", "Hello there young chap, you got a wrench I could use to get into this gat over here?"
              , "You hand the Spronken your wrench", "Spronken opens the lock and leads you to a door in the back of a room", "Welcome my bingchlling friend, you are free here in this land of tranquil.", "You enter through the door that John Cena was guarding, and you find yourself in a room filled with hundreds upon hundreds of people, each on cheering out, or atleast thats what yiu can hear.", "The room continues on, theres a passageway that leads to light, you enter through the passageway tpo find a ring with the marks WWE on its side, you realiseze that you are in a WWE stand, with many spectators, hungry for action.", "you see a man in the ring, he looks over to you, and raises his eyebrow menacingly, its THE ROCK JOHHNSON!!!!"
              , "Attack the rock?", "You enter through the small opening, the door is pretty small after all, and you go through, leading you to the another door to a buidling.", "You enter the building that leads you to a disco, looks like a man is standing at the middle, dancing his life away.", "You come to see the man's face, you instatly recognise him as DR MUNDO FROM LEAGUE OF LEGENDS!!",
              "Attack Dr Mundo?"]

left_talk = ["You go down the left path, taking you to a slide that loops around itself, creating an optical illusion.", "You exit the slide into a rocky biome with a danger sign",
              "You see a steel sword infront of you.", "You take the steel sword infront of you", "It seems that a huge crater can be seen infront of you, at the centre you see a tall menacing man, you can't quite make him out but you can sense that he means trouble.",
             "You stand infront of the man, he's wearing a name tag, you read it out as 'Mr. Jones'. You are instantly filled with terror, as you read the name, for some odd reason.",
             "You cannot enter there yet, you are not powerful enough. You decide to instead walk to the shop."]
bf = ["You enter battle with MR. Jones.", "[Mr. Jones | HP 500]", "You | HP 100", "You attack Mr.Jones with a swooping swing of your sword.",
      "Mr.Jones Clubs you with his metal kanaboa.", "You perfect roll the attack, rendering it useless.", "You enter battle with DWAYNE THE ROCK JOHNSON!!!", "[DWAYNE THE ROCK JOHNSON! | HP 500]"
      , "You slam DWAYNE THE ROCK JOHNSON!", "DWAYNE THE ROCK JOHNSON does his signature move, THE ROCK BOTTOM!!!! on you.", "You enter battle with Dr Mundo."
      , "[Dr Mundo | HP 500]", "You attack Dr Mundo with a fierce punch", "Dr Mundo uses his club to hit you"]
sword = ["Sword", "sword", "take the sword", "take", "take it", "yes", "Yes", "yessirrr", "You die, foolishly", "You vanquish the Boss named Mr.Jones, and plunder his pockets of all the booty your hands can grab [ENDING 1/3]", "You vanquish the Boss named DWAYNE THE ROCK JOHNSON!!!! and achieve the gratest of great endiings. [ENDING 2/3]"]
yes_no = ["Yes", "yes", "No", "no", "Take", "take", "take it", "Take it", "Pickup", "pickup", "give", "Give", "Give burger", "give burger"]
attack = ["Attack", "attack", "Mr.Jones takes", "You take", "DWAYNE THE ROCK JOHNSON takes"]
block = ["Block", "block", "You don't have a shield idiot"]
flee = ["Flee", "flee", "You forget how to run"]
Inventory = []
#lists are called when you use the brackets [] and in the newer version you always need (), But I
#didn't put them in because they work on the school computers.'
#I used various numbers and amounts of lists, I did this because I found it easier to use than functions.
#I call the lists when I am using dialogue or when the system is telling you something, or when the
#narrator is announcing a problem or question.
print("Welcome traveler, go right or left?")



#LEFT PATH
# I have while true's here so I can see if something goes wrong, and that there will be no errors.
#This is a good and siple way to execute 'full proof' codes.
while True:
    try:
        c1 = raw_input("left or right")
        if c1 not in left and c1 not in right:
            print("something went wrong try again")
        else:
            break
    except ValueError:
        print("Joe")


if c1 in left:
    print("you go left")
if c1 in left:
    print left_talk[0]
    print left_talk[1]
    print left_talk[2]
    while True:
        try:
            c1_biome = raw_input("Take the steel sword?")
            if c1_biome not in sword and c1_biome not in yes_no:
                print("something went wrong try again")
            else:
                break
        except ValueError:
            print("joe")


    if c1_biome in sword:
        print left_talk[3]
        print left_talk[4]
        c2_biome = raw_input("Walk over to the menacing man and get ready to face him in battle?")
        if c2_biome in yes_no:
            print left_talk[5]
            bf_1 = raw_input("Attack Mr. Jones?")
            if bf_1 in yes_no:
                print bf[0]
                print bf[1]
                print bf[2]
#This is a boos fight sysytem, mainly based off of the early adventure and rpg games, such as
# pokemon and etc.
#I also took inspiration from elden ring, just mainly the boss part though, and I took inspiration
# from undertale with the whole Attack and block system.
        while True:
                bf_1 = raw_input("Attack | Flee | Block")
                if bf_1 in attack:
                    print bf[3]
                    player_damage = random.randint(10, 90)
                    mr_j_hp = mr_j_hp - player_damage
                    print attack[2], player_damage, "damage"
                    print mr_j_hp, "HP"

                if bf_1 in block:
                        print block[2]

                if bf_1 in flee:
                        print flee[2]

                if bf_1 in attack:
                    print bf[4]
                    mr_j_damage = random.randint(10, 200)
                    if mr_j_damage >= 90:
                        print bf[5]
                    else:
                        player_hp = player_hp - mr_j_damage
                        print attack[3], mr_j_damage, "damage"
                        print player_hp, "HP"
                        if mr_j_hp <=0:
                            print sword[9]
                            break
                        if player_hp <=0:
                            print sword[8]
                            break
                            exit()






#This is the start of the right path, I have the paths in different sections because it takes less
# time to organise and they look better in seperate forms.



#RIGHT PATH
if c1 in right:
    print("you go right")
    if c1 in right:
        print right_talk[0]
        while True:
            try:
                c2 = raw_input("Pickup wrench? Walk to tower? See the shop?")
                if c2 in wrench:
                    print right_talk[1]
                    if c2 not in wrench:
                            print("something went wrong try again")
                    else:
                        break
                elif c2 in tower:
                    print left_talk[6]
                    break
                elif c2 in shop:
                    print right_talk[2]
                    break
            except ValueError:
                print("joe")

if c2 in wrench:
    Inventory.append("Wrenches (1)")
    print Inventory
if c2 in wrench:
    print right_talk[2]

if c2 in wrench:
    print shop[3]

if c2 in shop:
    print right_talk[4]
    while True:
        try:
            c2_shop = raw_input("Shop owner: Hello young man, care to take a free burger?")
            if c2_shop not in burger:
                print("something went wrong try again")
            else:
                break
        except ValueError:
            print("joe")
#I use raw inputs, and use while true's at the start of every raw input, because I did not
# input time.sleep, which would have made the game slower and harder to code.
#I also didn't use the import time.sleep because of how the code was designed to use.
#As you can also see here I have a three way system, where if you choose one action it can change the
#outcome of future actions.
    if c2_shop not in c2_shop:
        if c2_shop in burger:
            print right_talk[3]
        if c2_shop in burger:
            Inventory.append("Burgers (1)")
            print Inventory
        if c2_shop in burger:
            print right_talk[5]
            print right_talk[6]
            print right_talk[7]
            c3_john_cena = raw_input("Walk to John Cena or Walk to the Spronken?")
            if c3_john_cena in john_cena:
                print right_talk[8]
            if c3_john_cena in john_cena:
                print right_talk[9]
                print right_talk[10]
            if c3_john_cena in john_cena_burger:
                print right_talk[11]
                print right_talk[12]

            if c3_john_cena in spronken:
                print right_talk[13]
                c3_spronken = raw_input("Give him the wrench?")
                if c3_spronken in spronken_wrench:
                    print right_talk[14]


if shop[3] in shop:
    print
    c2_shop2 = raw_input("Shop onwer: Hello young man, care to take a free burger?")
    if c2_shop2 in burger:
        print right_talk[3]
    if c2_shop2 in burger:
        Inventory.append("Burgers (1)")
        print Inventory
        if c2_shop2 in burger:
            print right_talk[5]
            print right_talk[6]
            print right_talk[7]
            while True:
                try:
                    c3_john_cena = raw_input("Walk to John Cena or Walk to the Spronken?")
                    if c3_john_cena not in john_cena and c3_john_cena not in spronken:
                         print("something went wrong try again")
                    elif c3_john_cena in spronken:
                        print("you walk to spronken")
                        break
                    else:
                        break
                except ValueError:
                    print("joe")

            if c3_john_cena in spronken:
                print right_talk[13]
                while True:
                    try:
                        c3_spronken = raw_input("Give him the wrench?")
                        if c3_spronken not in spronken_wrench:
                            print ("something went wrong try again")
                        if c3_spronken not in spronken_wrench:
                            print right_talk[14]
                        else:
                            break
                    except ValueError:
                        print("joe")

                if c3_spronken in spronken_wrench:
                    print right_talk[15]

                c4_spronken = raw_input("Enter through the door?")
                print right_talk[20]
                print right_talk[21]
                print right_talk[22]
                while True:
                    try:
                        dr_mundo = raw_input("Talk to Dr Mundo?")
                        if dr_mundo not in yes_no:
                            print("something went wrong try again")
                        if dr_mundo in yes_no:
                            print bf[10]
                        else:
                            break
                    except ValueError:
                        print("joe")

                print("You know, its been really hard in the ring, I really would like a break, can you pass me that towel over there?")
                while True:
                    try:
                        towel = raw_input("Get the towel?")
                        if towel not in yes_no:
                            print("Just go get him the towel man.. stop being so hard..")
                        if towel in yes_no:
                            print("You get the towel and give it to Dr Mundo")
                        else:
                            break
                    except ValueError:
                        print("joe")

                print("Thanks man, you're a real chap you know!")
                print("Here, take this leave game card")
                print("[ENDINGS 3/3]")
                exit()

#As you can see this one of the many endings you can get, and this was the third one, where you had
#to stop using violence as a way to defeat all the bosses, and use kindness to help Dr Mundo out.
#And from the rest on, it is just a repeat of codes that I explained up top.




            if c3_john_cena in john_cena:
                print right_talk[8]
            if c3_john_cena in john_cena:
                print right_talk[9]
                print right_talk[10]
            if c3_john_cena in john_cena_burger:
                print right_talk[11]
                print right_talk[12]
            while True:
                try:
                    c4_john_cena = raw_input("Hand him the burger you got form the burger shop?")
                    if c4_john_cena in yes_no:
                        Inventory.remove("Burgers (1)")
                        print Inventory
                        print right_talk[16]
                        print right_talk[17]
                        print right_talk[18]
                        print right_talk[19]
                    if c4_john_cena not in yes_no:
                        print("something went wrong try again")
                    else:
                        break

                except ValueError:
                    print("joe")
            while True:
                try:
                    bf_2 = raw_input("Attack DWAYNE THE ROCK JOHNSON??!!!")
                    if bf_2 in yes_no:
                        print bf[6]
                        print bf[7]
                    if bf_2 not in yes_no:
                        print("something went wrong try again")
                    else:
                        break
                except ValueError:
                    print("joe")

            while True:
                bf_2 = raw_input("Attack | Flee | Block")
                if bf_2 in attack:
                    print bf[8]
                    player_damage = random.randint(10, 90)
                    mr_j_hp = mr_j_hp - player_damage
                    print attack[4], player_damage, "damage"
                    print mr_j_hp, "HP"

                if bf_2 in block:
                    print block[2]

                if bf_2 in flee:
                    print flee[2]

                if bf_2 in attack:
                    print bf[9]
                    mr_j_damage = random.randint(10, 200)
                    if mr_j_damage >= 90:
                        print bf[5]
                    else:
                        player_hp = player_hp - mr_j_damage
                        print attack[3], mr_j_damage, "damage"
                        print player_hp, "HP"
                        if mr_j_hp <= 0:
                            print sword[10]
                            break
                            print("Hey you beat the game, nice, And you took down THE ROCK JONHSONNNN")
                            exit()
                        if player_hp <= 0:
                            print sword[8]
                            break
                            exit()




        if c3_john_cena in spronken:
            print right_talk[13]
            while True:
                try:
                    c3_spronken = raw_input("Give him the wrench?")
                    if c3_spronken in spronken_wrench:
                        print right_talk[14]
                    if c3_spronken not in spronken_wrench:
                         print("something went wrong try again")
                    else:
                        break
                except ValueError:
                    print("joe")


                if c3_spronken in spronken_wrench:
                    print right_talk[15]


                c4_spronken = raw_input("Enter through the door?")
                print right_talk[20]
                print right_talk[21]
                print right_talk[22]

