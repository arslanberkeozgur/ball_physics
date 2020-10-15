import pygame
pygame.mixer.init()

WIDTH, HEIGHT = 1200, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

hit = pygame.mixer.Sound('hit.wav')


FPS = 120
clock = pygame.time.Clock()


class Ball:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.ax = 0
        self.ay = 0

    def move(self):
        self.vx += self.ax
        self.vy += self.ay
        self.x += self.vx
        self.y += self.vy

    def draw(self):
        pygame.draw.circle(WIN, (255, 255, 255), (int(self.x), int(self.y)), 16)


ball = Ball(600,484,0,0)


def main():
    run = True
    mouse_down = False
    mouse_release = False

    def draw():
        WIN.fill((110, 110, 110))
        pygame.draw.rect(WIN, (0, 0, 0),(0, 500, WIDTH, 100))
        pygame.draw.rect(WIN, (50, 50, 50),(0, 502, WIDTH, 100))
        ball.draw()

        if mouse_down:
            pygame.draw.line(WIN,(255,255,255),(int(ball.x), int(ball.y)), (pos[0], pos[1]), 2)

        pygame.display.update()

    while run:
        pos = pygame.mouse.get_pos()
        clock.tick(FPS)

        if mouse_release:
            ball.ax = (ball.x - pos[0]) // 20
            ball.ay = (ball.y - pos[1]) // 20
            mouse_release = False

        if ball.x <= 0 or ball.x >= WIDTH:
            ball.vx = - ball.vx
            hit.play()
        if ball.y <= 0 or ball.y >= 485:
            ball.vy = - ball.vy
            hit.play()

        ball.move()

        ball.vx *= 0.998
        ball.vy *= 0.998
        if ball.y < 482:
            ball.ay = 0.12
        else:
            ball.ay = 0

        if ball.vy > 0 and 470 < ball.y < 485:
            ball.vx *= 0.98
            ball.vy *= 0.98
            if ball.vy < 1.2 and 482 < ball.y < 485:
                ball.y = 484
                ball.vy = 0
                ball.vx *= 0.5
        ball.ax = 0

        draw()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_release = False
                mouse_down = True
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_release = True
                mouse_down = False

            if event.type == pygame.QUIT:
                run = False





main()