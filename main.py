import pygame
from mainmenu import *
from gamemenu import *
from game import *

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('三消游戏')
screen.fill((255, 255, 255))
main_menu = MainMenu(screen)
main_menu.run()
game_menu = GameMenu(screen)
game_menu.run()
game = Game(screen,'erzerge','player1')
game.run()

print('ssc')


# # =======================图片教学========================
# #游戏开始静态效果
# # 1. 加载
# image = pygame.image.load('image/pic1.jpg')
# # 2. 渲染图片
# window.blit(image,(0,0))
# # 3. 操作图片
# #1) 获取图片大小
# w,h = image.get_size()
# window.blit(image,(800-w,600-h))
# #2) 旋转缩放
# # scale(对象，目标大小)
# new1 = pygame.transform.scale(image,(100,100))
# # rotozoom(缩放/旋转对象，旋转角度，缩放比例)
# new2 = pygame.transform.rotozoom(image,0,0.5)
# # 4. 刷新 ，第一次刷新用flip，之后用update
# pygame.display.flip()
# # =======================图片教学========================
#
# pygame.draw.rect(screen, (255, 0, 0), (30, 100, 100, 50))
# pygame.draw.rect(screen, (0, 255, 0), (30, 200, 100, 50))
# pygame.display.update()
# # =======================字体教学========================
# # 1. 创建字体
# # Font(字体文件路径，字号)
# font1=pygame.font.Font('font/font.ttf',30)
# # 2. 创建文字对象
# # render(内容，是否平滑(True)，文字颜色，背景颜色)
# text1=font1.render('test message',True,(255,0,0))
# # 3. 渲染
# window.blit(text1,(400,0))
# w ,h = text1.get_size()  #文字对象也可使用get_size()方法,缩放旋转同理
# pygame.display.update()


# =======================字体教学========================
