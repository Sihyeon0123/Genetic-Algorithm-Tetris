# 가중치를 입력받을 화면
# 작성자: 양시현
# 수정 이력:
# - 2024-03-26: 초기버전 생성
import pygame
import sys

import individual
import tetris
import genetic_algorithm

class NumberInputBox:
    def __init__(self, screen, x, y, width, height, font, text_color, box_color, active_box_color, prompt):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font = pygame.font.SysFont("malgungothic", 25, bold=True)
        self.text_color = text_color
        self.box_color = box_color
        self.active_box_color = active_box_color
        self.text = ''
        self.prompt = prompt
        self.active = False  # 활성화 상태를 나타내는 플래그

    def draw(self):
        prompt_surface = self.font.render(self.prompt, True, self.text_color)
        self.screen.blit(prompt_surface, (self.x - 120, self.y))
        if self.active:  # 활성화된 상자인 경우 다른 색상으로 그림
            pygame.draw.rect(self.screen, self.active_box_color, (self.x, self.y, self.width, self.height), 0)
        else:
            pygame.draw.rect(self.screen, self.box_color, (self.x, self.y, self.width, self.height), 0)
        font_surface = self.font.render(self.text, True, self.text_color)
        self.screen.blit(font_surface, (self.x + 5, self.y + 5))

    def add_text(self, char):
        if (char.isdigit() or char == '.' or (char == '-' and len(self.text) == 0)) and len(self.text) < 22:
            # If the character is a digit, dot, or a negative sign at the beginning of the text and the length is less than 18
            if char == '.' and '.' in self.text:
                return
            # Ignore additional negative signs
            if char == '-' and '-' in self.text:
                return
            # Add the character to the text
            self.text += char

    def delete_text(self):
        self.text = self.text[:-1]

    def get_text(self):
        return self.text

    def set_active(self, active):
        self.active = active

def main():
    pygame.init()

    screen_width = 500
    screen_height = 450
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("가중치 입력창")

    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()

    input_boxes = []
    box_x = 150
    box_width = 320
    box_height = 40
    spacing = 10

    font2 = pygame.font.SysFont("malgungothic", 15, bold=True)
    # 메시지 설정
    msg_line1 = "가중치 값을 기본값으로 두면"
    msg_line2 = "목표와 개체수만 조절 가능합니다."
    label_msg1 = font2.render(msg_line1, True, (255, 255, 255))
    label_msg2 = font2.render(msg_line2, True, (255, 255, 255))
    msg_rect1 = label_msg1.get_rect(center=(screen_width // 2, 360))
    msg_rect2 = label_msg2.get_rect(center=(screen_width // 2, 380))

    prompts = ["목표점수:", "개체수   :", "구멍개수:", "높이      :", "완성될줄:", "불연속성:"]
    for i in range(6):
        box_y = 50 + (box_height + spacing) * i
        input_box = NumberInputBox(screen, box_x, box_y, box_width, box_height, font, (255, 255, 255), (43, 45, 48), (64, 68, 72), prompts[i])
        input_boxes.append(input_box)

    # 3~6칸의 기본값을 0.0으로 설정
    input_boxes[0].text = '0'
    input_boxes[1].text = '0'
    input_boxes[2].text = '0.0'
    input_boxes[3].text = '0.0'
    input_boxes[4].text = '0.0'
    input_boxes[5].text = '0.0'

    current_box_index = 0  # 현재 입력 중인 상자 인덱스
    input_boxes[current_box_index].set_active(True)  # 첫 번째 상자 활성화
    running = True
    
    while running:
        screen.fill((43, 45, 48))
        screen.blit(label_msg1, msg_rect1)
        screen.blit(label_msg2, msg_rect2)
        for input_box in input_boxes:
            input_box.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_TAB:
                    if current_box_index == 5:  # 마지막 상자
                        numbers = [float(input_box.get_text()) for input_box in input_boxes]
                        running = False
                        
                        if numbers[2] == 0 and numbers[3] == 0 and numbers[4] == 0 and numbers[5] == 0:
                            genetic_algorithm.start(int(numbers[0]), int(numbers[1]))
                        else:
                            indv = individual.Individual(0, numbers[2],numbers[3],numbers[4],numbers[5])
                            game = tetris.main('AI', 0, indv, int(numbers[0]), int(numbers[1]))
                    else:
                        # 현재 상자 비활성화 및 다음 상자 활성화
                        input_boxes[current_box_index].set_active(False)
                        current_box_index = min(current_box_index + 1, 5)
                        input_boxes[current_box_index].set_active(True)
                elif event.key == pygame.K_BACKSPACE:
                    input_boxes[current_box_index].delete_text()
                elif event.key == pygame.K_DOWN:
                    input_boxes[current_box_index].set_active(False)
                    current_box_index = min(current_box_index + 1, 5)
                    input_boxes[current_box_index].set_active(True)
                elif event.key == pygame.K_UP:
                    input_boxes[current_box_index].set_active(False)
                    current_box_index = max(current_box_index - 1, 0)
                    input_boxes[current_box_index].set_active(True)
                else:
                    input_boxes[current_box_index].add_text(event.unicode)
        
        pygame.display.flip()
        clock.tick(30)
        

if __name__ == "__main__":
    main()
