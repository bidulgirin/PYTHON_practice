# https://www.youtube.com/watch?v=Qsk-xsi73YA 에서 보고만들었음
import pygame
# 시작 화면 보여주기


def display_start_screen():

    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)
    # 흰색으로 동그라미를 그리는데 중심좌표는 start_button 의 중심좌표를 따라가고,
    # 반지름은 60, 선 두께는 5


# 초기화
pygame.init()
screen_width = 1280  # 가로크기
screen_height = 720  # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")


# 시작버튼
start_button = pygame.Rect(0, 0, 120, 120)
start_button.center = (120, screen_height - 120)


# 색상
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


# 게임루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 화면 전체를 까맣게 칠함
    screen.fill(BLACK)

    # 시작 화면 표시
    display_start_screen()

    # 화면 업데이트
    pygame.display.update()
pygame.quit()
