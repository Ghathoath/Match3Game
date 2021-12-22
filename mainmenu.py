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
        self.bg = pygame.image.load('image/mainmenu_bg.jpg')
        self.bg_options = pygame.image.load('image/bg_options.png')

    def draw_main_menu(self, button_state):
        self.screen.blit(self.bg, (0, 0))
        if button_state['start']:
            start_button = pygame.image.load('image/mainmenu_start_pressed.png')
        else:
            start_button = pygame.image.load('image/mainmenu_start.png')
        if button_state['options']:
            options_button = pygame.image.load('image/mainmenu_options_pressed.png')
        else:
            options_button = pygame.image.load('image/mainmenu_options.png')
        if button_state['exit']:
            exit_button = pygame.image.load('image/mainmenu_exit_pressed.png')
        else:
            exit_button = pygame.image.load('image/mainmenu_exit.png')

        self.screen.blit(start_button, (self.BUTTON_X_ALL, self.BUTTON_Y_START + button_state['start'] * 6))
        self.screen.blit(options_button, (self.BUTTON_X_ALL, self.BUTTON_Y_OPTIONS + button_state['options'] * 6))
        self.screen.blit(exit_button, (self.BUTTON_X_ALL, self.BUTTON_Y_EXIT + button_state['exit'] * 6))
        pygame.display.update()

    def run(self):
        if pygame.display.get_init():
            print('True')
        # 获取参数
        button_state = {'start': 0, 'options': 0, 'exit': 0}
        # 渲染主菜单
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.bg,(0,0))
        pygame.display.flip()
        self.draw_main_menu(button_state)

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
                        button_state['start'] = 1

                    # options
                    if (self.BUTTON_X_ALL <= mouse_x <= self.BUTTON_X_ALL+self.BUTTON_WIDTH and
                            self.BUTTON_Y_OPTIONS <= mouse_y <= self.BUTTON_Y_OPTIONS + self.BUTTON_HEIGHT):
                        button_state['options'] = 1

                    # exit
                    if (self.BUTTON_X_ALL <= mouse_x <= self.BUTTON_X_ALL+self.BUTTON_WIDTH and
                            self.BUTTON_Y_EXIT <= mouse_y <= self.BUTTON_Y_EXIT + self.BUTTON_HEIGHT):
                        button_state['exit'] = 1

                # 鼠标抬起
                if event.type == pygame.MOUSEBUTTONUP:
                    if button_state['start'] == 1:
                        button_state['start'] = 0
                        mainloop = False
                        break
                    if button_state['options'] == 1:
                        button_state['options'] = 0
                        self.options_menu()
                    if button_state['exit'] == 1:
                        button_state['exit'] = 0
                        exit()
                if event.type == pygame.QUIT:
                    exit()

            # 渲染主菜单
            self.screen.fill((255, 255, 255))
            self.draw_main_menu(button_state)
            pygame.display.flip()

    def options_menu(self):
        print('options start')
        options_loop = 1
        while options_loop:
            self.screen.blit(self.bg_options,(0,0))
            pygame.display.update()
            click_on_yes = 0
            for event in pygame.event.get():
                if click_on_yes:
                    print('启用音效')
                if event.type == pygame.MOUSEBUTTONUP:
                    print('mouse up')
                    mx,my = pygame.mouse.get_pos()
                    if mx < 300 and my > 500:
                        print('回到主菜单')
                        options_loop = 0
                        break


    class ButtonState(Enum):
        normal = 0
        pressed = 1
