import pygame
pygame.init()

# Get a list of available system fonts
available_fonts = pygame.font.get_fonts()

# Print the list of fonts
for font_name in available_fonts:
    print(font_name)
