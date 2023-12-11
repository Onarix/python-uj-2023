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
    push_speed = 15.0
    g = (0, 0.9)

    while True:
        clock.tick(60)
        pygame.time.delay(50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            sys.exit()
        if keys[pygame.K_UP]:
            while speed[1] > -push_speed:
                speed[1] -= 1.0
        elif keys[pygame.K_DOWN]:
            while speed[1] < push_speed:
                speed[1] += 1.0
        elif keys[pygame.K_LEFT]:
            while speed[0] > -push_speed:
                speed[0] -= 1.0
        elif keys[pygame.K_RIGHT]:
            while speed[0] < push_speed:
                speed[0] += 1.0

        # w poziomie - ruch jednostajny (speed[0] - const)
        # w pionie - ruch przyspieszony (speed[1] += g[1])
        if ballrect.bottom < height:
            speed[1] += g[1]

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
