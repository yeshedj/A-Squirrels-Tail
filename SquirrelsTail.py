import pygame as pg


class SquirrelGame:

    def __init__(self):
        # initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((480, 600))
        pg.display.set_caption("A Squirrel's Tail")
        self.clock = pg.time.Clock()
        self.running = True
        self.font_name = pg.font.match_font("Arial")

    def new(self):
        # start a new game
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        # self.player = Player(self)
        # self.all_sprites.add(self.player)
        # for plat in PLATFORM_LIST:
        #     p = Platform(*plat)
        #     self.all_sprites.add(p)
        #     self.platforms.add(p)
        self.run()

g = SquirrelGame()
# g.show_start_screen()
# while g.running:
#     g.new()
#     g.show_go_screen()

# pg.quit()
g.running()