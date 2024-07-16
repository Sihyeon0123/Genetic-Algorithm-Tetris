# 결과를 출력할 화면
# 작성자: 양시현
# 수정 이력:
# - 2024-03-26: 초기버전 생성
import pygame
import sys

def display_result(screen, font, param1, param2, param3, param4, param5):
    font_label = pygame.font.SysFont("malgungothic", 20, bold=True)
    font_param = pygame.font.SysFont("malgungothic", 20, bold=True)
    screen.fill((0, 0, 0))  # 화면을 검은색으로 채웁니다.

    # "목표 도달!" 텍스트를 그립니다. 화면의 중앙 상단에 위치시킵니다.
    text_goal = font.render("목표 도달!", True, (255, 255, 255))
    text_goal_rect = text_goal.get_rect(center=(screen.get_width() // 2, 50))
    screen.blit(text_goal, text_goal_rect)

    # 매개변수 라벨을 설정하고 출력합니다.
    labels = ["도달 점수 :", "구멍 개수 :", "높      이 :", "완성될 줄 :", "불연속성  :"]
    y_offset = 150  # 텍스트의 세로 위치를 설정합니다.
    for label, param in zip(labels, [param1, param2, param3, param4, param5]):
        text_label = font_label.render(label, True, (255, 255, 255))
        text_label_rect = text_label.get_rect(center=(screen.get_width() // 4, y_offset))
        screen.blit(text_label, text_label_rect)
        
        text_param = font_param.render(str(param), True, (255, 255, 255))
        text_param_rect = text_param.get_rect(center=(screen.get_width() // 2 + 20, y_offset))
        screen.blit(text_param, text_param_rect)
        
        y_offset += 80  # 다음 텍스트의 위치를 조정합니다.

    pygame.display.flip()  # 화면을 업데이트합니다.

def main(fitness, hw, aw, clw, bw):
    pygame.init()

    # 화면 설정
    screen_width = 610
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("결과화면")

    # 폰트 설정
    font = pygame.font.SysFont("malgungothic", 35, bold=True)

    # 매개변수 설정
    param1 = str(fitness)
    param2 = str(hw)
    param3 = str(aw)
    param4 = str(clw)
    param5 = str(bw)

    # 결과 출력
    display_result(screen, font, param1, param2, param3, param4, param5)

    # 이벤트 루프
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
                    running = False

if __name__ == "__main__":
    main(0,0,0,0,0)
