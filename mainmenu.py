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

    def __init__(self, screen):
        self.screen = screen

    def draw_main_menu(self):
        start_button = pygame.image.load('image/mainmenu_start.png')
        options_button = pygame.image.load('image/mainmenu_options.png')
        exit_button = pygame.image.load('image/mainmenu_exit.png')

        self.screen.blit(start_button, (self.BUTTON_X_ALL, self.BUTTON_Y_START))
        self.screen.blit(options_button, (self.BUTTON_X_ALL, self.BUTTON_Y_OPTIONS))
        self.screen.blit(exit_button, (self.BUTTON_X_ALL, self.BUTTON_Y_EXIT))
        pygame.display.update()

    def run(self):
        if pygame.display.get_init():
            print('True')
        # 渲染主菜单
        self.screen.fill((255, 255, 255))
        pygame.display.flip()
        self.draw_main_menu()
        # 获取参数
        button_state = {'start': 0, 'options': 0, 'exit': 0}

        # 主循环
        mainloop = True
        while mainloop:
            for event in pygame.event.get():
                # 鼠标按下
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    # start
                    if (self.BUTTON_X_ALL <= mouse_x <= self.BUTTON_X_ALL+self.BUTTON_WIDTH and
                            self.BUTTON_Y_START <= mouse_y <= self.BUTTON_Y_START + self.BUTTON_HEIGHT):
                        start_button = pygame.image.load('image/mainmenu_start_pressed.png')
                        self.screen.blit(start_button, (self.BUTTON_X_ALL, self.BUTTON_Y_START+6))
                        button_state['start'] = 1

                    # options
                    if (self.BUTTON_X_ALL <= mouse_x <= self.BUTTON_X_ALL+self.BUTTON_WIDTH and
                            self.BUTTON_Y_OPTIONS <= mouse_y <= self.BUTTON_Y_OPTIONS + self.BUTTON_HEIGHT):
                        options_button = pygame.image.load('image/mainmenu_options_pressed.png')
                        self.screen.blit(options_button, (self.BUTTON_X_ALL, self.BUTTON_Y_OPTIONS+6))
                        button_state['options'] = 1

                    # exit
                    if (self.BUTTON_X_ALL <= mouse_x <= self.BUTTON_X_ALL+self.BUTTON_WIDTH and
                            self.BUTTON_Y_EXIT <= mouse_y <= self.BUTTON_Y_EXIT + self.BUTTON_HEIGHT):
                        exit_button = pygame.image.load('image/mainmenu_exit_pressed.png')
                        self.screen.blit(exit_button, (self.BUTTON_X_ALL, self.BUTTON_Y_EXIT+6))
                        button_state['exit'] = 1

                    pygame.display.update()

                # 鼠标抬起
                if event.type == pygame.MOUSEBUTTONUP:
                    if button_state['start'] == 1:
                        button_state['start'] = 0
                        start_button = pygame.image.load('image/mainmenu_start.png')
                        self.screen.blit(start_button, (self.BUTTON_X_ALL, self.BUTTON_Y_START))
                        mainloop = False
                        break
                    if button_state['options'] == 1:
                        button_state['options'] = 0
                        options_button = pygame.image.load('image/mainmenu_options.png')
                        self.screen.blit(options_button, (self.BUTTON_X_ALL, self.BUTTON_Y_OPTIONS))
                    if button_state['exit'] == 1:
                        button_state['exit'] = 0
                        exit_button = pygame.image.load('image/mainmenu_exit.png')
                        self.screen.blit(exit_button, (self.BUTTON_X_ALL, self.BUTTON_Y_EXIT))
                        exit()
                    pygame.display.update()
                if event.type == pygame.QUIT:
                    exit()

    class Button_State(Enum):
        normal = 0
        pressed = 1
