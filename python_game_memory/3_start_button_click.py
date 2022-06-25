# https://www.youtube.com/watch?v=Qsk-xsi73YA 에서 보고만들었음
import pygame

# 시작 화면 보여주기


def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)
    # 흰색으로 동그라미를 그리는데 중심좌표는 start_button 의 중심좌표를 따라가고,
    # 반지름은 60, 선 두께는 5

# 게임화면 보여주기


def display_game_screen():

    print("Game Start")

# pos에 해당하는 버튼 확인


def check_buttons(pos):
    global start
    if start_button.collidepoint(pos):
        start = True


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

# 게임 시작 여부
start = False
# 게임루프
running = True  # 게임이 실행중인가?
while running:
    click_pos = None
    # 이벤트루프
    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?

        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트인가?
            running = False  # 게임이 더 이상 실행중이 아님

        elif event.type == pygame.MOUSEBUTTONUP:
            click_pos = pygame.mouse.get_pos()
            print(click_pos)

    # 화면 전체를 까맣게 칠함
    screen.fill(BLACK)

    # 게임이 true면 실행 아니면 false
    if start:
        display_game_screen()  # 게임 화면 표시
    else:
        # 시작 화면 표시
        display_start_screen()  # 시작 화면 표시
    # 사용자가 클릭한 좌표값이 있다면 (어딘가 클릭했다면)
    if click_pos:
        check_buttons(click_pos)

    # 화면 업데이트
    pygame.display.update()
pygame.quit()