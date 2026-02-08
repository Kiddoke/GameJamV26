import pygame
import sys
from .assets import *
from .settings import *

QUESTION = "Hva er hovedoppgaven til en DNS-server?"

ANSWERS = [
    ("Kryptere data som sendes over internett", False),
    ("Oversette domenenavn til IP-adresser", False),
    ("Lagre nettsider slik at de lastes raskere", True)
]

def run_quiz2(screen, board_rect):
    font = pygame.font.Font(PIXELFONT, 28)
    clock = pygame.time.Clock()

    # click answers
    answer_rects = []
    for i in range(3):
        rect = pygame.Rect(
            board_rect.x + 40,          # absolutt x
            board_rect.y + 100 + i*60,  # absolutt y
            board_rect.width - 80,      # bredde
            40                           # høyde
        )
        answer_rects.append(rect)
    
    running = True
    while running:
        clock.tick(60)
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for i, rect in enumerate(answer_rects):
                    if rect.collidepoint(mouse_pos):
                        return ANSWERS[i][1]
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return False
        
        screen.blit(WHITEBOARD, board_rect.topleft)
        
        # draw overlay on whiteboard
        # question
        q_surf = font.render(QUESTION, True, BLACK)
        screen.blit(q_surf, (board_rect.x + 40, board_rect.y + 40))

        # answers
        for rect, (text, _) in zip(answer_rects, ANSWERS):
            hovered = rect.collidepoint(mouse_pos)
            outline_color = (200, 200, 200) if hovered else BLACK
            pygame.draw.rect(screen, outline_color, rect, 2)
            a_surf = font.render(text, True, BLACK)
            screen.blit(a_surf, (rect.x + 10, rect.y + 8))
        pygame.display.flip()

