import pygame
import random

# спрайт фона
background1 = pygame.image.load('img/background.png')
background2 = pygame.image.load('img/background.png')
hp = pygame.image.load('img/hp_icon.png')
fuel = pygame.image.load('img/fuel_icon.png')

display_w = 800
display_h = 600
game_exit = False

pygame.init()
game_display = pygame.display.set_mode((display_w, display_h))
my_font = pygame.font.Font("fonts/Pixel.ttf", 24)

# глобальные переменные
background_h = 2356
background_y = display_h - background_h
world_speed = 7
accelerate = 0
score = 0
distance = 0
hp = 100
fuel = 100
fuel_x = 100
fuel_y = 100


class OurCar():
    def __init__(self):
        self.sprite = pygame.image.load('img/car.png')
        self.x = 0
        self.y = (display_h * 0.6)


class OtherCar1():
    def __init__(self):
        self.sprite = pygame.image.load('img/car_red2.png')
        self.x = 1
        self.y = -100
        self.visible = 0
        self.speed = -4


class OtherCar2():
    def __init__(self):
        self.sprite = pygame.image.load('img/car_red1.png')
        self.x = 0
        self.y = -100
        self.visible = 0
        self.speed = 4


car = OurCar()

other_cars = [OtherCar1(), OtherCar2(), OtherCar1()]

# здесь можно смело поменять название
pygame.display.set_caption('Hot race 0.3')
clock = pygame.time.Clock()


def check_collision():
    global score
    car_rect = car.sprite.get_rect().move((335 + car.x * 75, car.y))
    for idx in range(len(other_cars)):
        other_rect = other_cars[idx].sprite.get_rect().move((335 + other_cars[idx].x * 75, other_cars[idx].y))
        if other_cars[idx].visible == 1:
            if car_rect.colliderect(other_rect):
                other_cars[idx].visible = 0
                score -= 200
                if score < 0:
                    score = 0


def draw_background():
    global background_y

    game_display.blit(background1, (0, background_y))
    game_display.blit(background2, (0, background_y - background_h))
    background_y += world_speed + accelerate

    if background_y >= display_h:
        background_y = display_h - background_h


def draw_ui():
    text_image = my_font.render(str(score), True, (255, 255, 255))
    game_display.blit(text_image, (720, 20))

    text_image = my_font.render(str(distance), True, (255, 255, 255))
    game_display.blit(text_image, (720, 40))

    distance_pb_w = 800
    pygame.draw.rect(game_display, (200, 200, 200), (0, 0, distance_pb_w, 20))
    if distance <= 500:
        distance_k = distance / 500
        pygame.draw.rect(game_display, (255, 255, 255), (0, 0, distance_pb_w * distance_k, 20))

    fuel_pb_w = 250
    pygame.draw.rect(game_display, (252, 235, 2), (10, 50, fuel_pb_w, 20))
    if fuel == 250:
        fuel_k = 10
        pygame.draw.rect(game_display, (0, 0, 0), (10, 50, fuel_pb_w * fuel_k, 20))

    hp_pb_w = 250
    pygame.draw.rect(game_display, (252, 2, 2), (10, 100, hp_pb_w, 20))
    if hp == 250:
        hp_k = 10
        pygame.draw.rect(game_display, (0, 0, 0), (10, 50, hp_pb_w * hp_k, 20))


def draw_car():
    global distance, fuel
    game_display.blit(car.sprite, (335 + car.x * 75, car.y))
    distance += 1
    fuel -= 0.1


def draw_other_car():
    global other_car, score

    for idx in range(len(other_cars)):
        if other_cars[idx].visible == 1:
            # машинка есть и едет
            game_display.blit(other_cars[idx].sprite, (335 + other_cars[idx].x * 75, other_cars[idx].y))
            other_cars[idx].y += world_speed + accelerate - other_cars[idx].speed

        else:
            rnd = random.randint(0, 300)
            if rnd == 1:
                # машинки нет и мы создаем ее заново
                car_x = random.randint(0, 1)
                if car_x == 0:
                    other_cars[idx] = OtherCar1()
                else:
                    other_cars[idx] = OtherCar2()
                other_cars[idx].visible = 1
        # Условие исчезновения автомобиля
        if other_cars[idx].y > display_h + 300:
            if other_cars[idx].visible == 1:
                score += 100
                other_cars[idx].visible = 0


def process_keyboard(event):
    global accelerate
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            car.x = 0
        if event.key == pygame.K_RIGHT:
            car.x = 1
        if event.key == pygame.K_UP:
            accelerate += 2
            if accelerate > 10:
                accelerate = 10
        if event.key == pygame.K_DOWN:
            accelerate -= 2
            if accelerate < -6:
                accelerate = -6
        if event.key == pygame.K_SPACE:
            accelerate = -6


# самая важная функция в ней все и происходит
def game_loop(update_time):
    global game_exit
    while not game_exit:
        for event in pygame.event.get():
            # print(event)

            process_keyboard(event)
            if event.type == pygame.QUIT:
                game_exit = True

        # Функции поведения
        check_collision()

        # Функции отрисовки
        draw_background()
        draw_car()
        draw_other_car()
        draw_ui()

        pygame.display.update()
        clock.tick(update_time)


game_loop(30)
pygame.quit()
import random

# спрайт фона
background1 = pygame.image.load('img/background.png')
background2 = pygame.image.load('img/background.png')
hp = pygame.image.load('img/hp_icon.png')
fuel = pygame.image.load('img/fuel_icon.png')

display_w = 800
display_h = 600
game_exit = False

pygame.init()
game_display = pygame.display.set_mode((display_w, display_h))
my_font = pygame.font.Font("fonts/Pixel.ttf", 24)

# глобальные переменные
background_h = 2356
background_y = display_h - background_h
world_speed = 7
accelerate = 0
score = 0
distance = 0
hp = 100
fuel = 100
fuel_x = 100
fuel_y = 100


class OurCar():
    def __init__(self):
        self.sprite = pygame.image.load('img/car.png')
        self.x = 0
        self.y = (display_h * 0.6)


class OtherCar1():
    def __init__(self):
        self.sprite = pygame.image.load('img/car_red2.png')
        self.x = 1
        self.y = -100
        self.visible = 0
        self.speed = -4


class OtherCar2():
    def __init__(self):
        self.sprite = pygame.image.load('img/car_red1.png')
        self.x = 0
        self.y = -100
        self.visible = 0
        self.speed = 4


car = OurCar()

other_cars = [OtherCar1(), OtherCar2(), OtherCar1()]

# здесь можно смело поменять название
pygame.display.set_caption('Hot race 0.3')
clock = pygame.time.Clock()


def check_collision():
    global score
    car_rect = car.sprite.get_rect().move((335 + car.x * 75, car.y))
    for idx in range(len(other_cars)):
        other_rect = other_cars[idx].sprite.get_rect().move((335 + other_cars[idx].x * 75, other_cars[idx].y))
        if other_cars[idx].visible == 1:
            if car_rect.colliderect(other_rect):
                other_cars[idx].visible = 0
                score -= 200
                if score < 0:
                    score = 0


def draw_background():
    global background_y

    game_display.blit(background1, (0, background_y))
    game_display.blit(background2, (0, background_y - background_h))
    background_y += world_speed + accelerate

    if background_y >= display_h:
        background_y = display_h - background_h


def draw_ui():
    text_image = my_font.render(str(score), True, (255, 255, 255))
    game_display.blit(text_image, (720, 20))

    text_image = my_font.render(str(distance), True, (255, 255, 255))
    game_display.blit(text_image, (720, 40))

    distance_pb_w = 800
    pygame.draw.rect(game_display, (200, 200, 200), (0, 0, distance_pb_w, 20))
    if distance <= 500:
        distance_k = distance / 500
        pygame.draw.rect(game_display, (255, 255, 255), (0, 0, distance_pb_w * distance_k, 20))

    fuel_pb_w = 250
    pygame.draw.rect(game_display, (252, 235, 2), (10, 50, fuel_pb_w, 20))
    if fuel == 250:
        fuel_k = 10
        pygame.draw.rect(game_display, (0, 0, 0), (10, 50, fuel_pb_w * fuel_k, 20))

    hp_pb_w = 250
    pygame.draw.rect(game_display, (252, 2, 2), (10, 100, hp_pb_w, 20))
    if hp == 250:
        hp_k = 10
        pygame.draw.rect(game_display, (0, 0, 0), (10, 50, hp_pb_w * hp_k, 20))


def draw_car():
    global distance, fuel
    game_display.blit(car.sprite, (335 + car.x * 75, car.y))
    distance += 1
    fuel -= 0.1


def draw_other_car():
    global other_car, score

    for idx in range(len(other_cars)):
        if other_cars[idx].visible == 1:
            # машинка есть и едет
            game_display.blit(other_cars[idx].sprite, (335 + other_cars[idx].x * 75, other_cars[idx].y))
            other_cars[idx].y += world_speed + accelerate - other_cars[idx].speed

        else:
            rnd = random.randint(0, 300)
            if rnd == 1:
                # машинки нет и мы создаем ее заново
                car_x = random.randint(0, 1)
                if car_x == 0:
                    other_cars[idx] = OtherCar1()
                else:
                    other_cars[idx] = OtherCar2()
                other_cars[idx].visible = 1
        # Условие исчезновения автомобиля
        if other_cars[idx].y > display_h + 300:
            if other_cars[idx].visible == 1:
                score += 100
                other_cars[idx].visible = 0


def process_keyboard(event):
    global accelerate
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            car.x = 0
        if event.key == pygame.K_RIGHT:
            car.x = 1
        if event.key == pygame.K_UP:
            accelerate += 2
            if accelerate > 10:
                accelerate = 10
        if event.key == pygame.K_DOWN:
            accelerate -= 2
            if accelerate < -6:
                accelerate = -6
        if event.key == pygame.K_SPACE:
            accelerate = -6


# самая важная функция в ней все и происходит
def game_loop(update_time):
    global game_exit
    while not game_exit:
        for event in pygame.event.get():
            # print(event)

            process_keyboard(event)
            if event.type == pygame.QUIT:
                game_exit = True

        # Функции поведения
        check_collision()

        # Функции отрисовки
        draw_background()
        draw_car()
        draw_other_car()
        draw_ui()

        pygame.display.update()
        clock.tick(update_time)


game_loop(30)
pygame.quit()
