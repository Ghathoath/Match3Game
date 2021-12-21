import pygame
import random


class Player:
    ROW_DAMAGE = 0
    DAMAGE_TYPE = 0  # 0：物理   1：魔法
    MAX_MP = 0
    MAX_HP = 0

    def __init__(self, player_type):
        self.player_type = player_type
        self.profile_img = pygame.image.load('image/profile.png')
        self.skill1 = pygame.image.load('image/skill1.png')
        self.skill2 = pygame.image.load('image/skill2.png')
        self.skill3 = pygame.image.load('image/skill3.png')
        self.skill4 = pygame.image.load('image/skill4.png')
        self.skill_empty = pygame.image.load('image/skill_empty.png')
        self.skill_map = {0: self.skill_empty,
                          1: self.skill1,
                          2: self.skill2,
                          3: self.skill3,
                          4: self.skill4}
        self.stat = self.StatPlayer()
        self.read_player_stat()
        self.blocks_require = {0: 0,
                               1: 1,
                               2: 1,
                               3: 1,
                               4: 1}
        self.mp_require = {0: 0,
                           1: 10,
                           2: 10,
                           3: 10,
                           4: 10}

    def read_player_stat(self):
        # 从文件读入数值
        file = open('playerdata/' + self.player_type)
        self.stat.name = file.readline()
        self.stat.str = int(file.readline())
        self.stat.wis = int(file.readline())
        self.stat.hp = int(file.readline())
        self.stat.mp = int(file.readline())
        self.stat.armor = int(file.readline())
        self.stat.magic_resist = int(file.readline())
        # 读入技能组
        skillset_line = file.readline()
        skillset_line.strip()
        skills = skillset_line.split(',')
        for skill in skills:
            self.stat.skillset.append(int(skill))
        while len(self.stat.skillset) < 4:
            self.stat.skillset.append(0)
        # 读入习得技能列表
        learned_skill_line = file.readline()
        learned_skill_line.strip()
        learned_skills = learned_skill_line.split(',')
        for skill in learned_skills:
            self.stat.learned_skill.append(int(skill))
        self.MAX_HP = self.stat.hp
        self.MAX_MP = self.stat.mp
        file.close()

    def move(self, field, index):
        self.RAW_DAMAGE = 0
        self.skill_index(field, index)
        return self.RAW_DAMAGE, self.DAMAGE_TYPE

    def get_damage(self, damage):
        if damage[0] == 0:
            pass
        elif damage[0] <= self.stat.armor:
            self.stat.hp -= 1
        else:
            self.stat.hp -= damage[0] - self.stat.armor
        if damage[1] == 0:
            pass
        elif damage[1] <= self.stat.magic_resist:
            self.stat.hp -= 1
        else:
            self.stat.hp -= damage[1] - self.stat.magic_resist

    def effect(self, level, cube_type):
        if cube_type == 1:
            return level * self.stat.str, 0
        elif cube_type == 2:
            return level * self.stat.wis, 1
        elif cube_type == 3:
            if self.stat.hp + level * 20 > self.MAX_HP:
                self.stat.hp = self.MAX_HP
            else:
                self.stat.hp += level * 20
            return 0, 0
        elif cube_type == 4:
            if self.stat.mp + level * 20 > self.MAX_MP:
                self.stat.mp = self.MAX_MP
            else:
                self.stat.mp += level * 20
            return 0, 0
        else:
            return 0, 0

    def skill_index(self, field, index):
        if self.blocks_require[self.stat.skillset[index]]:
            return self.blocks_require[self.stat.skillset[index]]
        else:
            self.skill_without_block(field, index)

    def eliminate_blocks(self, field, index, blocks):
        self.stat.mp -= self.mp_require[self.stat.skillset[index]]
        if self.stat.skillset[index] == 1:
            field[blocks[0][0]][blocks[0][1]] = 0

    def skill_without_block(self, field, index):
        pass

    class StatPlayer(object):
        def __init__(self):
            self.name = 'player_not_init'
            self.str = 1  # 力量
            self.wis = 1  # 智力
            self.hp = 1  # 血量
            self.mp = 1
            self.armor = 1  # 护甲
            self.magic_resist = 1  # 魔抗
            self.skillset = []  # 技能组
            self.learned_skill = []  # 习得技能
