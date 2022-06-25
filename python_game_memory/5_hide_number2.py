# https://www.youtube.com/watch?v=Qsk-xsi73YA 에서 보고만들었음
import pygame
from random import *


# 레벨에 맞게 설정
def setup(level):
    # 얼마나 많은 숫자를 보여줄 것인가?
    number_count = (level // 3) + 5
    number_count = min(number_count, 20)  # 만약 20을 초과하면 20으로 처리
    # 실제 화면에 grid 형태로 숫자를 랜덤으로 배치
    shuffle_grid(number_count)

# 숫자 섞기 (가장 중요한 부분)


def shuffle_grid(number_count):
    rows = 5
    columns = 9

    cell_size = 130 # 각 Grid cell별 가로, 세로 크기
    button_size = 110 # Grid cell 내에 실제로 그려질 버튼 크기
    screen_left_margin = 55 # 전체 스크린 왼쪽 여백
    screen_top_margin = 20 # 전체 스크린 위쪽 여백
    grid = [[0 for col in range(columns)] for row in range(rows)]  # 5*9

    number = 1  # 시작 숫자 1부터 number_count 까지
    while number <= number_count:
        row_idx = randrange(0, rows)    # 0, 1, 2, 3, 4 중에서 랜덤으로 뽑기
        col_idx = randrange(0, columns)  # 0 ~ 8 중에서 랜덤으로 뽑기

        if grid[row_idx][col_idx] == 0:
            grid[row_idx][col_idx] = number  # 숫자 지정
            number += 1

            #  현재 gird cell  위치 기준으로 x , y  위치를 구함
            center_x = screen_left_margin + (col_idx * cell_size) + (cell_size / 2)
            center_y = screen_top_margin + (row_idx * cell_size) + (cell_size /2 )
            # 버튼생성
            button = pygame.Rect(0, 0 , button_size , button_size) 
            button.center = (center_x , center_y) # 버튼 중심 생성
            # 변수에다가  button(배열) 를 넣는다(append)
            number_buttons.append(button) 

            
    # 배치된 랜덤 숫자 확인
    print(grid)
# 시작 화면 보여주기


def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)
    # 흰색으로 동그라미를 그리는데 중심좌표는 start_button 의 중심좌표를 따라가고,
    # 반지름은 60, 선 두께는 5

# 게임화면 보여주기
def display_game_screen():
    # 버튼범위그려주는코드 enumerate는 이 함수는 입력받은 숫자에 해당되는 범위의 값을 반복 가능한 객체로 만들어 리턴합니다
   for idx, rect in enumerate(number_buttons, start = 1):
        pygame.draw.rect(screen, GRAY , rect)

        # 실제 숫자 텍스트
        cell_text = game_font.render(str(idx), True, WHITE)
        text_rect = cell_text.get_rect(center=rect.center)
        screen.blit(cell_text , text_rect)

# pos에 해당하는 버튼 확인
def check_buttons(pos):
    global start

    if start: # 게임이 시작했다면
        check_number_button(pos)
    elif start_button.collidepoint(pos):
        start = True
def check_number_button(pos):
    for button in number_buttons:
        if button.collidepoint(pos):
            if button == number_buttons[0]:
                print("Correct")
            else:
                print("Wrong")
            break
# 초기화
pygame.init()
screen_width = 1280  # 가로크기
screen_height = 720  # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")

# font 설정
game_font = pygame.font.Font(None ,120)

# 시작버튼
start_button = pygame.Rect(0, 0, 120, 120)
start_button.center = (120, screen_height - 120)

# 색상
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50 ,50, 50)

number_buttons = []
# 게임 시작 여부
start = False
# 숫자 숨김 여부 (사용자가 1을 클릭했거나, 보여주는 시간 초과했을 때 )
hidden = False

setup(1)
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
