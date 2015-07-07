from sys import exit


class Scene(object):

    def enter(self):
        exit(1)

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map
    
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Home(Scene):
    
    def enter(self):
        print ("You wake up, your house is quiet. You get out of bed and look around the house.")
        print("Confusion and panic sets in, you can't find your wife or kids.")
        print("You look outside and see chaos, people running and screaming, and getting attacked by what looks to be Zombies!")
        print("You've been waiting your whole life for this moment.")
        print("What do you do next? [Go to weapon room?], [Look for my family?] [Go outside?]")

        action = raw_input(">").lower()
        
        if action == "go to weapon room":
            print("You rush to the weapon room")
            return 'weapon_room'

        elif action == "look for my family":
            print("You yell and quickly search the house but don't find anyone. You rush to the weapon room.")
            return 'weapon_room'
        
        elif action == "go outside":
            print("You open the door and a zombie bites your neck and starts eating you")
            return 'death'

        else:
            print("Not an option!")
            return 'main_room'

class Main_Room(Scene):
    def enter(self):
        print "You rethink your options. What will you do? \n [Go to the weapon room?], [Look for my family?] or [Go outside?]"
        
        action = raw_input(">").lower()
        
        if action == "go to weapon room":
            print "You rush to the weapon room."
            return 'weapon_room'
        
        elif action == "look for my family":
           print("You yell and quickly search the house but don't \n find anyone. You rush to the weapon room.")
           return 'weapon_room'
        
        elif action == "go outside":
            print("You open the door and a zombie bites your neck \n and starts eating you")
            return 'death'

        else:
            print("Not an option!")
            return 'main_room'

class Weapon_Room(Scene):
           
    def enter(self):
        print "You're in the weapon room, you quickly grab your bag full of weapons. You are finally ready to venture outside."
        print "You're outside and quickly move into the next door neighors house"
       
        print "You see a vile of what looks to be the cure to end the \nzombie apocalypse but it's in a room full of zombies"
        print "Do you [Go into the room?] or [Run?]"
       
        action = raw_input(">").lower()
        
        if action == 'go into the room':
            return 'fight_zombie'
        
        elif action == 'run':
            print "You run and slip on a banana peel!"
            return 'death'


class Find_Cure(Scene):

    def enter(self):
        print "You grab what looks like the vile to cure the zombie apocalypse."
        return 'finished'  
        
        

class Fight_Zombie(Scene):    
    def enter(self):
        print "You look around the house and see a room full of zombies."
        print "You enter a room full of zombies, you quickly\n pull out your weapons and start destroying every zombie in the room beause \nyou're a bad ass!" 
        return 'find_cure'


class Death(Scene):
    
    def enter(self):
        
        print("You fight back but the Zombie has already won, you slowly turn and become one of them.")
        exit(1)

class Finished(Scene):
    
    def enter(self):
        print "You've found the cure! You're journey is only beggining..."
        return 'finished'

class Map(object):
    scenes = {
        'home': Home() ,
        'weapon_room': Weapon_Room() ,
        'find_cure': Find_Cure() ,
        'fight_zombie': Fight_Zombie() ,
        'main_room': Main_Room(), 
        'death': Death() ,
        'finished': Finished() ,
        }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('home')
a_game = Engine(a_map)
a_game.play()
