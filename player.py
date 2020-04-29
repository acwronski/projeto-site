import pygame

class Guy(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("desenho/navinha.png")
        self.image = pygame.transform.scale(self.image, [50, 50])
        self.rect = pygame.Rect(50, 50, 50, 50)

    def update(self, *args):
        # logica

        keys = pygame.key.get_pressed()

        if keys[pygame.K_s]:
            self.rect.y += 2

        elif keys[pygame.K_w]:
            self.rect.y += -2

        elif keys[pygame.K_d]:
            self.rect.x += 2

        elif keys[pygame.K_a]:
            self.rect.x += -2