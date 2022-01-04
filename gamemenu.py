import pygame
from enum import Enum
from game import *
from player import *
from builtins import str


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
        self.bg_shop = pygame.image.load('image/bg_shop.jpg')
        self.bg_skill = pygame.image.load('image/bg_skill.jpg')
        self.player = Player('player1')

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

    def draw_chapter_menu(self, level):
        back = pygame.image.load('image/chapter_back.png')
        level1 = pygame.image.load('image/level1.png')
        level2 = pygame.image.load('image/level2.png')
        self.screen.blit(back, (0, 0))
        self.screen.blit(level1, (100, 100))
        self.screen.blit(level2, (100, 300))
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
                        self.chapter()
                    if button_state['skill'] == 1:
                        button_state['skill'] = 0
                        self.skill_menu()
                    if button_state['shop'] == 1:
                        button_state['shop'] = 0
                        self.shop_menu()
                if event.type == pygame.QUIT:
                    exit()

            # 渲染主菜单
            self.screen.fill((255, 255, 255))
            self.screen.blit(stand, (380, 0))
            self.draw_game_menu(button_state)
            pygame.display.update()

    def chapter(self):
        button_state = 0
        # 初始化
        self.screen.fill((255, 255, 255))
        self.draw_chapter_menu(button_state)
        pygame.display.update()
        # 选关主循环
        chapter_loop = 1
        while chapter_loop:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    if 0 <= mx <= 200 and 0 <= my <= 80:
                        return
                    if 100 <= mx <= 700 and 100 <= my <= 200:
                        button_state = 1
                    if 100 <= mx <= 700 and 300 <= my <= 400:
                        button_state = 2
                if event.type == pygame.QUIT:
                    exit()
                if button_state == 1:
                    game = Game(self.screen, 'erzerge', 'player1')
                    game.run()
                    button_state = 0
                    chapter_loop = 0
                    break
                if button_state == 2:
                    game = Game(self.screen, 'supana', 'player1')
                    game.run()
                    button_state = 0
                    chapter_loop = 0
                    break
            self.screen.fill((255, 255, 255))
            self.draw_chapter_menu(button_state)
            pygame.display.update()

    def shop_menu(self):
        print('shop start')
        shop_loop = 1
        while shop_loop:
            self.screen.blit(self.bg_shop,(0,0))
            pygame.display.update()
            click_on_item = 0
            for event in pygame.event.get():
                if click_on_item:
                    print('购买物品')
                if event.type == pygame.MOUSEBUTTONUP:
                    print('mouse up')
                    mx,my = pygame.mouse.get_pos()
                    if mx < 250 and my > 400:
                        print('回到游戏菜单')
                        shop_loop = 0
                        break

    def skill_menu(self):
        print('skill start')
        skill_loop = 1
        while skill_loop:
            self.screen.blit(self.bg_skill,(0,0))
            self.print_player_stat()

            pygame.display.update()
            click_on_item = 0
            for event in pygame.event.get():
                if click_on_item:
                    print('切换技能')
                if event.type == pygame.MOUSEBUTTONUP:
                    print('mouse up')
                    mx,my = pygame.mouse.get_pos()
                    if mx < 250 and my > 400:
                        print('回到游戏菜单')
                        skill_loop = 0
                        break

    def print_player_stat(self):
        # 1. 创建字体
        # Font(字体文件路径，字号)
        font1=pygame.font.Font('font/font.ttf',20)
        # 2. 创建文字对象
        # render(内容，是否平滑(True)，文字颜色，背景颜色)
        maxhp =   font1.render('MAX HP  ' + str(self.player.stat.hp),True,(0,0,0))
        maxmp =   font1.render('MAX MP  '+ str(self.player.stat.mp),True,(0,0,0))
        strength= font1.render('STR     '+ str(self.player.stat.str),True,(0,0,0))
        wis =     font1.render('WIS     '+ str(self.player.stat.wis),True,(0,0,0))
        armor =   font1.render('ARMOR   '+ str(self.player.stat.armor),True,(0,0,0))
        mig_ris = font1.render('MAG RES '+ str(self.player.stat.magic_resist),True,(0,0,0))
        exp =     font1.render('EXP     '+ str(self.player.stat.exp),True,(0,0,0))
        # 3. 渲染
        self.screen.blit(maxhp,(50,50))
        self.screen.blit(maxmp,(50,80))
        self.screen.blit(strength,(50,110))
        self.screen.blit(wis,(50,140))
        self.screen.blit(armor,(50,170))
        self.screen.blit(mig_ris,(50,200))
        self.screen.blit(exp,(50,230))
        self.screen.blit(self.player.skill1,(358,96))
        self.screen.blit(self.player.skill2,(358+90,96))
        self.screen.blit(self.player.skill3,(358+180,96))
        self.screen.blit(self.player.skill_empty,(358+270,96))
        pygame.display.update()

    class ButtonState(Enum):
        normal = 0
        pressed = 1
