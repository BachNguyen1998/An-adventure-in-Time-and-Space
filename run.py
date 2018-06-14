from sys import exit
from random import randint
import vlc
import functions
#comment
class Scene(object):

    def loading(self):
        for i in range(1,1111):
            for j in ["/","|","\\","-"]:
                print "%s\r" % j,

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



class Engine(object):

    def __init__(self, scene_name):
        self.scene_name = scene_name

    def play(self):
        current_scene = self.scene_name.opening_scene()
        last_scene = self.scene_name.next_scene('finish')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_name.next_scene(next_scene_name)

        current_scene.enter()

class Death(Scene):
    die = [
        "You've made a wrong choice! You're gonna die in any second... Goodbye!",
        "Bad decision! Don't call yourself \"The Doctor's companion\". You're about to die. Goodbye...!",
        "Stupid choice! don't call your self a \"Whovian\"... Goodbye!"
    ]

    def enter(self):
        print self.die[randint(0, len(self.die) - 1)]
        exit()

class Dream(Scene):

    def enter(self):
        self.loading()
        ex36.start()
        print "What would you do?"
        print "1. Stay away from it. Run as fast as you can."
        print "2. Get inside and discover..."
        choice1 = raw_input("> ")
        if "2" in choice1:
            return 'tardis'
        else:
            return "death"


class Tardis(Scene):

    space = False
    time = False

    def enter(self):
        print "Entered Tardis!"
        self.tardis_()

        if self.space == True:
            return self.space_travel()
        elif self.time == True:
            return self.time_travel()
        else:
            exit()


    def tardis_(self):
        tcount_classic()
        print "You walk inside the TARDIS - Time and Relative Dimension in Space"
        print "Yes... It's bigger on the inside!"
        print "In the center, you see a control panel."
        print "You walk around, you see that there're 4 main operators."
        print "They are: throttle, handbrake, left lever, right Lever."
        print "How would you operate them? (if you don't know, be honest when you type!)"
        operate = raw_input("> ")
        if "throttle" in operate or "handbrake" in operate or "left" in operate:
            print "You've just activated Space Travel. You can travel to anywhere in space."
        elif "throttle" in operate or "handbrake" in operate or "right" in operate:
            print "You've just activated Time Travel. You can travel to any moment in time."
        elif "throttle" in operate or "handbrake" in operate or "left" in operate or "right" in operate:
            print "You've just activated Space - Time Travel. You can travel to anywhere at any moment!"
        elif "don't know" in operate:
            self.tardis_function()
        else:
            print "You've just created a Time Loop inside TARDIS... You'll never can get out. Goodluck!"
            exit(0)


    def tardis_function(self): # Bug: Can't activate Space-Time travel
        tcount_classic()
        print "***TARDIS Inteface Instruction***"
        print "Space travel: on off on on"
        print "Time travel: off on on on"
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
            self.space = True
        elif right_lever == True and Handbreak == True and Throttle == True :
            for i in range (1,1111):
                for j in ["/","|","\\","-"]:
                    print "%s\r" % j,
            self.time = True
        else:
            print "TARDIS not operating..."
            for i in range (1,1111):
                for j in ["/","|","\\","-"]:
                    print "%s\r" % j,
            self.tardis_function()


    def space_travel(self):
        print "Activating Space Travel..."
        t= vlc.MediaPlayer(".\music\\tardis.mp3")
        tl = vlc.MediaPlayer(".\music\\Tardis Landing.mp3")
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

        return Map('dream').places[randint(0, len(Map('dream').places)-1)]


    def time_travel(self):
        print "Activating Time Travel..."
        t = vlc.MediaPlayer(".\music\\tardis.mp3")
        tt = vlc.MediaPlayer(".\music\\Tardis in Time Vortex.mp3")
        tl = vlc.MediaPlayer(".\music\\Tardis Landing.mp3")
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

        return Map('dream').times[randint(0, len(Map('dream').times) - 1)]


class WeepingAngel(Scene):

    def enter(self):
        self.loading()
        ex36.door_left()
        door1 = False
        tcount()
        print "What will you do?"
        print """
        1. Blink!
        2. Don't blink!"""
        choice4 = raw_input("> ")

        if "2" in choice4:
            print "There's a mirror to your left. If you put it in front of the Angel, it can help you freeze the statue."
            print "What will you do?"
            const = True
            while const == True:
                choice5 = raw_input("> ")
                tcount()
                if "mirror" in choice5 and not door1:
                    print "The Weeping Angel will not move. You're able to open the door now!"
                    door1 = True
                elif "mirror" in choice5 and door1:
                    print "You've just broken the mirror... Oh.. and... I forgot to tell you to keep looking at the Angel..."
                    tcount()
                    Death().enter()
                elif "open" in choice5 and door1:
                    const = False
                    return 'silence'

                else:
                    print "What are you doing?? Make up your decision now! Before the Angel turns out the light!!!"
        else:
            tcount()
            Death().enter()

class Silence(Scene):

    def enter(self):
        self.loading()
        ex36.door_front()
        print "What will you do?"
        door2 = False
        tcount()
        const = True
        while const == True:
            choice6 = raw_input("> ")

            if "camera" in choice6 or "fight" in choice6:
                print "You defeated the Silence. You may go. The doors are unlocked..."
                door2 = True
            elif "open" in choice6 and door2:
                tcount()
                print "Which door do you want to go? Front or Behind?"
                choice7 = raw_input("> ")
                tcount()

                if "Behind" in choice7:
                    return 'weeping_angel'
                    const = False
                elif "Front" in choice7:
                    const = False
                    return 'dalek'
                else:
                    print "You can't even make your own decision. TARDIS is leaving...Goodbye!"

            else:
                tcount()
                Death().enter()


class Dalek(Scene):

    def enter(self):
        self.loading()
        ex36.door_right()
        print "What will you do? *Daleks are scared of The Doctor*"
        door3 = False
        dw = vlc.MediaPlayer(".\music\\who.mp3")
        rose = vlc.MediaPlayer(".\music\\rose.mp3")
        exterminate = vlc.MediaPlayer(".\music\\dalek.mp3")
        const = True
        while const == True:
            choice7 = raw_input("> ")
            if "Doctor" in choice7:
                dw.play()
                daleks()
                dw.stop()
                print "The Dalek is confused. You can take the chance to open door NOW!!!"
                door3 = True
            elif "open" in choice7 and door3:
                tcount()
                rose.play()
                tcount()
                rose.stop()
                const = False
                return 'finish'

            else:
                exterminate.play()
                daleks2()
                exterminate.stop()
                print "You've just been exterminated by the Dalek."
                Death().enter()

class FirstDoctor(Scene):

    def enter(self):
        first = vlc.MediaPlayer(".\music\\first doctor.mp3")
        first.play()
        for i in range (1,75111):
            for j in [".","..","..."]:
                print "%s\r" % j,
        first.stop()
        print "You've just met the 1st Doctor."
        tcount()
        print "Do you want to time travel again? Yes or No?"
        choice = raw_input("> ")
        if "Yes" in choice:
            return Tardis().time_travel()
        else:
            print "You're about to leave the TARDIS..."
            tcount()
            print "*The Doctor is coming...*"
            tcount()
            print "And you wake up! Too bad..."
            exit()

class NinthDoctor(Scene):

    def enter(self):
        ninth = vlc.MediaPlayer(".\music\\ninth doctor.mp3")
        ninth.play()
        for i in range (1,80111):
            for j in [".","..","..."]:
                print "%s\r" % j,
        ninth.stop()
        print "You've just met the 9th Doctor and..."
        tcount()
        return 'finish'

class TenthDoctor(Scene):

    def enter(self):
        tenth = vlc.MediaPlayer(".\music\\ten doctor.mp3")
        tenth.play()
        for i in range (1,24111):
            for j in [".","..","..."]:
                print "%s\r" % j,
        tenth.stop()
        print "You've just met the 10th Doctor."
        tcount()
        print "Do you want to time travel again? Yes or No?"
        choice = raw_input("> ")
        if "Yes" in choice:
            return Tardis().time_travel()
        else:
            print "You're about to leave the TARDIS..."
            tcount()
            print "*The Doctor is coming...*"
            tcount()
            print "And you wake up! Too bad..."
            exit()

class EleventhDoctor(Scene):

    def enter(self):
        eleventh = vlc.MediaPlayer(".\music\\eleven doctor.mp3")
        eleventh.play()
        for i in range (1,22111):
            for j in [".","..","..."]:
                print "%s\r" % j,
        eleventh.stop()
        print "You've just met the 11th Doctor."
        tcount()
        print "Do you want to time travel again? Yes or No?"
        choice = raw_input("> ")
        if "Yes" in choice:
            return Tardis().time_travel()
        else:
            print "You're about to leave the TARDIS..."
            tcount()
            print "*The Doctor is coming*"
            tcount()
            print "And you wake up! Too bad..."
            exit()

class TweleveDoctor(Scene):

    def enter(self):
        twelveth = vlc.MediaPlayer(".\music\\twelve doctor.mp3")
        twelveth.play()
        for i in range (1,55111):
            for j in [".","..","..."]:
                print "%s\r" % j,
        twelveth.stop()
        print "You've just met the 12th Doctor."
        tcount()
        print "Do you want to time travel again? Yes or No?"
        choice = raw_input("> ")
        if "Yes" in choice:
            return Tardis().time_travel()
        else:
            print "You're about to leave the TARDIS..."
            tcount()
            print "*The Doctor is coming*"
            tcount()
            print "And you wake up! Too bad..."
            exit()

class Finish(Scene):

    def enter(self):
        print "You've found Rose!"
        print "You won!"
        exit()

class Map(object):
    scenes = {
        'death': Death(),
        'dream': Dream(),
        'tardis': Tardis(),
        'weeping_angel': WeepingAngel(),
        'silence': Silence(),
        'dalek': Dalek(),
        'first_doctor': FirstDoctor(),
        'ninth_doctor': NinthDoctor(),
        'tenth_doctor': TenthDoctor(),
        'eleventh_doctor': EleventhDoctor(),
        'twelve_doctor': TweleveDoctor(),
        'finish': Finish()
    }
    places = ['weeping_angel', 'silence', 'dalek']
    times = ['first_doctor', 'ninth_doctor', 'tenth_doctor', 'eleventh_doctor', 'twelve_doctor']
    def __init__(self, scene_name):
        self.scene_name = scene_name
    def next_scene(self, next_scene):
        a = self.scenes.get(next_scene)
        return a
    def opening_scene(self):
        return self.next_scene(self.scene_name)

a_map = Map('dream')
a_game = Engine(a_map)
a_game.play()
