import pygame

# 游戏的初始化
pygame.init()

# 创建游戏的窗口 480 * 700
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0, 0))

# 绘制英雄的飞机(初始位置)
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (150, 300))

# update更新屏幕显示
pygame.display.update()

# 创建时钟对象 (可以控制游戏循环频率)
clock = pygame.time.Clock()

# 1. rect矩形类记录飞机的位置
hero_rect = pygame.Rect(150, 300, 102, 126)

# 游戏循环 -> 意味着游戏的正式开始！
while True:
    # 通过时钟对象指定循环频率
    clock.tick(60)  # 每秒循环60次

    # 2. 修改飞机的位置
    hero_rect.y -= 1  # 向上移动

    # 3. 调用blit方法绘制图像
    screen.blit(bg, (0, 0))  # 元组参数表示绘制位置,也可以通过Rect矩形类来表示位置.
    screen.blit(hero, hero_rect)  # 每次循环都重新绘制背景,是为了用背景遮盖之前绘制的内容

    # 4. 调用update方法更新显示
    pygame.display.update()

