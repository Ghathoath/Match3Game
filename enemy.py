import pygame
import random

# enemy类影响棋盘，经由game类传递伤害
class Enemy:
    RAW_DAMAGE = 0
    DAMAGE_TYPE = 0 # 0:物理攻击  1:魔法攻击
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
        self.stat = self.Stat_Struct()
        self.init_enemy()

    def init_enemy(self):
        self.stat.make_stat_from_file(self.enemy_type)
        print(self.stat.hp)
        print(self.stat.skillset)
        self.skill_now = random.choice(self.stat.skillset)
        self.skill_wait_turn = self.skill_wait_turn_map[self.skill_now]

    def move(self,field):
        self.RAW_DAMAGE = 0
        if self.skill_wait_turn == 0:
            self.skill_index(self.skill_now)
            # 随机选择下一技能
            self.skill_now = random.choice(self.stat.skillset)
            # 下一释放技能回合数设置
            self.skill_wait_turn=self.skill_wait_turn_map[self.skill_now]
        else:
            self.skill_wait_turn-=1

        return self.RAW_DAMAGE,self.DAMAGE_TYPE


    def skill_index(self,index):
        # 普通物理攻击
        if self.skill_now == 1:
            self.physical_attack_1()
        elif self.skill_now == 2:
            self.magical_attack_2()


    def physical_attack_1(self):
        self.RAW_DAMAGE = self.stat.str
        self.DAMAGE_TYPE = 0

    def magical_attack_2(self):
        self.RAW_DAMAGE = self.stat.wis
        self.DAMAGE_TYPE = 1

    class Stat_Struct(object):
        def __init__(self):
            self.name = 'not_init'
            self.str = 1                # 力量
            self.wis = 1                # 智力
            self.hp = 1                 # 血量
            self.armor = 1              # 护甲
            self.magic_resist = 1       # 魔抗
            self.skillset = []           # 技能组

        # 调试用函数
        def make_stat(self, name, str, wis, hp, armor, magic_resist, skillset):
            self.name = name
            self.str = str                      # 力量
            self.wis = wis                      # 智力
            self.hp = hp                        # 血量
            self.armor = armor                  # 护甲
            self.magic_resist = magic_resist    # 魔抗
            self.skillset = skillset            # 技能组


        def make_stat_from_file(self, filename):
            file = open('enemystat/' + filename)
            self.name = file.readline()
            self.str = int(file.readline())
            self.wis = int(file.readline())
            self.hp = int(file.readline())
            self.armor = int(file.readline())
            self.magic_resist = int(file.readline())
            skillsetstr = file.readline()
            skillsetstr.strip()
            skills = skillsetstr.split(',')
            for skill in skills:
                self.skillset.append(int(skill))
            file.close()

