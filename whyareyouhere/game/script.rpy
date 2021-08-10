# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character(_("Alex"), color="#ffcccc")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "dark-room.png" or "dark-room.jpg") to the
    # images directory to show it.

    scene dark-room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show alex happy

    # These display lines of dialogue.
    e "Hello! I see you're alone. Where are you from?":
    
    menu: 
        "Just in the area.":
            jump choice_a
            #"I honestly don't know."
            #jump choice_b    
            #"Why do you care?"
            #jump choice_c
    
    label choice_a: 
        $ menu_flag = True
        
        e "Why are you still here?":
            #"What do you mean?":
            #    jump a1
            #"Are you exploring?":
            #    jump a2
            #"Do you know why you're here?":
            #    jump a3
    
    #a1: "Why haven't you moved?"
    
    #a2: "Are you comfortable with where you are in life?"
    
    #a3: "I honestly don't know."
    
    #menu choice_b: "You're here because you wanted to be here."
    
    #menu choice_c: "Do you want me to care?"
    
    
        
    # This ends the game.

    return
