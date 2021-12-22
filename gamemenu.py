import pygame
from enum import Enum
from game import *


class GameMenu:
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    BUTTON_X_ALL = 100
    BUTTON_Y_CHAPTER = 150
    BUTTON_Y_SKILL = 250
    BUTTON_Y_SHOP = 350
    BUTTON_WIDTH = 190
    BUTTON_HEIGHT = 50
    INFO_X = 350
    INFO_Y = 80

    def __init__(self, screen):
        self.screen = screen

    def draw_game_menu(self, button_state):
        if button_state['chapter']:
            chapter_button = pygame.image.load('image/gamemenu_pressed_chapter.png')
        else:
            chapter_button = pygame.image.load('image/gamemenu_chapter.png')
        if button_state['skill']:
            skill_button = pygame.image.load('image/gamemenu_pressed_skill.png')
        else:
            skill_button = pygame.image.load('image/gamemenu_skill.png')
        if button_state['shop']:
            shop_button = pygame.image.load('image/gamemenu_pressed_shop.png')
        else:
            shop_button = pygame.image.load('image/gamemenu_shop.png')
        # character_info = pygame.image.load('image/character_info.png')

        self.screen.blit(chapter_button, (self.BUTTON_X_ALL, self.BUTTON_Y_CHAPTER + button_state['chapter'] * 6))
        self.screen.blit(skill_button, (self.BUTTON_X_ALL, self.BUTTON_Y_SKILL + button_state['skill'] * 6))
        self.screen.blit(shop_button, (self.BUTTON_X_ALL, self.BUTTON_Y_SHOP + button_state['shop'] * 6))
        # self.screen.blit(character_info, (self.INFO_X, self.INFO_Y))
        pygame.display.update()

    def run(self):
        if pygame.display.get_init():
            print('True')
        # 获取参数
        button_state = {'chapter': 0, 'skill': 0, 'shop': 0}
        # 渲染主菜单
        self.screen.fill((255, 255, 255))
        stand = pygame.image.load('image/gamemenu_stand.jpg')
        self.screen.blit(stand,(430,0))
        pygame.display.flip()
        self.draw_game_menu(button_state)

        # 主循环
        gamemenuloop = True
        while gamemenuloop:
            for event in pygame.event.get():
                # 鼠标按下
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    # chapter
                    if (self.BUTTON_X_ALL <= mouse_x <= self.BUTTON_X_ALL + self.BUTTON_WIDTH and
                            self.BUTTON_Y_CHAPTER <= mouse_y <= self.BUTTON_Y_CHAPTER + self.BUTTON_HEIGHT):
                        button_state['chapter'] = 1

                    # skill
                    if (self.BUTTON_X_ALL <= mouse_x <= self.BUTTON_X_ALL + self.BUTTON_WIDTH and
                            self.BUTTON_Y_SKILL <= mouse_y <= self.BUTTON_Y_SKILL + self.BUTTON_HEIGHT):
                        button_state['skill'] = 1

                    # shop
                    if (self.BUTTON_X_ALL <= mouse_x <= self.BUTTON_X_ALL + self.BUTTON_WIDTH and
                            self.BUTTON_Y_SHOP <= mouse_y <= self.BUTTON_Y_SHOP + self.BUTTON_HEIGHT):
                        button_state['shop'] = 1

                # 鼠标抬起
                if event.type == pygame.MOUSEBUTTONUP:
                    if button_state['chapter'] == 1:
                        button_state['chapter'] = 0
                        gamemenuloop = False
                        break
                    if button_state['skill'] == 1:
                        button_state['skill'] = 0
                    if button_state['shop'] == 1:
                        button_state['shop'] = 0
                if event.type == pygame.QUIT:
                    exit()

            # 渲染主菜单
            self.screen.fill((255, 255, 255))
            self.screen.blit(stand, (380, 0))
            self.draw_game_menu(button_state)
            pygame.display.update()

    class ButtonState(Enum):
        normal = 0
        pressed = 1
