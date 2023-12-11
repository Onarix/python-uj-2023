import pygame
from random import randint
import os.path

pygame.init()

# kolory
CZARNY = (0, 0, 0)
BIALY = (255, 255, 255)


class Rakietka(pygame.sprite.Sprite):
    # klasa Rakietka dziedziczy z klasy "Sprite" w Pygame.

    def __init__(self, color, width, height):
        # wołamy najpierw konstruktor klasy bazowej (Sprite)
        # dzięki metodzie super() dziedziczymy wszystkie elementy klasy bazowej
        super().__init__()

        # przekazanie koloru Rakietka oraz szerokości i wysokości, kolor tła i ustawienie go na przezroczyste
        self.image = pygame.Surface([width, height])
        self.image.fill(CZARNY)
        self.image.set_colorkey(CZARNY)

        # rysuję Rakietka jako prostokąt
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # pobieramy prostokąt (jego rozmiary) z obiektu image
        self.rect = self.image.get_rect()

    def moveLeft(self, pixels):
        self.rect.x -= pixels
        # sprawdzanie położenia brzegowego
        if self.rect.x < 0:
            self.rect.x = 0

    def moveRight(self, pixels):
        self.rect.x += pixels
        # sprawdzanie położenia brzegowego
        if self.rect.x > 600:
            self.rect.x = 600


class Pilka(pygame.sprite.Sprite):
    # klasa Pilka dziedziczy ze "Sprite" w Pygame.

    def __init__(self, color, width, height):
        # wołamy konstruktor klasy bazowej
        super().__init__()

        # przekazujemy rozmiary, kolor, przezroczystość
        self.image = pygame.Surface([width, height])
        self.image.fill(CZARNY)
        self.image.set_colorkey(CZARNY)

        # rysowanie piłki (jako prostokącika)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # losowanie prędkości
        self.velocity = [0, randint(4, 8)]

        # pobieramy prostokąt (jego rozmiary) z obiektu image
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = randint(-8, 8)
        self.velocity[1] = -self.velocity[1]


# definiujemy rozmiary i otwieramy nowe okno
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ping Pong")

rakietka = Rakietka(BIALY, 100, 10)
rakietka.rect.x = 300
rakietka.rect.y = 470

pileczka = Pilka(BIALY, 10, 10)
pileczka.rect.x = 345
pileczka.rect.y = 95

# lista wszystkich widzalnych obiektów potomnych z klasy Sprite
all_sprites_list = pygame.sprite.Group()

# dodanie obu rakietek i piłeczki do listy
all_sprites_list.add(rakietka)
all_sprites_list.add(pileczka)

# zaczynamy właściwy blok programu
kontynuuj = True

# służy do kontroli liczby klatek na sekudnę (fps)
clock = pygame.time.Clock()

# Początkowy wynik gracza
score = 0

# -------- GLÓWNA PĘTLA PROGRAMU -----------
while kontynuuj:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # zamknięcie okienka
            kontynuuj = False

    # ruchy obiektów Rakietkas klawisze strzałka góra dół
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rakietka.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        rakietka.moveRight(5)

    # aktualizacja listy duszków
    all_sprites_list.update()

    # sprawdzenie czy piłeczka nie uderza w którąś ścianę
    # i odpowiednie naliczenie punktu jeśli minie rakietkę i uderzy w ścianę za nią
    if pileczka.rect.x >= 690:
        pileczka.velocity[0] = -pileczka.velocity[0]
    if pileczka.rect.x <= 0:
        pileczka.velocity[0] = -pileczka.velocity[0]
    if pileczka.rect.y > 490:
        print(f"Score: {score}")
        if not os.path.exists("wynik.txt"):
            with open("wynik.txt", "x") as f:
                f.write("0")
        with open("wynik.txt", "r") as f:
            high_score = f.read()
        if int(high_score) < score:
            with open("wynik.txt", "w") as w:
                w.write(str(score))
                high_score = str(score)
        print(f"High score: {high_score}")
        kontynuuj = False
        pileczka.velocity[1] = -pileczka.velocity[1]
    if pileczka.rect.y < 0:
        pileczka.velocity[1] = -pileczka.velocity[1]

    # sprawdzenie kolizji piłeczki z obiektem rakietka
    if pygame.sprite.collide_mask(pileczka, rakietka):
        score += 1
        pileczka.bounce()

    # RYSOWANIE
    # czarny ekran
    screen.fill(CZARNY)

    # narysowanie obiektów
    all_sprites_list.draw(screen)

    # wyświetlanie wyniku
    font = pygame.font.Font(None, 74)
    text = font.render(str(score), 1, BIALY)
    screen.blit(text, (350, 10))

    # odświeżenie / przerysowanie całego ekranu
    pygame.display.flip()

    # 60 klatek na sekundę
    clock.tick(60)

# koniec
pygame.quit()
