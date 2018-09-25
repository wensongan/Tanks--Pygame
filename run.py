'''
Author:Wenson Gan

Game Title:Tanks

Date: May/8/2015

Description: This program will be the main logic of my game tanks
'''
# I - Import and Initialize
import pygame, mySprites, random
pygame.init()
screen = pygame.display.set_mode((1080, 480))


def main():
    '''This function contains the main logic of the game'''
# Display
    pygame.display.set_caption("Raid of Red Square")
     
    # Entities
    background = pygame.image.load("background1.JPG")
    screen.blit(background, (0, 0))
    spawn_rate = 0
    score = 0
    counter = 0
    #Initialize audio
    pygame.mixer.init()
    pygame.mixer.music.load("Music\\background music.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)
    scream_effects = []
    for i in range(3):
        scream_effects.append(pygame.mixer.Sound("Sound effects\\Screams\\scream"+str(i+1) + ".wav"))
    for i in scream_effects:
        i.set_volume(1)
    explosion_effects = []
    for i in range(14):
        explosion_effects.append(pygame.mixer.Sound("Sound effects\\Explosions\\explosion"+str(i+1) + ".wav"))
    for i in explosion_effects:
        i.set_volume(0.2)    
          
    #Sprites
    endzone = mySprites.Endzone(screen)
    score_keeper = mySprites.ScoreKeeper()
    # Create tank
    player = mySprites.Player(screen) 
    # Create bullet list
    bullet_group = pygame.sprite.Group()
    infantry_group= pygame.sprite.Group()
    truck_group = pygame.sprite.Group()
    tank_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    powerup_group = pygame.sprite.Group()

    allsprites = pygame.sprite.OrderedUpdates(player,bullet_group,powerup_group,infantry_group,truck_group,tank_group,score_keeper,endzone)   
   
    # ACTION
     
    # Assign 
    keepGoing = True
    clock = pygame.time.Clock()
    
    # Loop
    while keepGoing:
     
       # Time
        clock.tick(30)
     
       # Events 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.go_up()
                elif event.key == pygame.K_LEFT:
                    player.go_left()
                elif event.key == pygame.K_DOWN:
                    player.go_down()
                elif event.key == pygame.K_RIGHT:
                    player.go_right()
                elif event.key == pygame.K_SPACE:
                    # Fire a bullet(s) if the user clicks space
                    if counter >10:
                        bullet = mySprites.Bullet(screen,player.get_direction(),player.get_x_coord(), player.get_y_coord(),player.get_power())
                        # Add the bullet to the lists
                        bullet_group.add(bullet)
                        allsprites.clear(screen, background)
                        allsprites = pygame.sprite.OrderedUpdates(player,bullet_group,powerup_group,infantry_group,truck_group,tank_group,score_keeper,endzone)   
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_DOWN or event.key == pygame.K_RIGHT or event.key == pygame.K_UP:
                    player.rest()   
        
        for tank in tank_group:
            if tank.get_shoot() == True:
                # Fire a bullet if the statement is true
                bullet = mySprites.Bullet(screen,7,tank.get_x(), tank.get_y(),3)
                # Add the bullet to the lists
                bullet_group.add(bullet)
                allsprites.clear(screen, background)
                allsprites = pygame.sprite.OrderedUpdates(player,bullet_group,powerup_group,infantry_group,truck_group,tank_group,score_keeper,endzone)   
                print "tank shot"
                print tank.get_x(), tank.get_y()
                
        if random.randrange(0,500) < spawn_rate:
            # Spawns an infantry by random
            infantry = mySprites.Infantry(screen,0,score_keeper, scream_effects)
            # Add the bullet to the lists
            infantry_group.add(infantry)
            enemy_group.add(infantry)
            allsprites.clear(screen, background)
            allsprites = pygame.sprite.OrderedUpdates(player, bullet_group, powerup_group,infantry_group, truck_group, tank_group, score_keeper,endzone)
            
        if spawn_rate > 1:
            if  random.randrange(0,1000) < spawn_rate:
                print "truck"
                # Create truck by random
                truck = mySprites.Vehicle(screen, score, "truck",score_keeper)
                # Add the truck to the group
                truck_group.add(truck)
                enemy_group.add(truck)
                allsprites.clear(screen, background)
                allsprites = pygame.sprite.OrderedUpdates(player,bullet_group,powerup_group,infantry_group,truck_group,tank_group,score_keeper,endzone)     
        if spawn_rate > 3:
            if  random.randrange(0,1500) < spawn_rate:
                print "tank"
                # Create tank by random
                tank = mySprites.Vehicle(screen, score, "tank",score_keeper)
                # Add the tank to the group
                tank_group.add(tank)
                enemy_group.add(tank)
                allsprites.clear(screen, background)
                allsprites = pygame.sprite.OrderedUpdates(player,bullet_group,powerup_group,infantry_group,truck_group,tank_group,score_keeper,endzone)   
        
        if random.randrange(0,1500) == 0:
            #Create powerup by random
            print "powerup"
            powerup = mySprites.Powerup(screen)
            powerup_group.add(powerup)
            allsprites.clear(screen, background)
            allsprites = pygame.sprite.OrderedUpdates(player,bullet_group,powerup_group,infantry_group,truck_group,tank_group,score_keeper,endzone)
            
        for bullet in bullet_group:
            #Check coliision detection with infantrys
            if bullet.get_type() == 0 or bullet.get_type() == 1:
                infantry_hit_list = pygame.sprite.spritecollide(bullet,infantry_group,False)
                for infantry in infantry_hit_list:
                    infantry.minus_health(bullet.get_damage())
                    bullet_group.remove(bullet)
                    allsprites.clear(screen, background)
                    allsprites = pygame.sprite.OrderedUpdates(player,bullet_group,powerup_group,infantry_group,truck_group,tank_group,score_keeper,endzone)   
                    
        for bullet in bullet_group:
             #Check coliision detection with trucks
            if bullet.get_type() == 0 or bullet.get_type() == 1:
                truck_hit_list = pygame.sprite.spritecollide(bullet,truck_group,False)
                for truck in truck_hit_list:
                    truck.minus_health(bullet.get_damage())
                    bullet_group.remove(bullet)
                    allsprites.clear(screen, background)
                    allsprites = pygame.sprite.OrderedUpdates(player,bullet_group,powerup_group,infantry_group,truck_group,tank_group,score_keeper,endzone)   
                    explosion_effects[random.randrange(1,14)].play()

        for bullet in bullet_group:
             #Check coliision detection with tanks
            if bullet.get_type() == 0 or bullet.get_type() == 1:
                tank_hit_list = pygame.sprite.spritecollide(bullet,tank_group,False)
                for tank in tank_hit_list:
                    tank.minus_health(bullet.get_damage())
                    bullet_group.remove(bullet)
                    allsprites.clear(screen, background)
                    allsprites = pygame.sprite.OrderedUpdates(player,bullet_group,powerup_group,infantry_group,truck_group,tank_group,score_keeper,endzone)   
                    explosion_effects[random.randrange(1,14)].play()
                    
        for bullet in bullet_group:
             #Check coliision detection with player
            if bullet.rect.colliderect(player.rect):
                if bullet.get_type() == 3:
                    bullet_group.remove(bullet)
                    allsprites.clear(screen, background)
                    allsprites = pygame.sprite.OrderedUpdates(player,bullet_group,powerup_group,infantry_group,truck_group,tank_group,score_keeper,endzone)
                    score_keeper.minus_armour(30)
                                 
        for powerup in powerup_group:
             #Check coliision detection with player
            if powerup.rect.colliderect(player.rect):
                if powerup.get_type() == 1:
                    player.powerup()
                    powerup.kill()
                elif powerup.get_type() == 2:
                    score_keeper.minus_armour(-40)
                    powerup.kill()
                    
        for enemy in enemy_group:
             #Check coliision detection with the end zone and deducts points(population) accordingly
            if enemy.rect.colliderect(endzone.rect):
                if str(enemy).lstrip("<").partition(" sprite")[0] == "Infantry":
                    enemy.revive()
                    score_keeper.minus_population(500000)
                elif str(enemy).lstrip("<").partition(" sprite")[0] == "Vehicle":
                    if enemy.get_type() == "truck":
                        score_keeper.minus_population(1000000)
                        enemy.kill()
                    elif enemy.get_type() == "tank":
                        score_keeper.minus_population(2500000)
                        enemy.kill()
                        
            if enemy.rect.colliderect(player.rect):
                #Decides what each enemy colission does to the player
                player.powerdown()
                try:
                    enemy.minus_health(10)
                except:
                    enemy.revive()
                explosion_effects[random.randrange(1,14)].play()
                score_keeper.minus_armour(1)
                        
        
        if spawn_rate < 6:
            #Controls spawn rate of the game increasing with difficulty
            if score_keeper.score() <100:
                spawn_rate = 3
            elif score_keeper.score() < 351:
                spawn_rate = int(score_keeper.score()/100)
            elif score_keeper.score() < 450:
                spawn_rate = int((score_keeper.score()*0.8) / 100)
            elif score_keeper.score() < 500:
                spawn_rate = int((score_keeper.score()*0.7) / 100)
                
                
        if counter >100:
            counter = 0
        counter += 1
        # Refresh screen
        allsprites.clear(screen, background)
        allsprites.update()
        truck_group.update()
        allsprites.draw(screen)
        pygame.display.flip()
 
    # Close the game window
    pygame.quit()     

# Call the main function
main()       