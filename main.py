import pygame
from sprites import *
from config import *
import sys

class Game: 
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT)) # Set screen dimensions 
        self.clock = pygame.time.Clock()
        self.running = True

        self.character_spritesheet = SpriteSheet("img/_character.png")
        self.terrain_spritesheet = SpriteSheet("img/terrain.png")

    def create_tilemap(self):
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                Ground(self, j, i)
                
                if column == "B":
                    Block(self, j, i)
                if column == "P":
                    Player(self, j, i)


    def new(self):
        # New game starts 
        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.block = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()

        self.create_tilemap();


    def events(self):
        # Game loop - events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        # Game loop - updates
        self.all_sprites.update()

    def draw(self):
        # Game loop - draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()

    def main(self):
        # Game loop
        while self.playing:
            self.events()
            self.update()
            self.draw()

        self.running = False

    def game_over(self):
        pass

    def intro_screen(self):
        pass

g = Game()
g.intro_screen();
g.new()
while g.running:
    g.main()
    g.game_over()

pygame.quit()
sys.exit()