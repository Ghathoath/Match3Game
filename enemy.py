import pygame
import random

# enemy类影响棋盘，经由game类传递伤害
class Enemy:
    RAW_DAMAGE = (0,0)  # 0:物理攻击  1:魔法攻击

    def __init__(self,enemy_type):
        # 当前技能释放咏唱时间（等待回合数）
        self.skill_wait_turn = 0
        # 当前技能，由1~max(int)标识
        self.skill_now = 0
        # 敌人种类，字符串类型
        self.enemy_type = enemy_type
        # 技能对应咏唱时间
        self.skill_wait_turn_map = {1:2,2:2,3:2,4:2,5:2}
        # 存储敌人数值的结构体
        self.stat = self.StatEnemy()
        self.read_enemy_stat()
        self.enemy_img = pygame.image.load('image/'+enemy_type+'.png')

    def read_enemy_stat(self):
        # 从文件读入数值
        file = open('enemydata/' + self.enemy_type)
        self.stat.name = file.readline()
        self.stat.str = int(file.readline())
        self.stat.wis = int(file.readline())
        self.stat.hp = int(file.readline())
        self.stat.max_hp = self.stat.hp
        self.stat.armor = int(file.readline())
        self.stat.magic_resist = int(file.readline())
        skillsetstr = file.readline()
        skillsetstr.strip()
        skills = skillsetstr.split(',')
        for skill in skills:
            self.stat.skillset.append(int(skill))
        file.close()
        # 选择第一个技能
        self.skill_now = random.choice(self.stat.skillset)
        self.skill_wait_turn = self.skill_wait_turn_map[self.skill_now]

    def move(self,field): # 敌人行动
        self.RAW_DAMAGE = [0,0]
        if self.skill_wait_turn == 0:
            self.skill_index(field)
            # 随机选择下一技能
            self.skill_now = random.choice(self.stat.skillset)
            # 下一释放技能回合数设置
            self.skill_wait_turn=self.skill_wait_turn_map[self.skill_now]
        else:
            self.skill_wait_turn-=1

        return self.RAW_DAMAGE

    def get_damage(self,damage):
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

    def skill_index(self,field):
        # 普通物理攻击
        if self.skill_now == 1:
            self.physical_attack_1()
        elif self.skill_now == 2:
            self.magical_attack_2()

    def physical_attack_1(self):
        self.RAW_DAMAGE[0] = self.stat.str

    def magical_attack_2(self):
        self.RAW_DAMAGE[1] = self.stat.wis

    class StatEnemy(object):
        def __init__(self):
            self.name = 'not_init'
            self.str = 1                # 力量
            self.wis = 1                # 智力
            self.hp = 1                 # 血量
            self.armor = 1              # 护甲
            self.magic_resist = 1       # 魔抗
            self.skillset = []           # 技能组
            self.max_hp = 0


