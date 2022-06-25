# https://www.youtube.com/watch?v=Qsk-xsi73YA 에서 보고만들었음
import pygame

# 초기화
pygame.init()
screen_width = 1280  # 가로크기
screen_height = 720  # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")

# 게임루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
