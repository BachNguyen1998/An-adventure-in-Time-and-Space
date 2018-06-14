import vlc
from sys import exit

def daleks():
    for i in range (1,13111):
        for j in [".","..","..."]:
            print "%s\r" % j,


def daleks2():
    for i in range (1,8111):
        for j in [".","..","..."]:
            print "%s\r" % j,


def tcount():
    for i in range (1,1111):
        for j in [".","..","..."]:
            print "%s\r" % j,


def tcount_classic():
    for i in range (1,1111):
        for j in ["/","|","\\","-"]:
            print "%s\r" % j,


def tcount_tl():
    for i in range (1,17111):
        for j in [".","..","..."]:
            print "%s\r" % j,


def dead(why):
    print why, "Goodbye..."
    exit(0)


def start():
    print "You're dreaming..."
    tcount()
    print "You're surrounded by darkness"
    tcount()
    print ("Suddenly a Blue Box appears in front of you...")
    tl = vlc.MediaPlayer(".\music\\Tardis Landing.mp3")
    tl.play()
    tcount_tl()
    tl.stop()



def tardis():
    tcount_classic()
    print "You walk inside the TARDIS - Time and Relative Dimension in Space"
    print "Yes... It's bigger on the inside!"
    print "In the center, you see a control panel."
    print "You walk around, you see that there're 4 main operators."
    print "They are: throttle, handbrake, left lever, right Lever."
    print "How would you operate them?"
    operate = raw_input("> ")
    if "throttle" in operate or "handbrake" in operate or "left" in operate:
        print "You've just activated Space Travel. You can travel to anywhere in space."
    elif "throttle" in operate or "handbrake" in operate or "right" in operate:
        print "You've just activated Time Travel. You can travel to any moment in time."
    elif "throttle" in operate or "handbrake" in operate or "left" in operate or "right" in operate:
        print "You've just activated Space - Time Travel. You can travel to anywhere at any moment!"
    elif "don't know" in operate:
        tardis_function()
    else:
        print "You've just created a Time Loop inside TARDIS... You'll never can get out. Goodluck!"


def tardis_function(): # Bug: Can't activate Space-Time travel
    tcount_classic()
    print "***TARDIS Inteface Instruction***"
    #space_travel = False
    #time_travel = False
    #space_time_travel = False
            # Left_lever
    print "Activate Left Lever: On / Off ?"
    left_lever = False
    left = raw_input("> ")
    if "on" in left or "On" in left and not left_lever:
        left_lever = True
    else:
        left_lever = False
            # Right_lever
    print "Activate Right Lever: On / Off ?"
    right_lever = False
    right = raw_input("> ")
    if "on" in right or "On" in right and not right_lever:
        right_lever = True
    else:
        right_lever = False
            # Handbreak
    print "Activate Handbreak: On / Off ?"
    handbreak = False
    hand = raw_input("> ")
    if "on" in hand or "On" in hand and not handbreak:
        Handbreak = True
    else:
        Handbreak = False
            # Throttle
    print "Activate Throttle: On / Off ?"
    Throttle = False
    throttle = raw_input("> ")
    if "on" in throttle or "On" in throttle and not Throttle:
        Throttle = True
    else:
        Throttle = False
    if left_lever == True and Handbreak == True and Throttle == True :
        for i in range (1,1111):
            for j in ["/","|","\\","-"]:
                print "%s\r" % j,
        space_travel()
    elif right_lever == True and Handbreak == True and Throttle == True :
        for i in range (1,1111):
            for j in ["/","|","\\","-"]:
                print "%s\r" % j,
        time_travel()
    elif left_lever == True and right_lever == True and Handbreak == True and Throttle == True:
        for i in range (1,1111):
            for j in ["/","|","\\","-"]:
                print "%s\r" % j,
        print "Activating Space-Time Travel..."
    else:
        print "TARDIS not operating..."
        for i in range (1,1111):
            for j in ["/","|","\\","-"]:
                print "%s\r" % j,
        tardis_function()


def space_travel():
    print "Activating Space Travel..."
    t= vlc.MediaPlayer("C:\Users\DELL_5537\Downloads\Music\\tardis.mp3")
    tl = vlc.MediaPlayer("C:\Users\DELL_5537\Downloads\Music\\Tardis Landing.mp3")
    t.play()
    for i in range (1,13111):
        for j in ["/","|","\\","-"]:
            print "%s\r" % j,
    t.stop()
    tl.play()
    for i in range (1,15111):
        for j in ["/","|","\\","-"]:
            print "%s\r" % j,
    tl.stop()
    places()


def time_travel():
    print "Activating Time Travel..."
    t = vlc.MediaPlayer("C:\Users\DELL_5537\Downloads\Music\\tardis.mp3")
    tt = vlc.MediaPlayer("C:\Users\DELL_5537\Downloads\Music\\Tardis in Time Vortex.mp3")
    tl = vlc.MediaPlayer("C:\Users\DELL_5537\Downloads\Music\\Tardis Landing.mp3")
    t.play()
    for i in range (1,13111):
        for j in ["/","|","\\","-"]:
            print "%s\r" % j,
    t.stop()
    tt.play()
    for i in range (1,13111):
        for j in ["/","|","\\","-"]:
            print "%s\r" % j,
    tt.stop()
    tl.play()
    for i in range (1,15111):
        for j in ["/","|","\\","-"]:
            print "%s\r" % j,
    tl.stop()


def places():
    print "You've just teleported to a random place"
    tcount()
    print "What do you want to do now?"
    tcount()
    print """
    1. Get outside TARDIS
    2. Continue traveling with TARDIS.
    3. Playing..."""
    choice2 = raw_input("> ")
    tcount()

    if "1" in choice2:
        rooms()
    elif "2" in choice2:
        tardis_function()
    else:
        dead("Warning!!! Time Loop detected... System Critical!!! TARDIS is locked.")


def rooms():
    tcount()
    print "You've just walked outside TARDIS."
    tcount()
    print "There're 3 doors on your Left, Right, and Front of you."
    tcount()
    print "Which door do you choose?"
    choice3 = raw_input("> ")

    if "Left" in choice3:
        door_left()
    elif "Front" in choice3:
        door_front()
    elif "Right" in choice3:
        door_right()
    else:
        dead("Shadow Kin's found you!!! Get ready to die...")


def door_left():
    tcount()
    print "You walked into an ancient room..."
    tcount()
    print "There's a Weeping Angel statue blocking another door in front of you."
    pass



def door_front():
    print "You walked into a dark room with 2 other doors (Front & Behind you)... "
    tcount()
    print "There's an alien creature called *The Silence* waiting for you."
    print "You will immediately forget when you stop looking it."
    tcount()
    pass





import vlc
def door_right():

    print "You've just walked into the room contains the most dangerous creature in the universe - Dalek!"
    print "The Dalek is standing between you and the Golden Door."
    dw = vlc.MediaPlayer("C:\Users\DELL_5537\Downloads\Music\\who.mp3")
    identify = vlc.MediaPlayer("C:\Users\DELL_5537\Downloads\Music\\indentify.mp3")
    identify.play()
    daleks2()
    identify.stop()
    tcount()
    pass
