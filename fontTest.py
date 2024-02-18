# import pygame
# pygame.init()
#
# # Get a list of available system fonts
# available_fonts = pygame.font.get_fonts()
#
# # Print the list of fonts
# for font_name in available_fonts:
#     print(font_name)


import pygame
pygame.init()
font = pygame.font.Font('freesansbold.ttf', 24)
screen = pygame.display.set_mode([800,500])
timer = pygame.time.Clock()
message = ['Check out this. lalalahahahahskdjsjiwoihdfao hello bitch',
           'gusjdkasf jshbdvksd fuckkkkk',
           'isn t djaudfhihsdnfcwesd  whisdfcksd ']
snip = font.render('', True, 'white')
counter = 0
speed = 2
active_message = 0
message = message[active_message]
done = False

run = True
while run:
    screen.fill('dark gray')
    timer.tick(60)
    pygame.draw.rect(screen,'black',[0,300,800,200])
    if counter < speed * len(message):
        counter += 1
    elif counter >= speed*len(message):
        done = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and done and active_message < len(message):
                active_message += 1
                done = False
                message = message[active_message]
                counter = 0

    snip = font.render(message[0:counter//speed], True, 'white')
    screen.blit(snip,(10, 310))

    pygame.display.flip()

pygame.quit()
