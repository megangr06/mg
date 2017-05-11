###########################################################################################
# Name: Merrick Watson and Megan Griffin
# Date: 5/12/2017
# Description: Look to the Stars - CyberStorm Puzzle 
###########################################################################################
from Tkinter import *
from time import sleep
import RPi.GPIO as GPIO
import pygame;
from random import randint

# the question class
class Question(object):
        # the constructor
        def __init__(self, name, image):
                # questions have a name, an image, and an answer to the question asked
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

        

        # adds an answer to each question
        def addAnswer(self, answer, question):
                # append the answer and question to the appropriate dictionary
                self._answer[answer] = question
        

        # returns a string that will be displayed on the right of the screen
        def __str__(self):
                # the question number the user is on
                s = "You are on {}.\n".format(self.name)
                # the question that is being asked
                s += "What is the constellation? "
                return s

# the game class
# inherits from the Frame class of Tkinter
class Game(Frame):
        # the constructor
        def __init__(self, parent):
                # call the constructor in the superclass
                Frame.__init__(self, parent)

        # creates the questions
        def createQuestions(self):
            #each r is a question
            global r1
            global r2
            global r3
            global r4
            global r5

            global currentQuestion
        

            #create the questions and give them names and an
            #image in the current dictionary
            r1 = Question("Question 1", "generic.gif")
            r2 = Question("Question 2", "sagittarius.gif")
            r3 = Question("Question 3", "virgo.gif")
            r4 = Question("Question 4", "ursa.gif")
            r5 = Question("Winner", "orion.gif")

            r1.addAnswer(c1.name, r2)
            r2.addAnswer(c2.name, r3)
            r3.addAnswer(c3.name, r4)
            r4.addAnswer(c4.name, r5)

            #starts the game on the first question
            Game.currentQuestion = r1
 



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
            ##Game.player_input = Entry(self, bg="white")
            ##Game.player_input.bind("<Return>", self.process)
            ##Game.player_input.pack(side=BOTTOM, fill=X)
            ##Game.player_input.focus()
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
            Game.player_input = Entry(self, bg="white")
            Game.player_input.bind("<Return>", self.process)
            Game.player_input.pack(side=BOTTOM, fill=X)
            Game.player_input.focus()
            # the widget is a Tkinter Text
            # disable it by default
            # don't let the widget control the frame's size
            Game.text = Text(text_frame, bg="AliceBlue", state=DISABLED)
            Game.text.pack(fill=Y, expand=1)
            text_frame.pack(side=RIGHT, fill=Y)
            text_frame.pack_propagate(False)

        # sets the current question image
        def setQuestionImage(self):
        #if player completes the game it shows the winning screen.
            if (Game.currentQuestion == r5):
                Game.img = PhotoImage(file="win.gif")
            else:
                # otherwise grab the image for the current question
                Game.img = PhotoImage(file=Game.currentQuestion.image)
            # display the image on the left of the GUI
            Game.image.config(image=Game.img)
            Game.image.image = Game.img

        # sets the status displayed on the right of the GUI
        def setStatus(self, status):
            # enable the text widget, clear it, set it, and disabled it
            Game.text.config(state=NORMAL)
            Game.text.delete("1.0", END)
            #player wins if they make it past this question
            if (Game.currentQuestion == r5):
                Game.text.insert(END, "Mission Complete!")
            else:
                # otherwise, display the appropriate status
                Game.text.insert(END, str(Game.currentQuestion) +\
                    ""  +\
                    "\n\n" + status)
                self.lighting()


                
                
            Game.text.config(state=DISABLED)
            
        # determines which constellation should be lighting up        
        def lighting(self):
                if (Game.currentQuestion == r1):
                        c1.light(c1.name)
                elif (Game.currentQuestion == r2):
                        c2.light(c2.name)
                elif (Game.currentQuestion == r3):
                        c3.light(c3.name)
                elif (Game.currentQuestion == r4):
                        c4.light(c4.name)
                

        # plays the game
        def play(self):
                # configure the GUI
                self.setupGUI()
                # create the constellations
                self.createConstellations()
                # add the questions to the game
                self.createQuestions()
                # set the current quesetion image
                self.setQuestionImage()
                # set the current status
                self.setStatus("")

                

        #assigns each constellation with the proper name
        def createConstellations(self):
                global c1
                global c2
                global c3
                global c4
            
                c1 = Constellation("sagittarius")
                c2 = Constellation("virgo")
                c3 = Constellation("ursa")
                c4 = Constellation("orion")
                  


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
        #if the player makes it past the last quesetion, the game is over
            elif (Game.currentQuestion == r5):
                Game.player_input.delete(0, END)
                return

            # split the user input into words (words are separated by
            # spaces) and store the words in a list
            words = action.split()

            
            # the game only understands one word inputs
            if (len(words) == 1):
                # isolate the verb and noun
                noun = words[0]
                
                
                    
            # check for valid answer to the current question
            if (noun in Game.currentQuestion.answer):
                # if one is found, change the question to
                # the one that is next
                Game.currentQuestion =\
                    Game.currentQuestion.answer[noun]
                #set the response (success)
                response = "Correct."


                

            # display the response on the right of the GUI
            # display the room's image on the left of the GUI
            # clear the player's input
            self.setStatus(response)
            self.setQuestionImage()
            Game.player_input.delete(0, END)

class Constellation(object):
    # use broadcom pin mode
    GPIO.setmode(GPIO.BCM)

    # create array of GPIO pins
    pins = [26, 19, 13, 6, 5, 22, 27, 17]
    # setup the output pins
    GPIO.setup(pins, GPIO.OUT)

    # initialize the constellation
    def __init__(self, name):
        self.name = name

    # off function
    def off(self):
        GPIO.output(26, False)
        GPIO.output(19, False)
        GPIO.output(13, False)
        GPIO.output(6, False)
        GPIO.output(5, False)
        GPIO.output(22, False)
        GPIO.output(27, False)
        GPIO.output(17, False)
        sleep(.3)

    # on function
    def on(self):
        GPIO.output(26, True)
        GPIO.output(19, True)
        GPIO.output(13, True)
        GPIO.output(6, True)
        GPIO.output(5, True)
        GPIO.output(22, True)
        GPIO.output(27, True)
        GPIO.output(17, True)
        
    # depending on name light LEDs a certain way
    def light(self, name):
        self.off()
        if (name == "sagittarius"):
            # turn on 4, 5, 6, 8
            GPIO.output(6, True)
            GPIO.output(5, True)
            GPIO.output(22, True)
            GPIO.output(17, True)
            sleep(2.5)
            self.off()
            # turn on 3
            GPIO.output(13, True)
            sleep(2.5)
            self.off()
            # turn on 1, 2, 4, 7, 8
            GPIO.output(26, True)
            GPIO.output(19, True)
            GPIO.output(6, True)
            GPIO.output(27, True)
            GPIO.output(17, True)
            sleep(2.5)
            self.off()
            # turn on 3, 5
            GPIO.output(13, True)
            GPIO.output(5, True)
            sleep(2.5)
            self.off()
            # turn on 4
            GPIO.output(6, True)
            sleep(2.5)
            self.off()
            # turn on 3
            GPIO.output(13, True)
            sleep(2.5)
            self.off()
            # turn on 2, 4, 5
            GPIO.output(19, True)
            GPIO.output(6, True)
            GPIO.output(5, True)
            sleep(2.5)
            self.off()
            # turn on 4, 6
            GPIO.output(6, True)
            GPIO.output(22, True)
            sleep(2.5)
            self.off()
            # blink showing reset
            for i in range(3):
                self.on()
                sleep(.2)
                self.off()
                sleep(.2)
        if (name == "virgo"):
            # turn on 5, 7
            GPIO.output(5, True)
            GPIO.output(27, True)
            sleep(2.5)
            self.off()
            # turn on 4, 6
            GPIO.output(6, True)
            GPIO.output(22, True)
            sleep(2.5)
            self.off()
            # turn on 7
            GPIO.output(27, True)
            sleep(2.5)
            self.off()
            # turn on 1, 4
            GPIO.output(26, True)
            GPIO.output(6, True)
            sleep(2.5)
            self.off()
            # turn on 2, 5, 6
            GPIO.output(19, True)
            GPIO.output(5, True)
            GPIO.output(22, True)
            sleep(2.5)
            self.off()
            # turn on 3
            GPIO.output(13, True)
            sleep(2.5)
            self.off()
            # turn on 2
            GPIO.output(19, True)
            sleep(2.5)
            self.off()
            # turn on 1
            GPIO.output(26, True)
            sleep(2.5)
            self.off()
            # blink showing reset
            for i in range(3):
                self.on()
                sleep(.2)
                self.off()
                sleep(.2)
        if (name == "ursa"):
            # turn on 1
            GPIO.output(26, True)
            sleep(2.5)
            self.off()
            # turn on 1
            GPIO.output(26, True)
            sleep(2.5)
            self.off()
            # turn on 2, 5, 7
            GPIO.output(19, True)
            GPIO.output(5, True)
            GPIO.output(27, True)
            sleep(2.5)
            self.off()
            # turn on 3, 4, 6
            GPIO.output(13, True)
            GPIO.output(6, True)
            GPIO.output(22, True)
            sleep(2.5)
            self.off()
            # turn on 4, 7
            GPIO.output(6, True)
            GPIO.output(27, True)
            sleep(2.5)
            self.off()
            # turn on 3, 6
            GPIO.output(13, True)
            GPIO.output(22, True)
            sleep(2.5)
            self.off()
            # turn on none
            sleep(2.5)
            self.off()
            # turn on 3, 4, 6
            GPIO.output(13, True)
            GPIO.output(6, True)
            GPIO.output(22, True)
            sleep(2.5)
            self.off()
            # turn on 7
            GPIO.output(27,True)
            sleep(2.5)
            self.off()
            # turn on 3, 6
            GPIO.output(13, True)
            GPIO.output(22, True)
            sleep(2.5)
            self.off()
            # blink showing reset
            for i in range(3):
                self.on()
                sleep(.2)
                self.off()
                sleep(.2)
        if (name == "orion"):
            # turn on 1, 2
            GPIO.output(26, True)
            GPIO.output(19, True)
            sleep(2.5)
            self.off()
            # turn on 1, 2
            GPIO.output(26, True)
            GPIO.output(19, True)
            sleep(2.5)
            self.off()
            # turn on 3
            GPIO.output(13, True)
            sleep(2.5)
            self.off()
            # turn on 4
            GPIO.output(6, True)
            sleep(2.5)
            self.off()
            # turn on 6, 8
            GPIO.output(22, True)
            GPIO.output(17, True)
            sleep(2.5)
            self.off()
            # turn 6
            GPIO.output(22, True)
            sleep(2.5)
            self.off()
            # turn 3, 6
            GPIO.output(13, True)
            GPIO.output(22, True)
            sleep(2.5)
            self.off()
            # turn on 4, 8
            GPIO.output(6, True)
            GPIO.output(17, True)
            sleep(2.5)
            self.off()
            # turn on none
            sleep(2.5)
            self.off()
            # turn on 2, 7
            GPIO.output(19, True)
            GPIO.output(27, True)
            sleep(2.5)
            self.off()
            # turn on 3, 4, 5, 6
            GPIO.output(13, True)
            GPIO.output(6, True)
            GPIO.output(5, True)
            GPIO.output(22, True)
            sleep(2.5)
            self.off()
            # blink showing reset
            for i in range(3):
                self.on()
                sleep(.2)
                self.off()
                sleep(.2)


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
