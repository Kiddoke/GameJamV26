import pygame

class BottleCounter:
    def __init__(self, bottleImage, canImage):
        self.count = 0
        self.font = pygame.font.Font(None, 30)
        self.x = 710
        self.y = 60
        self.hintCost = 3
        
        self.bottle = bottleImage
        self.can = canImage

    def addBottle(self):
        self.count += 1

    def useHint(self):
        if (self.count - self.hintCost) >= 0:
            self.count -= self.hintCost
    
    def draw(self, screen):
        # bottle + can icon
        screen.blit(self.bottle, (self.x, self.y - 2))
        screen.blit(self.can, (self.x - 20, self.y))

        text = self.font.render(f"x {self.count}", True, (255,255,255))
        screen.blit(text, (self.x + 30, self.y + 10))

