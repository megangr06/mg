###########################################################################################
# Name: Megan Griffin
# Date: 3/24/2017
# Description: Room Adventure... Revolutions 
###########################################################################################
from Tkinter import *



# the question class

class Question(object):
        # the constructor
        def __init__(self, name, image):
                # questions have a name, an image (the name of a file), an answer (e.g., south)
                # (e.g., to the south is room n), items (e.g., table), item descriptions (for each item),
                # and grabbables (things that can be taken into inventory)
                self.name = name
                self.image = image
                self.answer ={}


        # getters and setters for the instance variables
        @property
        def name(self):
                return self._name

        @name.setter
        def name(self, value):
                self._name = value

        @property
        def image(self):
                return self._image

        @image.setter
        def image(self, value):
                self._image = value

        @property
        def answer(self):
                return self._answer

        @answer.setter
        def answer(self, value):
                self._answer = value

        

        # adds an exit to the room
        # the exit is a string (e.g., north)
        # the room is an instance of a room
        def addAnswer(self, answer, question):
                # append the exit and room to the appropriate dictionary
                self._answer[answer] = question

        # adds an item to the room
        # the item is a string (e.g., table)
        # the desc is a string that describes the item (e.g., it is made of wood)
                # adds a grabbable item to the room
        # the item is a string (e.g., key)
                # removes a grabbable item from the room
        # the item is a string (e.g., key)
        

        # returns a string description of the room
        def __str__(self):
                # first, the room name
                s = "You are on {}.\n".format(self.name)

                # next, the items in the room
                s += "What is the constellation? "


        

                return s

# the game class
# inherits from the Frame class of Tkinter
class Game(Frame):
        # the constructor
        def __init__(self, parent):
                # call the constructor in the superclass
                Frame.__init__(self, parent)

        # creates the rooms
        def createQuestions(self):
            #r1 through r4 are the four rooms in the mansion
            #currentRoom is the room the player is currently in (which
            #can be one of r1 through r4)
            global r1
            global r2
            global r3
            global r4
            global r5
            
            global r7

            global currentRoom
        

            #create the rooms and give them meaningful names and an
            #image in the current dictionary
            r1 = Question("Question 1", "sagittarius.gif")
            r2 = Question("Question 2", "virgo.gif")
            r3 = Question("Question 3", "ursa.gif")
            r4 = Question("Question 4", "orion.gif")
            r5 = Question("Winner", "roomroom.gif")
            

            #adds exits to room 1
            r1.addAnswer("sagittarius", r2) # to the east of room 1 is room 2
            #add items to room 1
            

            #add exits to room 2
            r2.addAnswer("virgo", r3)

            # add items to room 2
            
            # add exits to room 3
            r3.addAnswer("ursa_major", r4)
           
            

            # add exits to room 4
            r4.addAnswer("orion", r5)
            #add items to room 4
            

           
            Game.currentRoom = r1

            
            Game.inventory = []

 

        # sets up the GUI
        def setupGUI(self):
            # organize the GUI
            self.pack(fill=BOTH, expand=1)
            # setup the player input at the bottom of the GUI

            # the widget is a Tkinter Entry
            # set its background to white and bind the return key to the
            # function process in the class
            # push it to the bottom of the GUI and let it fill
            # horizontally
            # give it focus so the player doesn't have to click on it
            Game.player_input = Entry(self, bg="white")
            Game.player_input.bind("<Return>", self.process)
            Game.player_input.pack(side=BOTTOM, fill=X)
            Game.player_input.focus()
            # setup the image to the left of the GUI
            # the widget is a Tkinter Label
            # don't let the image control the widget's size
            img = None
            Game.image = Label(self, width=WIDTH / 2, image=img)
            Game.image.image = img
            Game.image.pack(side=LEFT, fill=Y)
            Game.image.pack_propagate(False)
            # setup the text to the right of the GUI
            # first, the frame in which the text will be placed
            text_frame = Frame(self, width=WIDTH / 2)
            # the widget is a Tkinter Text
            # disable it by default
            # don't let the widget control the frame's size
            Game.text = Text(text_frame, bg="lightgrey", state=DISABLED)
            Game.text.pack(fill=Y, expand=1)
            text_frame.pack(side=RIGHT, fill=Y)
            text_frame.pack_propagate(False)

        # sets the current room image
        def setRoomImage(self):
        #if player makes it to the dining room then they win and a photo of the money is shown.
            if (Game.currentRoom == r5):
                Game.img = PhotoImage(file="money2.gif")
            elif (Game.currentRoom == None):
                # if dead, set the skull image
                Game.img = PhotoImage(file="skull.gif")
            else:
                # otherwise grab the image for the current room
                Game.img = PhotoImage(file=Game.currentRoom.image)
            # display the image on the left of the GUI
            Game.image.config(image=Game.img)
            Game.image.image = Game.img

        # sets the status displayed on the right of the GUI
        def setStatus(self, status):
            # enable the text widget, clear it, set it, and disabled it
            Game.text.config(state=NORMAL)
            Game.text.delete("1.0", END)
            #player wins if they make it to this room
            if (Game.currentRoom == r5):
                Game.text.insert(END, "Mission Complete! You know your constellations!")
                
            elif (Game.currentRoom == None):
                # if dead, let the player know
                Game.text.insert(END, "You are dead. The only thing you can do \nnow is quit.\n")
            else:
                # otherwise, display the appropriate status
                Game.text.insert(END, str(Game.currentRoom) +\
                    ""  +\
                    "\n\n" + status)
            Game.text.config(state=DISABLED)


        # plays the game
        def play(self):
                # add the rooms to the game
                self.createQuestions()
                # configure the GUI
                self.setupGUI()
                # set the current room
                self.setRoomImage()
                # set the current status
                self.setStatus("")
                


        # processes the player's input
        def process(self, event):
            # grab the player's input from the input at the bottom of
            # the GUI
            
            action = Game.player_input.get()
            # set the user's input to lowercase to make it easier to
            # compare the verb and noun to known values
            action = action.lower()
            # set a default response
            response = "Sorry! That is not correct. Try again!"
            
            # exit the game if the player wants to leave (supports quit,
            # exit, and bye)
            if (action == "quit" or action == "exit" or action == "bye"\
            or action == "sionara!"):
                exit(0)
            # if the player is dead if goes/went south from room 4
            if (Game.currentRoom == None):
                # clear the player's input
                Game.player_input.delete(0, END)
                return
        #if the player makes it to the dining room, the game is over
            elif (Game.currentRoom == r5):
                Game.player_input.delete(0, END)
                return

            # split the user input into words (words are separated by
            # spaces) and store the words in a list
            words = action.split()

            
            # the game only understands two word inputs
            if (len(words) == 1):
                # isolate the verb and noun
                noun = words[0]
                
                
                    
            # check for valid exits in the current room
            if (noun in Game.currentRoom.answer):
                # if one is found, change the current room to
                # the one that is associated with the
                # specified exit
                Game.currentRoom =\
                    Game.currentRoom.answer[noun]
                #set the response (success)
                response = "Correct."

                

                        
                               

        

        

            # display the response on the right of the GUI
            # display the room's image on the left of the GUI
            # clear the player's input
            self.setStatus(response)
            self.setRoomImage()
            Game.player_input.delete(0, END)


##########################################################
# the default size of the GUI is 800x600
WIDTH = 800
HEIGHT = 600

# create the window
window = Tk()
window.title("Star Game")

# create the GUI as a Tkinter canvas inside the window
g = Game(window)
# play the game
g.play()

# wait for the window to close
window.mainloop()
