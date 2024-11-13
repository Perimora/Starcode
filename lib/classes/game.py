import tkinter as tk

from abc import ABC, abstractmethod

from game_types import GameType

class Game(ABC):
    """
    Abstract class game. Template for Hangman and / or snake game.
    """
    
    g_type : GameType

    @classmethod
    @abstractmethod 
    def init_gui(self):
        pass

    @classmethod
    @abstractmethod 
    def start_game(self):
        pass

class HangManGame(Game):
    """
    Class HangmanGame. Implements the GUI and game logic for the game 'Hangman'. 
    """

    def __init__(self):
        """
        Constructor for HangManGame. Sets the game type and boots up GUI.
        """

        # call constructor of base class 
        super().__init__()
        
        # set game type
        self.g_type = GameType.HANGMAN
        
        # initialize gui
        self.gui_root = self.init_gui()
        
        # start main event loop
        self.start_game()

    def init_gui(self):
        # create the main window
        root = tk.Tk()
        root.title("hangman")

        # binding to exit fullscreen
        root.bind("<Escape>", lambda event: root.attributes("-fullscreen", False))

        # create the label to display the word
        guess_label = tk.Label(root, text="- - - - -", font=("Arial", 20))
        guess_label.pack()

        # create the input box for user guesses
        guess_entry = tk.Entry(root, font=("Arial", 16))
        guess_entry.pack()

        # create the button to check the user's guess
        check_button = tk.Button(root, text="check guess", command=lambda: print("checking..."))
        check_button.pack()

        # create the label to show the remaining tries
        tries_label = tk.Label(root, text="tries left: XXX", font=("Arial", 14))
        tries_label.pack()

        return root


    def start_game(self):
        # start the main event loop and fullscreen
        self.gui_root.attributes("-fullscreen", True)
        self.gui_root.mainloop()   

    def stop_game(self):
        pass 

