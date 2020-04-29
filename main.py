import pygame

from player import Guy
# inicializando o pygame


pygame.init()

display = pygame.display.set_mode([1240, 600])
pygame.display.set_caption("jogo das estrelas dudu")

# objects
objectGroup = pygame.sprite.Group()

guy = Guy(objectGroup)

# musicas


pygame.mixer.music.load("sons/goty.mp3")
pygame.mixer.music.play(-1)

# sounds
shoot = pygame.mixer.Sound("sons/explosion.wav")


gameloop = True


if __name__ == "__main__":
    while gameloop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameloop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    shoot.play()


        display.fill([133, 135, 140])

        objectGroup.update()

        objectGroup.draw(display)
      
        pygame.display.update()
