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
message = 'Check out this'
snip = font.render('', True, 'white')
counter = 0
speed = 3
done = False

run = True
while run:
    screen.fill('dark gray')
    timer.tick(60)
    pygame.draw.rect(screen,'black',[0,300,800,200])
    if counter < speed * len(message)
        counter += 1
    elif counter >

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit()
