import pygame
import random
import math
from enum import IntEnum


class Game:
    FEILD_X = 100  # 452
    FEILD_Y = 60  # 368
    CUBE_WIDTH = 44
    CUBE_HEIGHT = 44
    FIELD_DROPING = 1
    FIELD_DROPING_STEP = 1
    FIELD_AFTER_SWAP = 1
    GAME_LOOP = 1
    FPS = 30
    GLOBAL_TIME = 0
    DELTA = 0
    SWAPPING = 0
    SHOW_SWAP = 0
    SWAP_SPEED = 4
    DROP_SPEED = 11

    def __init__(self, screen):
        test = 1
        self.screen = screen
        # 棋盘，8*8规格，最上方行不显示，实际棋盘为7*8。全部初始化为EMPTY类型(0)
        # self.field = [[self.Cube_Type.EMPTY for y in range(8)] for x in range(8)]
        self.field = [[0 for y in range(8)] for x in range(8)]
        self.clock = pygame.time.Clock()
        self.cube_empty = pygame.image.load('image/background_cube.png')
        self.cube_phyatk = pygame.image.load('image/physical_attack.png')
        self.cube_magatk = pygame.image.load('image/magic_attack.png')
        self.cube_hp = pygame.image.load('image/hp_potion.png')
        self.cube_mp = pygame.image.load('image/mp_potion.png')
        self.cube_map = {0: self.cube_empty,
                         1: self.cube_phyatk,
                         2: self.cube_magatk,
                         3: self.cube_hp,
                         4: self.cube_mp}
        self.swap_source = (0, 0)
        self.swap_dest = (0, 0)
        self.drop_list = []
        self.swap_list = []
        self.distance = 0

    def init_field(self):
        while self.FIELD_DROPING:
            self.generate()
            self.gravity()
            self.draw()
        self.after_swap()

    def run(self):
        if pygame.display.get_init():
            print('True')
        self.init_field()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    print('mouse click on %f,%f', mx, my)
                    if (self.FEILD_X <= mx <= self.FEILD_X + 8 * self.CUBE_WIDTH and
                            self.FEILD_Y <= my <= self.FEILD_Y + 8 * self.CUBE_HEIGHT):
                        if self.SWAPPING == 0:
                            self.swap_source = (mx, my)
                            self.SWAPPING = 1
                            print('click another')
                        elif self.SWAPPING == 1:
                            if True:
                                print('swaping')
                                self.swap_dest = (mx, my)
                                self.swap()
                                self.after_swap()
                                self.SWAPPING = 0
                    else:
                        print('cancel swap')
                        self.SWAPPING = 0

                if event.type == pygame.QUIT:
                    exit()

    def swap(self):
        i1 = (self.swap_source[1] - self.FEILD_Y) // self.CUBE_HEIGHT
        j1 = (self.swap_source[0] - self.FEILD_X) // self.CUBE_WIDTH
        i2 = (self.swap_dest[1] - self.FEILD_Y) // self.CUBE_HEIGHT
        j2 = (self.swap_dest[0] - self.FEILD_X) // self.CUBE_WIDTH
        print('%d,%d and %d,%d', i1, j1, i2, j2)
        self.swap_list.append((i1, j1))
        self.swap_list.append((i2, j2))
        self.SHOW_SWAP = 1
        self.all_anime()
        self.field[i1][j1], self.field[i2][j2] = self.field[i2][j2], self.field[i1][j1]

    def after_swap(self):
        self.FIELD_AFTER_SWAP = 1
        while self.FIELD_AFTER_SWAP:
            self.FIELD_DROPING = 1
            while self.FIELD_DROPING:
                self.generate()
                self.gravity()
            self.draw()
            self.match()

    def generate(self):
        for i in range(len(self.field[0])):
            # 也可使用random库choices函数，若棋盘第一行有元素为空，则随机为1~4
            if self.field[0][i] == self.Cube_Type.EMPTY:
                self.field[0][i] = random.randint(1, 4)

    # gravity:遍历棋盘，若元素下方为空，将该元素加入下移列表，调用drop_anime播放下坠动画
    def gravity(self):
        for i in [6, 5, 4, 3, 2, 1, 0]:  # 从倒数第二行开始
            for j in [0, 1, 2, 3, 4, 5, 6, 7]:
                if self.field[i + 1][j] == self.Cube_Type.EMPTY and self.field[i][j] != self.Cube_Type.EMPTY:
                    self.drop_list.append((i, j))
        if len(self.drop_list) == 0:
            self.FIELD_DROPING = 0
        else:
            self.FIELD_DROPING_STEP = 1
            self.all_anime()
            for i, j in self.drop_list:
                self.field[i][j], self.field[i + 1][j] = self.field[i + 1][j], self.field[i][j]
            self.drop_list.clear()

    # drop:将下移列表的中的元素全部下移
    def drop_anime(self):
        start_time = self.GLOBAL_TIME
        self.clock_tick()
        self.distance += self.DROP_SPEED
        # 绘制动画中的方块
        for i, j in self.drop_list:
            cube = self.cube_map[self.field[i][j]]
            self.screen.blit(cube,
                             (self.FEILD_X + j * self.CUBE_WIDTH, self.FEILD_Y + i * self.CUBE_HEIGHT + self.distance))
        if self.distance >= self.CUBE_HEIGHT:
            self.FIELD_DROPING_STEP = 0
            self.distance = 0

    def swap_anime(self, i1, j1, i2, j2):
        self.clock_tick()
        self.distance += self.SWAP_SPEED
        # 绘制动画中的方块
        cube1 = self.cube_map[self.field[i1][j1]]
        cube2 = self.cube_map[self.field[i2][j2]]
        self.screen.blit(cube2, (self.FEILD_X + j2 * self.CUBE_WIDTH + (j1 - j2) * self.distance
                                 , self.FEILD_Y + i2 * self.CUBE_HEIGHT + (i1 - i2) * self.distance))
        self.screen.blit(cube1, (self.FEILD_X + j1 * self.CUBE_WIDTH + (j2 - j1) * self.distance
                                 , self.FEILD_Y + i1 * self.CUBE_HEIGHT + (i2 - i1) * self.distance))
        if self.distance >= self.CUBE_HEIGHT:
            self.SHOW_SWAP = 0
            self.swap_list.clear()
            self.distance = 0

    def match(self):
        match_list = []
        # 1.横向匹配

        for i in [1, 2, 3, 4, 5, 6, 7]:
            row_match = []
            for j in [0, 1, 2, 3, 4, 5, 6, 7]:
                if len(row_match) == 0:
                    row_match.append((i, j))
                else:  # 与匹配列表最后一项进行比较
                    row_match_last_i, row_match_last_j = row_match[-1][0], row_match[-1][1]
                    if self.field[i][j] == self.field[row_match_last_i][row_match_last_j]:
                        row_match.append((i, j))
                    else:  # self.field[i][j]  !=  self.field[row_match_last_i][row_match_last_j]
                        # 若匹配列表中项数大于3，则将这些元素添加到匹配列表大全，然后清空，否则直接清空
                        if len(row_match) >= 3:
                            match_list.extend(row_match)
                            row_match.clear()
                        else:
                            row_match.clear()
                            row_match.append((i, j))
            if len(row_match) >= 3:
                match_list.extend(row_match)

        # 2.纵向匹配
        for j in [0, 1, 2, 3, 4, 5, 6, 7]:
            col_match = []
            for i in [1, 2, 3, 4, 5, 6, 7]:
                if len(col_match) == 0:
                    col_match.append((i, j))
                else:  # 与匹配列表最后一项进行比较
                    col_match_last_i, col_match_last_j = col_match[-1][0], col_match[-1][1]
                    if self.field[i][j] == self.field[col_match_last_i][col_match_last_j]:
                        col_match.append((i, j))
                    else:  # self.field[i][j]  !=  self.field[col_match_last_i][col_match_last_j]
                        # 若匹配列表中项数大于3，则将这些元素添加到匹配列表大全，然后清空，否则清空再添加自己
                        if len(col_match) >= 3:
                            match_list.extend(col_match)
                            col_match.clear()
                        else:
                            col_match.clear()
                            col_match.append((i, j))
            if len(col_match) >= 3:
                match_list.extend(col_match)
        if len(match_list) == 0:
            self.FIELD_AFTER_SWAP = 0
        self.match_logical_anime(match_list)

    def match_logical_anime(self, match_list_all):
        for tuple in match_list_all:
            i, j = tuple[0], tuple[1]
            self.field[i][j] = 0
        self.draw()

    def all_anime(self):
        while self.FIELD_DROPING_STEP:
            self.draw()
        while self.SHOW_SWAP:
            self.draw()

    # draw:画图
    def draw(self):
        self.draw_background()
        for i in [1, 2, 3, 4, 5, 6, 7]:
            for j in [0, 1, 2, 3, 4, 5, 6, 7]:
                if (i, j) not in self.drop_list:
                    if (i, j) not in self.swap_list:
                        cube = self.cube_map[self.field[i][j]]
                        self.screen.blit(cube,
                                         (self.FEILD_X + j * self.CUBE_WIDTH, self.FEILD_Y + i * self.CUBE_HEIGHT))
        if self.FIELD_DROPING_STEP:
            self.drop_anime()
        if self.SHOW_SWAP:
            self.swap_anime(self.swap_list[0][0], self.swap_list[0][1], self.swap_list[1][0], self.swap_list[1][1])
        pygame.display.flip()

    def draw_background(self):
        self.screen.fill((255, 255, 255))

    def clock_tick(self):
        self.clock.tick(self.FPS)
        self.GLOBAL_TIME += self.DELTA / 1000

    class Cube_Type(IntEnum):
        EMPTY = 0
        PHYSICAL_ATTACK = 1
        MAGIC_ATTACK = 2
        HP_POTION = 3
        MP_POTION = 4
