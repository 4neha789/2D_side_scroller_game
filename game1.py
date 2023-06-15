score = 0
# Inside the game loop
score += 1
# Import pygame module 
import pygame

# Import random for random numnbers
import random

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Display a player score
class Player(pygame.sprite.Sprite):
    def display_score():
        font = pygame.font.Font(None, 36)
        text = font.render("Score: " + str(score), True, (255, 255, 255))
        screen.blit(text, (10, 10))  # Adjust the position as per your preference


        # Inside the main game loop, after updating the screen
        display_score()
        # Before the game loop
        clock = pygame.time.Clock()

        # Inside the game loop
        clock.tick(60)
        # Adjust the frame rate as per your preference
        # Open the file
    file = open("scores.txt", "a")

   # Game logic
    player_name = input("Enter your name: ")
    score = int(input("Enter your score: "))

   # Write the player's name and score to the file
    file.write(player_name + "," + str(score) + "\n")

    # Close the file
    file.close()
    
# Define a player object by extending pygame.sprite.Sprite
# The surface dawn on the screen is now an attribute of "player"
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("C:\\Users\\Home\\Desktop\\pygame\\images\\jet.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()

    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
       try:
           if pressed_keys[K_UP]:
               self.rect.move_ip(0, -5)
               move_up_sound.play
           if pressed_keys[K_DOWN]:
               self.rect.move_ip(0, 5)
               move_down_sound.play
           if pressed_keys[K_LEFT]:
               self.rect.move_ip(0, -5)
               move_up_sound.play
           if pressed_keys[K_DOWN]:
               self.rect.move_ip(0, 5)
               move_down_sound.play
           if pressed_keys[K_LEFT]:
               self.rect.move_ip(-5, 0)
           if pressed_keys[K_RIGHT]:
               self.rect.move_ip(5, 0)

               # Keep player on the screen
           if self.rect.left < 0: 
              self.rect.left = 0
           if self.rect.right > SCREEN_WIDTH:
              self.rect.right = SCREEN_WIDTH
           if self.rect.top <= 0:
              self.rect.top = 0
           if self.rect.bottom >= SCREEN_HEIGHT:
              self.rect.bottom = SCREEN_HEIGHT
              # File handling code
           with open("data.txt", "w") as file:
                  file.write("Some data to write to the file")   
       except NameError as e:
            print("An NameError is occurred: {str(e)}")
    
