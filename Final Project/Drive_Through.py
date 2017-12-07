import pygame
import time
import random
pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
light_blue = (75, 193, 252)
car_width = 70
fails = 0

gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption ('Drive_Through')
carImag = pygame.image.load('car_green_3.png')

plus1 = pygame.image.load('C:\Users\apearl3\Desktop\Final Project\+1.png')
plus2 = pygame.image.load('C:\Users\apearl3\Desktop\Final Project\+2.png')
plus3 = pygame.image.load('C:\Users\apearl3\Desktop\Final Project\+3.png')
plus4 = pygame.image.load('C:\Users\apearl3\Desktop\Final Project\+4.png')
plus5 = pygame.image.load('C:\Users\apearl3\Desktop\Final Project\+5.png')
plus10 = pygame.image.load('C:\Users\apearl3\Desktop\Final Project\+10.png')
min1 = pygame.image.load('C:\Users\apearl3\Desktop\Final Project\-1.png')
min2 = pygame.image.load('C:\Users\apearl3\Desktop\Final Project\-2.png')
min3 = pygame.image.load('C:\Users\apearl3\Desktop\Final Project\-3.png')
min4 = pygame.image.load('C:\Users\apearl3\Desktop\Final Project\-4.png')
min5 = pygame.image.load('C:\Users\apearl3\Desktop\Final Project\-5.png')
min10 = pygame.image.load('C:\Users\apearl3\Desktop\Final Project\-10.png')
div1 = pygame.image.load('C:\Users\apearl3\Desktop\Final Project\divide 1.png')
div2 = pygame.image.load('C:\Users\apearl3\Desktop\Final Project\divide 2.png')
div3 = pygame.image.load('C:\Users\apearl3\Desktop\Final Project\divide 3.png')
div4 = pygame.image.load('C:\Users\apearl3\Desktop\Final Project\divide 4.png')
div5 = pygame.image.load('C:\Users\apearl3\Desktop\Final Project\divide 5.png')
div10 = pygame.image.load('C:\Users\apearl3\Desktop\Final Project\divide 10.png')
x1 = pygame.image.load('C:\Users\apearl3\Desktop\Final Project\x1.png')
x2 = pygame.image.load('C:\Users\apearl3\Desktop\Final Project\x2.png')
x3 = pygame.image.load('C:\Users\apearl3\Desktop\Final Project\x3.png')
x4 = pygame.image.load('C:\Users\apearl3\Desktop\Final Project\x4.png')
x5 = pygame.image.load('C:\Users\apearl3\Desktop\Final Project\x5.png')
x10 = pygame.image.load('C:\Users\apearl3\Desktop\Final Project\x10.png')

scorecard = [plus1, plus2, plus3, plus4, plus5, plus10, min1, min2, min3, min4, min5, min10, div1, div2, div3, div4, div5, div10, x1, x2, x3, x4, x5, x10] 

"""
def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
"""

def game_clock(thirty):
    font = pygame.font.SysFont(None, 40)
    text = font.render("Time Left:" + " " + str(thirty), True, black)
    gameDisplay.blit(text, (display_width /2, 0))

def score_amount(score):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score:" + " " + str(score), True, black)
    gameDisplay.blit(text, (0, 90))
    
def total_amount(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Total:" + " " + str(count), True, black)
    gameDisplay.blit(text, (0,0))
    

def target_amount(number):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Target:" + " " + str(number), True, black)
    gameDisplay.blit(text, (0, 30))

def rounds_won(won):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Rounds Won:" + " " + str(won), True, black)
    gameDisplay.blit(text, (0, 60))

def car(x,y):
    gameDisplay.blit(carImag, (x,y))

def points(x, y, image):
    gameDisplay.blit(image, (x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


   
def message_display(text, fails):
    largeText = pygame.font.Font('freesansbold.ttf', 50)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    time.sleep(2)

    Drive_Through(fails)

def lose(won, fails):
    fails = fails + 1
    message_display('Out of Time. Rounds Won:' + " " + str(won), fails)

#location starts at top left in which +x goes right and +y goes down
def Drive_Through(fails):
    
    car_x = (display_width * 0.45)
    car_y = (display_height * 0.75)

    time = 30
    x_change = 0
    clock = pygame.time.Clock()
    spawn_width = 130
    spawn_x = random.randrange(0, display_width - spawn_width)
    spawn_y = - 600
    spawn_speed = 10
    total = 0
    last_change = 0
    target = 0
    won = 0
    start_ticks = pygame.time.get_ticks()
    second = 0
    thirty = 30 - second
    fails = fails + 1
    #score = 0

    
    
    spawn_height = 130
    image = random.choice(scorecard)
    number = random.randrange(1, 100)

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -10
                elif event.key == pygame.K_RIGHT:
                    x_change = 10

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0 

        car_x += x_change
        if car_x < 0 or car_x > display_width - car_width:
            x_change = 0
                    

            #print(event)
    
        
        gameDisplay.fill(light_blue)
        if spawn_y == -100: 
            image = random.choice(scorecard)
            
        points(spawn_x,spawn_y, image)
               
            
        
        spawn_y += spawn_speed
        car(car_x, car_y)
        total_amount(total)
        target_amount(number)
        rounds_won(won)
        #score_amount(score)
        if number - 5 <= total <= number + 5:
            number = random.randint(1, 100)
            won += 1
            total = 0
            second = int(pygame.time.get_ticks() - start_ticks/1000)
            fails = fails + 1
            #score = score + 1000 - abs(total - number) * 100

            
             

        if time == 0:
            lose(won, fails)

        
        if spawn_y > display_height:
            spawn_y = -100
            spawn_x = random.randrange(0, display_width - spawn_width)

        
        if car_y < spawn_y+ spawn_height: 
            if car_x > spawn_x and car_x < spawn_x + spawn_width or car_x + car_width > spawn_x and car_x + car_width < spawn_x + spawn_width:
                for x in range(len(scorecard)):
                    if image == scorecard[x]:
                        if 0 <= x <= 4 and last_change != x:
                            total += x + 1
                            last_change = x
                            if total > 99:
                                total = 99
                        elif x == 5 and last_change != x :
                            total += 10
                            last_change = x
                            if total > 99:
                                total = 99
                        elif 6 <= x <= 10 and last_change != x:
                            total -= x - 5
                            last_change = x
                            if total < 1:
                                total = 1
                        elif x == 11 and last_change != x:
                            total -= 10
                            last_change = x
                            if total < 1:
                                total = 1
                        elif 18 <= x <= 22 and last_change != x:
                            total *= x - 17
                            last_change = x
                            total = round(total)
                            if total > 99:
                                total = 99
                        elif x == 23 and last_change != x:
                            total *= 10
                            last_change = x
                            total = round(total)
                            if total > 99:
                                total = 99
                        elif 12 <= x <= 16 and last_change != x :
                            total = total / (x - 11)
                            last_change = x 
                            total = round(total)
                            if total < 1 and total != 0:
                                total = 1
                        elif x == 17 and last_change != x:
                            total = total / 10
                            last_change = x
                            total = round(total)
                            if total < 1 and total != 0:
                                total = 1
        second = int(pygame.time.get_ticks() - start_ticks/1000)
        thirty = (45 * fails) - round((second - 8000)/1000)
        game_clock(thirty)
        if thirty == 0:
            lose(won, fails)
        

        pygame.display.update() #alternatively pygame.display.flip()
        clock.tick(90)

Drive_Through(fails)
pygame.quit()
quit()
