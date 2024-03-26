# 메인화면
# 작성자: 양시현
# 수정 이력:
# - 2024-03-26: 초기버전 생성
import pygame
from pygame.locals import *
import sys

import genetic_algorithm
import modal

class Main:
    # 색깔 정의
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    BLACK = (0, 0, 0)
    GRAY = (43, 45, 48)
    WIDTH, HEIGHT = 800, 600
    
    def __init__(self) -> None:
        self.game = genetic_algorithm
        # 파이게임 초기화
        pygame.init()
        # 화면 크기 설정
        pygame.display.set_caption("메인화면")
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.screen.fill(self.BLACK)
        self.font = pygame.font.SysFont(None, 50)
        self.font2 = pygame.font.SysFont("malgungothic", 40, bold=True)
        self.font3 = pygame.font.SysFont("malgungothic", 30, bold=True)
        # 라벨에 들어갈 문자
        self.label_kor = "유전 알고리즘 테트리스" 
        self.label_eng = "- Genetic Algorithm Tetris -"
        self.label_exit = "나가기"
        self.label_start = "시작"
        self.label_custom = "커스텀 모드"
        # 라벨 렌더링
        self.label_image_kor = self.font2.render(self.label_kor, True, (255, 255, 255))
        self.label_image_eng = self.font.render(self.label_eng, True, (255, 255, 255))
        self.label_image_exit = self.font3.render(self.label_exit, True, (255, 255, 255))
        self.label_image_start = self.font3.render(self.label_start, True, (255, 255, 255))
        self.label_image_custom = self.font3.render(self.label_custom, True, (255, 255, 255))
        self.start_rect = self.label_image_start.get_rect(center=(self.WIDTH//2, self.HEIGHT//2))
        self.exit_rect = self.label_image_exit.get_rect(center=(self.WIDTH//2, self.HEIGHT//2 + 130))
        self.custom_rect = self.label_image_custom.get_rect(center=(self.WIDTH//2, self.HEIGHT//2 + 60))

    def main(self):    
        running = True
        while running:  
            # 입력키가 ESC라면 종료
            for event in pygame.event.get():
                if event.type == KEYDOWN: # 키를 눌렀을때 만약 esc키라면 종료
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                elif event.type == QUIT: # 창을 닫았을 때
                        pygame.quit()
                        sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
                    if self.start_rect.collidepoint(event.pos):
                        self.game.start(2000, 50)
                        pygame.display.set_caption("메인화면")
                        pygame.display.set_mode([self.WIDTH, self.HEIGHT])
                        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
                    elif self.custom_rect.collidepoint(event.pos):
                        modal.main()
                        pygame.display.set_caption("메인화면")
                        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
                    elif self.exit_rect.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()

            # 화면바탕색 지정 
            self.screen.fill(self.GRAY)
            # 라벨 위치 설정
            self.screen.blit(self.label_image_kor, (self.WIDTH // 2 - self.label_image_kor.get_width() // 2, 70))
            self.screen.blit(self.label_image_eng, (self.WIDTH // 2 - self.label_image_eng.get_width() // 2, 130))
            self.screen.blit(self.label_image_start, self.start_rect)
            self.screen.blit(self.label_image_exit, self.exit_rect)
            self.screen.blit(self.label_image_custom, self.custom_rect)
            # 화면 업데이트
            pygame.display.flip()  


if __name__ == "__main__":
    game = Main()
    game.main()