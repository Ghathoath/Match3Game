import pygame
from enum import Enum

class MainMenu:
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    BUTTON_X_ALL = 305
    BUTTON_Y_START = 300
    BUTTON_Y_OPTIONS = 380
    BUTTON_Y_EXIT = 460
    BUTTON_WIDTH = 190
    BUTTON_HEIGHT = 50

    def __init__(self):
        TEST_VALUE=200

    def run(self):
        if pygame.display.get_init():
            print('True')
        screen = pygame.display.set_mode((self.SCREEN_WIDTH,self.SCREEN_HEIGHT))
        pygame.display.set_caption('三消游戏')
        # 渲染标题和按钮
        screen.fill((255, 255, 255))

        start_button = pygame.image.load('image/mainmenu_start.png')
        options_button = pygame.image.load('image/mainmenu_options.png')
        exit_button = pygame.image.load('image/mainmenu_exit.png')

        screen.blit(start_button, (self.BUTTON_X_ALL, self.BUTTON_Y_START))
        screen.blit(options_button, (self.BUTTON_X_ALL, self.BUTTON_Y_OPTIONS))
        screen.blit(exit_button, (self.BUTTON_X_ALL, self.BUTTON_Y_EXIT))
        pygame.display.flip()

        # 获取参数
        button_state = {'start':0,'options':0,'exit':0}

        # 主循环
        while True:
            for event in pygame.event.get():
                # 鼠标按下
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x,mouse_y=pygame.mouse.get_pos()
                    # start
                    if (mouse_x >= self.BUTTON_X_ALL and
                        mouse_x <= self.BUTTON_X_ALL+self.BUTTON_WIDTH and
                        mouse_y >= self.BUTTON_Y_START and
                        mouse_y <= self.BUTTON_Y_START+self.BUTTON_HEIGHT):
                        start_button = pygame.image.load('image/mainmenu_start_pressed.png')
                        screen.blit(start_button, (self.BUTTON_X_ALL, self.BUTTON_Y_START+6))
                        button_state['start']=1

                    # options
                    if (mouse_x >= self.BUTTON_X_ALL and
                        mouse_x <= self.BUTTON_X_ALL+self.BUTTON_WIDTH and
                        mouse_y >= self.BUTTON_Y_OPTIONS and
                        mouse_y <= self.BUTTON_Y_OPTIONS+self.BUTTON_HEIGHT):
                        options_button = pygame.image.load('image/mainmenu_options_pressed.png')
                        screen.blit(options_button, (self.BUTTON_X_ALL, self.BUTTON_Y_OPTIONS+6))
                        button_state['options']=1

                    # exit
                    if (mouse_x >= self.BUTTON_X_ALL and
                        mouse_x <= self.BUTTON_X_ALL+self.BUTTON_WIDTH and
                        mouse_y >= self.BUTTON_Y_EXIT and
                        mouse_y <= self.BUTTON_Y_EXIT+self.BUTTON_HEIGHT):
                        exit_button = pygame.image.load('image/mainmenu_exit_pressed.png')
                        screen.blit(exit_button, (self.BUTTON_X_ALL, self.BUTTON_Y_EXIT+6))
                        button_state['exit']=1

                    pygame.display.update()

                # 鼠标抬起
                if event.type == pygame.MOUSEBUTTONUP:
                    if button_state['start']==1:
                        button_state['start'] = 0
                        start_button = pygame.image.load('image/mainmenu_start.png')
                        screen.blit(start_button, (self.BUTTON_X_ALL, self.BUTTON_Y_START))
                    if button_state['options']==1:
                        button_state['options'] = 0
                        options_button = pygame.image.load('image/mainmenu_options.png')
                        screen.blit(options_button, (self.BUTTON_X_ALL, self.BUTTON_Y_OPTIONS))
                    if button_state['exit']==1:
                        button_state['exit'] = 0
                        exit_button = pygame.image.load('image/mainmenu_exit.png')
                        screen.blit(exit_button, (self.BUTTON_X_ALL, self.BUTTON_Y_EXIT))
                        exit()
                    pygame.display.update()
                if event.type == pygame.QUIT:
                    exit()


    class Button_State(Enum):
        normal = 0
        pressed =1
