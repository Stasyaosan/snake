import pygame
import random

pygame.init()


def game():
    x_win = 1200
    y_win = 820
    size = (x_win, y_win)
    win = pygame.display.set_mode(size)
    pygame.display.set_caption('Змейка любит есть')
    frame_color = (120, 255, 50)
    size_blok = 26
    trava_1 = pygame.image.load('Трава 1.jpg')
    trava_2 = pygame.image.load('Трава 2.jpg')
    trava_1_small = pygame.transform.scale(trava_1, (size_blok, size_blok))
    trava_2_small = pygame.transform.scale(trava_2, (size_blok, size_blok))
    count_bloks = 26
    apple = pygame.image.load('яблоко.png')
    apple_small = pygame.transform.scale(apple, (size_blok, size_blok))
    snake_head_up = pygame.image.load('голова змеи вверх.png')
    snake_head_up_small = pygame.transform.scale(snake_head_up, (size_blok, size_blok))
    snake_head_down = pygame.image.load('голова змеи вниз.png')
    snake_head_down_small = pygame.transform.scale(snake_head_down, (size_blok, size_blok))
    snake_head_left = pygame.image.load('голова змеи влево.png')
    snake_head_left_small = pygame.transform.scale(snake_head_left, (size_blok, size_blok))
    snake_head_right = pygame.image.load('голова змеи вправо.png')
    snake_head_right_small = pygame.transform.scale(snake_head_right, (size_blok, size_blok))
    snake_color = pygame.image.load('тело змеи.png')
    snake_color_small = pygame.transform.scale(snake_color, (size_blok, size_blok))
    margin = 1
    run = True
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('comicsansms', 32)

    class Snake():
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.left = False
            self.right = True
            self.up = False
            self.down = False
            self.speed = 1
            self.step_y = self.speed
            self.step_x = self.speed
            self.stop = 10
            self.stop_new = self.stop
            self.eat_stop = False
            self.snake_blocks = [[self.x, self.y]]
            self.dlina = 3

        def move(self):
            if self.up == True:
                self.step_y = -1
                self.step_x = 0

            if self.down == True:
                self.step_y = 1
                self.step_x = 0

            if self.left == True:
                self.step_x = -1
                self.step_y = 0

            if self.right == True:
                self.step_x = 1
                self.step_y = 0
            self.x += self.step_x
            self.y += self.step_y
            self.snake_blocks.append([self.x, self.y])
            while len(self.snake_blocks) > self.dlina:
                self.snake_blocks.pop(0)

        def draw_blok_snake(self, color, row, column):
            win.blit(color, (10 + column * size_blok + margin * (column + 1),
                             100 + row * size_blok + margin * (row + 1)))

    def draw_blok(color, row, column):
        win.blit(color, (10 + column+ * size_blok + margin * (column + 1),
                         100 + row * size_blok + margin * (row + 1)))

    class Apple():
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.apple_x_y = [self.x, self.y]

    snake = Snake(count_bloks / 2, count_bloks / 2)
    apple_pro = Apple(random.randint(1, count_bloks - 1), random.randint(1, count_bloks - 1))

    def redraw():
        win.fill(frame_color)
        font_render = font.render('Счёт:' + str(snake.dlina), True, (255, 0, 0))
        textRect = font_render.get_rect()
        textRect.center = (300, 50)
        win.blit(font_render, textRect)
        for row in range(count_bloks):
            for column in range(count_bloks):
                if (row + column) % 2 == 0:
                    color = trava_2_small
                else:
                    color = trava_1_small
                draw_blok(color, row, column)
        draw_blok(apple_small, apple_pro.y, apple_pro.x)
        if snake.stop >= 0:
            snake.stop -= 1

        if snake.stop <= 0:
            snake.move()
            snake.eat_stop = False
            snake.stop = snake.stop_new
            snake.stop_new -= 0.005

        for o in range(len(snake.snake_blocks) - 1):
            snake.draw_blok_snake(snake_color_small, snake.snake_blocks[o][1], snake.snake_blocks[o][0])
            if snake.up:
                snake.draw_blok_snake(snake_head_up_small, snake.snake_blocks[-1][1], snake.snake_blocks[-1][0])
            elif snake.down:
                snake.draw_blok_snake(snake_head_down_small, snake.snake_blocks[-1][1], snake.snake_blocks[-1][0])
            elif snake.right:
                snake.draw_blok_snake(snake_head_right_small, snake.snake_blocks[-1][1], snake.snake_blocks[-1][0])
            elif snake.left:
                snake.draw_blok_snake(snake_head_left_small, snake.snake_blocks[-1][1], snake.snake_blocks[-1][0])

        pygame.display.update()

    while run:
        clock.tick(20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit(0)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and not snake.down:
            snake.up = True
            snake.down = False
            snake.left = False
            snake.right = False

        if keys[pygame.K_DOWN] and not snake.up:
            snake.down = True
            snake.up = False
            snake.left = False
            snake.right = False

        if keys[pygame.K_LEFT] and not snake.right:
            snake.up = False
            snake.down = False
            snake.left = True

            snake.right = False

        if keys[pygame.K_RIGHT] and not snake.left:
            snake.up = False
            snake.down = False
            snake.left = False
            snake.right = True
        redraw()
        if snake.snake_blocks[-1] == apple_pro.apple_x_y and snake.eat_stop == False:
            snake.dlina += 1
            apple_pro.x = random.randint(1, count_bloks - 1)
            apple_pro.y = random.randint(1, count_bloks - 1)
            apple_pro.apple_x_y = [apple_pro.x, apple_pro.y]
            snake.eat_stop = True

        for k in snake.snake_blocks:
            if k[0] > count_bloks - 1 or k[0] < 0:
                run = False
            if k[1] > count_bloks - 1 or k[1] < 0:
                run = False

        for j in range(len(snake.snake_blocks) - 1):
            if snake.snake_blocks[j] == snake.snake_blocks[-1]:
                run = False

    pygame.quit()


x_win = 1200
y_win = 820
size = (x_win, y_win)
win = pygame.display.set_mode(size)
pygame.display.set_caption('Змейка любит есть')
menu_bg = pygame.image.load('Главный фон.jpg')
menu_bg_small = pygame.transform.scale(menu_bg, size)
play_button = pygame.image.load('Кнопка играть.png')
quit_button = pygame.image.load('Кнопка выход.png')
run = True
hitbox_play_button = (x_win / 2 + 70, 200, 163, 51)
hitbox_quit_button = (x_win / 2 + 70, 500, 160, 47)
clock = pygame.time.Clock()


def redraw():
    win.blit(menu_bg_small, (0, 0))
    win.blit(play_button, (x_win / 2 + 70, 200))
    win.blit(quit_button, (x_win / 2 + 70, 500))
    pygame.display.update()


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pos = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONUP:
        if hitbox_play_button[1] <= pos[1] <= hitbox_play_button[3] + hitbox_play_button[1]:
            if hitbox_play_button[0] <= pos[0] <= hitbox_play_button[2] + hitbox_play_button[0]:
                game()

        if hitbox_quit_button[1] <= pos[1] <= hitbox_quit_button[3] + hitbox_quit_button[1]:
            if hitbox_quit_button[0] <= pos[0] <= hitbox_quit_button[2] + hitbox_quit_button[0]:
                raise SystemExit(0)

    redraw()
pygame.quit()
