#!/usr/bin/python

import os

import time

def clear(text=None):
  os.system("clear")
  if text:
    print text

def entercont():
  print "<<<PRESS ENTER TO CONTINUE>>>"
  raw_input()
      
def userinput(text, reply):
  while True:
    clear()
    answer = raw_input(text)
    if answer:
      return answer
      pause()
    else:
      print reply
      entercont()
           
pause=raw_input

clear()

name = userinput("Grot: What is your name?  \n", "Grot: You probably didn't hear me there, kiddo. I'm going to assume you didn't; this isn't a meritocracy, you answer your betters when they ask you a question. Don't test me.\n")

print "Grot: Hello", name

pause()

print "Grot: I am going to need your help.\n"

entercont()

device = userinput("Grot: Do you know how to use a Medrigal Inflictor? \n", "Grot: My patience has a limit. If you refuse to answer me, the next inmate in this cell will have your charred bones for company. I shall ask you one more time:\n")

if device.lower() == "yes": 
  print "Grot: Alright then. I'll get right on with it then.\n"
else:
  print "Grot: You clearly have no idea what I'm talking about, so I'll just give you the low down before I leave you to it.\n"
  entercont()
  print "Grot: The dial should always be between 4 and 5; if it gets any lower, you need to pull this lever and twist this knob. If it goes any higher, you need to move your foot off that pedal completely. Also watch the temperature...\n"
  entercont()
  print "(This monologue continues for several hours before Grot, finally satisfied that you can learn no more about the Medrigal Inflictor, returns to his questioning)\n" 
  entercont()

clear()

print "Grot: I have work to do now. You've kept me away from it for long enough. Look on the bright side: if you focus all your energy on the task, your twenty years of hard labour will only seem like ten!\n"

entercont()

print "(Grot leaves, chuckling as he slams the heavy iron door behind him. The heat of the furnace powering the Medrigal Inflictor has left a film of sweat on your brow; you have not started work on the inflictor yet, and you have no intention of starting. First you need to escape.\n)"

entercont()

print "In front of you, the Medrigal Inflictor steams and bellows; its knobs, levers and pedals move of their own accord, as if some vengeful poltergeist were thoughtfully doing your job for you. A spartan wooden chair sits to the left of the room. What little light there is comes from a greasy pain of glass situated far above the door. There is no way you can squeeze through it. The door is heavy and iron, bolted from the other side.\n"

responses = {
  "lever": "If what Grot said was true, pulling this lever will increase the core temperature of the Medrigal Inflictor. Here goes nothing...\n",
  "pedal": "The pedal won't budge\n",
  "knob": "Turning this knob will release the steam into the central valve of the Inflictor; if the tempurate is high enough, it will cause a meltdown. Let's see what happens...\n",
  "chair": "What do you expect me to do with that? Please be serious\n",
  "door": "It's locked. I already told you that.\n",
  "medrigal": "It looks like an outdated piece of junk. Maybe if I can get it to blow, I'll be able to get out of here. I could be killed in the process, but I'd prefer that to Grot's lectures for the next twenty years. The hard labour doesn't sound like much fun either.\n",
  "window": "It's a window.\n"
}

responses["inflictor"] = responses["machine"] = responses["medrigal inflictor"] = responses["medrigal"]

responses["glass"] = responses["pane"] = responses["window"]

leverturn = False
knobturn = False

kaboom = """


          |\ 
          | \  
          |  \                  /
          |   \          /|    //\\
          | |\ \        / |   //  \\
          | | \ \      /  |  //    \\
          | |  \ \    / /|| //      \\
__________| |   \ \  / / ||//        \\_________
\  _______       \ \/ /  ||/           ---------/        
 \ \              \  /   |/                   //
  \ \              \/                        //
   \ \     /\    KABOOM!!!      ||\\        //
    \ \   //\\            /\    || \\      //
    ||/  //  \\          //\\   ||  \\    //
    ||  //    \\        //  \\  ||   \\  //
    || //      \\      //    \\ ||    \\//
    ||//        \\    //      \\||     \/   
    ||/          \\  //        \||
    |/            \\//          \|
                   \/        
                   
"""




terminalscreen = """

    _    ____ ____ _____ ____ ____    ____  _____ _   _ ___ _____ ____  
   / \  / ___/ ___| ____/ ___/ ___|  |  _ \| ____| \ | |_ _| ____|  _ \ 
  / _ \| |  | |   |  _| \___ \___ \  | | | |  _| |  \| || ||  _| | | | |
 / ___ \ |__| |___| |___ ___) |__) | | |_| | |___| |\  || || |___| |_| |
/_/   \_\____\____|_____|____/____/  |____/|_____|_| \_|___|_____|____/ 
                                                                        
 ____   _    ____ ____   ____    _    ____  ____  
|  _ \ / \  / ___/ ___| / ___|  / \  |  _ \|  _ \ 
| |_) / _ \ \___ \___ \| |     / _ \ | |_) | | | |
|  __/ ___ \ ___) |__) | |___ / ___ \|  _ <| |_| |
|_| /_/   \_\____/____/ \____/_/   \_\_| \_\____/ 
                                                  
 ____  _____ ___  _   _ ___ ____  _____ ____  
|  _ \| ____/ _ \| | | |_ _|  _ \| ____|  _ \ 
| |_) |  _|| | | | | | || || |_) |  _| | | | |
|  _ <| |__| |_| | |_| || ||  _ <| |___| |_| |
|_| \_\_____\__\_\\___/|___|_| \_\_____|____/ 


"""

terminalscreen2 = """

                                                     _           _ 
  __ _  ___ ___ ___  ___ ___    __ _ _ __ __ _ _ __ | |_ ___  __| |
 / _` |/ __/ __/ _ \/ __/ __|  / _` | '__/ _` | '_ \| __/ _ \/ _` |
| (_| | (_| (_|  __/\__ \__ \ | (_| | | | (_| | | | | ||  __/ (_| |
 \__,_|\___\___\___||___/___/  \__, |_|  \__,_|_| |_|\__\___|\__,_|
                               |___/      

       
"""

rbinterface = """
__        _______ _     ____ ___  __  __ _____   _____ ___  
\ \      / / ____| |   / ___/ _ \|  \/  | ____| |_   _/ _ \ 
 \ \ /\ / /|  _| | |  | |  | | | | |\/| |  _|     | || | | |
  \ V  V / | |___| |__| |__| |_| | |  | | |___    | || |_| |
   \_/\_/  |_____|_____\____\___/|_|  |_|_____|   |_| \___/ 
                                                            
 ____   ___  ____   ___ _____ 
|  _ \ / _ \| __ ) / _ \_   _|
| |_) | | | |  _ \| | | || |  
|  _ <| |_| | |_) | |_| || |  
|_| \_\\___/|____/ \___/ |_|  
                              
 ___ _   _ _____ _____ ____  _____ _    ____ _____ 
|_ _| \ | |_   _| ____|  _ \|  ___/ \  / ___| ____|
 | ||  \| | | | |  _| | |_) | |_ / _ \| |   |  _|  
 | || |\  | | | | |___|  _ <|  _/ ___ \ |___| |___ 
|___|_| \_| |_| |_____|_| \_\_|/_/   \_\____|_____|
              
"""


rbinterface2 = """
 _   _                                         ___                           
| | | | _____      __  _ __ ___   __ _ _   _  |_ _|  ___  ___ _ ____   _____ 
| |_| |/ _ \ \ /\ / / | '_ ` _ \ / _` | | | |  | |  / __|/ _ \ '__\ \ / / _ \
|  _  | (_) \ V  V /  | | | | | | (_| | |_| |  | |  \__ \  __/ |   \ V /  __/
|_| |_|\___/ \_/\_/   |_| |_| |_|\__,_|\__, | |___| |___/\___|_|    \_/ \___|
                                       |___/                                 
                  ___ 
 _   _  ___  _   |__ \
| | | |/ _ \| | | |/ /
| |_| | (_) | |_| |_| 
 \__, |\___/ \__,_(_) 
 |___/                

"""


while True:
  clear()
  action = raw_input("What would you like to do? If you need a clue, type look to remind yourself of your surroundings.\n")
  action = action.lower()
  if action in responses:
    print responses[action]
    entercont()
  elif action == "look":
    clear("In front of you, the Medrigal Inflictor steams and bellows; its knobs, levers and pedals move of their own accord, as if some vengeful poltergeist were thoughtfully doing your job for you. A spartan wooden chair sits to the left of the room. What little light there is comes from a greasy pain of glass situated far above the door. There is no way you can squeeze through it. The door is heavy and iron, bolted from the other side.\n")
    entercont()
  else:
    print "I'm afraid you're going to have to try harder than that\n"
    entercont()
  if action == "lever":
    leverturn = True
    
  if action == "knob":
    knobturn = True
    
  if leverturn:
    if knobturn:
      clear()
      print kaboom
      break
      
entercont()
      
clear("The Tale of the Dark Sun\n\n\nWritten and Directed by James Alexander Brain\n\nA Python Apocalypse Production\n\nStarring(in order of appearance):\n\n" + name + " as Himself\n\nOlaf McKnight as Grot\n\nTheodore Thane as Oldham\n\n")
      
entercont()

clear()

print "You emerge from the devestated room in a state of shock. The long metalic corridor outside seems unaffected by the colossal explosion that just occured. You can either go left or right.\n"

entercont()

direction = None
seconddirection = None
thirddirection = None
keygot = False
passcardgot = False
door = False
powersupply = False
robotfollow = False
finishsectionone = False

while True:
  if finishsectionone == True:
    break
  clear()
  direction = raw_input("You are in the main corridor. Would you like to go left or right?\n")
  direction = direction.lower()
  if direction:
    
    if direction == "left":
      print "you go left\n"
      entercont()
      print "After solid minutes of walking, you eventually come to three doors. You can either go to the left, right, forward or back to the corridor.\n"
      entercont()
      while True:
        clear()
        seconddirection = raw_input("Would you like to go left, right, forward, or back to the corridor?\n")
        seconddirection = seconddirection.lower()
        if seconddirection == "left":
          print "you go through the left door"
          while True:
            clear()
            leftroomaction = raw_input("There is a set of drawers which appears to be locked. If you had a key, perhaps you could try to unlock it\n")
            if leftroomaction in ["open", "unlock"] and keygot == True:
              clear("The drawer opens with a noise of protest. You wince at the thought that someone may have heard. However, insisde the drawer is a passcard. You take this, and leave the room seeing nothing else of interest.\n")
              passcardgot = True
              entercont()
              break
            if leftroomaction == "back":
              break
            if leftroomaction in ["open", "unlock"] and keygot == False:
              print "The drawer is locked and you do not have the key. Perhaps you should try another room.\n"
              entercont()
              clear()
              break
            
        elif seconddirection == "right":
          if door == False:
            print "the door to the right is locked and you cannot open it\n"
            entercont()
          elif door == True:
            while True:
              clear()
              powersupplyquest = raw_input("You have entered the supply room. What would you like to look for? Note you can type back to return to the corridor.\n")
              powersupplyquest = powersupplyquest.lower()
              if powersupplyquest in ["power", "supply", "powersupply", "power supply", "battery", "part", "flux capacitor"]:
                powersupply = True
                clear("You now have the power supply required to fix the robot. On the side, you notice the words 'Flux Capacitor', but don't trouble yourself as to their meaning.\n")
                entercont()
                break
              if powersupplyquest == "look":
                clear("There are lots of boxes everywhere. Some have initials, such as one close to you with FC written on the side.\n")
                entercont()
              if powersupplyquest == "fc":
                clear("I believe it stands for Flux Capacitor. It's a type of power supply. Perhaps I could use this for something.\n")
                entercont()
              if powersupplyquest == "back":
                break
              if powersupplyquest == None:
                entercont()
              else:
                if powersupplyquest not in ["look", "fc"]:
                  print "I'll just repeat myself to clarify, since you didn't get the hint.\n"
                  entercont()
        elif seconddirection == "forward":
          print "you go through the door infront of you"
          key = None
          while True:
            clear()
            findkey = raw_input("The room seems to be relatively bare; clearly some low level administrator's office. An item of interest catches your eye on the desk...\n")
            if findkey == "desk" or findkey == "table" or findkey == "item":
              key = raw_input("The item seems to be a key. Would you like to pick it up? On one hand, if you do, you could have your hands cut off for stealing. On the other hand, the guards will probably kill you if they catch you anyway.\n")
              if key == "pick" or key == "pick up" or key == "up" or key == "take" or key == "steal" or key == "fuck it" or key == "get" or key == "key" or key == "item":
                clear("You now have a stolen key in your posession. I hope for your sake it is worth the risk you took to steal it. There is nothing left to do in this room so you walk back out.\n")
                keygot = True
                entercont()
                break
              if key == None:
                print "Erring on the side of caution is always a good idea these days.\n"
                entercont()
              else:
                print "Erring on the side of caution is always a good idea these days.\n"
                entercont()
                break
            if findkey == "back":
              break
            else:
              print "Unless you'd like to go back out and try another door, tell me what you want me to do with this item on the desk.\n"
                  
        elif seconddirection == "back" or seconddirection == "corridor":
          print "you go back to the corridor"
          break
        elif seconddirection == "forward":
          clear("You end up back in front of the three doors. Where would you like to go now? (I will take this opportunity to remind you that you can try the left door, the right door, the door infront of you, or go back to the corridor)\n")
        else:
          print "You're trying my patience. I shall have to leave you here if you keep this up; schizophrenia or no."
                   
    if direction == "right":
      clear("You are in the corridor right of the room in which you started.\n")
      entercont()
      print "The tunnel gets narrower and narrower. You eventually come to a pile of debris blocking your path. You noticed a service robot on the way in which could clear this debris, if you could find it. You also passed a security room on the way up.\n"
      entercont()
      while True:
        if finishsectionone == True:
          break
        clear()
        thirddirection = raw_input("Would you like to stay at the pile of debris, go to the security room, or return back to the corridor?\n")
        thirddirection = thirddirection.lower()
        if thirddirection == "pile" or thirddirection == "debris" or thirddirection == "stay" or thirddirection == "pile of debris" or thirddirection == "debris pile":
          print "You stay at the pile of debris"
          if robotfollow == False:
            print "There's nothing here. Feel free to look around though\n"
            while True:
              clear()
              if finishsectionone:
                break
              else:
                if robotfollow == False:
                  redherring1 = raw_input("There's nothing here. Feel free to look around though. Remember that if you are stuck, you can look or go back.\n")
                  redherring1 = redherring1.lower()
                  if redherring1 in ["look", "debris", "do something", "something", "anything", "red", "herring", "red herring", "redherring", "dig", "loot", "use"]:
                    print "I'm telling you, there's nothing here. You should probably leave.\n"
                    entercont()
                  elif redherring1 in ["leave", "back", "give", "up", "give up", "giveup", "go", "exit", "return"]:
                    break
          if robotfollow:
            clear("Now that you have the robot with you, perhaps you can use it to help you escape.\n")
            entercont()
            while True:
              if finishsectionone:
                break
              clear(rbinterface)
              time.sleep(1)
              clear("HOW MAY I SERVE YOU?")
              time.sleep(1)
              clear()
              while True:
                if finishsectionone:
                  break
                robotjob = raw_input("PLEASE TYPE A COMMAND-\n")
                robotjob = robotjob.lower()
                if robotjob in ["work", "escape", "rubble", "debris", "pile", "help", "move"]:
                  finishsectionone = True
                  clear("WORKING-")
                  time.sleep(.2)
                  clear("WORKING--")
                  time.sleep(.2)
                  clear("WORKING---")
                  time.sleep(.2)
                  clear("WORKING----")
                  time.sleep(.2)
                  clear("WORKING-----")
                  time.sleep(.2)
                  clear("WORKING------")
                  time.sleep(.2)
                  clear("WORKING-------")
                  time.sleep(.2)
                  clear("WORKING--------")
                  time.sleep(.2)
                  clear("WORKING-")
                  time.sleep(.2)
                  clear("WORKING--")
                  time.sleep(.2)
                  clear("WORKING---")
                  time.sleep(.2)
                  clear("WORKING----")
                  time.sleep(.2)
                  clear("WORKING-----")
                  time.sleep(.2)
                  clear("WORKING------")
                  time.sleep(.2)
                  clear("WORKING-------")
                  time.sleep(.2)
                  clear("WORKING--------")
                  time.sleep(.2)
                  clear("PASSAGE CLEAR")
                  time.sleep(1)
                  clear()
                  break
                if robotjob in ["back", "exit", "escape", "cancel"]:
                  break
                else:
                  clear("DOES NOT COMPUTE")
                  time.sleep(1)
          else:
            if robotfollow == False: 
              print "We should probably leave here- there's nothing to do.\n"
              entercont()
                
                
        elif thirddirection == "security" or thirddirection == "room" or thirddirection == "security room" or thirddirection == "room of security":
          print "You go to the security room"
          secroom = None
          while True:
            if robotfollow:
              break
            if secroom == "back":
              break
            else:
              clear("So here's the security room There is a computer in one corner, and a computer in another. You can see Grot watching CSI: Metropolis on one of the many moniters of the computer The interface on another screen boldly states: PASSCARD REQUIRED. The robot look dead, and you notice it is missing a power supply in its hulk.\n")
              entercont()
              while True:
                if robotfollow:
                  break
                clear()
                secroom = raw_input("Would you like to examine the computer of the robot first? You could go back if you would like to explore another room first.\n")
                if secroom in ["computer", "terminal", "moniter", "machine"] and passcardgot == False:
                  clear(terminalscreen)
                  time.sleep(1)
                  clear()
                if secroom in ["computer", "terminal", "moniter", "machine", "pc", "interface"] and passcardgot == True: 
                  
                  clear(terminalscreen2)
                  time.sleep(1)
                  clear("LOADING-")
                  time.sleep(.5)
                  clear("LOADING--")
                  time.sleep(.5)
                  clear("LOADING---")
                  time.sleep(.5)
                  clear("LOADING----")
                  time.sleep(.5)
                  clear("LOADING-----")
                  time.sleep(.5)
                  clear("LOADING------")
                  time.sleep(.5)
                  clear("LOADING-------")
                  time.sleep(.5)
                  clear("LOADING--------")
                  time.sleep(.5)
                  clear("LOADING IS COMPLETE")
                  time.sleep(1)
                  clear()
                  lockeddoor = raw_input("SUPPLY ROOM STATUS: [LOCK][UNLOCK]\n")
                  lockeddoor = lockeddoor.lower()
                  if lockeddoor == "unlock":
                    door = True
                    clear("SUPPLY ROOM UNLOCKED")
                    time.sleep(1)
                  else:
                    door = False
                    clear("SUPPLY ROOM LOCKED")
                    time.sleep(1)
                  
                if secroom in ["robot", "android", "sexrobot", "hulk"] and powersupply == True:
                    while True:
                      if robotfollow:
                        break
                      else:
                        clear()
                        robotpower = raw_input("What do you want me to do?\n")
                        robotpower = robotpower.lower()
                        if robotpower in ["fix", "power", "supply", "power supply", "powersupply", "battery", "flux", "capacitor", "fluxcapacitor", "flux capacitor", "fix robot", "repair", "repair robot"]:
                          clear("The robot now works. You must now program it to do something. Come to think of it, the bit of metal on the hulk looks remarkably like a bulldozer...\n")
                          entercont()
                          while True:
                            if finishsectionone:
                              break
                            else:
                              robotinterface = raw_input("Would you like to interface with this robot?\n")
                              robotinterface = robotinterface.lower()
                              if robotinterface == "yes":
                                while True:
                                  if robotfollow:
                                    break
                                  else:
                                    clear(rbinterface)
                                    time.sleep(1)
                                    clear("HOW MAY I SERVE YOU?")
                                    time.sleep(1)
                                    while True:
                                      clear()
                                      robotjob = raw_input("PLEASE TYPE A COMMAND-\n")
                                      robotjob = robotjob.lower()
                                      if robotjob in ["follow", "come", "work", "activate", "move", "go", "act"]:
                                        robotfollow = True
                                        break
                                      if robotjob in ["back", "exit", "escape", "cancel"]:
                                        break
                                      else:
                                        clear("DOES NOT COMPUTE")
                                        time.sleep(1)
                              
                            if robotinterface in ["no", "back", "cancel", "not"]:
                              clear ("You can come back and attempt to use the robot again at any point.\n")
                              break
                            if robotfollow:
                              clear("The robot is now following you. It will go with you wherever you go.")
                              entercont()
                              break
                            else:
                              print "Excuse me?.\n"
                              entercont()
                        else:
                          break
                                           
                    if robotpower == "no":
                      print "Your choice."
                      break
                    if finishsectionone:
                      break
                    else:
                      if robotfollow == False:
                        print "Let me try that again.\n"
                        entercont()
                    
                if secroom in ["robot", "android", "sexrobot", "hulk"] and powersupply == False:
                  print "I have no way to fix this robot.\n"
                  entercont()
                if secroom == "back":
                  break
              
        elif thirddirection == "room" or thirddirection == "security room" or thirddirection == "room of security":
          print "You go to the security room"
        elif thirddirection == "back" or thirddirection == "corridor":
          print "you go back to the corridor"
          break
        else:
          print "You're trying my patience. I shall have to leave you here if you keep this up; schizophrenia or no.\n"
          entercont()
          
    if finishsectionone:
      break
    elif seconddirection == "back" or seconddirection == "corridor":
      clear()
      print "You end up back at the coridor.\n"
    elif thirddirection == "back" or thirddirection == "corridor":
      clear()
      print "You end up back at the corridor.\n"
    else:
      print "Nice try. Pick a real direction."
      entercont()
    
clear ("The robot rumbles out of the security room and deftly removes the pile of rubble blocking you from any possibility of escape. Congratulations on completing the first part of my adventure game " + name + "!")
pause()    


      
  
   
    


  



