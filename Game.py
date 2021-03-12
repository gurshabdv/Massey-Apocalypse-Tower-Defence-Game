from pygame import *
from math import * # Used for calculating sine and cosine of angles when shooting bullets
from random import * # Used to choose a random number for the tips loading screen
from os import path # Used to locate files from the computer for the high score feature

init()

width,height=1200,700# Set the width and the height of the screen to 1200 by 700
screen=display.set_mode((width,height))

score=0 # set innitial score to 0

def gamepause(level_available):
    # gamepasue function takes no parameters. When the player presses p, it pauses the game,
    #if the press c it continues the game, if they press q it quit to the main menu
    width,height=1200,700
    white=(255,255,255)
    black=(0,0,0)
    red=(255,0,0)
    blue=(0,0,255)
    health=3
    font.init()# innitializing the font
    paused=True
    myClock=time.Clock()
    while paused:# while pasued is equal to True
        for evt in event.get():
            if evt.type==QUIT:# if screen is closed, the player will return to the main menu
                quit()# the value of action will be switched to "menu"
            if evt.type==KEYDOWN:# if a key is pressed on the keyboard
                if evt.key==K_c:# if the c key is pressed
                    paused=False# the game will continue
                if evt.key==K_q:# if the q key is pressed
                    menu("menu",level_available)# the game will quit
        pause_screen=Surface((1200,700),SRCALPHA)# when the user clicks pause, a white scren will be shown
        pause_screen.fill((255,255,255,5))
        screen.blit(pause_screen,(0,0))
        pause_text=font.SysFont("Chiller",60)
        pause_text=pause_text.render("PAUSED",True,black)
        screen.blit(pause_text,(500,300))
        cq_text=font.SysFont("Chiller",30)
        cq_text=cq_text.render("Press C to Continue, Press Q to Quit",True,black)
        screen.blit(cq_text,(425,375))
        display.update()
        #myClock.tick(30)

def gameover(level_available):
    # game over function takes one parameters. The parameter determines which level was lost in order to display the correct menu screen.
    #This function is used when the health of the base reaches 0.
    bg=image.load("Maps/Map1.jpg").convert()
    bg=transform.scale(bg,(1000,700))
    white=(255,255,255)
    black=(0,0,0)
    red=(255,0,0)
    blue=(0,0,255)
    gameover_screen=image.load("Intro/gameover.png").convert()
    gameover_screen=transform.scale(gameover_screen,(1200,700))
    font.init()# innitializes the font
    dim=Surface((1200,700))
    dim.fill((179,0,0))
    over=True# function will run as long as the value of over is True
    myClock=time.Clock()
    while over:
        for evt in event.get():
            if evt.type==QUIT:
                menu("menu",level_available)
            if evt.type==KEYDOWN:
                if evt.key==K_r:# if r key is pressed
                    for alpha in range(0,255):# the range is to slowly change the opacity of the background from 0 to 255. This creates a fading effect
                        dim.set_alpha(alpha)
                        screen.blit(bg,(0,0))
                        screen.blit(dim,(0,0))
                        display.update()
                        time.delay(5)#Opacity increases every 5 milliseconds
                    menu("menu",level_available)# after the fading efect is completed, screen wil swith to the menu
        #before the r key is pressed the following occurs ...            
        screen.blit(gameover_screen,(0,0))#game over screen is shown
        gameover_text=font.SysFont("Chiller",50)
        gameover_text=gameover_text.render("Press R to Return to Menu",True,white)# instructs the user to press r to retuen to the menu
        screen.blit(gameover_text,(375,600))

            
        display.update()
        myClock.tick(60)

def loading(action):
    # this function is displayed after the user chooses their level. It displays a random tp that is helpful to the player. It takes one parameter called action
    # list that contains the properties for the first wave of enemies
    ###         x   y  frame alive delay timer lives   (2 seconds delay (30,150,270)  1 second=60 frames)  
    enemies=[[-100,500,  0,  True,   60,        5], [-100,500,0,True,120,5],[-100,500,0,True,180,5],[-100,500,0,True,240,5],[-100,500,0,True,300,5],[-100,500,0,True,360,5],[-100,500,0,True,420,5],[-100,500,0,True,480,5],[-100,500,0,True,540,5],[-100,500,0,True,600,5],[-100,500,0,True,660,5],[-100,500,0,True,720,5],[-100,500,0,True,780,5],[-100,500,0,True,840,5],[-100,500,0,True,900,5],[-100,500,0,True,960,5],[-100,500,0,True,1020,5],[-100,500,0,True,1080,5],[-100,500,0,True,1140,5],[-100,500,0,True,1200,5]]                                                                                                                                                                                                                                                                             
    enemies2=[[-100,500,  0,  True,   60,        7], [-100,500,0,True,120,7],[-100,500,0,True,180,7],[-100,500,0,True,240,7],[-100,500,0,True,300,7],[-100,500,0,True,360,7],[-100,500,0,True,420,7],[-100,500,0,True,480,7],[-100,500,0,True,540,7],[-100,500,0,True,600,7],[-100,500,0,True,660,7],[-100,500,0,True,720,7],[-100,500,0,True,780,7],[-100,500,0,True,840,7],[-100,500,0,True,900,7],[-100,500,0,True,960,7],[-100,500,0,True,1020,7],[-100,500,0,True,1080,7]]                                                                                                                                                                                                                                                                             
    enemies3=[[-100,500,  0,  True,   60,        9], [-100,500,0,True,120,9],[-100,500,0,True,180,9],[-100,500,0,True,240,9],[-100,500,0,True,300,9],[-100,500,0,True,360,9],[-100,500,0,True,420,9],[-100,500,0,True,480,9],[-100,500,0,True,540,9],[-100,500,0,True,600,9],[-100,500,0,True,660,9],[-100,500,0,True,720,9],[-100,500,0,True,780,9],[-100,500,0,True,840,9],[-100,500,0,True,900,9],[-100,500,0,True,960,9]]                                                                                                                                                                                                                                                                             
    white=(255,255,255)
    black=(0,0,0)
    red=(255,0,0)
    blue=(0,0,255)
    font.init()# innitializes the font
    tip=randint(1,5)# chooses a random number from 1 to 5
    space=font.SysFont("Chiller",50)
    space=space.render("Press the Number of Your Level to Continue",True,red)# prompts the user to enter a keyboard input of their level
    loading=True
    myClock=time.Clock()
    while action=="loading":# as long as the value of loading is equal to True
        for evt in event.get():
            if evt.type==QUIT:
                action="menu"# if the user quits from the screen they will go back to menu
            if evt.type==KEYDOWN:
                if evt.key==K_1:# if the user inputs 1
                    start("start",enemies,6,3,"Enemies1","wave 1",1,20,15)# go to level 1
                elif evt.key==K_2:# if the user inputs 2
                    start("start",enemies2,4,4,"Enemies2","wave 2",2,18,20)# go to level 2
                elif evt.key==K_3:# if the user inputs 3
                    start("start",enemies3,8,5,"Enemies3","wave 3",3,16,25)# go to level 3
        waveBG=image.load("Intro/blood.jpg")
        waveBG=transform.scale(waveBG,(1200,700))
        warning_text=font.SysFont("Chiller",45)
        warning_text=warning_text.render("NOTE: Once Weapon is placed on the path, Previously placed weapons will not shoot !!!",True,black)
        screen.blit(waveBG,(0,0))
        screen.blit(space,(275,600))
        tip_text=font.SysFont("Chiller",40)
        # based on the random number that tip is assigned to.
        # the corresponding tip will be displayed
        if tip==1:
            tip_text=tip_text.render("The more expensive a cannon is, the more damage it deals!",True,black)
            screen.blit(tip_text,(270,375))
            screen.blit(warning_text,(13,500))
        elif tip==2:
            tip_text=tip_text.render("Buy multiple cannons to defeat the zombies faster!",True,black)
            screen.blit(tip_text,(315,375))
            screen.blit(warning_text,(13,500))
        elif tip==3:
            tip_text=tip_text.render("For every defeated zombie, you will receive 3,4 or 5 coins. Use them wisely!",True,black)
            screen.blit(tip_text,(180,375))
            screen.blit(warning_text,(13,500))
        elif tip==4:
            tip_text=tip_text.render("Remember – your coins reset after every round!",True,black)
            screen.blit(tip_text,(335,375))
            screen.blit(warning_text,(13,500))
        else:
            tip_text=tip_text.render("Be careful with your shots, you only have 3 lives!",True,black)
            screen.blit(tip_text,(265,375))
            screen.blit(warning_text,(13,500))
        display.update()
        myClock.tick(60)


def menu(action,level_available):
    white=(255,255,255)
    black=(0,0,0)
    red=(255,0,0)
    blue=(0,0,255)
    font.init()
    intro_bg=image.load("Intro/game_intro.png")
    intro_gb=transform.scale(intro_bg,(1200,700))
    buttons=[Rect(850,250,200,50),Rect(850,350,200,50),Rect(850,450,200,50)]# list of buttons in the shape of rectangles
    count=10# the number of coins that the player statrs with is 15
    health=3# the base statrs off with a health of 3
    myClock=time.Clock()
    while action=="menu":
        screen.blit(intro_bg,(0,0)) 
        intro_text=font.SysFont("Chiller",100)
        intro_text=intro_text.render("Massey Apocalypse",True,black)
        # 4 buttons are displayed from which the user can go to either level 1, 2, 3 or instructions
        level1_text=font.SysFont("Chiller",40)
        level1_text=level1_text.render("LEVEL 1",True,white)
        level2_text=font.SysFont("Chiller",40)
        level2_text=level2_text.render("LEVEL 2",True,white)
        level3_text=font.SysFont("Chiller",40)
        level3_text=level3_text.render("LEVEL 3",True,white)
        ins_text=font.SysFont("Chiller",40)
        ins_text=ins_text.render("INSTRUCTIONS",True,white)
        print("menu")
        for evnt in event.get():            
            if evnt.type == QUIT:# if the user quits
                # the game will close
                quit()
                
        mx,my=mouse.get_pos()# determining the coordinates of the mouse
        mb=mouse.get_pressed()# determining if mouse is being pressed
        for b in buttons[0:level_available]:# loop throught the list of buttons
            # display all of the text that needs to be on the meun screen
            # The following 21 lines of code determine how the menu screen is going to look based on how many levels/waves the player has completed
            # When the player statrs, only the level 1 button will be available. Once the player beats level 1, the level 2 button will become available. etc.  
            if level_available==1:
                ins_rect=Rect(850,550,300,50)
                draw.rect(screen,black,ins_rect)
                draw.rect(screen,black,b)
                
                screen.blit(intro_text,(20,10))
                screen.blit(level1_text,(860,250))
                screen.blit(ins_text,(860,550))
            elif level_available==2:
                ins_rect=Rect(850,550,300,50)
                draw.rect(screen,black,ins_rect)
                draw.rect(screen,black,b)
                
                screen.blit(intro_text,(20,10))
                screen.blit(level1_text,(860,250))
                screen.blit(level2_text,(860,350))
                screen.blit(ins_text,(860,550))
            elif level_available==3:
                ins_rect=Rect(850,550,300,50)
                draw.rect(screen,black,ins_rect)
                draw.rect(screen,black,b)
                
                screen.blit(intro_text,(20,10))
                screen.blit(level1_text,(860,250))
                screen.blit(level2_text,(860,350))
                screen.blit(ins_text,(860,550))
                screen.blit(level3_text,(860,450))

            elif level_available==4:
                ending()

        
                
        if mb[0]==1:# if left clicking
            # if one of the level buttons are clicked, call the loading function
            if buttons[0].collidepoint(mx,my):
                loading("loading")
            elif buttons[1].collidepoint(mx,my):
                loading("loading")
            elif buttons[2].collidepoint(mx,my):
                loading("loading")
            # if instructions button is clicked, call on the instructions function    
            elif ins_rect.collidepoint(mx,my):
                instructions("ins")
        
        display.flip()
        myClock.tick(60)

def gameFinish(wave_number,level_available):
    # the function takes wave_number as parameter to determine which wave has just been completed. The function also takes level available in order to display the
    # correct menu screen
    #   This function is displayed when the user completes a level.
    white=(255,255,255)
    black=(0,0,0)
    red=(255,0,0)
    end=image.load("Intro/end.jpg").convert()
    end=transform.scale(end,(1200,700))
    font.init()
    done=True
    myClock=time.Clock()
    while done:
        for evt in event.get():
            if evt.type==QUIT:# if the player quits
                return menu("menu",level_available)# the game closes
            if evt.type==KEYDOWN:# if a keyboard input is detected
                if evt.key==K_r:# if r key is pressed
                    return menu("menu",level_available)# return to menu
        # before r key is pressed            
        screen.blit(end,(0,0))#display the level complete screen
        endtext1=font.SysFont("Chiller",50)
        endtext1=endtext1.render("Congratulations, you survived "+wave_number+"...",True,red)
        screen.blit(endtext1,(350,300))
        gamefinish_text=font.SysFont("Chiller",50)
        gamefinish_text=gamefinish_text.render("Press R to Return to Menu",True,white)
        screen.blit(gamefinish_text,(375,600))
        display.update()
        myClock.tick(60)

def ending():
    # Ending function takes no parameters. It is called when the player is done the whole game
    white=(255,255,255)
    ending=True
    myClock=time.Clock()
    while ending:
        for evt in event.get():
            if evt.type==QUIT:
                menu("menu",3)
            if evt.type==KEYDOWN:
                if evt.key==K_r:
                    menu("menu",3)
        youWin=image.load("Intro/youWin.jpg")
        youWin=transform.scale(youWin,(1200,700))
        menu_text=font.SysFont("Chiller",50)
        menu_text=menu_text.render("Press R to return to menu", True, white)
        screen.blit(youWin,(0,0))
        screen.blit(menu_text,(450,550))
        display.update()
        myClock.tick(60)
    
    
def start(action,enemytype,enemysprites,enemycoins,enemyfile,wave_number,level_available,zombie_number,start_coins):
    # this function is called upon when the player wants to proceed to the level. It takes the following parameters - action whcih must be assigned to "start",
    # eneytype which is the liast that is being used, enemysprites whcih is the number of sprites there are for a certain enemy, enemycoins whcih is how many coins
    # the player recieves if the kill the enemy, enemyfile which is the file where the pictures of enemy sprites are located, and wave_number which is the numerical
    # value of the level that the player is about to start. level_available is the level that th eplayer is on plus one. this helps to determine which menu screen
    # will be displayed once the player has beat the game. zombie_number is the amount of zombies there are for each level. start_coins is how many coins the player
    # statrs with for each level 
    font.init()# innitializes font
               #0                 #1              #2                 #3
    playlist=["Music/song1.mp3","Music/song2.mp3","Music/song3.mp3","Music/song4.mp3"]#playlist of all songs
    currentSong=0#default song is song1.mp3
    mixer.music.load(playlist[currentSong])#loading all songs
    mixer.music.play(-1)#playing on a loop

    number_of_enemies=zombie_number# number of enemies is different for each wave

    vol=0.5#default volume

    # empty list of rectangles where rectangles that are dragged and dropped will be appended to
    myRects0=[]
    myRects1=[]
    myRects2=[]
    myRects3=[]
    myRects4=[]

    myWeapons0=[]
    myWeapons1=[]
    myWeapons2=[]
    myWeapons3=[]
    myWeapons4=[]
    
    print("starting")

    score=0# innitial score is 0. Score will increase everytimr a zombie is killed

    rapid=20

    #Loading in images for music------------------------------
    volumeDown=image.load("Music/volumeDown.png")
    volumeDown=transform.scale(volumeDown,(40,40))
    volumeUp=image.load("Music/volumeUp.png")
    volumeUp=transform.scale(volumeUp,(40,40))
    shuffle=image.load("Music/shuffle.png")
    shuffle=transform.scale(shuffle,(40,40))
    pause=image.load("Music/pause.png")
    pause=transform.scale(pause,(40,40))
    play=image.load("Music/play.png")
    play=transform.scale(play,(40,40))

    shufRect=Rect(20,170,40,40)
    pauseRect=Rect(80,170,40,40)
    playRect=Rect(140,170,40,40)
    vdRect=Rect(50,230,40,40)
    vuRect=Rect(110,230,40,40)

    #loading and resizing song covers-------------------------------
    monstermash=image.load("Music/monstermash.jpg")
    monstermash=transform.scale(monstermash,(100,100))
    halloween=image.load("Music/halloween.png")
    halloween=transform.scale(halloween,(100,100))
    monster=image.load("Music/monster.jpg")
    monster=transform.scale(monster,(100,100))
    themonster=image.load("Music/themonster.jpg")
    themonster=transform.scale(themonster,(100,100))

    # set of rectangles that the zombies will follow (in accordance to the path on the map)
    route=[Rect(440,390,40,140),Rect(440,385,140,5),Rect(580,320,40,140),Rect(580,40,280,280),Rect(860,40,10,10)]

    # set of retangles that make up the path. This will prevent the user from using weapons that they have placed on the map
    path=[Rect(0,580,440,20),Rect(455,440,40,140),Rect(520,440,100,20),Rect(600,345,40,105),Rect(640,315,30,30),Rect(670,285,30,30),Rect(700,255,30,30),Rect(730,225,30,30),Rect(760,195,30,30),Rect(790,165,30,30)]


    white=(255,255,255)
    black=(0,0,0)
    red=(255,0,0)
    blue=(0,0,255)

    ###         x   y  frame alive delay timer lives   (2 seconds delay (30,150,270)  1 second=60 frames)
    enemies=[[-100,500,  0,  True,   60,        5], [-100,500,0,True,120,5],[-100,500,0,True,180,5],[-100,500,0,True,240,5],[-100,500,0,True,300,5],[-100,500,0,True,360,5],[-100,500,0,True,420,5],[-100,500,0,True,480,5],[-100,500,0,True,540,5],[-100,500,0,True,600,5],[-100,500,0,True,660,5],[-100,500,0,True,720,5],[-100,500,0,True,780,5],[-100,500,0,True,840,5],[-100,500,0,True,900,5],[-100,500,0,True,960,5],[-100,500,0,True,1020,5],[-100,500,0,True,1080,5],[-100,500,0,True,1140,5],[-100,500,0,True,1200,5]]                                                                                                                                                                                                                                                                             
    enemies2=[[-100,500,  0,  True,   60,        7], [-100,500,0,True,120,7],[-100,500,0,True,180,7],[-100,500,0,True,240,7],[-100,500,0,True,300,7],[-100,500,0,True,360,7],[-100,500,0,True,420,7],[-100,500,0,True,480,7],[-100,500,0,True,540,7],[-100,500,0,True,600,7],[-100,500,0,True,660,7],[-100,500,0,True,720,7],[-100,500,0,True,780,7],[-100,500,0,True,840,7],[-100,500,0,True,900,7],[-100,500,0,True,960,7],[-100,500,0,True,1020,7],[-100,500,0,True,1080,7]]                                                                                                                                                                                                                                                                             
    enemies3=[[-100,500,  0,  True,   60,        9], [-100,500,0,True,120,9],[-100,500,0,True,180,9],[-100,500,0,True,240,9],[-100,500,0,True,300,9],[-100,500,0,True,360,9],[-100,500,0,True,420,9],[-100,500,0,True,480,9],[-100,500,0,True,540,9],[-100,500,0,True,600,9],[-100,500,0,True,660,9],[-100,500,0,True,720,9],[-100,500,0,True,780,9],[-100,500,0,True,840,9],[-100,500,0,True,900,9],[-100,500,0,True,960,9]]                                                                                                                                                                                                                                                                             


    bg=image.load("Maps/Map1.jpg").convert()#loading the map
    bg=transform.scale(bg,(1000,700))# resizing the map

    # original location of the rectangles that can be dragged and droppped
    rectangle0=Rect(1030,100,50,50)
    rectangle1=Rect(1120,100,50,50)
    rectangle2=Rect(1030,200,50,50)
    rectangle3=Rect(1120,200,50,50)
    rectangle4=Rect(1030,300,50,50)

    # before the rectangles are clicked on they cannot be dragged meaning that their dragging value is innitially assigned to false 
    rectangle_draging0= False
    rectangle_draging1= False
    rectangle_draging2= False
    rectangle_draging3= False
    rectangle_draging4= False

    currentSong=0# the count of the current song is 0
    pics1=[]# empty list into which the images of the zombie sprites will be appended to.
    
    count=start_coins# players start off with different coins for each level
    health=3# the base starts off with health of 3
    #print("sega")
    bgRect=Rect(0,0,1000,700)# draws teh background rectangle

    # draws a resizes the sidebar from where the weapons can be dragged and dropped 
    grey=image.load("Weapons/grey.png").convert()
    grey=transform.scale(grey,(200,700))

    # loads all three images of the health bars
    health3=image.load("Health/health3.png")
    health3=transform.scale(health3,(100,35))

    health2=image.load("Health/health2.png")
    health2=transform.scale(health2,(100,35))

    health1=image.load("Health/health1.png")
    health1=transform.scale(health1,(100,35))

    # loads images of the different weapons 
    cannonPic1=image.load("Weapons/cannon1.png").convert_alpha()
    cannonPic1=transform.scale(cannonPic1,(50,50))
    cannonPic2=image.load("Weapons/cannon2.png").convert_alpha()
    cannonPic2=transform.scale(cannonPic2,(50,50))
    cannonPic3=image.load("Weapons/cannon3.png").convert_alpha()
    cannonPic3=transform.scale(cannonPic3,(50,50))
    cannonPic4=image.load("Weapons/cannon4.png").convert_alpha()
    cannonPic4=transform.scale(cannonPic4,(50,50))
    cannonPic5=image.load("Weapons/cannon5.png").convert_alpha()
    cannonPic5=transform.scale(cannonPic5,(50,50))

    # loads images of the different bullets
    bulletL=image.load("Weapons/bulletleft.png")
    bulletL=transform.scale(bulletL,(40,40))
    bulletR=image.load("Weapons/bulletRight.png")
    bulletR=transform.scale(bulletR,(40,40))
    bulletU=image.load("Weapons/bulletUp.png")
    bulletU=transform.scale(bulletU,(40,40))
    bulletD=image.load("Weapons/bulletDown.png")
    bulletD=transform.scale(bulletD,(40,40))

    # loads the image of the coin icon
    coin=image.load("Weapons/coin2.png")
    coin=transform.scale(coin,(150,150))

    #loads the text that will be displayed on the side bar (number of coins, weapon values, etc)
    counter=font.SysFont("Chiller",25)
    counter=counter.render("Coins: ",True,white)

    round1=font.SysFont("Chiller",25)
    round1=round1.render("$15",True,white)

    cost1=font.SysFont("Chiller",25)
    cost1=cost1.render("$10",True,black)
    cost2=font.SysFont("Chiller",25)
    cost2=cost2.render("$20",True,black)
    cost3=font.SysFont("Chiller",25)
    cost3=cost3.render("$30",True,black)
    cost4=font.SysFont("Chiller",25)
    cost4=cost4.render("$40",True,black)
    cost5=font.SysFont("Chiller",25)
    cost5=cost5.render("$50",True,black)
    cost6=font.SysFont("Chiller",20)
    cost6=cost6.render("$35",True,black)
    cost7=font.SysFont("Chiller",20)
    cost7=cost7.render("$30",True,black)

    # loads the images of the text for the music
    songTitle1=font.SysFont("Chiller",15)
    songTitle1=songTitle1.render("Monster Mash - Bobby Pickett",True,white)
    songTitle2=font.SysFont("Chiller",15)
    songTitle2=songTitle2.render("Halloween - Kodak Black",True,white)
    songTitle3=font.SysFont("Chiller",15)
    songTitle3=songTitle3.render("Monster - 21 Savage",True,white)
    songTitle4=font.SysFont("Chiller",15)
    songTitle4=songTitle4.render("The Monster - Eminem ft. Rihanna",True,white)

    # loads the text that instructs the user on how to pause
    pause_info=font.SysFont("Chiller",20)
    pause_info=pause_info.render("Press P to Pause",True,white)

    # draw the power up rectangles
    fivekill_rect=Rect(rectangle0.x,25,50,50)
    threekill_rect=Rect(rectangle3.x,25,50,50)

    # loads the images for the power ups
    fivekill=image.load("PowerUp/five_kill.png")
    fivekill=transform.scale(fivekill,(50,50))
    threekill=image.load("PowerUp/three_kill.png")
    threekill=transform.scale(threekill,(50,50))
    

    # empty list into which the bullets that are goign to be shot will be appended
    bullets1=[]
    bullets2=[]
    bullets3=[]
    bullets4=[]
    bullets5=[]

    # variables assigned to determine if a weapon has been dragged and dropped
    moved0=False
    moved1=False
    moved2=False
    moved3=False
    moved4=False

    # the speed of the bullet is 1
    speed=1

    base=Rect(750,30,200,100)# sets the values of the base rectangle

    hit=image.load(enemyfile+"/hit.png")# laods the image that is going to be displayed if the zombie is hit by a bullet

    # loads the images of sprites for the coresponding zombie
    for i in range(enemysprites):
        monsters1=image.load(enemyfile+"/tile"+str(i)+".png")
        pics1.append(monsters1)

    # determines how long it as been since the game has started
    last_bullet0=time.get_ticks()
    last_bullet1=time.get_ticks()
    last_bullet2=time.get_ticks()
    last_bullet3=time.get_ticks()
    last_bullet4=time.get_ticks()
    wait=20# wait varibale is going to be used later on to prevent spamming of the bullets

    myClock=time.Clock()
    while action=="start":
        if rapid<20:
            rapid+=1
        
        print(rapid)
        click=False
        for evt in event.get():
            if evt.type==QUIT:# if player quits
                menu("menu",level_available)# player will be taken back to menu screen
                

            elif evt.type == KEYDOWN:
                if evt.key==K_p:# if player presses p
                    gamepause(level_available)# the game will be paused

            elif evt.type == MOUSEBUTTONDOWN:        
                if vdRect.collidepoint(mx,my) and vol<0.99:#stopping volume from going over 1.0
                    vol+=0.1#if volumeUp is selected, inc is increased by 0.1
                if vuRect.collidepoint(mx,my) and vol>0.00:#stopping volume from going under 0.0
                    vol-=0.1#if volumeDown is selected, inc is decreased by 0.1
                if playRect.collidepoint(mx,my):
                    mixer.music.unpause()#if play is selected, music is unpaused
                if pauseRect.collidepoint(mx,my):
                    mixer.music.pause()#if pause is selected, music is paused
                if shufRect.collidepoint(mx,my):
                    currentSong+=1#if shuffle is selected, next song in list plays
                    mixer.music.load(playlist[currentSong%4])#loading playlist
                    mixer.music.play(-1)#playing infinitely

                if evt.button == 1:# if left clicked ...
                    click=True# set clicked to True
                    if rectangle0.collidepoint(evt.pos) and count>=10:# if the mouse is colliding with one of the weapons and the player has more than a certain
                    #amount of coins ...
                        rectangle_draging0= True# set the draging of the weapon to true
                        mouse_x, mouse_y = evt.pos# determine the location og the mouse
                        offset_x = rectangle0.x - mouse_x# determine how much x value is going to be offsetted
                        offset_y = rectangle0.y - mouse_y# determine how much the y value is going to be offsetted
                        count-=10# reduce however many coins the weapon is worth from the players balance
                    elif rectangle0.collidepoint(evt.pos) and count<10:# if the player does not have enough coins for the weapon
                        rectangle_draging0= False# do not let them drga the weapon
                    elif rectangle1.collidepoint(evt.pos) and count>=20:
                        rectangle_draging1= True
                        mouse_x, mouse_y = evt.pos
                        offset_x = rectangle1.x - mouse_x
                        offset_y = rectangle1.y - mouse_y
                        count-=20
                    elif rectangle1.collidepoint(evt.pos) and count<10:
                        rectangle_draging1= False
                    elif rectangle2.collidepoint(evt.pos) and count>=30:
                        rectangle_draging2=True
                        mouse_x, mouse_y = evt.pos
                        offset_x = rectangle2.x - mouse_x
                        offset_y = rectangle2.y - mouse_y
                        count-=30
                    elif rectangle2.collidepoint(evt.pos) and count<10:
                        rectangle_draging2= False
                    elif rectangle3.collidepoint(evt.pos) and count>=40:
                        rectangle_draging3=True
                        mouse_x, mouse_y=evt.pos
                        offset_x = rectangle3.x - mouse_x
                        offset_y = rectangle3.y - mouse_y
                        count-=40
                    elif rectangle3.collidepoint(evt.pos) and count<10:
                        rectangle_draging3= False
                    elif rectangle4.collidepoint(evt.pos) and count>=50:
                        rectangle_draging4= True
                        mouse_x, mouse_y = evt.pos
                        offset_x = rectangle4.x - mouse_x
                        offset_y = rectangle4.y - mouse_y
                        count-=50
                    elif rectangle4.collidepoint(evt.pos) and count<10:
                        rectangle_draging4= False
                    # The next two button are for power ups
                    elif fivekill_rect.collidepoint(mx,my) and count>=35:# if the five kill power up rectangle is clicked
                        count-=35# reduce the amount of coins by 35
                        for en in enemytype[score:score+5]:# loop through the first a certain 5 elements in the list. Starting from the number of zombies that have neem killed
                            # until you reach the number of zombies that have been killed plus 5
                            # change the coordinates of the zombies off the map
                            en[0]=-100
                            en[1]=-100
                            number_of_enemies-=1# decrease the number of enemies variable by 1
                            if number_of_enemies==0:# if the number of enemies reaches 0 
                                gameFinish(wave_number,level_available+1)# display the gameover function
                        score+=5# increase teh score by 5
                    # repeat the code above for the three kill power up
                    # However this time only loop throught the first 3 elements of the list and only decrease the count by 30
                    elif threekill_rect.collidepoint(mx,my) and count>=30:
                        count-=30
                        for en in enemytype[score:score+3]:
                            en[0]=-100
                            en[1]=-100
                            number_of_enemies-=1
                            if number_of_enemies==0:
                                gameFinish(wave_number,level_available+1)
                        score+=3# increase the score by 3
                        

            elif evt.type == MOUSEMOTION:# if the mouse is moving
                if rectangle_draging0:# if the weapon can be dragged
                    mouse_x, mouse_y = evt.pos# determine the position of the mouse
                    newrectangle0x = mouse_x + offset_x# set the x coordinate of where ever the weapon is placed 
                    newrectangle0y = mouse_y + offset_y# set the x coordinate of where ever the weapon is placed
                    moved0=True# set the moved value to True
                elif rectangle_draging1:
                    mouse_x, mouse_y = evt.pos
                    newrectangle1x = mouse_x + offset_x
                    newrectangle1y = mouse_y + offset_y
                    moved1=True
                elif rectangle_draging2:
                    mouse_x, mouse_y = evt.pos
                    newrectangle2x = mouse_x + offset_x
                    newrectangle2y = mouse_y + offset_y
                    moved2=True
                elif rectangle_draging3:
                    mouse_x, mouse_y = evt.pos
                    newrectangle3x = mouse_x + offset_x
                    newrectangle3y = mouse_y + offset_y
                    moved3=True
                elif rectangle_draging4:
                    mouse_x, mouse_y = evt.pos
                    newrectangle4x = mouse_x + offset_x
                    newrectangle4y = mouse_y + offset_y
                    moved4=True

            elif evt.type == MOUSEBUTTONUP:# Once the playerclicks up
                if evt.button == 1 and rectangle_draging0==True:# if left clicked and the qeapon was allowed to be dragged
                    rectangle_draging0= False# now set the dragging to false
                    if moved0:# if the weapon was moved
                        myRects0.append(Rect(newrectangle0x,newrectangle0y,50,50))# append the coordinates, width , and height of rectangle into the respective list
                        myWeapons0.append((newrectangle0x,newrectangle0y))
                        for i in range(len(path)):# loop through the path list
                            if path[i].colliderect(Rect(newrectangle0x,newrectangle0y,50,50)):# if the rectangle placed is colliding with the rectangles on the path... 
                                # stop the functionality of all rectangles that were placed before that moment
                                for r in myRects0:
                                    myRects0.remove(r)
                                
                # the above code repeats for all the weapons        
                elif evt.button == 1 and rectangle_draging1==True:
                    rectangle_draging1= False
                    if moved1:
                        myRects1.append(Rect(newrectangle1x,newrectangle1y,50,50))
                        myWeapons1.append((newrectangle1x,newrectangle1y))
                        for i in range(len(path)):# loop through the path list
                            if path[i].colliderect(Rect(newrectangle1x,newrectangle1y,50,50)):# if the rectangle placed is colliding with the rectangles on the path... 
                                # stop the functionality of all rectangles that were placed before that moment
                                for r in myRects1:
                                    myRects1.remove(r)
                elif evt.button == 1 and rectangle_draging2==True:
                    rectangle_draging2= False
                    if moved2:
                        myRects2.append(Rect(newrectangle2x,newrectangle2y,50,50))
                        myWeapons2.append((newrectangle2x,newrectangle2y))
                        for i in range(len(path)):# loop through the path list
                            if path[i].colliderect(Rect(newrectangle2x,newrectangle2y,50,50)):# if the rectangle placed is colliding with the rectangles on the path... 
                                # stop the functionality of all rectangles that were placed before that moment
                                for r in myRects2:
                                    myRects2.remove(r)
                elif evt.button == 1 and rectangle_draging3==True:
                    rectangle_draging3= False
                    if moved3:
                        myRects3.append(Rect(newrectangle3x,newrectangle3y,50,50))
                        myWeapons3.append((newrectangle3x,newrectangle3y))
                        for i in range(len(path)):# loop through the path list
                            if path[i].colliderect(Rect(newrectangle3x,newrectangle3y,50,50)):# if the rectangle placed is colliding with the rectangles on the path... 
                                # stop the functionality of all rectangles that were placed before that moment
                                for r in myRects3:
                                    myRects3.remove(r)
                elif evt.button == 1 and rectangle_draging4==True:
                    rectangle_draging4= False
                    if moved4:
                        myRects4.append(Rect(newrectangle4x,newrectangle4y,50,50))
                        myWeapons4.append((newrectangle4x,newrectangle4y))
                        for i in range(len(path)):# loop through the path list
                            if path[i].colliderect(Rect(newrectangle4x,newrectangle4y,50,50)):# if the rectangle placed is colliding with the rectangles on the path... 
                                # stop the functionality of all rectangles that were placed before that moment
                                for r in myRects4:
                                    myRects4.remove(r)
                

        mx,my=pos=mouse.get_pos()# determine the coordinates of the mouse
        mb=mouse.get_pressed()# determine if the mouse is being pressed
            

        draw.rect(screen,(255,255,255),bgRect)# draw the background rectangle
        screen.blit(bg,(0,0))# blit the background
        screen.blit(grey,(1000,0))# blit te sidebar grey

        # blit the music images
        screen.blit(shuffle,(20,170))
        screen.blit(pause,(80,170))
        screen.blit(play,(140,170))
        screen.blit(volumeDown,(50,230))
        screen.blit(volumeUp,(110,230))

        # blit the coin icon and the counter text
        screen.blit(coin,(1030,400))
        screen.blit(counter,(1030,600))


        # blit the weapons images
        screen.blit(cannonPic1,(rectangle0.x,rectangle0.y))
        screen.blit(cannonPic2,(rectangle1.x,rectangle1.y))
        screen.blit(cannonPic3,(rectangle2.x,rectangle2.y))
        screen.blit(cannonPic4,(rectangle3.x,rectangle3.y))
        screen.blit(cannonPic5,(rectangle4.x,rectangle4.y))

        # blit the power up images
        screen.blit(fivekill,(rectangle0.x,25))
        screen.blit(threekill,(rectangle3.x,25))

        # blit the text that displays how much the weapons and power ups cost
        screen.blit(cost1,(1035,110))
        screen.blit(cost2,(1125,110))
        screen.blit(cost3,(1035,210))
        screen.blit(cost4,(1125,210))
        screen.blit(cost5,(1035,310))
        screen.blit(cost6,(1035,5))
        screen.blit(cost7,(1135,5))
        

        # blit the text that tells the user how to pasue 
        screen.blit(pause_info,(460,675))

        # determines what song to play based on the currentSong counter
        if currentSong==0:
            screen.blit(monstermash,(50,10))
            screen.blit(songTitle1,(20,130))
        elif currentSong==1:
            screen.blit(halloween,(50,10))
            screen.blit(songTitle2,(20,130))
        elif currentSong==2:
            screen.blit(monster,(50,10))
            screen.blit(songTitle3,(20,130))
        elif currentSong==3:
            screen.blit(themonster,(50,10))
            screen.blit(songTitle4,(20,130))
        
        if click and rapid==20:# if mouse is clicked and rapid variable has reached 40 ... (to prevent spamming)
            for i in range(len(myRects0)):# loops through the list that contains the weapons that were dragged
                if myRects0[i].colliderect(bgRect):# if the weapons that were dragged collide with the background screen ...
                    ang=atan2(my-myRects0[i].top,mx-myRects0[i].left)#determine the angle the bullet needs to go
                    vx=cos(ang)*speed
                    vy=sin(ang)*speed
                    bullets1.append([myRects0[i].left,myRects0[i].top,vx,vy])#append the bullet to the respective bulletes list
 
            # the code above is repeated for all the weapons                
            for i in range(len(myRects1)):
                if myRects1[i].colliderect(bgRect): 
                    ang=atan2(my-myRects1[i].top,mx-myRects1[i].left)
                    vx=cos(ang)*speed
                    vy=sin(ang)*speed
                    bullets2.append([myRects1[i].left,myRects1[i].top,vx,vy])


            for i in range(len(myRects2)):
                if myRects2[i].colliderect(bgRect):
                    ang=atan2(my-myRects2[i].top,mx-myRects2[i].left)
                    vx=cos(ang)*speed
                    vy=sin(ang)*speed
                    bullets3.append([myRects2[i].left,myRects2[i].top,vx,vy])


            for i in range(len(myRects3)):
                if myRects3[i].colliderect(bgRect):
                    ang=atan2(my-myRects3[i].top,mx-myRects3[i].left)
                    vx=cos(ang)*speed
                    vy=sin(ang)*speed
                    bullets4.append([myRects3[i].left,myRects3[i].top,vx,vy])


            for i in range(len(myRects4)):
                if myRects4[i].colliderect(bgRect):
                    ang=atan2(my-myRects4[i].top,mx-myRects4[i].left)
                    vx=cos(ang)*speed
                    vy=sin(ang)*speed
                    bullets5.append([myRects4[i].left,myRects4[i].top,vx,vy])

            rapid=0            


        ############blitting the bullets
        for b in bullets1:# loops throught the bullets list
            screen.blit(bulletL,(int(b[0]),int(b[1])))# blit the bullets that are in the list
        for b in bullets2:
            screen.blit(bulletL,(int(b[0]),int(b[1])))
        for b in bullets3:
            screen.blit(bulletL,(int(b[0]),int(b[1])))
        for b in bullets4:
            screen.blit(bulletL,(int(b[0]),int(b[1])))
        for b in bullets5:
            screen.blit(bulletL,(int(b[0]),int(b[1])))

            
        # loops through the enemy sprites and blit them. 
        for en in (enemytype):
            screen.blit(pics1[en[2]],(en[0],en[1]))#en[2] is the frame number
            en[2]+=1
            if en[2]>=enemysprites:
                en[2]=0

        

        # makes the zombies follow the path by determining if they are colliding with th rectangles that are in the route list
        for en in (enemytype):
            zombieRect=Rect(en[0]+10,en[1],30,70)# draw a rectangle around the zombies
            en[4]-=1#this is the delay
            if en[4]<=0:
                if en[0]+5<450:
                    en[0]+=2
                if route[0].collidepoint(en[0],en[1]):
                    en[1]-=2
                if route[1].collidepoint(en[0],en[1]): 
                    en[0]+=2
                if route[2].collidepoint(en[0],en[1]):
                    en[1]-=2
                if route[3].collidepoint(en[0],en[1]):
                    en[0]+=2
                    en[1]-=2
                if zombieRect.colliderect(base):
                    en[0]=-100
                    en[1]=-100
                    health-=1
                    number_of_enemies-=1
                    if number_of_enemies==0:# if number of enemies reaches 0 ...
                                gameFinish(wave_number,level_available+1)# call on the gameFinish function


                # moves the bullet by increasing it x and y value
                for b in bullets1[:]:
                    b[0]+=b[2]
                    b[1]+=b[3]
                    if b[0]>1000 or b[0]<0 or b[1]>700 or b[1]<0:# if the bullet goes off of the screen
                        bullets1.remove(b)# remove it from its respsective list
                for b in bullets2[:]:
                    b[0]+=b[2]
                    b[1]+=b[3]
                    if b[0]>1000 or b[0]<0 or b[1]>700 or b[1]<0:
                        bullets2.remove(b)
                for b in bullets3[:]:
                    b[0]+=b[2]
                    b[1]+=b[3]
                    if b[0]>1000 or b[0]<0 or b[1]>700 or b[1]<0:
                        bullets3.remove(b)
                for b in bullets4[:]:
                    b[0]+=b[2]
                    b[1]+=b[3]
                    if b[0]>1000 or b[0]<0 or b[1]>700 or b[1]<0:
                        bullets4.remove(b)
                for b in bullets5[:]:
                    b[0]+=b[2]
                    b[1]+=b[3]
                    if b[0]>1000 or b[0]<0 or b[1]>700 or b[1]<0:
                        bullets5.remove(b)

                for b in bullets1:
                    bulletRect=Rect(int(b[0]),int(b[1]),30,20)
                    
                    if bulletRect.colliderect(zombieRect):#if the bullet rectangle collides with the zombie rectangle
                        en[5]=en[5]-1#decrease the zombies lives by 1
                        screen.blit(hit,(en[0],en[1]))# blit the image that shows the zombies have been hit
                        
                        bullets1.remove(b)# remove the bullet from its respective list
                        if en[5]<=0:# if the zombies lives are less then or equal to 0...
                            en[0]=-100
                            en[1]=-100
                            # blit the enemies off the screen
                            count+=enemycoins# add a specific amount of coins to the players balance
                            number_of_enemies-=1# decrease the varaible that counts the number of enemies
                            score+=1 # If zombie is killed, increase the score by 1
                            print(score)
                            if number_of_enemies==0:# if number of enemies reaches 0 ...
                                gameFinish(wave_number,level_available+1)# call on the gameFinish function
                
                for b in bullets2:
                    bulletRect=Rect(int(b[0]),int(b[1]),30,20)
                    
                    if bulletRect.colliderect(zombieRect):
                        en[5]-=2
                        screen.blit(hit,(en[0],en[1]))
                        
                        bullets2.remove(b)
                        if en[5]<=0:
                            en[0]=-100
                            en[1]=-100
                            count+=enemycoins
                            number_of_enemies-=1
                            score+=1 # If zombie is killed, increase the score by 1
                            print(score)
                            if number_of_enemies==0:
                                gameFinish(wave_number,level_available+1)
                for b in bullets3:
                    bulletRect=Rect(int(b[0]),int(b[1]),30,20)
                    
                    if bulletRect.colliderect(zombieRect):
                        en[5]-=3
                        screen.blit(hit,(en[0],en[1]))
                        
                        bullets3.remove(b)
                        if en[5]<=0:
                            en[0]=-100
                            en[1]=-100
                            count+=enemycoins
                            number_of_enemies-=1
                            score+=1 # If zombie is killed, increase the score by 1
                            print(score)
                            if number_of_enemies==0:
                                gameFinish(wave_number,level_available+1)
                for b in bullets4:
                    bulletRect=Rect(int(b[0]),int(b[1]),30,20)
                    
                    if bulletRect.colliderect(zombieRect):
                        en[5]-=4
                        screen.blit(hit,(en[0],en[1]))
                        
                        bullets4.remove(b)
                        if en[5]<=0:
                            en[0]=-100
                            en[1]=-100
                            count+=enemycoins
                            number_of_enemies-=1
                            score+=1 # If zombie is killed, increase the score by 1
                            if number_of_enemies==0:
                                gameFinish(wave_number,level_available+1)
                for b in bullets5:
                    bulletRect=Rect(int(b[0]),int(b[1]),30,20)
                    
                    if bulletRect.colliderect(zombieRect):
                        en[5]-=5
                        screen.blit(hit,(en[0],en[1]))
                        
                        bullets5.remove(b)
                        if en[5]<=0:
                            en[0]=-100
                            en[1]=-100
                            count+=enemycoins
                            number_of_enemies-=1
                            score+=1 # If zombie is killed, increase the score by 1
                            if number_of_enemies==0:
                                gameFinish(wave_number,level_available+1)
                            
                            
                        
                                               
        
        coins=int(count)# set coins to the integer count
        countString=str(coins)
        counter1=font.SysFont("Chiller",25)
        counter1=counter1.render("$"+countString,True,white)# display the coins
        
        screen.blit(counter1,(1120,600))

        if health==3:# if health of the base is equal to 3
            screen.blit(health3,(690,114))# blit a full health bar
        elif health==2: # if health of the base is equal to 2
            screen.blit(health2,(690,114))# blit a damaged health bar
        elif health==1:# if health of the base is equal to 1
            screen.blit(health1,(690,114))# blit a damaged health bar
        elif health==0:# if health of thebase is equal to 0
            gameover(level_available)# call on the gameover function

        # by looping through lists that containg the dragged and dropped rectangles, display the rectangles on the screen
        for r in myRects0:
            draw.rect(screen,(133,105,65),r)
        for r in myRects1:
            draw.rect(screen,(133,105,65),r)
        for r in myRects2:
            draw.rect(screen,(133,105,65),r)
        for r in myRects3:
            draw.rect(screen,(133,2105,65),r)
        for r in myRects4:
            draw.rect(screen,(133,105,65),r)

        for w in myWeapons0:
            screen.blit(cannonPic1,(w[0],w[1]))
        for w in myWeapons1:
            screen.blit(cannonPic2,(w[0],w[1]))
        for w in myWeapons2:
            screen.blit(cannonPic3,(w[0],w[1]))
        for w in myWeapons3:
            screen.blit(cannonPic4,(w[0],w[1]))
        for w in myWeapons4:
            screen.blit(cannonPic5,(w[0],w[1]))
            
        display.flip()
        myClock.tick(30)

def instructions(action):
    # this is the instruction function that takes on action as a parameter. This function will run as long as action is assigned to "ins".
    # this function is called upon when the user clicks the instructions button from the main menu.
    # loads images of the different weapons
    cannonPic1=image.load("Weapons/cannon1.png").convert_alpha()
    cannonPic1=transform.scale(cannonPic1,(50,50))
    cannonPic2=image.load("Weapons/cannon2.png").convert_alpha()
    cannonPic2=transform.scale(cannonPic2,(50,50))
    cannonPic3=image.load("Weapons/cannon3.png").convert_alpha()
    cannonPic3=transform.scale(cannonPic3,(50,50))
    cannonPic4=image.load("Weapons/cannon4.png").convert_alpha()
    cannonPic4=transform.scale(cannonPic4,(50,50))
    cannonPic5=image.load("Weapons/cannon5.png").convert_alpha()
    cannonPic5=transform.scale(cannonPic5,(50,50))
    # loads the images of the different power ups
    fivekill=image.load("PowerUp/five_kill.png")
    fivekill=transform.scale(fivekill,(50,50))
    threekill=image.load("PowerUp/three_kill.png")
    threekill=transform.scale(threekill,(50,50))
    # loads the images of a zombie
    enemy1=image.load("Enemies1/tile0.png")
    enemy1=transform.scale(enemy1,(55,110))
    enemy2=image.load("Enemies2/tile0.png")
    enemy2=transform.scale(enemy2,(55,110))
    enemy3=image.load("Enemies3/tile0.png")
    enemy3=transform.scale(enemy3,(55,110))
    font.init()# innitializes the font
    white=(255,255,255)
    black=(0,0,0)
    red=(255,0,0)
    blue=(0,0,255)
    zombieIns=image.load("Intro/zombieIns.jpg")# loads instructions background
    zombieIns=transform.scale(zombieIns,(1200,700))# resizes it 
    myClock=time.Clock()
    while action=="ins":
        print("instructions")
        for evnt in event.get():            
            if evnt.type == QUIT:# if the user quits
                action="menu"# the player will return to the menu screen
                
        screen.blit(zombieIns,(0,0))# displys the instructions background
        # displays the set of instrction
        ins_text1=font.SysFont("Chiller",50)
        ins_text1=ins_text1.render("1. Use your coins and buy cannons to defend yourself.",True,red)
        ins_text2=font.SysFont("Chiller",50)
        ins_text2=ins_text2.render("2. Drag and drop your cannons onto the map and click anywhere to shoot.",True,red)
        ins_text3=font.SysFont("Chiller",50)
        ins_text3=ins_text3.render("3. The more expensive your weapons are, the more damage they will do.",True,red)
        ins_text4=font.SysFont("Chiller",50)
        ins_text4=ins_text4.render("4. As you progess in the levels, the incoming zombies will have",True,red) 
        ins_text4_2=font.SysFont("Chiller",50)
        ins_text4_2=ins_text4_2.render("more and more health.",True,red)
        ins_text5=font.SysFont("Chiller",50)
        ins_text5=ins_text5.render("5. Eliminate all zombies to move on to the next level. Good Luck!",True,red)
        ins_text6=font.SysFont("Chiller",50)
        ins_text6=ins_text6.render("6. As you complete level, new levels will beome available",True,red) 
        ins_text7=font.SysFont("Chiller",50)
        ins_text7=ins_text7.render("7. Survive all 3 waves to become the ultimate champion!",True,red)
        # Displays the chracteristics of the weapons --- Damage, Rapid Fire, Cost
        screen.blit(ins_text1,(20,20))
        screen.blit(ins_text2,(20,80))
        screen.blit(ins_text3,(20,140))
        screen.blit(ins_text4,(20,200))
        screen.blit(ins_text4_2,(20,260))
        screen.blit(ins_text5,(20,320))
        screen.blit(ins_text6,(20,380))
        draw.rect(screen,(133,105,65),Rect(20,450,50,50))
        screen.blit(cannonPic1,(20,450))
        draw.rect(screen,(133,105,65),Rect(20,520,50,50))
        screen.blit(cannonPic2,(20,520))
        draw.rect(screen,(133,105,65),Rect(20,590,50,50))
        screen.blit(cannonPic3,(20,590))
        draw.rect(screen,(133,105,65),Rect(350,450,50,50))
        screen.blit(cannonPic4,(350,450))
        draw.rect(screen,(133,105,65),Rect(350,520,50,50))
        screen.blit(cannonPic5,(350,520))
        screen.blit(threekill,(660,450))
        screen.blit(fivekill,(660,520))
        screen.blit(enemy1,(350,570))
        screen.blit(enemy2,(650,570))
        screen.blit(enemy3,(950,570))
        w1_text=w2_text=w3_text=w4_text=w5_text=w6_text=w7_text=w8_text=w9_text=w10_text=font.SysFont("Chiller",35)
        w1_text=w1_text.render("Damage: 1 Cost: $10",True,red)
        w2_text=w2_text.render("Damage: 2 Cost: $20",True,red)
        w3_text=w3_text.render("Damage: 3 Cost: $30",True,red)
        w4_text=w4_text.render("Damage: 4 Cost: $40",True,red)
        w5_text=w5_text.render("Damage: 5 Cost: $50",True,red)
        w6_text=w6_text.render("Damage: Kills 3 zombies in a row Cost: $30",True,red)
        w7_text=w7_text.render("Damage: Kills 5 zombies in a row Cost: $35",True,red)
        w8_text=w8_text.render("Lives: 5",True,red)
        w9_text=w9_text.render("Lives: 7",True,red)
        w10_text=w10_text.render("Lives: 9",True,red)
        screen.blit(w1_text,(90,450))
        screen.blit(w2_text,(90,520))
        screen.blit(w3_text,(90,590))
        screen.blit(w4_text,(420,450))        
        screen.blit(w5_text,(420,520))
        screen.blit(w6_text,(720,450))
        screen.blit(w7_text,(720,520))
        screen.blit(w8_text,(400,590))
        screen.blit(w9_text,(700,590))
        screen.blit(w10_text,(1000,590))
        display.flip()
        
        myClock.tick(60)

    display.flip()
menu("menu",1)# when the game opens, the menu function is called upon               
quit()
