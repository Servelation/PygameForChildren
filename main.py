from sprites import *


def collide(sprite1, sprite2):
    if ((sprite1.x < sprite2.x < sprite1.x + sprite1.width
         and sprite1.y < sprite2.y < sprite1.y + sprite1.height)
            or (sprite1.x < sprite2.x + sprite2.width < sprite1.x + sprite1.width
                and sprite1.y < sprite2.y + sprite2.height < sprite1.y + sprite1.height)
            or (sprite2.x < sprite1.x < sprite2.x + sprite2.width
                and sprite2.y < sprite1.y < sprite2.y + sprite2.height)
            or (sprite2.x < sprite1.x + sprite1.width < sprite2.x + sprite2.width
                and sprite2.y < sprite1.y + sprite1.height < sprite2.y + sprite2.height)):
        return True
    else:
        return False


WORLD_WIDTH = 4000  # Ширина игрового мира
WORLD_HEIGHT = 3000  # Высота игрового мира
SCREEN_WIDTH = 800  # Ширина экрана
SCREEN_HEIGHT = 600  # Высота экрана
pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
world = pygame.Surface((WORLD_WIDTH, WORLD_HEIGHT))

camera = Camera(WORLD_WIDTH, WORLD_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT)
player = Player(100,700)
player.image = pygame.transform.scale(player.image,
                                      [
                                        int(player.image.get_width()*0.2),
                                        int(player.image.get_height()*0.2)
                                      ])

stage = 1
game = True
while game:
    # Для закрытия проги - НЕ ТРОГАТЬ
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            game = False
    # -----------------
    if stage == 1:
        keys = pygame.key.get_pressed()
        player.update(keys)
        camera.update(player)
        world.fill((255,255,255))
        world.blit(pygame.image.load(r'images/Grass.jpg'),(0,0))
        world.blit(player.image, (player.x,player.y))
        window.blit(world, (camera.x, camera.y))
    clock.tick(60)
    pygame.display.flip()

pygame.quit()
