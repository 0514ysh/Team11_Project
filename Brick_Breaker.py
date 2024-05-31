import pygame
import sys

# 초기화
pygame.init()

# 화면 설정
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Brick Breaker")

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# 패들 설정
paddle = pygame.Rect(375, 550, 50, 10)

# 공 설정
ball = pygame.Rect(390, 540, 10, 10)
ball_dx = 3
ball_dy = -3

# 게임 루프
running = True
while running:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 패들 이동
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= 5
    if keys[pygame.K_RIGHT] and paddle.right < 800:
        paddle.right += 5
    
    # 공 이동
    ball.left += ball_dx
    ball.top += ball_dy

    # 벽과 충돌 처리
    if ball.left <= 0 or ball.right >= 800:
        ball_dx = -ball_dx
    if ball.top <= 0:
        ball_dy = -ball_dy

    # 패들과 충돌 처리
    if ball.colliderect(paddle):
        ball_dy = -ball_dy

    # 화면 그리기
    screen.fill(BLACK)
    pygame.draw.rect(screen, BLUE, paddle)
    pygame.draw.ellipse(screen, RED, ball)
    pygame.display.flip()

    # 프레임 속도 조절
    pygame.time.delay(30)

# 게임 종료 처리
pygame.quit()
sys.exit()
