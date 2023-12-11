import pygame, sys

pygame.init()


def main():
    clock = pygame.time.Clock()

    pygame.display.set_caption("Tytul naszego okienka")
    icon = pygame.image.load("icon.png")
    pygame.display.set_icon(icon)

    pygame.mixer.music.load(r"music.mp3")
    pygame.mixer.music.play(-1)
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)

    image = pygame.image.load(r"moon.jpg")
    image = pygame.transform.scale(image, size)

    surf_center = ((width - image.get_width()) / 2, (height - image.get_height()) / 2)

    ball = pygame.image.load("ball.gif")
    screen.blit(ball, (width / 2, height / 2))
    ballrect = ball.get_rect(center=(width / 2, height / 2))
    pygame.display.flip()

    screen.blit(image, surf_center)
    pygame.display.flip()
    speed = [0.0, 0.0]
    accel = [0.0, 0.0]
    max_accel = 1.0

    while True:
        clock.tick(60)
        pygame.time.delay(50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYUP:
                if (
                    event.key == pygame.K_UP
                    or event.key == pygame.K_DOWN
                    or event.key == pygame.K_LEFT
                    or event.key == pygame.K_RIGHT
                ):
                    accel = [0.0, 0.0]

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            sys.exit()
        if keys[pygame.K_UP]:
            if accel[1] < max_accel:
                accel[1] += 0.2
            speed[1] -= accel[1]
        elif keys[pygame.K_DOWN]:
            if accel[1] < max_accel:
                accel[1] += 0.2
            speed[1] += accel[1]
        elif keys[pygame.K_LEFT]:
            if accel[0] < max_accel:
                accel[0] += 0.2
            speed[0] -= accel[0]
        elif keys[pygame.K_RIGHT]:
            if accel[0] < max_accel:
                accel[0] += 0.2
            speed[0] += accel[0]

        ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]

        screen.blit(image, surf_center)
        screen.blit(ball, ballrect)
        pygame.display.flip()


if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()
