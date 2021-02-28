import pygame
import random
import time
import pickle

pygame.init()

sound = pygame.mixer.Sound('eaten.mp3')

width = 800
height = 600
size = width, height

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Змейка")
clock = pygame.time.Clock()

snake_head = (0, 255, 0)
snake_tail = (0, 153, 0)
fruit = (255, 0, 0)

clock = pygame.time.Clock()

snake_speed = 10
snake_size = 10


def snake(snake_size, snake_lst):
    for i in snake_lst:
        pygame.draw.rect(screen, snake_tail, [i[0], i[1], snake_size, snake_size])


def score(score):
    font = pygame.font.Font(None, 50)
    text = font.render('Счёт:' + str(score), True, (0, 153, 0))
    screen.blit(text, [0, 0])


def loss(message):
    font = pygame.font.Font(None, 50)
    text = font.render(message, True, (0, 100, 100))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (0, 255, 0), (text_x - 10, text_y - 10,
                                           text_w + 20, text_h + 20), 1)


def main():
    game_over = False
    game_close = False

    x = width / 2
    y = height / 2
    x_shift = 0
    y_shift = 0

    snake_lst = []
    snake_length = 1

    food_x = round(random.randrange(0, width - snake_size) / 10.0) * 10
    food_y = round(random.randrange(0, width - snake_size) / 10.0) * 10

    while not game_over:
        while game_close == True:
            screen.fill((0, 0, 0))
            loss("Вы проиграли <3")
            score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_e:
                        main()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_shift == 0:
                    x_shift = -snake_size
                    y_shift = 0
                elif event.key == pygame.K_RIGHT and x_shift == 0:
                    x_shift = snake_size
                    y_shift = 0
                elif event.key == pygame.K_UP and y_shift == 0:
                    y_shift = -snake_size
                    x_shift = 0
                elif event.key == pygame.K_DOWN and y_shift == 0:
                    y_shift = snake_size
                    x_shift = 0

        if x >= width or y >= height or x < 0 or y < 0:
            game_close = True

        x += x_shift
        y += y_shift
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, snake_head, [x, y, snake_size, snake_size])
        pygame.draw.rect(screen, fruit, [food_x, food_y, snake_size, snake_size])
        pygame.display.update()
        snake_head1 = []
        snake_head1.append(x)
        snake_head1.append(y)
        snake_lst.append(snake_head1)
        if len(snake_lst) > snake_length:
            del snake_lst[0]

        for i in snake_lst[:-1]:
            if i == snake_head1:
                game_close = True

        snake(snake_size, snake_lst)
        score(snake_length - 1)
        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(1, width - snake_size) / 10.0) * 10
            food_y = round(random.randrange(1, height - snake_size) / 10.0) * 10
            snake_length += 1
            sound.play()
            print('<3')
        clock.tick(30)

    pygame.quit()
    quit()

if __name__ == '__main__':
    main()
