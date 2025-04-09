import pygame

class Buttons:
    def __init__(self, x, y, text, height):                                                                                                             
        self._buttonBackground = pygame.image.load("images/woodButton.jpg")                                                 # Backgorund of the button
        self._pos = (x,y)                                                                                                   # Position in the picture
        self._text = text                                                                                                   # Button text
        self._isClicked = False                                                                                             # Checks if button is clicked
        self._hoverColor = (0,0,139,128)                                                                                    # Hovercolor
        self._isClickedColor = (0,0,100)                                                                                    # Color when button is clicked
        self._font = pygame.font.SysFont("PressStart2P-Regular.ttf", 40, bold=True, italic=False)                           # Font style and attributes
        self._rendered_text = self._font.render(self._text, True, (0, 0, 0))                                                # Rendered text
        self._width = self._rendered_text.get_width()                                                                       # Button width
        self._height = height                                                                                               # Button height
        self._buttonBackgroundTransform = pygame.transform.scale(self._buttonBackground, (self._width, self._height))       # Wood style background for Button scaled
        self._form = pygame.Rect(x, y, self._width, self._height)                                                           # Appereance of the Button in a rectangel
        self._isSelected = False                                                                                            # Checks if the button is selected
    
    
    # Function to draw the button    
    def drawButton(self, screen):
        # Building the Button 
        buttonText = self._font                                         # Sets the Text on the button
        buttonText = self._rendered_text
        pygame.draw.rect(screen, (0,0,0),self._form, width=0)           # Creates the Button
        buttonText = buttonText.get_rect(center=self._form.center)      # Puts the text in the center of the Button
        screen.blit(self._buttonBackgroundTransform, self._form)        # Draws the end result of the Button
        
      

        # implementing Button logic
        global in_main_menu, two_player_game, one_player_game            
        mouse_pos = pygame.mouse.get_pos()                              # Checks which mouse button was clicked
        mouseClick = pygame.mouse.get_pressed()[0]
        
        if self._form.collidepoint(mouse_pos): # Checks whether mouse is on button or not
            transparency = pygame.Surface(self._form.size, pygame.SRCALPHA)
            transparency.fill((0, 0, 255, 128))                                # Sets a transparency as a hover effect for the mouse
            screen.blit(transparency, self._form)
            if mouseClick and not self._isClicked: 
                self._isClicked = True
                transparency.fill((0,0,139,128))                               # If the mouse is clicked inside of a button isClicked should be True preventing from holding down the button
                screen.blit(transparency, self._form)
                if twoPlayer._isClicked == True:                                
                    twoPlayerGame(screen)
                if onePlayer._isClicked == True:
                    in_main_menu = False                                        # Checks which button was clicked and sets it on True for the right function to call
                    one_player_game = True                                      # Global variables are set to track the game state
                    onePlayerGameSelection(screen)
                if backToMenu._isClicked == True:
                    print("test")
                    one_player_game = False
                    in_main_menu = True
                
            self._isClicked = mouseClick
        else:
            self._isClicked = False                                             # Setting isClicked False instantely when mouse is clicked down to prevent holding down the mouse
        screen.blit(self._rendered_text, buttonText)                            # Just the function to prevent the hover color to dominate the text in the button

# Class for buttons in the selection screen of the 2 Player game
class Selectorbuttons:
    def __init__(self, x, y, img, color):
        self._pos = (x,y)
        self._img = pygame.image.load(img)
        self._form = pygame.Rect(x, y, self._img.get_width(), self._img.get_height())
        self._color = color
        self._buttonBackground = pygame.image.load("images/woodButton.jpg") 
        self._buttonBackgroundTransform = pygame.transform.scale(self._buttonBackground, (self._img.get_width(), self._img.get_height()))       # Wood style background for Button scaled
        self._b_king = pygame.image.load("sprites/b_King.png")
        self._w_king = pygame.image.load("sprites/w_King.png")
        self._isClicked = False

    # This function draws the right button for the selection
    def drawButton(self, screen):
        if self._color == "black":
            pygame.draw.rect(screen, (0,0,0), self._form)
            screen.blit(self._buttonBackgroundTransform, self._form)         # This draws the black king button 
            screen.blit(self._b_king, self._form)
        if self._color == "white":
            pygame.draw.rect(screen, (0,0,0), self._form)
            screen.blit(self._buttonBackgroundTransform, self._form)         # This draws the white king button
            screen.blit(self._w_king, self._form)

        # Button logic
        mouse_pos = pygame.mouse.get_pos()                              # Checks which mouse button was clicked
        mouseClick = pygame.mouse.get_pressed()[0]
        global in_main_menu, two_player_game
        if self._form.collidepoint(mouse_pos): # Checks whether mouse is on button or not
            transparency = pygame.Surface(self._form.size, pygame.SRCALPHA)
            transparency.fill((0, 0, 255, 128))                                # Sets a transparency as a hover effect for the mouse
            screen.blit(transparency, self._form)
            if mouseClick and not self._isClicked: 
                self._isClicked = True
                transparency.fill((0,0,139,128))                               # If the mouse is clicked inside of a button isClicked should be True preventing from holding down the button
                screen.blit(transparency, self._form)
                if b_king._isClicked == True: 
                    print("schwarz beginnt")                               
                    


                if w_king._isClicked == True:
                    print("weiß beginnt")
                
                

                
            self._isClicked = mouseClick
        else:
            self._isClicked = False                                             # Setting isClicked False instantely when mouse is clicked down to prevent holding down the mouse
        

        
# This function designs the mainMenu 
def mainMenu(screen):
    if in_main_menu:
        background = pygame.image.load("images/chessBackground.jpg")              # If the global variable in_main_menu is True, the main menu should be drawn with a background image
        background = pygame.transform.scale(background, (1000, 700))       # Scales the background image
        screen.blit(background, (0,0))                                     # Draws the background image
        onePlayer.drawButton(screen)
        twoPlayer.drawButton(screen)                                       # Draws both buttons for game selection on the main menu

# This function will execute if the one player gamemode was selected
def onePlayerGameSelection(screen):
    if one_player_game:
        background = pygame.image.load("images/chessBackground.jpg")               # If the global variable one_player_game is True the background image should stay but the buttons schould vanish
        background = pygame.transform.scale(background, (1000, 700))
        screen.blit(background, (0,0))
        b_king.drawButton(screen)
        w_king.drawButton(screen)
        backToMenu.drawButton(screen)

def twoPlayerGame(screen):
    print("test")




# Initializing pygame
pygame.init()
pygame.font.init()
in_main_menu = True     
two_player_game = False
one_player_game = False
backToMenu = Buttons(0, 650, "Back to Menu", 50)
onePlayer = Buttons(50, 100, "1 Player Game", 50)
twoPlayer = Buttons(50, 200, "2 Player Game", 50)
b_king = Selectorbuttons(200, 100,"sprites/b_King.png", "black")
w_king = Selectorbuttons(200, 350, "sprites/w_King.png", "white")

# Main loop
running = True
timer = pygame.time.Clock()
fps = 60
pygame.display.set_caption("Chess")
screen = pygame.display.set_mode((1000, 700))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if in_main_menu:                # Checks the game state
        mainMenu(screen)
    if one_player_game:
        onePlayerGameSelection(screen)
    pygame.display.flip()