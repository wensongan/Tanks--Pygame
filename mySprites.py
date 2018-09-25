'''
Author: Wenson Gan

Game Title: Tanks

Date: May/8/2015

Description: This code contains all my sprites for the game Tanks
'''
import pygame, random

class Player(pygame.sprite.Sprite):
    def __init__(self, screen):
        '''Will take the game screen as a parameter'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        # Set inital movement        
        self.__dx = 0
        self.__dy = 0
        # Set screen dimensions
        self.__screen_width = screen.get_width()
        self.__screen_height = screen.get_height()
 
        # Set the image and rect attributes for the tank
        self.image_up = pygame.image.load("Tank sprites\\Tank-up.gif").convert_alpha()
        self.image_down = pygame.image.load("Tank sprites\\Tank-down.gif").convert_alpha()
        self.image_left = pygame.image.load("Tank sprites\\Tank-left.gif").convert_alpha()
        self.image_right = pygame.image.load("Tank sprites\\Tank-right.gif").convert_alpha()
        self.image_up_left = pygame.image.load("Tank sprites\\Tank-upleft.gif").convert_alpha()
        self.image_up_right = pygame.image.load("Tank sprites\\Tank-upright.gif").convert_alpha()
        self.image_down_left = pygame.image.load("Tank sprites\\Tank-downleft.gif").convert_alpha()
        self.image_down_right = pygame.image.load("Tank sprites\\Tank-downright.gif").convert_alpha()
        
        # Set the direction varaible
        self.__direction = 3
        # Set the initial picture and location
        self.image = self.image_right
        self.rect = self.image.get_rect()
        self.rect.centerx = 200
        self.rect.centery = 200 
        
        self.__power = 0
        
    def powerup(self):
        '''Will increase player power when called'''
        if self.__power <1:
            self.__power += 1
            
    def powerdown(self):
        '''Will decrease player power when called'''
        if self.__power > 0:
            self.__power -= 1
            
    def get_power(self):
        '''Will return player power when called'''
        return self.__power
            
    def rest(self):
        '''Puts the player to a rest'''
        self.__dx = 0
        self.__dy = 0

    def go_left(self):
        '''Will move the player left'''
        self.__dx = -2
        
    def go_right(self): 
        '''Will move the player right'''
        self.__dx = 2
        
    def go_up(self):
        '''Will move the player up'''
        self.__dy = -2
        
    def go_down(self):
        '''Will move the player down'''
        self.__dy = 2
        
    def get_direction(self):
        '''Will return player direction'''
        return self.__direction

    def get_x_coord(self):
        '''Will return player x coord'''
        return self.rect.centerx
    
    def get_y_coord(self):
        '''Will return player y coord'''
        return self.rect.centery
    
    def update(self):
        '''Automatically gets called to update the sprite'''
        if (self.__dx != 0) :
            self.rect.right += self.__dx
        #Ensures the player is within the game screen and its boundaries given
        if (self.rect.left < 55) or (self.rect.right > self.__screen_width - 55):
            self.__dx = 0
            if self.rect.left < 50:
                self.rect.right += 5
            elif self.rect.right > self.__screen_width - 50:
                self.rect.right -= 5
        #Updates player location and allows for movement
        if (self.__dy !=0) :
            self.rect.top += self.__dy
        if (self.rect.top < 5) or (self.rect.bottom > self.__screen_height - 5):
            self.__dy = 0
            if self.rect.top < 0:
                self.rect.top += 5
            elif self.rect.bottom >self.__screen_height - 5:
                self.rect.top -= 5
        #Updates player image according to its movement
        if self.__dy < 0:
            if self.__dx > 0:
                self.image = self.image_up_right
                self.__dx = 1
                self.__dy = -1
                self.__direction = 2
            elif self.__dx < 0:
                self.image = self.image_up_left
                self.__dx = -1
                self.__dy = -1       
                self.__direction = 8
            elif self.__dx == 0:
                self.image = self.image_up
                self.__direction = 1
        elif self.__dy > 0:
            if self.__dx > 0:
                self.image = self.image_down_right
                self.__dx = 1
                self.__dy = 1     
                self.__direction = 4
            elif self.__dx < 0:
                self.image = self.image_down_left
                self.__dx = -1
                self.__dy = 1     
                self.__direction = 6
            elif self.__dx == 0:
                self.image = self.image_down
                self.__direction = 5
        elif self.__dy == 0:
            if self.__dx > 0:
                self.image = self.image_right
                self.__direction = 3
            elif self.__dx < 0:
                self.image = self.image_left
                self.__direction = 7
                
class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, direction, x_coord, y_coord, bullet_type):
        '''This takes the game screen, direction to be shot, x and y starting coords and bullet type as parameters'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        #Set variables for the screen dimensions
        self.__screen_width = screen.get_width()
        self.__screen_height = screen.get_height()
        
        self.image = pygame.Surface((10,10)).convert_alpha()
        if bullet_type == 0:
            self.image = pygame.image.load("Flying entities\\Bullets\\player_bullet.png").convert_alpha()
        elif bullet_type ==3:
            self.image = pygame.image.load("Flying entities\\Bullets\\enemy_bullet.png").convert_alpha()
 
        # Set the bullet
        self.__hostile_bullet = bullet_type
        
        self.__rockets = []
        for i in range(8):
            self.__rockets.append(pygame.image.load("Flying entities\\Rockets\\rocket"+str(i+1)+".png").convert_alpha())
    
        # Set image variables according to the game        
        if direction == 3 and (bullet_type == 1):
            self.image = self.__rockets[2]
        elif direction == 7 and (bullet_type == 1):
            self.image = self.__rockets[6]         
        elif direction == 1 and (bullet_type == 1):
            self.image = self.__rockets[0]       
        elif direction == 5 and (bullet_type == 1):
            self.image = self.__rockets[4]
        elif direction == 2 and (bullet_type == 1):
            self.image = self.__rockets[1]
        elif direction == 8 and (bullet_type == 1):
            self.image = self.__rockets[7]
        elif direction == 4 and (bullet_type == 1):
            self.image = self.__rockets[3]
        elif direction == 6 and (bullet_type == 1):
            self.image = self.__rockets[5]
             
        #Set location and rect
        self.rect = self.image.get_rect()
        self.rect.centerx =  x_coord
        self.rect.centery =  y_coord
        
        
        #Set direction
        if direction == 3:
            self.__dx = 7
            self.__dy = -0
        elif direction == 7:
            self.__dx = -7
            self.__dy = -0            
        elif direction == 1:
            self.__dx = 0
            self.__dy = -7            
        elif direction == 5:
            self.__dx = 0
            self.__dy = 7
        elif direction == 2:
            self.__dx = 5
            self.__dy = -5
            self.rect.centerx += 5  
            self.rect.centery += 5
        elif direction == 8:
            self.__dx = -5
            self.__dy = -5        
        elif direction == 4:
            self.__dx = 5
            self.__dy = 5
        elif direction == 6:
            self.__dx = -5
            self.__dy = 5    
            self.rect.centerx += 10
            self.rect.centery += 1        
        
        if bullet_type == 0 :
            self.__damage = 1
        elif bullet_type == 1:
            self.__damage = 2
            
    def get_type(self):
        '''Will return the type of bullet when called'''
        return self.__hostile_bullet
    
    def get_damage(self):
        '''Will return the amount of damage when called'''
        return self.__damage
        
    def update(self):
        '''Automatically gets called to update the sprite'''
        if self.__dx != 0:
            self.rect.right += self.__dx
        else:
            self.rect.right = self.rect.right
            
        if self.__dy != 0:
            self.rect.top += self.__dy
        if self.rect.right > self.__screen_width or self.rect.left < 0 or self.rect.bottom > self.__screen_height or self.rect.top < 0:
            self.kill()
            
class Infantry(pygame.sprite.Sprite):
    def __init__(self, screen, score, score_keeper,scream_effects):
        '''This takes the game screen, score and score_keeper sprite as well as the audio for the scream effects as parameters'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)    
        
        #Set variables for the screen dimensions
        self.__screen_width = screen.get_width()
        self.__screen_height = screen.get_height()
        
        #Create image list
        self.__image_list = []
        #Append the different type of screams
        for i in range(2):
            self.__image_list.append(pygame.image.load ("Soldier sprites\\Soldier 1\\soldier"+str(i)+".png"))       
        #Create scream effects variable
        self.__scream_effects = scream_effects
        
        #Create image and define rects and location
        self.image = self.__image_list[0]
        self.rect = self.image.get_rect()
        self.rect.left = self.__screen_width 
        #Set random spawn locations
        self.rect.top = random.randrange(50, self.__screen_height-20) 
        
        #Define a counter and frame variable as well as a scorekeeping variable
        self.__counter = 0
        self.__frame = 0
        self.__score_keeper = score_keeper
        #Make the infantry move towards the target
        self.__dy = 0
        self.__dx = -0.1
        
        #Adjust the difficulty of infantry by changing their health value
        if score > 1000:
            self.__health =2
        else:
            self.__health =1 
        
    def revive(self):
        '''Will respawn the infantry at the left side of the screen'''
        self.rect.left = self.__screen_width 
        self.rect.top = random.randrange(0, self.__screen_height) 
        
    def get_health(self):
        '''Will return the amount of health the infantry has'''
        return self.__health
    
    def minus_health(self, health):
        '''Will subtract health accordingly taking health as a parameter'''
        self.__health -= health    
        
    def update(self):
        '''Automatically gets called to update the sprite'''
        if self.__counter <10:
            self.__frame = 0
        else:
            self.__frame = 1
        self.image = self.__image_list[self.__frame]
        self.__counter += 1
        if self.__counter > 20:
            self.__counter = 0
        self.rect.left += self.__dx
        if self.__health <= 0:
            if random.randrange(0,3) == 0:
                self.__scream_effects[(random.randrange(0,2)+1)].play()
            self.kill()
            self.__score_keeper.player_points(20)

class Vehicle(pygame.sprite.Sprite):
    def __init__(self, screen, score, vehicle,score_keeper):
        '''This takes the game screen, score, vehicle type as well as the score_keeper sprite as parameters'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)   
        
        #Set variables for the screen dimensions
        self.__screen_width = screen.get_width()
        self.__screen_height = screen.get_height()
        
        #Make the infantry move towards the target
        self.__dx = -0.1
        self.__shoot = False
        self.__type = vehicle
        self.__score_keeper = score_keeper
        self.__counter = 0
        #Create explosion image list
        self.__explosion_list =[]
        for i in range(1,13):
                    self.__explosion_list.append(pygame.image.load ("Explosions\\selfmade explosion\\explosion"+str(i)+".png"))         
        
        #Create image and define rects and location
        if self.__type == "truck":
            #Create image and define rects and location
            self.image = pygame.image.load("Jeeps\\jeep"+str(random.randrange(0,2)) +".png")
            self.rect = self.image.get_rect()
            self.rect.right = self.__screen_width
            #Set random spawn locations
            self.rect.top = random.randint(50, self.__screen_height-20)
            print "truck sprite"
            self.__dx = -0.5
            if score > 1000:
                self.__health =3
            else:
                self.__health =2
        elif self.__type == "tank":
            #Create image and define rects and location
            self.image = pygame.image.load("Enemy Tank sprites\\tank"+ str(random.randrange(1,6)) + ".png")
            self.rect = self.image.get_rect()
            self.rect.right = self.__screen_width
            #Set random spawn locations
            self.rect.top = random.randint(30, self.__screen_height-30)
            print "tank sprite"
            self.__dx = -0.05
            if score > 1000:
                self.__health =5
            else:
                self.__health =3            
            
    def get_health(self):
        '''will return the health value of the vehicle'''
        return self.__health
    
    def get_type(self):
        '''will return the type of the vehicle'''
        return self.__type
    
    def minus_health(self, health):
        '''will subtract health accordintly taking health as a parameter'''
        self.__health -= health
    
    def get_shoot(self):
        '''will return the status of the vehicle shooting'''
        return self.__shoot
    
    def get_x(self):
        '''will return the x value of the vehicle '''
        return self.rect.left
        
    def get_y(self):
        '''will return the y value of the vehicle'''
        return self.rect.centery    
                
    def update(self):
        '''Automatically gets called to update the sprite'''
        self.rect.centerx += self.__dx
        if self.__health <= 0:
            self.__dy =0
            self.__dx =0
            self.__counter += 1
            self.__frame = self.__counter/3
            self.image = self.__explosion_list[self.__frame+1]
            if self.__counter >= 30:
                self.kill()
                if self.__type == "tank":
                    self.__score_keeper.player_points(80)
                elif self.__type =="truck":
                    self.__score_keeper.player_points(40)
        if self.__type == "tank":
            if self.__shoot == True:
                self.__shoot = False
            if random.randrange(0,120) == 0:
                self.__shoot = True
class ScoreKeeper(pygame.sprite.Sprite):
    '''This class defines a label sprite to display the score.'''
    def __init__(self):
        '''This initializes the variables for the class'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
 
        # Load our custom font, and initialize the starting score.
        self.__font = pygame.font.Font("Russian.TTF", 30)
        self.__playerscore = 0
        self.__population = 12197596
        
        # Set up variable to keep track of armour
        self.__armour = 100
        
    def player_points(self, score):
        '''This method adds one to the score for player 1. Taking the score as a parameter'''
        self.__playerscore += score
    
    def minus_armour(self, value):
        '''This method will deduct lives when the ball hits the end zone. Taking value as a parameter'''
        self.__armour -= value
        
    def minus_population(self, value):
        '''This method will deduct lives for the population taking valee as a parameter'''
        self.__population -= value

    def score(self):
        '''This will return the score of the game'''
        return self.__playerscore

    def update(self):
        '''This method will be called automatically to display 
        the current score at the top of the game window.'''
        #REVISE THIS PART

        if self.__armour <= 0 or self.__population <= 0:
            if self.__armour <= 0:
                message = "Game over You died!"
            else:
                message = "You failed to protect Mother Russia"
            self.image = self.__font.render(message, 1, (144, 144, 144))
            self.rect = self.image.get_rect()
            self.rect.center = (540, 15)   
        elif self.__playerscore < 10000:
            message = "Armour:%d  Score:%d  Population:%d "% (self.__armour, self.__playerscore, self.__population)
            self.image = self.__font.render(message, 1, (144, 144, 144))
            self.rect = self.image.get_rect()
            self.rect.center = (540, 15)

            
class Endzone(pygame.sprite.Sprite):
    def __init__(self, screen):
        '''This initializer loads the system font "Arial", and
        sets the starting score to 0:0'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        #Set variables for the screen dimensions
        self.__screen_width = screen.get_width()
        self.__screen_height = screen.get_height()        
        
        # Set the image and attributes
        self.image = pygame.Surface((5,self.__screen_width)).convert_alpha()
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.right = 1
        self.rect.top = 0
        
class Powerup(pygame.sprite.Sprite):
    def __init__(self, screen):
        '''This initializer loads the system font "Arial", and
        sets the starting score to 0:0'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        #Set variables for the screen dimensions
        self.__screen_width = screen.get_width()
        self.__screen_height = screen.get_height()
        
        self.__type = random.randrange(1,3)
        
        # Set the image and attributes
        self.image = pygame.image.load("Power ups\\powerup"+ str(self.__type) + ".png")
        self.rect = self.image.get_rect()
        if random.randrange(0,2) ==0:
            self.rect.right = self.__screen_width
            self.rect.top = 0
            self.__dy = 1
            self.__dx = -1
        else:
            self.rect.right = self.__screen_width
            self.rect.bottom = self.__screen_height
            self.__dy = -1
            self.__dx = -1
        print"power up created"
        print self.rect.centerx
        print self.rect.centery
            
    def get_type(self):
        '''This will return the type of powerup that is being used'''
        return self.__type
    
    def update(self):
        '''Automatically gets called to update the sprite'''
        if self.rect.top < 0:
            self.__dy= -self.__dy
        elif self.rect.bottom > self.__screen_height:
            self.__dy= -self.__dy
            
        self.rect.centerx += self.__dx
        self.rect.centery += self.__dy
        
        if self.rect.left <0:
            self.kill()
