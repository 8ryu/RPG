"""
Date             : 2025/01/24
Title            : Role-playing game
File name        : main.py
Author nickname  : 8ryu
"""

import pygame
import numpy
import random
import secrets
import string
import sys
import time
import webbrowser
import pickle
from pygame.locals import *

#########
# color
# 色
#########

AQUA = (0, 255, 255)
AZURE = (240, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 149, 217)
BURLYWOOD = (222, 185, 135)
CYAN = (0, 255, 255)
GRAY = (128, 128, 128)
GREEN = (0, 128, 0)
LIGHTCYAN = (224, 255, 255)
LIME = (0, 255, 0)
MAGENTA = (255, 0, 255)
MAROON = (128, 0, 0)
NAVY = (0, 0, 128)
RED = (255,0,0)
OLIVE = (128, 128, 0)
ORANGE = (255,165,0)
PINK = (255,190,200)
PLUM = (220, 160, 220)
PURPLE = (168, 88, 168)
ROYALBLUE = (65, 105, 225)
SILVER = (192, 192, 192)
TEAL = (0, 128, 128)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

#################
# color scheme
# 配色
#################

# Title screen
# タイトル画面
COLOR_SCHEME1 = [(72,61,139), (0,0,128),(100,149,237),(70,130,180),(65,105,225),(25,25,112),(0,0,255),(0,0,205),(0,0,139),(0,0,128)]

# 2D exploration end text
# ２次元探検の終了テキスト
COLOR_SCHEME2 = [(255,250,255),(255,250,240),(255,250,210),(255,250,220),(255,240,220),(255,235,210),(255,240,240),(255,240,255),(255,230,205),(255,230,200)]

# Internet
# インターネット
COLOR_SCHEME3 = [(255,255,240),(255,255,220),(255,250,250),(255,250,240),(255,250,200),(255,250,220),(255,240,230),(255,230,180),(255,230,225),(255,190,200)]

# Fortune telling hall
# 占いの館
COLOR_SCHEME4 = [(255,0,255),(255,20,150),(255,100,70),(240,130,240),(233,150,120),(255,160,120),(255,105,180),(255,20,150),(255,100,70),(255,70,0)]

# Password generator
# パスワード生成ツール
COLOR_SCHEME5 = [(0,0,255),(0,0,205),(0,0,140),(0,0,130),(0,130,130),(0,140,140),(25,25,110),(65,105,225),(105,90,205),(123,105,240)]

# rock, paper, scissors game
# じゃんけんゲーム
COLOR_SCHEME6 = [(245,170,100),(240,130,130),(230,150,120),(222,185,140),(220,160,220),(222,185,140),(220,165,30),(210,180,140),(190,180,105),(185,135,10)]

# random color
# ランダムな色
COLOR_SCHEME7 = [(255,220,0),(255,140,0),(255,160,125),(255,100,70),(255,222,175),(255,170,20),(245,165,100),(240,130,130),(210,105,30),(205,140,60)]

# combat command
# 戦闘コマンド
COLOR_SCHEME8 = [(240,250,255),(240,255,240),(240,255,255),(225,255,255),(245,245,220),(230,230,250),(180,225,230),(175,240,240),(175,215,230),(135,205,235)]

###########################
# Generate random colors.
# ランダムな色を生成する
###########################

# Random color in RGB format
# RGB形式のランダムな色

# random color definition
# ランダムな色の定義
RANDOM_COLOR = []

for i in range(1024):
    
    # Adds an element to the end of a list (array).
    # リスト（配列）の末尾に要素を追加する
    RANDOM_COLOR.append(i)
    
    RANDOM_COLOR[i] = list(numpy.random.choice(range(256), size=3))

###################
# Load the image.
# 画像の読み込み
###################

# Title
# タイトル
imgTitle = pygame.image.load("image/title_screen.png")

# Tree
# 木
imgTree = pygame.image.load("image/tree.png")

# Player
# プレイヤー
imgPlayer = [
    pygame.image.load("image/player0.png"),
    pygame.image.load("image/player1.png"),
    pygame.image.load("image/player2.png"),
    pygame.image.load("image/player3.png"),
    pygame.image.load("image/player4.png"),
    pygame.image.load("image/player5.png"),
    pygame.image.load("image/player6.png"),
    pygame.image.load("image/player7.png"),
    pygame.image.load("image/player8.png")
    ]

# Items placed/installed on the ground
# 地面に配置・設置するもの
imgGround = [
    pygame.image.load("image/grass.png"),
    pygame.image.load("image/up_stairs.png"),
    pygame.image.load("image/descending_stairs.png"),
    pygame.image.load("image/internet.png"),
    pygame.image.load("image/fortune.png"),
    pygame.image.load("image/password.png"),
    pygame.image.load("image/janken.png"),
    pygame.image.load("image/random_color.png"),
    pygame.image.load("image/memo.png"),
    pygame.image.load("image/bmi.png"),
    pygame.image.load("image/recovery_agents.png"),
    pygame.image.load("image/drink.png"),
    pygame.image.load("image/poison.png"),
    ]

# Robot
# ロボット
imgRobot = [
    pygame.image.load("image/robot0.png"),
    pygame.image.load("image/robot1.png"),
    pygame.image.load("image/robot2.png"),
    pygame.image.load("image/robot3.png")
    ]

# Adjust the size of the robot image.
# ロボット画像のサイズを調整する
imgRobot[0] = pygame.transform.scale(imgRobot[0], (50, 50))
imgRobot[1] = pygame.transform.scale(imgRobot[1], (200, 200))
imgRobot[2] = pygame.transform.scale(imgRobot[2], (200, 200))
imgRobot[3] = pygame.transform.scale(imgRobot[3], (200, 200))

# Robot comment image
# ロボットのコメント画像
imgRobotComment = [
    pygame.image.load("image/comment0.png"),
    pygame.image.load("image/comment1.png"),
    pygame.image.load("image/comment2.png")
    ]

# Adjust the size of the robot's comment image.
# ロボットのコメント画像のサイズを調整する
imgRobotComment[0] = pygame.transform.scale(imgRobotComment[0], (500, 300))
imgRobotComment[1] = pygame.transform.scale(imgRobotComment[1], (400, 200))
imgRobotComment[2] = pygame.transform.scale(imgRobotComment[2], (700, 200))

# Rock, paper, scissors
# じゃんけん（グー、チョキ、パー）
imgHand = [
    pygame.image.load("image/rock.png"),
    pygame.image.load("image/paper.png"),
    pygame.image.load("image/scissors.png")
    ]

# Adjust the size of the rock, paper, scissors image.
# じゃんけん画像のサイズを調整をする
imgHand[0] = pygame.transform.scale(imgHand[0], (100, 100))
imgHand[1] = pygame.transform.scale(imgHand[1], (100, 100))
imgHand[2] = pygame.transform.scale(imgHand[2], (100, 100))

# Image of where the enemy is on the ground
# 地面の上に敵がいる場所の画像
imgGroundEnemy = pygame.image.load("image/question.png")

# Background image to fight the enemy
# 敵と戦う背景画像
imgBackgroundFightEnemy = pygame.image.load("image/background_fight_enemy.png")
imgBackgroundFightEnemy = pygame.transform.scale(imgBackgroundFightEnemy, (800, 600))

# enemy image
# 敵の画像
imgEnemy = pygame.image.load("image/enemy0.png")

# Attack effect image
# 攻撃のエフェクト画像
imgEffect = pygame.image.load("image/effect.png")

#########
# maze
# 迷路
#########

# maze width
# 迷路の幅
MAZE_W = 15

# maze height
# 迷路の高さ
MAZE_H = 11

# maze definition
# 迷路の定義
maze = []
for y in range(MAZE_H):
    maze.append([0]*MAZE_W)

# sentinel
# 番兵
XP = [ 0, 1, 0,-1]
YP = [-1, 0, 1, 0]

#############
# hierarchy
# 階層
#############

# width of a hierarchy
# ある階層の幅
HIERARCHY_W = MAZE_W*3

# height of a hhierarchy
# ある階層の高さ
HIERARCHY_H = MAZE_H*3

# Definition of a hierarchy
# ある階層の定義
hierarchy = []
for y in range(HIERARCHY_H):
    hierarchy.append([0]*HIERARCHY_W)

# Current number of floors
# 現在の階層数
floor = 0

# Maximum number of floors reached
# 到達した階層数の最大値
floor_max = 1

#########################
# Frame rate management
# フレームレートの管理
#########################

# Overall screen management
# 画面全体の管理
speed = 1

# Managing screen transitions
# 画面の切り替えの管理
change_screen = 0

# Managing screen progress 
# 画面の進行の管理
timer = 0

#############################
# Player position management
# プレイヤーの位置管理
#############################

# x coordinate
# x座標
player_x = 0

# y coordinate
# y座標
player_y = 0

# player direction
# プレイヤーの向き
player_direction = 0

# Player animation patterns
# プレイヤーのアニメーションのパターン
player_animation = 0

##################
# Item
# アイテム
##################

# 回復薬
recovery_agents = 0

# 飲み物
drink = 0

# 毒薬
poison = 0

###################
# password length
# パスワードの長さ
###################

password_length = 0

#################################
# Player's rock, paper, scissors
# プレイヤーのじゃんけん
#################################

player_hand = 0

#################################
# Robot's rock, paper, scissors
# ロボットのじゃんけん
#################################

hand = ["rock", "paper", "scissors"]

########################
# Manage player lives
# プレイヤーのライフの管理
########################

# Player's current life
# プレイヤーの現在のライフ
player_life = 0

# Maximum player life
# プレイヤーのライフの最大値
player_lifemax = 0

########################
# Player's attack power
# プレイヤーの攻撃力
########################

player_attack_power = 0

####################
# enemy information
# 敵の情報
####################

# Default enemy name
# 敵の名前の初期値
enemy_name = ""

# list of enemy names
# 敵の名前のリスト
ENEMY_NAME = ["Gold God", "Gaikou", "Funku"] 

######################
# Managing enemy life
# 敵のライフの管理
######################

# enemy's current life
# 敵の現在のライフ
enemy_life = 0

# Maximum enemy life
# 敵のライフの最大値
enemy_lifemax = 0

#######################
# Enemy's attack power
# 敵の攻撃力
#######################

enemy_attack_power = 0

############################
# enemy position management
# 敵の位置管理
############################

# x coordinate
# x座標
enemy_x = 440-imgEnemy.get_width()/2

# y coordinate
# y座標
enemy_y = 560-imgEnemy.get_height()

# Move the enemy to the front.
# 敵を前方に移動する
enemy_front = 0

# Flashes when attacking an enemy.
# 敵を攻撃した時に、点滅する
enemy_flash = 0

# screen shaking
# 画面の揺れ
screen_shaking = 0

##################
# battle command
# 戦闘コマンド
##################

battle_command = 0

# List of combat commands
# 戦闘コマンドのリスト
BATTLE_COMMAND = ["[a]ttack","[r]ecovery", "[e]scape"]

##################
# battle message
# 戦闘メッセージ
##################

# List of battle messages
# 戦闘メッセージを入れるリスト
battle_message = [""]*2

#######################
# Data to save/load
# セーブ・ロードするデータ
#######################

data = {
    'player_lifemax':player_lifemax,
    'player_life':player_life,
    'player_attack_power':player_attack_power,
    'recovery_agents':recovery_agents
    }

##########################
# Displaying shaded text
# 影付き文字の表示
##########################

def draw_text(bg, txt, x, y, fnt, col):
    
    shadow = fnt.render(txt, True, BLACK)
    bg.blit(shadow, [x+1, y+2])
    
    shadow = fnt.render(txt, True, col)
    bg.blit(shadow, [x, y])

#######################################
# Automatic generation of hierarchies
# 階層の自動生成
#######################################

def make_hierarchy():

    # global variables
    # グローバル変数    
    global XP, YP

    ################################################
    # Generating a maze (pulling a pole down method)
    # 迷路の生成（棒倒し法）
    ################################################    

    # Empty the inside.
    # 中を何もない状態にする
    for y in range(1, MAZE_H-1):
        for x in range(1, MAZE_W-1):
            maze[y][x] = 0
        
    # Place and install objects on the x axis (tip and end).
    # x軸（先端と末端）にモノを配置・設置する
    for x in range(MAZE_W):
        maze[0][x] = 1
        maze[MAZE_H-1][x] = 1

    # Place and install objects on the y axis (tip and end).
    # y軸（先端と末端）にモノを設置・配置する
    for y in range(1, MAZE_H-1):
        maze[y][0] = 1
        maze[y][MAZE_W-1] = 1
            
    # Arrange and install objects every other square.
    # 1マスおきにモノを配置・設置する
    for y in range(2, MAZE_H-2, 2):
        for x in range(2, MAZE_W-2, 2):
            maze[y][x] = 1

    # Randomly place the installed objects up, down, left and right.  
    # 配置・設置されたモノを上下左右にランダムに設置する
    for y in range(2, MAZE_H-2, 2):
        for x in range(2, MAZE_W-2, 2):
         d = random.randint(0, 3)
         
         # Avoid building a object to the left from the second row.
         # 二列目からは左にモノを作らないようにする
         if x > 2:
             d = random.randint(0, 2)
         maze[y+YP[d]][x+XP[d]] = 1
         
    ####################################
    # Generate a hierarchy from a maze.
    # 迷路から階層を生成する
    ####################################
    
    # Make the whole area a forest.
    # 全体を森林にする
    for y in range(HIERARCHY_H):
        for x in range(HIERARCHY_W):
            hierarchy[y][x] = 100

    # Arrangement of mini areas and passages
    # ミニエリアと通路の配置
    for y in range(1, MAZE_H-1):
        for x in range(1, MAZE_W-1):
            dx = x*3+1
            dy = y*3+1
            if maze[y][x] == 0:
                
                # make a mini area
                # ミニエリアを作る
                if random.randint(0, 99) < 30:
                    for ry in range(-1, 2):
                        for rx in range(-1, 2):
                            hierarchy[dy+ry][dx+rx] = 0
                            
                # make a passage
                # 通路を作る
                else:
                    hierarchy[dy][dx] = 0
                    if maze[y-1][x] == 0:
                        hierarchy[dy-1][dx] = 0
                    if maze[y+1][x] == 0:
                        hierarchy[dy+1][dx] = 0
                    if maze[y][x-1] == 0:
                        hierarchy[dy][dx-1] = 0
                    if maze[y][x+1] == 0:
                        hierarchy[dy][dx+1] = 0
                    
######################
# Draw the hierarchy.
# 階層を描画する
######################

def draw_hierarchy(bg, fnt):
    
    # If you are on the 0th floor (ground), set it to the sea.
    # 0階（地上）の場合は海にする
    if floor == 0:
        bg.fill(BLUE)
        
    # If it is underground, set it to silver color.
    # 地下の場合はシルバー色にする
    if floor < 0:
        bg.fill(SILVER)
        
    # If it is on the first floor or above, set it to blue-green.
    # 1階以上の場合は青緑色にする
    if floor > 0:
        bg.fill(TEAL)
        
    for y in range(-5,100):
        for x in range(-5,100):
            X = (x+5)*16
            Y = (y+5)*16
            dx = player_x + x
            dy = player_y + y
            if 0 <= dx and dx < HIERARCHY_W and 0 <= dy and dy < HIERARCHY_H:
                
                # imgFloor images
                # imgFloorの画像
                if hierarchy[dy][dx] <= 13:
                    bg.blit(imgGround[hierarchy[dy][dx]], [X, Y])

                # imgGroundEnemy images
                # imgGroundEnemyの画像
                if hierarchy[dy][dx] == 50:
                    bg.blit(imgGroundEnemy, [X, Y])
                
                # forest display
                # 森林を表示する
                if hierarchy[dy][dx] == 100:
                    bg.blit(imgTree, [X, Y])
                    
            # Player display
            # プレイヤーの表示
            if x == 0 and y == 0:
                bg.blit(imgPlayer[player_animation], [X, Y])
                
    # Player strength information
    # プレイヤーの強さの情報
    player_strength_info(bg, fnt)


##############################
# Place objects on the ground.
# 地面にモノを配置する
##############################

def put_object():

    # global variables
    # グローバル変数    
    global player_x, player_y, player_direction, player_animation
    
    # Arrangement of ascending stairs
    # 上り階段の配置
    while True:
        x1 = random.randint(3, HIERARCHY_W-4)
        y1 = random.randint(3, HIERARCHY_H-4)
        if(hierarchy[y1][x1] == 0):
            
            # Make the area around the stairs the ground.
            # 階段の周囲を地面にする
            for ry1 in range(-1, 2):
                for rx1 in range(-1, 2):
                    hierarchy[y1+ry1][x1+rx1] = 0
            hierarchy[y1][x1] = 1
            break
        else:
            continue

    # Placement of descending stairs
    # 下り階段の配置
    while True:
        x2 = random.randint(3, HIERARCHY_W-4)
        y2 = random.randint(3, HIERARCHY_H-4)
        if(hierarchy[y2][x2] == 0):
            
            # Make the area around the stairs the ground.
            # 階段の周囲を地面にする
            for ry2 in range(-1, 2):
                for rx2 in range(-1, 2):
                    hierarchy[y2+ry2][x2+rx2] = 0
            hierarchy[y2][x2] = 2
            break
        else:
            continue

    # Internet placement
    # インターネットの配置
    while True:
        x3 = random.randint(3, HIERARCHY_W-4)
        y3 = random.randint(3, HIERARCHY_H-4)
        if(hierarchy[y3][x3] == 0):
            
            # Make the area around the Internet a ground.
            # インターネットの周囲を地面にする
            for ry3 in range(-1, 2):
                for rx3 in range(-1, 2):
                    hierarchy[y3+ry3][x3+rx3] = 0
            hierarchy[y3][x3] = 3
            break

    # Placement of fortune-telling hall
    # 占いの館の配置
    while True:
        x4 = random.randint(3, HIERARCHY_W-4)
        y4 = random.randint(3, HIERARCHY_H-4)
        if(hierarchy[y4][x4] == 0):
            
            # Make the area around the fortune-telling hall a ground.
            # 占いの館の周囲を地面にする
            for ry4 in range(-1, 2):
                for rx4 in range(-1, 2):
                    hierarchy[y4+ry4][x4+rx4] = 0
            hierarchy[y4][x4] = 4
            break

    # Placement of password generation tool
    # パスワード生成ツールの配置
    while True:
        x5 = random.randint(3, HIERARCHY_W-4)
        y5 = random.randint(3, HIERARCHY_H-4)
        if(hierarchy[y5][x5] == 0):
            
            # Create a ground around the password generator.
            # パスワード生成ツールの周囲を地面にする
            for ry5 in range(-1, 2):
                for rx5 in range(-1, 2):
                    hierarchy[y5+ry5][x5+rx5] = 0
            hierarchy[y5][x5] = 5
            break

    # Placement of the rock, paper, scissors game
    # じゃんけんゲームの配置
    while True:
        x6 = random.randint(3, HIERARCHY_W-4)
        y6 = random.randint(3, HIERARCHY_H-4)
        if(hierarchy[y6][x6] == 0):
            
            # Place the area around the rock, paper, scissors game on the ground.
            # じゃんけんゲームの周囲を地面にする
            for ry6 in range(-1, 2):
                for rx6 in range(-1, 2):
                    hierarchy[y6+ry6][x6+rx6] = 0
            hierarchy[y6][x6] = 6
            break

    # Placement of the random color
    # ランダムな色の配置
    while True:
        x7 = random.randint(3, HIERARCHY_W-4)
        y7 = random.randint(3, HIERARCHY_H-4)
        if(hierarchy[y7][x7] == 0):
            
            # Place the area around the random color on the ground.
            # ランダムな色の周囲を地面にする
            for ry7 in range(-1, 2):
                for rx7 in range(-1, 2):
                    hierarchy[y7+ry7][x7+rx7] = 0
            hierarchy[y7][x7] = 7
            break

    # Placement of the memo
    # メモの配置
    while True:
        x8 = random.randint(3, HIERARCHY_W-4)
        y8 = random.randint(3, HIERARCHY_H-4)
        if(hierarchy[y8][x8] == 0):
            
            # Place the area around the random color on the ground.
            # メモの周囲を地面にする
            for ry8 in range(-1, 2):
                for rx8 in range(-1, 2):
                    hierarchy[y8+ry8][x8+rx8] = 0
            hierarchy[y8][x8] = 8
            break

    # Placement of the BMI
    # BMIの配置
    while True:
        x9 = random.randint(3, HIERARCHY_W-4)
        y9 = random.randint(3, HIERARCHY_H-4)
        if(hierarchy[y9][x9] == 0):
            
            # Place the area around the random color on the ground.
            # BMIの周囲を地面にする
            for ry9 in range(-1, 2):
                for rx9 in range(-1, 2):
                    hierarchy[y9+ry9][x9+rx9] = 0
            hierarchy[y9][x9] = 9
            break

    # Placement of the enemy
    # 敵の配置
    for i in range(10):
        x50 = random.randint(3, HIERARCHY_W-4)
        y50 = random.randint(3, HIERARCHY_H-4)
        if(hierarchy[y50][x50] == 0):
            hierarchy[y50][x50] = random.choice([50,50,50])
            break

    # arrangement of objects
    # モノの配置
    for i in range(10):
        object_x = random.randint(3, HIERARCHY_W-4)
        object_y = random.randint(3, HIERARCHY_H-4)
        if(hierarchy[object_y][object_x] == 0):
            hierarchy[object_y][object_x] = random.choice([10,11,12])


    # Player's initial position  
    # プレイヤーの初期位置    
    while True:
        player_x = random.randint(3, HIERARCHY_W-4)
        player_y = random.randint(3, HIERARCHY_H-4)
        if(hierarchy[player_y][player_x] == 0):
            break
    player_direction = 1
    player_animation = 2

###################
# player movement
# プレイヤーの移動
###################

def move_player(key):

    # global variables
    # グローバル変数
    global change_screen, timer, player_x, player_y, player_direction, player_animation, player_life
    global recovery_agents, drink, poison

    
    # If you land on the ascending stairs
    # 上り階段に着地した場合
    if hierarchy[player_y][player_x] == 1:
        change_screen = 5
        timer = 0
        return

    # If you land on the descending stairs
    # 下り階段に着地した場合
    if hierarchy[player_y][player_x] == 2:
        change_screen = 6
        timer = 0
        return
    
    # Entering the world of the Internet
    # インターネットの世界に入る場合
    if (key[K_UP] == 1 and hierarchy[player_y-1][player_x] == 3) or\
       (key[K_DOWN] == 1 and hierarchy[player_y+1][player_x] == 3) or\
       (key[K_LEFT] == 1 and hierarchy[player_y][player_x-1] == 3) or\
       (key[K_RIGHT] == 1 and hierarchy[player_y][player_x+1] == 3):
        change_screen = 7
        timer = 0
        return    

    # If you enter a fortune-telling hall
    # 占いの館に入店した場合
    if (key[K_UP] == 1 and hierarchy[player_y-1][player_x] == 4) or\
       (key[K_DOWN] == 1 and hierarchy[player_y+1][player_x] == 4) or\
       (key[K_LEFT] == 1 and hierarchy[player_y][player_x-1] == 4) or\
       (key[K_RIGHT] == 1 and hierarchy[player_y][player_x+1] == 4):
        change_screen = 8
        timer = 0
        return    

    # When entering the password generation tool
    # パスワード生成ツールに入る場合
    if (key[K_UP] == 1 and hierarchy[player_y-1][player_x] == 5) or\
       (key[K_DOWN] == 1 and hierarchy[player_y+1][player_x] == 5) or\
       (key[K_LEFT] == 1 and hierarchy[player_y][player_x-1] == 5) or\
       (key[K_RIGHT] == 1 and hierarchy[player_y][player_x+1] == 5):
        change_screen = 10
        timer = 0
        return    

    # When entering the rock-paper-scissors game
    # じゃんけんゲームに入る場合
    if (key[K_UP] == 1 and hierarchy[player_y-1][player_x] == 6) or\
       (key[K_DOWN] == 1 and hierarchy[player_y+1][player_x] == 6) or\
       (key[K_LEFT] == 1 and hierarchy[player_y][player_x-1] == 6) or\
       (key[K_RIGHT] == 1 and hierarchy[player_y][player_x+1] == 6):
        change_screen = 12
        timer = 0
        return    

    # When entering the random color
    # ランダムな色に入る場合
    if (key[K_UP] == 1 and hierarchy[player_y-1][player_x] == 7) or\
       (key[K_DOWN] == 1 and hierarchy[player_y+1][player_x] == 7) or\
       (key[K_LEFT] == 1 and hierarchy[player_y][player_x-1] == 7) or\
       (key[K_RIGHT] == 1 and hierarchy[player_y][player_x+1] == 7):
        change_screen = 14
        timer = 0
        return    

    # When entering the memo
    # メモに入る場合
    if (key[K_UP] == 1 and hierarchy[player_y-1][player_x] == 8) or\
       (key[K_DOWN] == 1 and hierarchy[player_y+1][player_x] == 8) or\
       (key[K_LEFT] == 1 and hierarchy[player_y][player_x-1] == 8) or\
       (key[K_RIGHT] == 1 and hierarchy[player_y][player_x+1] == 8):
        change_screen = 15
        timer = 0
        return    

    # When entering the BMI
    # BMIに入る場合
    if (key[K_UP] == 1 and hierarchy[player_y-1][player_x] == 9) or\
       (key[K_DOWN] == 1 and hierarchy[player_y+1][player_x] == 9) or\
       (key[K_LEFT] == 1 and hierarchy[player_y][player_x-1] == 9) or\
       (key[K_RIGHT] == 1 and hierarchy[player_y][player_x+1] == 9):
        change_screen = 16
        timer = 0
        return    

    # If you land on a healing potion
    # 回復薬に着地した場合
    if hierarchy[player_y][player_x] == 10:
        hierarchy[player_y][player_x] = 0
        recovery_agents = recovery_agents + 1

    # If you land on a drink
    # ドリンクに着地した場合
    if hierarchy[player_y][player_x] == 11:
        hierarchy[player_y][player_x] = 0
        if player_life < player_lifemax:
            player_life = player_life + 5        

    # If you land on poison
    # 毒薬に着地した場合
    if hierarchy[player_y][player_x] == 12:
        hierarchy[player_y][player_x] = 0
        player_life = player_life - 10

    # when fighting an enemy
    # 敵と戦う場合
    if hierarchy[player_y][player_x] == 50:
        hierarchy[player_y][player_x] = 0
        timer = 0
        change_screen = 17
        return    

    # Move up/down/left/right using the direction keys.
    # 方向キーで上下左右に移動する
    x = player_x
    y = player_y

    # If you press up, it moves up.
    # 上を押した場合、上へ移動する
    if key[K_UP] == 1:
        player_direction = 0
        
        # If it's not a forest
        # 森林ではない場合
        if hierarchy[player_y-1][player_x] != 100:
            player_y = player_y - 1

    # If you press down, it moves down.
    # 下を押した場合、下へ移動する
    if key[K_DOWN] == 1:
        player_direction = 1
        
        # If it's not a forest
        # 森林ではない場合
        if hierarchy[player_y+1][player_x] != 100:
            player_y = player_y + 1

    # If you press left, move to the left.
    # 左を押した場合、左へ移動する
    if key[K_LEFT] == 1:
        player_direction = 2
        
        # If it's not a forest
        # 森林ではない場合
        if hierarchy[player_y][player_x-1] != 100:
            player_x = player_x - 1

    # If you press right, it moves to the right.
    # 右を押した場合、右へ移動する
    if key[K_RIGHT] == 1:
        player_direction = 3
        
        # If it's not a forest
        # 森林ではない場合
        if hierarchy[player_y][player_x+1] != 100:
            player_x = player_x + 1
    
    player_animation = player_direction * 2

    # When moving the player, make it walk more realistically.
    # プレイヤーを移動させた時に、よりリアルに近い状態で歩かせる
    if player_x != x or player_y != y:
        player_animation = player_animation + timer%2

#################
# Internet
# インターネット
#################

def internet(bg, key):

    #####################
    # Screen management
    # 画面の管理
    #####################
    
    # screen color
    # 画面の色
    bg.fill(ORANGE)

    ###################
    # Specifying font
    # フォントの指定
    ###################
    
    # Specifying normal font
    # 通常フォントの指定
    font = pygame.font.Font(None, 40)

    # Specifying small font
    # 小さいフォントの指定
    fontS = pygame.font.Font(None, 30)

    ####################
    # Managing titles
    # タイトルの管理
    ####################

    # Title
    # タイトル
    robot_comment = font.render("Welcome Internet", True, (0,0,0))
    
    # Title text alignment coordinates
    # タイトルのテキスト配置座標
    bg.blit(robot_comment, (300, 20))

    #######################
    # instead of button
    # ボタンの代わり
    #######################
    
    # Preparing to create a rectangle
    # 四角形作成の準備
    rectangle1 = pygame.Rect(80, 70, 270, 80)
    rectangle2 = pygame.Rect(80, 140, 270, 80)
    rectangle3 = pygame.Rect(80, 210, 270, 80)
    rectangle4 = pygame.Rect(80, 280, 270, 80)
    rectangle5 = pygame.Rect(80, 350, 270, 80)
    rectangle6 = pygame.Rect(430, 70, 270, 80)
    rectangle7 = pygame.Rect(430, 140, 270, 80)
    rectangle8 = pygame.Rect(430, 210, 270, 80)
    rectangle9 = pygame.Rect(430, 280, 270, 80)

    # Coloring and drawing rectangles
    # 四角形の色と描画
    pygame.draw.rect(bg, OLIVE, rectangle1)
    pygame.draw.rect(bg, BLUE, rectangle2)
    pygame.draw.rect(bg, MAGENTA, rectangle3)
    pygame.draw.rect(bg, YELLOW, rectangle4)
    pygame.draw.rect(bg, GREEN, rectangle5)
    pygame.draw.rect(bg, SILVER, rectangle6)
    pygame.draw.rect(bg, PLUM, rectangle7)
    pygame.draw.rect(bg, ROYALBLUE, rectangle8)
    pygame.draw.rect(bg, RED, rectangle9)

    # Display text above the created rectangle.
    # 作成された四角形の上にテキストを表示する
    text1 = font.render("[Press g] Google", True, (0,0,0))
    text2 = font.render("[Press b] Bing", True, (0,0,0))
    text3 = font.render("[Press y] Yahoo", True, (0,0,0))
    text4 = fontS.render("[Press d] DuckDuckGo", True, (0,0,0))
    text5 = font.render("[Press e] Ecosia", True, (0,0,0))
    text6 = font.render("[Press a] Amazon", True, (0,0,0))
    text7 = font.render("[Press r] Rakuten", True, (0,0,0))
    text8 = fontS.render("[Press t] Google translate", True, (0,0,0))
    text9 = fontS.render("[Press h] Bing translate", True, (0,0,0))

    # Text placement coordinates
    # テキストの配置座標
    bg.blit(text1, (100, 100))
    bg.blit(text2, (100, 170))
    bg.blit(text3, (100, 240))
    bg.blit(text4, (100, 310))
    bg.blit(text5, (100, 380))
    bg.blit(text6, (450, 100))
    bg.blit(text7, (450, 170))
    bg.blit(text8, (440, 240))
    bg.blit(text9, (450, 310))

    #####################
    # Robot management
    # ロボットの管理
    #####################
    
    # Arrangement of robot images
    # ロボットの画像の配置
    bg.blit(imgRobot[0], (250,10))

    #######################
    # Specifying the url
    # URLの指定
    #######################

    # Transit to Google search engine.
    # Google検索エンジンへ遷移する
    if key[K_g] == 1:
        url1 = 'https://www.google.com'
        webbrowser.open(url1, new=1, autoraise=True)

    # Transit to Microsoft search engine.
    # Microsoft検索エンジンへ遷移する
    if key[K_b] == 1:
        url1 = 'https://www.bing.com'
        webbrowser.open(url1, new=1, autoraise=True)

    # Transit to Yahoo search engine.
    # Yahoo検索エンジンへ遷移する
    if key[K_y] == 1:
        url1 = 'https://www.yahoo.com'
        webbrowser.open(url1, new=1, autoraise=True)

    # Transit to DuckDuckGo search engine.
    # DuckDuckGo検索エンジンへ遷移する
    if key[K_d] == 1:
        url1 = 'https://duckduckgo.com'
        webbrowser.open(url1, new=1, autoraise=True)

    # Transit to Ecosia search engine.
    # Ecosia検索エンジンへ遷移する
    if key[K_e] == 1:
        url1 = 'https://www.ecosia.org'
        webbrowser.open(url1, new=1, autoraise=True)
    
    # Transfer to Amazon site.
    # Amazonサイトへ遷移する
    if key[K_a] == 1:
        url1 = 'https://www.amazon.co.jp'
        webbrowser.open(url1, new=1, autoraise=True)

    # Transition to Rakuten site.       
    # 楽天サイトへ遷移する
    if key[K_r] == 1:
        url2 = 'https://www.rakuten.co.jp'
        webbrowser.open(url2, new=1, autoraise=True)

    # Transition to Google translation site.      
    # Google翻訳サイトへ遷移する
    if key[K_t] == 1:
        url2 = 'https://translate.google.co.jp'
        webbrowser.open(url2, new=1, autoraise=True)

    # Transition to Bing translation site.      
    # Bing翻訳サイトへ遷移する
    if key[K_h] == 1:
        url2 = 'https://www.bing.com/translator'
        webbrowser.open(url2, new=1, autoraise=True)    

    ######################
    # Leave the internet.
    # インターネットから出る
    ######################
    
    draw_text(bg, "[Press space] Leave the internet.", 220, 560, font, COLOR_SCHEME3[timer%10])


#########################
# Fortune telling hall
# 占いの館
#########################

def fortune_display(bg):

    ######################
    # Screen management
    # 画面の管理
    ######################
    
    # screen color
    # 画面の色
    bg.fill(PURPLE)

    ##################
    # Specifying font
    # フォントの指定
    ##################
    
    # Title font specification
    # タイトルのフォント指定
    fontT = pygame.font.Font(None, 60)

    # Specifying normal font
    # 通常フォントの指定
    font = pygame.font.Font(None, 40)

    ####################
    # Managing titles
    # タイトルの管理
    ####################
    
    # Title 
    # タイトル
    title_text = fontT.render("Fortune telling hall", True, (0,0,0))

    # Title text alignment coordinates
    # タイトルのテキスト配置座標
    bg.blit(title_text, (230, 20))

    ####################
    # Robot management
    # ロボットの管理
    ####################
    
    # robot comment
    # ロボットのコメント
    robot_comment = font.render("[Press d] draw a fortune", True, (0,0,0))

    # Placement coordinates of robot comment
    # ロボットのコメントの配置座標
    bg.blit(robot_comment, (330, 280))

    # Arrangement of robot images
    # ロボットの画像の配置
    bg.blit(imgRobot[1], (50,250))

    # Place an image of the robot's comment.
    # ロボットのコメントの画像を配置する
    bg.blit(imgRobotComment[0], (250,150))

    ##################################
    # Leave the fortune-telling hall.
    # 占いの館から離れる
    ##################################
    
    draw_text(bg, "[Press space] Leave the fortune-telling hall", 120, 560, font, COLOR_SCHEME4[timer%10])


################################
# Fortune telling result list
# 占い結果リスト
################################

def fortune():

    # List of results of drawing fortunes
    # おみくじを引いた結果リスト

    # daikichi：excellent luck（best luck）
    # chukichi：fair luck
    # shokichi：a little luck
    # kichi   ：good luck
    # suekichi：uncertain luck
    # kyo     ：bad luck
    # daikyo  ：very bad luck
    
    kuji = random.choice(["dai-kichi","chu-kichi","sho-kichi","kichi","sue-kichi","kyo","dai-kyo"])
    return kuji

###########################
# Fortune telling results
# 占い結果
###########################

def fortune_result(bg):

    #######################
    # Screen management
    # 画面の管理
    #######################
    
    # screen color
    # 画面の色    
    bg.fill(PURPLE)

    ##################
    # Specifying font
    # フォントの指定
    ##################
    
    # Title font specification
    # タイトルのフォント指定    
    fontT = pygame.font.Font(None, 60)

    # Font specification for fortune telling results
    # 占い結果のフォント指定
    fontR = pygame.font.Font(None, 70)

    # Specifying normal font
    # 通常フォントの指定
    font = pygame.font.Font(None, 40)

    ####################
    # Managing titles
    # タイトルの管理
    ####################
    
    # Title
    # タイトル
    title_text = fontT.render("Fortune telling hall", True, (0,0,0))

    # Title text alignment coordinates
    # タイトルのテキスト配置座標
    bg.blit(title_text, (230, 20))

    ##########################################
    # Management of fortune telling results
    # 占い結果の管理
    ##########################################

    # Fortune telling result display text
    # 占い結果表示のテキスト
    fortune_result_text = fontR.render(fortune(), True, (0,0,0))

    # Placement coordinates of fortune telling result text
    # 占い結果のテキストの配置座標
    bg.blit(fortune_result_text, (400, 270))

    ####################
    # Robot management
    # ロボットの管理
    ####################
    
    # Arrangement of robot images
    # ロボットの画像の配置
    bg.blit(imgRobot[2], (50,250))

    # Place an image of the robot's comment.
    # ロボットのコメントの画像を配置する
    bg.blit(imgRobotComment[0], (250,150))


###################################
# Password generation tool screen
# パスワード生成ツールの画面
###################################

def password_generation_tool_display(bg):

    ######################
    # Screen management
    # 画面の管理
    ######################
    
    # screen color
    # 画面の色    
    bg.fill(PINK)

    ###################
    # Specifying font
    # フォントの指定
    ###################
    
    # Title font specification
    # タイトルのフォント指定    
    fontT = pygame.font.Font(None, 60)

    # Specifying normal font
    # 通常フォントの指定
    font = pygame.font.Font(None, 32)

    ###################
    # Managing titles
    # タイトルの管理
    ###################
    
    # Title
    # タイトル
    title_text = fontT.render("Password generation tool", True, (0,0,0))

    # Title text alignment coordinates
    # タイトルのテキストの配置座標
    bg.blit(title_text, (150, 20))

    ######################
    # instead of button
    # ボタンの代わり
    ######################
    
    # Preparing to create a rectangle
    # 四角形作成の準備
    rectangle1 = pygame.Rect(80, 70, 270, 80)
    rectangle2 = pygame.Rect(80, 140, 270, 80)
    rectangle3 = pygame.Rect(80, 210, 270, 80)
    rectangle4 = pygame.Rect(80, 280, 270, 80)
    rectangle5 = pygame.Rect(80, 350, 270, 80)
    rectangle6 = pygame.Rect(430, 70, 270, 80)
    rectangle7 = pygame.Rect(430, 140, 270, 80)
    rectangle8 = pygame.Rect(430, 210, 270, 80)
    rectangle9 = pygame.Rect(430, 280, 270, 80)
    rectangle10 = pygame.Rect(430, 350, 270, 80)
    rectangle11 = pygame.Rect(430, 420, 270, 80)

    # Coloring and drawing rectangles
    # 四角形の色と描画
    pygame.draw.rect(bg, OLIVE, rectangle1)
    pygame.draw.rect(bg, YELLOW, rectangle2)
    pygame.draw.rect(bg, BLUE, rectangle3)
    pygame.draw.rect(bg, MAGENTA, rectangle4)
    pygame.draw.rect(bg, PLUM, rectangle5)
    pygame.draw.rect(bg, SILVER, rectangle6)
    pygame.draw.rect(bg, GREEN, rectangle7)
    pygame.draw.rect(bg, ROYALBLUE, rectangle8)
    pygame.draw.rect(bg, RED, rectangle9)
    pygame.draw.rect(bg, BURLYWOOD, rectangle10)
    pygame.draw.rect(bg, LIME, rectangle11)

    # Display text above the created rectangle.
    # 作成された四角形の上にテキストを表示する
    text1 = font.render("[Press q] 10 characters", True, (0,0,0))
    text2 = font.render("[Press w] 11 characters", True, (0,0,0))
    text3 = font.render("[Press e] 12 characters", True, (0,0,0))
    text4 = font.render("[Press r] 13 characters", True, (0,0,0))
    text5 = font.render("[Press t] 14 characters", True, (0,0,0))
    text6 = font.render("[Press y] 15 characters", True, (0,0,0))
    text7 = font.render("[Press u] 16 characters", True, (0,0,0))
    text8 = font.render("[Press i] 17 characters", True, (0,0,0))
    text9 = font.render("[Press o] 18 characters", True, (0,0,0))
    text10 = font.render("[Press p] 19 characters", True, (0,0,0))
    text11 = font.render("[Press a] 20 characters", True, (0,0,0))

    # Text placement coordinates
    # テキストの配置座標
    bg.blit(text1, (100, 100))
    bg.blit(text2, (100, 170))
    bg.blit(text3, (100, 240))
    bg.blit(text4, (100, 310))
    bg.blit(text5, (100, 380))
    bg.blit(text6, (450, 100))
    bg.blit(text7, (450, 170))
    bg.blit(text8, (450, 240))
    bg.blit(text9, (450, 310))
    bg.blit(text10, (450, 380))
    bg.blit(text11, (450, 450))

    ######################################
    # Leave the password generation tool.
    # パスワード生成ツールから離れる
    ######################################
    
    draw_text(bg, "[Press space] Leave the password generation tool screen", 100, 560, font, COLOR_SCHEME5[timer%10])

######################
# Password generator
# パスワード生成ツール
######################

def password_generation_tool(length):
    
    # Generate a password using half-width alphanumeric characters and symbols using the secrets module.
    # secretsモジュールを用いて、半角英数字と記号のパスワードを生成する
    combination = string.ascii_letters + string.digits + string.punctuation
    pw = ''.join(secrets.choice(combination) for i in range(length))    
    return pw

###############################
# Password generation result
# パスワード生成結果
###############################

def password_result(bg):
    
    ####################
    # Screen management
    # 画面の管理
    ####################

    # screen color
    # 画面の色    
    bg.fill(PINK)
    
    ##################
    # Specifying font
    # フォントの指定
    ##################

    # Title font specification
    # タイトルのフォント指定    
    fontT = pygame.font.Font(None, 60)

    # Specifying the font for password generation results
    # パスワード生成結果のフォントの指定
    fontR = pygame.font.Font(None, 50)

    # Specifying normal font
    # 通常フォントの指定    
    font = pygame.font.Font(None, 32)

    ####################
    # Managing titles
    # タイトルの管理
    ####################
    
    # Title
    # タイトル
    title_text = fontT.render("Password generation result", True, (0,0,0))

    # Title text alignment coordinates
    # タイトルのテキストの配置座標
    bg.blit(title_text, (130, 20))

    ########################################
    # Managing password generation results
    # パスワード生成結果の管理
    ########################################

    # Password generation result display text
    # パスワード生成結果の表示のテキスト
    password_generation_tool_result_text = fontT.render(password_generation_tool(password_length), True, (0,0,0))
    bg.blit(password_generation_tool_result_text, (100, 232))

    ####################
    # Robot management
    # ロボットの管理
    ####################

    # Arrangement of robot images
    # ロボットの画像の配置
    bg.blit(imgRobot[3], (310,340))

    # Place an image of the robot's comment.
    # ロボットのコメントの画像を配置する
    bg.blit(imgRobotComment[2], (70,150))

##########################################
# Rock, paper, scissors game start screen
# じゃんけんゲーム開始画面
##########################################

def janken_start_display(bg):
    
    #####################
    # Screen management
    # 画面の管理
    #####################

    # screen color
    # 画面の色    
    bg.fill(LIGHTCYAN)

    ####################
    # Specifying font
    # フォントの指定
    ####################
    
    # Title font specification
    # タイトルのフォント指定            
    fontT = pygame.font.Font(None, 60)

    # Specifying normal font
    # 通常フォントの指定    
    font = pygame.font.Font(None, 32)

    # Specify the font for robot comments.
    # ロボットのコメントのフォントを指定する
    fontS = pygame.font.Font(None, 24)

    ##################
    # Managing titles
    # タイトルの管理
    ##################
    
    # Title
    # タイトル
    title_text = fontT.render("Rock, paper, scissors", True, (0,0,0))

    # Title text alignment coordinates
    # タイトルのテキストの配置座標
    bg.blit(title_text, (200, 20))

    #####################################################
    # Ask the player which move they would like to make.
    # プレイヤーにどの手を出すかを質問する
    #####################################################
    
    # Ask the player which move they would like to make.
    # プレイヤーにどの手を出すかを質問する
    player_hand_question_text = font.render("Which hand will you make?", True, (0,0,0))

    # Placement coordinates of question text
    # 質問文の配置座標
    bg.blit(player_hand_question_text, (50, 150))

    #######################################################
    # Rock, paper, scissors options and image management
    # じゃんけんの選択肢と画像の管理
    #######################################################
    
    # Placement of rock-paper-scissors images
    # じゃんけん画像の配置
    bg.blit(imgHand[0], (50,220))
    bg.blit(imgHand[1], (150,220))
    bg.blit(imgHand[2], (250,220))

    # Display three options below the rock-paper-scissors image.
    # じゃんけん画像の下に３つの選択肢を表示させる
    rock_text = font.render("[Press 0] rock", True, (0,0,0))
    paper_text = font.render("[Press 1] paper", True, (0,0,0))
    scissors_text = font.render("[Press 2] scissors", True, (0,0,0))

    # Coordinates for text placement of three choices
    # ３つの選択肢のテキスト配置の座標
    bg.blit(rock_text, (50, 350))
    bg.blit(paper_text, (50, 390))
    bg.blit(scissors_text, (50, 430))

    #####################
    # Robot management
    # ロボットの管理
    #####################
    
    # Arrangement of robot images
    # ロボットの画像の配置
    bg.blit(imgRobot[3], (490,300))

    # robot comment
    # ロボットのコメント
    robot_comment = fontS.render("Let's play rock, paper, scissors with the robot!", True, (0,0,0))

    # Placement of robot comments
    # ロボットのコメントの配置
    bg.blit(robot_comment, (420, 190))

    # Place an image of the robot's comment.
    # ロボットのコメントの画像を配置する
    bg.blit(imgRobotComment[1], (400,100))

    #######################################
    # Leave the rock-paper-scissors game.
    # じゃんけんゲームから離れる
    #######################################
    
    draw_text(bg, "[Press space] Leave the Rock, paper, scissors game.", 100, 560, font, COLOR_SCHEME6[timer%10])

#################################
# Rock, paper, scissors result
# じゃんけんの結果
#################################

def janken_result(bg):
    
    #####################
    # Screen management
    # 画面の管理
    #####################

    # screen color
    # 画面の色      
    bg.fill(LIGHTCYAN)

    ####################
    # Specifying font
    # フォントの指定
    ####################
    
    # Title font specification
    # タイトルのフォント指定            
    fontT = pygame.font.Font(None, 60)

    # Specifying a large font
    # 大きいフォントの指定
    fontB = pygame.font.Font(None, 65)

    # Specifying normal font
    # 通常フォントの指定    
    font = pygame.font.Font(None, 50)

    ###################
    # Managing titles
    # タイトルの管理
    ###################
    
    # Title
    # タイトル
    title_text = fontT.render("Rock, paper, scissors", True, (0,0,0))

    # Title text alignment coordinates
    # タイトルのテキストの配置座標
    bg.blit(title_text, (200, 20))


    ####################
    # Robot management
    # ロボットの管理
    ####################

    # Arrangement of robot images
    # ロボットの画像の配置
    bg.blit(imgRobot[3], (290,350))

    # Place an image of the robot's comment.
    # ロボットのコメントの画像を配置する
    bg.blit(imgRobotComment[1], (200,150))

    # Robot rock, paper, scissors
    # ロボットのじゃんけん
    robot_hand = random.randint(0, 2)
    robot_hand_text = font.render(hand[robot_hand], True, (0,0,0))
        
    # Text placement coordinates
    # テキストの配置座標
    bg.blit(robot_hand_text, (340, 235))


    ###############################
    # Win/Loss Judgment Results
    # 勝敗の判定結果
    ###############################
  
    if player_hand == robot_hand:
            
        # draw
        # 引き分け
        draw_text = fontB.render("draw!", True, (0,0,0))

        # Placement coordinates of the draw
        # 引き分けの配置座標
        bg.blit(draw_text, (350, 120))

    if player_hand == 0:
        if robot_hand == 1:
            
            # Robot wins
            # ロボットの勝ち
            robot_win_text = fontB.render("Robot wins!", True, (0,0,0))

            # Robot winning placement coordinates
            # ロボットの勝ちの配置座標
            bg.blit(robot_win_text, (280, 120))

        if robot_hand == 2:
            
            # You win
            # あなたの勝ち
            you_win_text = fontB.render("You win!", True, (0,0,0))

            # your winning placement coordinates
            # あなたの勝ちの配置座標
            bg.blit(you_win_text, (310, 120))

    if player_hand == 1:
        if robot_hand == 0:
            
            # You win
            # あなたの勝ち
            you_win_text = fontB.render("You win!", True, (0,0,0))

            # your winning placement coordinates
            # あなたの勝ちの配置座標
            bg.blit(you_win_text, (310, 120))

        if robot_hand == 2:
            
            # Robot wins
            # ロボットの勝ち
            robot_win_text = fontB.render("Robot wins!", True, (0,0,0))

            # Robot winning placement coordinates
            # ロボットの勝ちの配置座標
            bg.blit(robot_win_text, (280, 120))
            
    if player_hand == 2:
        if robot_hand == 0:
            
            # Robot wins
            # ロボットの勝ち
            robot_win_text = fontB.render("Robot wins!", True, (0,0,0))

            # Robot winning placement coordinates
            # ロボットの勝ちの配置座標
            bg.blit(robot_win_text, (280, 120))

        if robot_hand == 1:
            
            # You win
            # あなたの勝ち
            you_win_text = fontB.render("You win!", True, (0,0,0))

            # your winning placement coordinates
            # あなたの勝ちの配置座標
            bg.blit(you_win_text, (310, 120))
        
##########################
# Display random colors.
# ランダムな色を表示する
##########################

def random_color(bg):
    
    # global variables
    # グローバル変数
    global RANDOM_COLOR

    #######################
    # Screen management
    # 画面の管理
    #######################

    # screen color
    # 画面の色    
    bg.fill(WHITE)
    
    #####################
    # Specifying font
    # フォントの指定
    #####################

    # Title font specification
    # タイトルのフォント指定    
    fontT = pygame.font.Font(None, 60)

    # Specifying normal font
    # 通常フォントの指定    
    font = pygame.font.Font(None, 32)

    ###################
    # Managing titles
    # タイトルの管理
    ###################

    # Title
    # タイトル
    title_text = fontT.render("Random Color", True, (0,0,0))

    # Title text alignment coordinates
    # タイトルのテキストの配置座標
    bg.blit(title_text, (250, 20))

    #################
    # draw shapes
    # 図形を描画する
    #################

    # Random color in RGB format（No duplicates）
    # RGB形式のランダムな色（重複なし）
    RANDOM_COLOR = random.sample(RANDOM_COLOR, 129)
        
    # Shape definition
    # 図形の定義
    shape = []
    
    for i in range(129):

        # Adds an element to the end of a list (array).
        # リスト（配列）の末尾に要素を追加する
        shape.append(i)
        
        if i <= 16:
            
            # drawing lines
            # 線の描画
            shape[i] = pygame.draw.line(bg, RANDOM_COLOR[i], [i%16*50+8, 150], [i%16*50+40, 150], 10)
            
        elif 17 <= i and i <= 32:

            # drawing lines
            # 線の描画            
            shape[i] = pygame.draw.line(bg, RANDOM_COLOR[i], [i%16*50+8, 190], [i%16*50+40, 190], 10)
            
        elif 33 <= i and i <= 48:

            # drawing a rectangle
            # 四角形の描画
            shape[i] = pygame.Rect(i%16*50, 220, 50, 50)
            pygame.draw.rect(bg, RANDOM_COLOR[i], shape[i])

        elif 49 <= i and i <= 64:

            # drawing a rectangle
            # 四角形の描画
            shape[i] = pygame.Rect(i%16*50, 270, 50, 50)
            pygame.draw.rect(bg, RANDOM_COLOR[i], shape[i])

        elif 65 <= i and i <= 80:

            # drawing a circle
            # 円の描画
            shape[i] = [i%16*50+22, 350]
            pygame.draw.circle(bg, RANDOM_COLOR[i], shape[i], 20)

        elif 81 <= i and i <= 96:

            # drawing a circle
            # 円の描画
            shape[i] = [i%16*50+22, 400]
            pygame.draw.circle(bg, RANDOM_COLOR[i], shape[i], 20)

        elif 97 <= i and i <= 112:

            # drawing a triangle
            # 三角形の描画
            shape[i] = [[i%16*50+22, 430], [i%16*50+5, 460], [i%16*50+40,460]]
            pygame.draw.polygon(bg, RANDOM_COLOR[i], shape[i], 5)

        elif 113 <= i and i <= 128:

            # drawing a triangle
            # 三角形の描画
            shape[i] = [[i%16*50+22, 480], [i%16*50+5, 510], [i%16*50+40,510]]
            pygame.draw.polygon(bg, RANDOM_COLOR[i], shape[i], 5)
    
    # Display text above the created rectangle.
    # 作成された四角形の上にテキストを表示する
    text1 = font.render("Random color in RGB format", True, (0,0,0))

    # Text placement coordinates
    # テキストの配置座標
    bg.blit(text1, (240, 80))

#########
# memo
# メモ
#########

def memo(bg):
    
    ####################
    # Specifying font
    # フォントの指定
    ####################

    # Title font specification
    # タイトルのフォント指定    
    fontT = pygame.font.Font(None, 60)

    # Specifying normal font
    # 通常フォントの指定       
    font = pygame.font.Font(None, 40)

    # Specifying the font for the explanatory text
    # 説明文のフォント指定
    fontE = pygame.font.Font(None, 30)

    ##################
    # time management
    # 時間の管理
    ##################
    
    clock = pygame.time.Clock()

    #################
    # Managing text
    # テキストの管理
    #################

    # memo text
    # メモテキスト
    memo_text = ''

    ######################
    # keyboard management
    # キーボードの管理
    ######################
    
    keypressed = True

    while True:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:

                # Close the window.
                # ウィンドウを終了する
                pygame.quit()

                # Terminate the program.
                # プログラムを終了させる
                sys.exit()
           
            if event.type == pygame.KEYDOWN:
                keypressed = True

                # When you press the return key, a file called memo.txt will be created.
                # returnキーを押すと、memo.txtというファイルが作成される
                if event.key == pygame.K_RETURN:
                    file = open("memo.txt", 'w')
                    file.write(memo_text)
                    file.close()
                    memo_text = ''

                # Pressing the BACKSPACE key deletes one character.
                # BACKSPACEキーを押すと、1文字が削除される。
                elif event.key == pygame.K_BACKSPACE:
                    memo_text = memo_text[:-1]
                    
                # If you input one alphanumeric character, one character will be output.
                # 英数字記号を1文字入力すると、1文字出力される
                else:
                    memo_text += event.unicode
            elif event.type == KEYUP:
                keypressed = False

        ######################
        # Screen management
        # 画面の管理
        ######################

        # screen color
        # 画面の色    
        bg.fill(WHITE)

        ####################
        # Title management
        # タイトルの管理
        ####################

        # Title
        # タイトル
        title_text = fontT.render("Memo", True, (0,0,0))

        # Title text alignment coordinates
        # タイトルのテキストの配置座標
        bg.blit(title_text, (330, 20))

        ###########################
        # Manage Explanatory text
        # 説明文の管理
        ###########################

        # Explanatory text
        # 説明文
        explanatory_text1 = fontE.render("Please input something.", True, (0,0,0))
        explanatory_text2 = fontE.render("When you press the return key, a file called memo.txt will be created.", True, (0,0,0))

        # Explanatory text placement coordinates
        # 説明文のテキスト配置座標
        bg.blit(explanatory_text1, (30, 100))
        bg.blit(explanatory_text2, (30, 140))

        ###################
        # Leave the Memo
        # Memoから離れる
        ###################

        leave_the_memo_text = font.render("[Press escape] Leave the Memo", True, (0,0,0))
        bg.blit(leave_the_memo_text, (200, 560))
        
        ##############################
        # Managing text input/output
        # テキスト入出力の管理
        ##############################
        
        text_surface = font.render(memo_text, True, NAVY)
        bg.blit(text_surface, text_surface.get_rect(center=(390,300)))

        #####################################
        # Update the display's txt_surface.
        # ディスプレイのtext_surfaceを更新する
        #####################################
        
        pygame.display.flip()

        ###################################################
        # Run at speeds greater than 30 frames per second.
        # 1秒毎に30フレームを超える速度で実行する
        ###################################################
        
        clock.tick(30)

        # Press the ESCAPE key to exit from the memo function.
        # ESCAPEキーを押すと、memo関数から抜ける
        if pygame.key.get_pressed()[K_ESCAPE] == 1:
            break

#####################
# BMI determination
# BMI判定
#####################

def bmi(bg):
        
    ####################
    # Specifying font
    # フォントの指定
    ####################

    # Title font specification
    # タイトルのフォント指定    
    fontT = pygame.font.Font(None, 60)

    # Specifying normal font
    # 通常フォントの指定       
    font = pygame.font.Font(None, 40)

    # Specifying the font for the explanatory text
    # 説明文のフォント指定
    fontE = pygame.font.Font(None, 30)

    ####################
    # time management
    # 時間の管理
    ####################
    
    clock = pygame.time.Clock()

    #################
    # Managing text
    # テキストの管理
    #################

    # height text and weight text
    # 身長テキストと体重テキスト
    height_weight_text = ''

    # Put the height and weight into the bmi_text array.
    # 身長と体重をbmi_textの配列に入れる
    bmi_text = []

    #######################
    # keyboard management
    # キーボードの管理
    #######################
    
    keypressed = True

    while True:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:

                # Close the window.
                # ウィンドウを終了する
                pygame.quit()

                # Terminate the program.
                # プログラムを終了させる
                sys.exit()

            if event.type == pygame.KEYDOWN:
                keypressed = True

                # If the RETURN key is pressed
                # RETURNキーが押された場合
                if event.key == pygame.K_RETURN:
                    bmi_text.append(height_weight_text)
                    height_weight_text = ''

                    if len(bmi_text) == 2:

                        # BMI calculation
                        # BMI計算
                        BMI_Cal = round(float(bmi_text[1])/(float(bmi_text[0])*float(bmi_text[0]))*10000, 2)

                        # BMI determination
                        # BMI判定

                        # If your BMI is less than 18.5
                        # BMIが18.5より小さい場合
                        if BMI_Cal < 18.5:

                            # 痩せすぎ
                            BMI_Jud = "too skinny"

                            file = open("bmi.txt", 'w')
                            file_text = ['height：', str(bmi_text[0]), '\n', 'weight：', str(bmi_text[1]), '\n', 'BMI calculation result：', str(BMI_Cal), '\n', 'BMI determination result：', str(BMI_Jud), '\n']
                            file.writelines(file_text)
                            file.close()

                        # If your BMI is greater than 18.5 and less than 25.0
                        # BMIが18.5より大きく、25.0より小さい場合
                        elif 18.5 < BMI_Cal and BMI_Cal < 25.0:

                            # 普通体重
                            BMI_Jud = "normal weight"

                            file = open("bmi.txt", 'w')
                            file_text = ['height：', str(bmi_text[0]), '\n', 'weight：', str(bmi_text[1]), '\n', 'BMI calculation result：', str(BMI_Cal), '\n', 'BMI determination result：', str(BMI_Jud), '\n']
                            file.writelines(file_text)
                            file.close()

                        # If BMI is greater than 25.0 and less than 30.0
                        # BMIが25.0より大きく、30.0より小さい場合
                        elif 25.0 < BMI_Cal and BMI_Cal < 30.0:

                            # 肥満（1度）
                            BMI_Jud = "Class I Obesity"

                            file = open("bmi.txt", 'w')
                            file_text = ['height：', str(bmi_text[0]), '\n', 'weight：', str(bmi_text[1]), '\n', 'BMI calculation result：', str(BMI_Cal), '\n', 'BMI determination result：', str(BMI_Jud), '\n']
                            file.writelines(file_text)
                            file.close()

                        # If your BMI is greater than 30.0 and less than 35.0
                        # BMIが30.0より大きく、35.0より小さい場合
                        elif 30.0 < BMI_Cal and BMI_Cal < 35.0:

                            # 肥満（2度）
                            BMI_Jud = "Class Ⅱ Obesity"

                            file = open("bmi.txt", 'w')
                            file_text = ['height：', str(bmi_text[0]), '\n', 'weight：', str(bmi_text[1]), '\n', 'BMI calculation result：', str(BMI_Cal), '\n', 'BMI determination result：', str(BMI_Jud), '\n']
                            file.writelines(file_text)
                            file.close()

                        # If your BMI is greater than 35.0 and less than 40.0
                        # BMIが35.0より大きく、40.0より小さい場合
                        elif 35.0 < BMI_Cal and BMI_Cal < 40.0:

                            # 肥満（3度）
                            BMI_Jud = "Class Ⅲ Obesity"

                            file = open("bmi.txt", 'w')
                            file_text = ['height：', str(bmi_text[0]), '\n', 'weight：', str(bmi_text[1]), '\n', 'BMI calculation result：', str(BMI_Cal), '\n', 'BMI determination result：', str(BMI_Jud), '\n']
                            file.writelines(file_text)
                            file.close()

                        # If your BMI is greater than 40.0
                        # BMIが40.0より大きい場合
                        elif 40.0 < BMI_Cal:

                            # 肥満（4度）
                            BMI_Jud = "Class Ⅳ Obesity"

                            file = open("bmi.txt", 'w')
                            file_text = ['height：', str(bmi_text[0]), '\n', 'weight：', str(bmi_text[1]), '\n', 'BMI calculation result：', str(BMI_Cal), '\n', 'BMI determination result：', str(BMI_Jud), '\n']
                            file.writelines(file_text)
                            file.close()

                # Pressing the BACKSPACE key deletes one character.
                # BACKSPACEキーを押すと、1文字が削除される。
                elif event.key == pygame.K_BACKSPACE:
                    height_weight_text = height_weight_text[:-1]

                # If you input one alphanumeric character, one character will be output.
                # 英数字記号を1文字入力すると、1文字出力される
                else:
                    height_weight_text += event.unicode
                    
            elif event.type == KEYUP:
                keypressed = False

        #####################
        # Screen management
        # 画面の管理
        #####################

        # screen color
        # 画面の色    
        bg.fill(WHITE)

        ####################
        # Title management
        # タイトルの管理
        ####################

        # Title
        # タイトル
        title_text = fontT.render("BMI", True, (0,0,0))

        # Title text alignment coordinates
        # タイトルのテキストの配置座標
        bg.blit(title_text, (350, 20))

        ###########################
        # Manage Explanatory text
        # 説明文の管理
        ###########################

        # Explanatory text
        # 説明文
        
        # まず、身長（cm）を入力して、RETURNキーを押してください。
        explanatory_text1 = fontE.render("First, enter your height (cm) and press the RETURN key.", True, (0,0,0))
        
        # 次に、体重（kg）を入力して、RETURNキーを押してください。
        explanatory_text2 = fontE.render("Next, enter your weight (kg) and press the RETURN key.", True, (0,0,0))
        
        # そして、入力された身長（cm）と体重（kg）に基づいて、BMI計算結果とBMI判定結果が作成される。
        explanatory_text3 = fontE.render("Based on the input height (cm) and weight (kg), BMI calculation", True, (0,0,0))
        explanatory_text4 = fontE.render("results and BMI determination results are created.", True, (0,0,0))
        
        #最後に、RETURNキーを押すと、身長（cm）と体重（kg）、BMI計算結果、BMI判定結果が「bmi.txt」というファイルに出力されます。
        explanatory_text5 = fontE.render("Finally, when you press the RETURN key,", True, (0,0,0))
        explanatory_text6 = fontE.render("the height (cm), weight (kg), BMI calculation results,", True, (0,0,0))
        explanatory_text7 = fontE.render("and BMI determination results are output to a file called bmi.txt.", True, (0,0,0))

        # Explanatory text placement coordinates
        # 説明文のテキスト配置座標
        bg.blit(explanatory_text1, (30, 100))
        bg.blit(explanatory_text2, (30, 140))
        bg.blit(explanatory_text3, (30, 190))
        bg.blit(explanatory_text4, (30, 230))
        bg.blit(explanatory_text5, (30, 280))
        bg.blit(explanatory_text6, (30, 320))
        bg.blit(explanatory_text7, (30, 360))
        
        #################
        # Leave the BMI
        # BMIから離れる
        #################

        leave_the_bmi_text = font.render("[Press escape] Leave the BMI", True, (0,0,0))
        bg.blit(leave_the_bmi_text, (200, 560))
        
        ##############################
        # Managing text input/output
        # テキスト入出力の管理
        ##############################
        
        text_surface = font.render(height_weight_text, True, NAVY)
        bg.blit(text_surface, text_surface.get_rect(center=(390,440)))

        #####################################
        # Update the display's txt_surface.
        # ディスプレイのtext_surfaceを更新する
        #####################################
        
        pygame.display.flip()

        ###################################################
        # Run at speeds greater than 30 frames per second.
        # 1秒毎に30フレームを超える速度で実行する
        ###################################################
        
        clock.tick(30)
            
        # Press the ESCAPE key to exit from the bmi function.
        # ESCAPEキーを押すと、bmi関数から抜ける
        if pygame.key.get_pressed()[K_ESCAPE] == 1:
            break

##############################
# Player strength information
# プレイヤーの強さの情報
##############################

def player_strength_info(bg, fnt):

    # Defines the color of the player's life as white.
    # プレイヤーのライフの色を白として定義する
    player_life_color = WHITE

    # If the player's life is less than 10 and the timer has a remainder of 0 when divided by 2.
    # プレイヤーのライフが10より小さく、timerが2で割った余りが0の場合
    if player_life < 10 and timer%2 == 0:

        # Changes the player's life color to red.
        # プレイヤーのライフの色を赤色に変更する
        player_life_color = RED

    # Player's life bar display and placement coordinates
    # プレイヤーのライフバーの表示と配置座標
    draw_text(bg, create_player_life_bar(bg, 90, 543, 170, 10, player_life, player_lifemax), 10, 510, fnt, WHITE)

    # Text display of number of player's healing potions and location coordinatess
    # プレイヤーの回復薬の数のテキスト表示と配置座標
    draw_text(bg, "recovery agents:", 10, 510, fnt, WHITE)

    # Placement coordinates of player's number of healing medicines
    # プレイヤーの回復薬の数の配置座標
    draw_text(bg, str(recovery_agents), 180, 510, fnt, WHITE)

    # Display and placement coordinates of the player's current life and maximum life
    # プレイヤーの現在のライフと最大値のライフの表示と配置座標
    draw_text(bg, "{}/{}".format(player_life, player_lifemax), 8, 540, fnt, WHITE)

    # Text display and placement coordinates as "Player's attack power:"
    # 「プレイヤーの攻撃力:」としてのテキスト表示と配置座標
    draw_text(bg, "player's attack power:", 10, 570, fnt, WHITE)

    # Location coordinates of player's attack power
    # プレイヤーの攻撃力の配置座標
    draw_text(bg, str(player_attack_power), 230, 570, fnt, WHITE)

#################################
# Creating a player's life bar
# プレイヤーのライフバー作成
#################################

def create_player_life_bar(bg, player_life_x, player_life_y, player_life_width, player_life_height, player_life_val, player_life_max):

    # Create a player's life as a rectangle.
    # プレイヤーのライフを四角形として作成する
    pygame.draw.rect(bg, WHITE, [player_life_x-2, player_life_y-2, player_life_width+4, player_life_height+4])
    pygame.draw.rect(bg, BLACK, [player_life_x, player_life_y, player_life_width, player_life_height])

    # If the player's current life is greater than 0
    # プレイヤーの現在のライフが0より大きい場合
    if player_life_val > 0:

        # Creates a rectangle according to the player's current life (color:  ROYALBLUE).
        # プレイヤーの現在のライフ（color:ROYALBLUE）に応じて、四角形を作成する
        pygame.draw.rect(bg, ROYALBLUE, [player_life_x, player_life_y, player_life_width*player_life_val/player_life_max, player_life_height])

########################
# appearance of enemy
# 敵の出現
########################

def appearance_of_enemy():

    # global variables
    # グローバル変数
    global imgEnemy, enemy_name, enemy_lifemax, enemy_life, enemy_attack_power, enemy_x, enemy_y
    global floor

    # Randomly selected depending on the number of enemies.
    # 敵の数に応じてランダムに選ぶ
    enemy_num = random.randint(0, 2)

    # enemy image
    # 敵の画像
    imgEnemy = pygame.image.load("image/enemy"+str(enemy_num)+".png")

    # Increase the size of enemy images.
    # 敵の画像のサイズを大きくする
    imgEnemy = pygame.transform.scale(imgEnemy, (250, 250))

    # Location coordinates of enemy image
    # 敵の画像の配置座標
    enemy_x = 390-imgEnemy.get_width()/2
    enemy_y = 440-imgEnemy.get_height()

    # enemy name
    # 敵の名前
    enemy_name = ENEMY_NAME[enemy_num]

    # If the hierarchy is 0th floor or higher
    # 階層が0階以上の場合
    if floor >= 0:

        # Maximum enemy life
        # 敵のライフの最大値
        enemy_lifemax = 100 + enemy_num*10 + floor*10

    # If the hierarchy is smaller than floor 0
    # 階層が0階より小さい場合
    if floor < 0:

        # Convert minus to plus.
        # マイナスをプラスに変換する
        floor = -floor

        # Maximum enemy life
        # 敵のライフの最大値
        enemy_lifemax = 100 + enemy_num*10 + floor*10

    # Assigns the enemy's maximum life to the current life.
    # 敵の最大値のライフを現在のライフに代入する
    enemy_life = enemy_lifemax

    # enemy attack power
    # 敵の攻撃力
    enemy_attack_power = int(enemy_lifemax/10)

###############################
# Enemy strength information
# 敵の強さの情報
###############################

def enemy_strength_info(bg, fnt):

    # Defines the color of the enemy's life as white.
    # 敵のライフの色を白として定義する
    enemy_life_color = WHITE

    # Enemy life bar display and placement coordinates
    # 敵のライフバーの表示と配置座標
    draw_text(bg, create_enemy_life_bar(bg, 290, 160, 200, 10, enemy_life, enemy_lifemax), 10, 510, fnt, WHITE)

    # Display and placement coordinates of the enemy's current life and maximum life
    # 敵の現在のライフと最大値のライフの表示と配置座標    
    draw_text(bg, "{}/{}".format(enemy_life, enemy_lifemax), 500, 154, fnt, enemy_life_color)

##########################
# Displaying enemy life
# 敵のライフバー作成
##########################

def create_enemy_life_bar(bg, enemy_life_x, enemy_life_y, enemy_life_width, enemy_life_height, enemy_life_val, enemy_life_max):

    # Create the enemy's life as a rectangle.
    # 敵のライフを四角形として作成する
    pygame.draw.rect(bg, WHITE, [enemy_life_x-2, enemy_life_y-2, enemy_life_width+4, enemy_life_height+4])
    pygame.draw.rect(bg, BLACK, [enemy_life_x, enemy_life_y, enemy_life_width, enemy_life_height])

    # If the enemy's current life is greater than 0
    # 敵の現在のライフが0より大きい場合
    if enemy_life_val > 0:

        # Creates a rectangle according to the enemy's current life (color:MAROON).
        # 敵の現在のライフ（color:MAROON）に応じて、四角形を作成する
        pygame.draw.rect(bg, MAROON, [enemy_life_x, enemy_life_y, enemy_life_width*enemy_life_val/enemy_life_max, enemy_life_height])

###########################
# Displaying enemy level
# 敵のレベル表示
###########################

def display_enemy_level(bg, fnt):

    # global variables
    # グローバル変数
    global floor, floor_max

    # Specify small font
    # 小さいフォント指定
    fontS = pygame.font.Font(None, 30)
   
    # If the hierarchy is 0th floor or higher
    # 階層が0階以上の場合
    if floor >= 0:
        
        # Assign the current level to e_level.
        # 現在いる階層をe_levelに代入する
        e_level = floor

    # If the hierarchy is smaller than floor 0
    # 階層が0階より小さい場合
    if floor < 0:

        # Convert minus to plus.
        # マイナスをプラスに変換する
        floor = -floor

        # Assign the current level to e_level.
        # 現在いる階層をe_levelに代入する
        e_level = floor

    # enemy level
    # 敵のレベル
    enemy_level = "LV" + str(e_level)

    # Enemy level display and location coordinates
    # 敵のレベル表示と配置座標
    draw_text(bg, enemy_level, 250, 155, fnt, WHITE)
   
#################
# battle screen
# 戦闘画面
#################

def battle_screen(bg, fnt):

    # global variables
    # グローバル変数
    global enemy_flash, screen_shaking

    # background x coordinate
    # 背景のx座標
    background_x = 0

    # background y coordinate
    # 背景のy座標
    background_y = 0

    # If the screen shake is greater than 0
    # 画面の揺れが0より大きい場合
    if screen_shaking > 0:

        # Decrease the screen shake value by 1.
        # 画面の揺れの値を1減らす
        screen_shaking = screen_shaking - 1

        # Select one from -20 to 20 and assign it to the x-coordinate of the background.
        # 背景のx座標に-20から20のいずれか選んで代入する
        background_x = random.randint(-20, 20)

        # Select one from -20 to 20 and assign it to the y-coordinate of the background.
        # 背景のy座標に-20から20のいずれか選んで代入する
        background_y = random.randint(-20, 20)

    # Display and placement coordinates of background images for fighting enemies
    # 敵と戦う背景画像の表示と配置座標
    bg.blit(imgBackgroundFightEnemy, [background_x, background_y])

    # If the enemy's life is greater than 0 and the value that flashes when attacking the enemy is divided by 2 and the remainder is 0.
    # 敵のライフが0より大きく、敵を攻撃した時に点滅する値を2で割った余りが0の場合
    if enemy_life > 0 and enemy_flash%2 == 0:
        bg.blit(imgEnemy, [enemy_x, enemy_y + enemy_front])

    # If the blinking value when attacking an enemy is greater than 0
    # 敵を攻撃した時に点滅する値が0より大きい場合
    if enemy_flash > 0:

        # Reduces the blinking value by 1 when attacking an enemy.
        # 敵を攻撃した時に点滅する値を1減らす
        enemy_flash = enemy_flash - 1

    # Battle message display and placement coordinates
    # 戦闘メッセージの表示と配置座標
    for i in range(2):
        draw_text(bg, battle_message[i], 10, 160, fnt, WHITE)

    # Player strength information
    # プレイヤーの強さの情報
    player_strength_info(bg, fnt)

    # Enemy strength information
    # 敵の強さの情報
    enemy_strength_info(bg, fnt)
    
    # Displaying enemy level
    # 敵のレベル表示
    display_enemy_level(bg, fnt)

#############################
# Managing combat commands
# 戦闘コマンドの管理
#############################

def combat_command(bg, fnt, key):
    
    # global variables
    # グローバル変数
    global battle_command

    # Assign False to enter.
    # Falseをenterに代入する
    enter = False

    # If you press a
    # aを押した場合
    if key[K_a]:

        # Set combat command to 0.
        # 戦闘コマンドを0にする
        battle_command = 0
        enter = True

    # If you press r
    # rを押した場合
    if key[K_r]:

        # Set combat command to 1.
        # 戦闘コマンドを1にする
        battle_command = 1
        enter = True

    # If you press e
    # eを押した場合
    if key[K_e]:

        # Set combat command to 2.
        # 戦闘コマンドを2にする
        battle_command = 2
        enter = True

    # If the ↑ key is pressed and the combat command is greater than 0
    # ↑キーを押し、戦闘コマンドが0より大きい場合
    if key[K_UP] and battle_command > 0:

        # Reduce combat commands by 1.
        # 戦闘コマンドを1減らす
        battle_command -= 1
        
    # If the ↓ key is pressed and the combat command is less than 2
    # ↓キーを押し、戦闘コマンドが2より小さい場合
    if key[K_DOWN] and battle_command < 2:

        # Increases combat commands by 1.
        # 戦闘コマンドを1増やす
        battle_command += 1

    # If you press the return key
    # returnキーを押した場合
    if key[K_RETURN]:

        # Assign True to enter.
        # Trueをenterに代入する
        enter = True

    # Combat command color
    # 戦闘コマンドの色
    for i in range(3):

        # Assign white to battle command color.
        # 白色を戦闘コマンドの色に代入する
        battle_command_color = WHITE

        # If the battle command is i
        # 戦闘コマンドがiの場合
        if battle_command == i:

            # Combat command color scheme
            # 戦闘コマンドの配色パターン
            battle_command_color = COLOR_SCHEME8[timer%10]

        # Battle command display and placement coordinates
        # 戦闘コマンドの表示と配置座標
        draw_text(bg, BATTLE_COMMAND[i], 20, 300+i*60, fnt, battle_command_color)
        
    return enter

####################################
# Initializing the battle message
# 戦闘メッセージの初期化
####################################

def init_battle_message():
    for i in range(2):
        battle_message[i] = ""  

######################################
# Function to insert battle message
# 戦闘メッセージを入れる関数
######################################

def insert_battle_message(message):
    if battle_message[0] == "":
        battle_message[0] = message
        return
    
    battle_message[0] = battle_message[1]
    battle_message[0] = message

###########
# Save
# セーブする
###########

def save_data(data, save_file):
    with open(save_file, "wb") as write_file:
        pickle.dump(data, write_file)

############
# Load
# ロードする
############
            
def load_data(save_file):
    with open(save_file, 'rb') as read_file:
        data = pickle.load(read_file)
        return data

################
# main function
# メイン関数
################

def main():

    # global variables
    # グローバル変数
    global speed, change_screen, timer, floor, floor_max, floor_num
    global player_animation
    global password_length
    global player_hand
    global player_lifemax, player_life, player_attack_power
    global recovery_agents
    global enemy_life, enemy_front, enemy_flash, screen_shaking
    global data

    # local variable
    # ローカル変数
    damage = 0
    life_power_up = 0
    strong_power_up = 0

    # Initialize all imported pygame modules
    # インポートした全てのpygameモジュールの初期化
    pygame.init()

    # Setting the window title
    # ウィンドウのタイトルの設定
    pygame.display.set_caption("Role-playing game")

    # Initializing window screens and screen controls
    # ウィンドウ画面とスクリーン制御の初期化
    screen = pygame.display.set_mode((800, 600))

    # Managing time within the program
    # プログラム内の時間の管理
    clock = pygame.time.Clock()

    # Title font specification
    # タイトルのフォント指定            
    fontT = pygame.font.Font(None, 80)

    # Specifying normal font
    # 通常フォントの指定       
    font = pygame.font.Font(None, 40)
    
    # Specify small font
    # 小さいフォント指定
    fontS = pygame.font.Font(None, 30)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                # Close the window.
                # ウィンドウを終了する
                pygame.quit()

                # Terminate the program.
                # プログラムを終了させる
                sys.exit()

        # Obtaining a save/load-only key
        # セーブ・ロード専用のキーの取得
        save_load_key = pygame.key.get_pressed()
        
        # Press s to save the data.
        # sを押すと、データをセーブする
        if save_load_key[pygame.K_s]:
            try:
                save_data(data, 'save_data.pickle')
                
            except:
                
                # セーブできませんでした
                print("Unable to save.")
                
            else:

                # セーブに成功しました
                print("I was able to save.")

        # Press l to read the saved data and start from where you left off.
        # lを押すと、セーブしたデータから読み出して、続きから始める
        if save_load_key[pygame.K_l]:

            # Load from saved data.
            # セーブしたデータから読み込む
            try:
                data = load_data('save_data.pickle')
                
            except:
                
                # ロードできませんでした
                print("Unable to load.")
                
            else:
                
                # ロードに成功しました
                print("It was loaded successfully.")
                
                # Inherit the saved data as is.
                # セーブしたデータをそのまま引き継ぐ
                player_lifemax = data['player_lifemax']
                player_life = data['player_life']
                player_attack_power = data['player_attack_power']
                recovery_agents = data['recovery_agents']

                # Set tmr (screen progress management) to 0.
                # timer（画面の進行の管理）を0にする              
                timer = 0

                # Transition to the start screen.
                # スタート画面に遷移する
                change_screen = 1

        # Add 1 to timer (screen progress management).
        # timer（画面の進行の管理）に1を加算する
        timer = timer + 1

        # Get the entered key
        # 入力されたキーの取得
        key = pygame.key.get_pressed()

        ###############
        # title screen            
        # タイトル画面              
        ###############
        
        if change_screen == 0:
            
            ####################
            # Screen management
            # 画面の管理
            ####################

            # screen color
            # 画面の色              
            screen.fill(AZURE)

            ####################
            # Title screen image
            # タイトル画面の画像
            ####################

            screen.blit(imgTitle, [10, 160])

            #################
            # Title of work
            # 作品のタイトル
            #################
            
            draw_text(screen, "Role-playing game", 150, 60, fontT, BLUE)

            #############################################
            # Text that says transition to start screen
            # スタート画面に遷移するというテキスト
            #############################################
            
            draw_text(screen, "[Press return] start from scratch", 200, 500, font, COLOR_SCHEME1[timer%10])
            draw_text(screen, "[Press l] Start where you left off", 200, 560, font, COLOR_SCHEME1[timer%10])            

            # If the return key is pressed
            # returnキーが押された場合
            if key[K_RETURN] == 1:

                # Set timer (screen progress management) to 0.
                # timer（画面の進行の管理）を0にする
                timer = 0

                # Initial values of player's physical strength and attack power
                # プレイヤーの体力・攻撃力の初期値
                player_lifemax = 100
                player_life = player_lifemax
                player_attack_power = 30

                # Transition to the start screen.
                # スタート画面に遷移する
                change_screen = 1

        ###################################
        # Transition to the start screen. 
        # スタート画面に遷移する              
        ###################################
        
        elif change_screen == 1:
            if 1 <= timer and timer <= 5:
                h = 80*timer
                pygame.draw.rect(screen, BLACK, [0, 0, 800, h])
                pygame.draw.rect(screen, BLACK, [0, 600-h, 800, h])
            if 6 <= timer and timer <= 9:

                # Automatic generation of hierarchies
                # 階層の自動生成
                make_hierarchy()

                # Place objects on the floor.
                # 床にモノを配置する
                put_object()

                # Set the current hierarchy to 0.
                # 現在の階層を0にする
                floor = 0

                # The hierarchy of the player's current position and the end of 2D exploration. 
                # プレイヤーの現在位置の階層と２次元探検の終了                                          
                change_screen = 2

        ################################################################################
        # The hierarchy of the player's current position and the end of 2D exploration. 
        # プレイヤーの現在位置の階層と２次元探検の終了                          
        ################################################################################
        
        elif change_screen == 2:
            move_player(key)
            draw_hierarchy(screen, fontS)
            draw_text(screen, "[Press s] Save", 600, 530, fontS, COLOR_SCHEME2[timer%10])
            draw_text(screen, "[Press delete] Exit", 600, 566, fontS, COLOR_SCHEME2[timer%10])

            # For floors above 1st floor
            # 1階以上の場合
            if floor > 0:
                
                # Displaying the current hierarchy
                # 現在の階層の表示
                draw_text(screen, "floor {}".format(floor), 350, 560, font, WHITE)

            # If it is on the ground
            # 地上の場合
            elif floor == 0:
                
                # Displaying the current hierarchy
                # 現在の階層の表示
                draw_text(screen, "above-ground", 320, 560, font, WHITE)

            # If you are underground
            # 地下の場合
            elif floor < 0:
                
                # Displaying the current hierarchy
                # 現在の階層の表示
                draw_text(screen, "underground {}".format(-floor), 320, 560, font, WHITE)                
                
            # Click the delete key to exit.
            # deleteキーをクリックすると、終了する
            if key[K_DELETE] == 1:
                timer = 0

                # Transition to the title screen. 
                # タイトル画面に遷移する              
                change_screen = 3
                
        ###################################
        # Transition to the title screen. 
        # タイトル画面に遷移する              
        ###################################
        
        elif change_screen == 3:
            if 1 <= timer and timer <= 5:
                h = 80*timer
                pygame.draw.rect(screen, BLACK, [0, 0, 800, h])
                pygame.draw.rect(screen, BLACK, [0, 600-h, 800, h])
            if 6 <= timer and timer <= 9:

                # title screen            
                # タイトル画面              
                change_screen = 0

        ##################################
        # Return to the original screen.
        # 元の画面に戻る                   
        ##################################
        
        elif change_screen == 4:
            if 1 <= timer and timer <= 5:
                h = 80*timer
                pygame.draw.rect(screen, BLACK, [0, 0, h, 600])
                pygame.draw.rect(screen, BLACK, [800-h, 0, h, 600])
            if 6 <= timer and timer <= 9:

                # The hierarchy of the player's current position and the end of 2D exploration. 
                # プレイヤーの現在位置の階層と２次元探検の終了                          
                change_screen = 2

        ##############################################
        # Switching the screen of the stairs going up
        # 上る階段の画面切り替え                          
        ##############################################
        
        elif change_screen == 5:
            
            # Draw the hierarchy.
            # 階層を描画する
            draw_hierarchy(screen, fontS)
            
            if 1 <= timer and timer <= 5:
                h = 80*timer
                pygame.draw.rect(screen, BLACK, [0, 0, 800, h])
                pygame.draw.rect(screen, BLACK, [0, 600-h, 800, h])
            if timer == 5:

                # Add 1 to the current hierarchy.
                # 現在の階層に1を加算する
                floor = floor + 1

                # If the current tier is greater than the maximum tier
                # 現在の階層が階層の最大値より大きい場合
                if floor > floor_max:

                    # Assigns the current hierarchy to the maximum value of the hierarchy.
                    # 現在の階層を階層の最大値に代入する
                    floor_max = floor

                # Automatic generation of hierarchies
                # 階層の自動生成
                make_hierarchy()

                # Place objects on the floor.
                # 床にモノを配置する
                put_object()
                
            if 6 <= timer and timer <= 9:
                h = 80*(11-timer)
                pygame.draw.rect(screen, BLACK, [0, 0, 800, h])
                pygame.draw.rect(screen, BLACK, [0, 600-h, 800, h])
            if timer == 10:

                # The hierarchy of the player's current position and the end of 2D exploration. 
                # プレイヤーの現在位置の階層と２次元探検の終了                          
                change_screen = 2

        ########################################
        # Switch screen for descending stairs
        # 下り階段の画面切り替え
        ########################################
        
        elif change_screen == 6:

            # Draw the hierarchy.
            # 階層を描画する
            draw_hierarchy(screen, fontS)
            
            if 1 <= timer and timer <= 5:
                h = 80*timer
                pygame.draw.rect(screen, BLACK, [0, 0, 800, h])
                pygame.draw.rect(screen, BLACK, [0, 600-h, 800, h])
            if timer == 5:

                # Subtract 1 from the current level.
                # 現在の階層から1を減算する
                floor = floor - 1

                # If the current tier is greater than the maximum tier
                # 現在の階層が階層の最大値より大きい場合
                if floor > floor_max:

                    # Assigns the current hierarchy to the maximum value of the hierarchy.
                    # 現在の階層を階層の最大値に代入する
                    floor_max = floor

                # Automatic generation of hierarchies
                # 階層の自動生成
                make_hierarchy()

                # Place objects on the ground.
                # 地面にモノを配置する
                put_object()
                
            if 6 <= timer and timer <= 9:
                h = 80*(11-timer)
                pygame.draw.rect(screen, BLACK, [0, 0, 800, h])
                pygame.draw.rect(screen, BLACK, [0, 600-h, 800, h])
            if timer == 10:

                # The hierarchy of the player's current position and the end of 2D exploration. 
                # プレイヤーの現在位置の階層と２次元探検の終了                          
                change_screen = 2

        #############################
        # Internet screen switching
        # インターネットの画面切り替え
        #############################
        
        elif change_screen == 7: 
            if 1 <= timer and timer <= 5:
                h = 80*timer
                pygame.draw.rect(screen, BLACK, [0, 0, h, 600])
                pygame.draw.rect(screen, BLACK, [800-h, 0, h, 600])
            if timer > 5:
                
                # Internet screen switching
                # インターネットの画面切り替え
                internet(screen, key)
                
                # Click the space key to return to the original screen.
                # spaceキーをクリックすると、元の画面に戻る
                if key[K_SPACE] == 1:
                    timer = 0
                    change_screen = 4
                    
        ##########################################
        # Fortune telling hall screen switching
        # 占いの館の画面切り替え
        ##########################################
        
        elif change_screen == 8:
            if 1 <= timer and timer <= 5:
                h = 80*timer
                pygame.draw.rect(screen, BLACK, [0, 0, h, 600])
                pygame.draw.rect(screen, BLACK, [800-h, 0, h, 600])
            if timer > 5:

                # Fortune telling hall screen switching
                # 占いの館の画面切り替え
                fortune_display(screen)
                
                # Click the space key to return to the original screen.
                # spaceキーをクリックすると、元の画面に戻る
                if key[K_SPACE] == 1:
                    timer = 0
                    change_screen = 4
                    
                # If you draw a fortune
                # おみくじを引いた場合
                if key[K_d] == 1:
                    timer = 0
                    change_screen = 9

        ##############################################
        # Screen switching of fortune telling results
        # 占い結果の画面切り替え
        ##############################################
        
        elif change_screen == 9:
            if 1 <= timer and timer <= 5:
                h = 80*timer
                pygame.draw.rect(screen, BLACK, [0, 0, h, 600])
                pygame.draw.rect(screen, BLACK, [800-h, 0, h, 600])
            if timer == 5:
                fortune()
                fortune_result(screen)
            if timer >= 6:
                draw_text(screen, "[Press space] Leave the fortune-telling hall", 120, 560, font, COLOR_SCHEME4[timer%10])
                
                # Click the space key to return to the original screen.
                # spaceキーをクリックすると、元の画面に戻る
                if key[K_SPACE] == 1:
                    timer = 0
                    change_screen = 4

        ##############################################
        # Switch to password generation tool screen
        # パスワード生成ツール画面に切り替え
        ##############################################
        
        elif change_screen == 10:
            if 1 <= timer and timer <= 5:
                h = 80*timer
                pygame.draw.rect(screen, BLACK, [0, 0, h, 600])
                pygame.draw.rect(screen, BLACK, [800-h, 0, h, 600])
            if timer > 5:
                
                # Switch to password generation tool screen
                # パスワード生成ツール画面に切り替え
                password_generation_tool_display(screen)

                # Click the space key to return to the original screen.
                # spaceキーをクリックすると、元の画面に戻る
                if key[K_SPACE] == 1:
                    timer = 0
                    change_screen = 4

                # Password generation result （10 characters)
                # パスワード生成結果（10文字）
                elif key[K_q] == 1:
                    timer = 0
                    password_length = 10
                    change_screen = 11

                # Password generation result （11 characters)
                # パスワード生成結果（11文字）                
                elif key[K_w] == 1:
                    timer = 0
                    password_length = 11
                    change_screen = 11

                # Password generation result （12 characters)
                # パスワード生成結果（12文字）
                elif key[K_e] == 1:
                    timer = 0
                    password_length = 12
                    change_screen = 11

                # Password generation result （13 characters)
                # パスワード生成結果（13文字）
                elif key[K_r] == 1:
                    timer = 0
                    password_length = 13
                    change_screen = 11

                # Password generation result （14 characters)
                # パスワード生成結果（14文字）
                elif key[K_t] == 1:
                    timer = 0
                    password_length = 14
                    change_screen = 11

                # Password generation result （15 characters)
                # パスワード生成結果（15文字）
                elif key[K_y] == 1:
                    timer = 0
                    password_length = 15
                    change_screen = 11

                # Password generation result （16 characters)
                # パスワード生成結果（16文字）
                elif key[K_u] == 1:
                    timer = 0
                    password_length = 16
                    change_screen = 11

                # Password generation result （17 characters)
                # パスワード生成結果（17文字）
                elif key[K_i] == 1:
                    timer = 0
                    password_length = 17
                    change_screen = 11

                # Password generation result （18 characters)
                # パスワード生成結果（18文字）
                elif key[K_o] == 1:
                    timer = 0
                    password_length = 18
                    change_screen = 11

                # Password generation result （19 characters)
                # パスワード生成結果（19文字）
                elif key[K_p] == 1:
                    timer = 0
                    password_length = 19
                    change_screen = 11

                # Password generation result （20 characters)
                # パスワード生成結果（20文字）
                elif key[K_a] == 1:
                    timer = 0
                    password_length = 20
                    change_screen = 11

        ###################################################################
        # Screen switching of password generation results (10 characters)
        # パスワード生成結果の画面切り替え
        ###################################################################
        
        elif change_screen == 11:
            if 1 <= timer and timer <= 5:
                h = 80*timer
                pygame.draw.rect(screen, BLACK, [0, 0, h, 600])
                pygame.draw.rect(screen, BLACK, [800-h, 0, h, 600])
            if timer == 5:
                password_result(screen)
            if timer >= 6:
                draw_text(screen, "[Press space] Leave the password generation results", 50, 560, font, COLOR_SCHEME5[timer%10])
                
                # Click the space key to return to the original screen.
                # spaceキーをクリックすると、元の画面に戻る
                if key[K_SPACE] == 1:
                    timer = 0
                    change_screen = 4

        ################################################
        # Rock, paper, scissors game screen switching
        # じゃんけんゲームの画面切り替え
        ################################################
        
        elif change_screen == 12:
            if 1 <= timer and timer <= 5:
                h = 80*timer
                pygame.draw.rect(screen, BLACK, [0, 0, h, 600])
                pygame.draw.rect(screen, BLACK, [800-h, 0, h, 600])
            if timer > 5:
                janken_start_display(screen)

                # Click the space key to return to the original screen.
                # spaceキーをクリックすると、元の画面に戻る
                if key[K_SPACE] == 1:
                    timer = 0
                    change_screen = 4

                # If the player's rock-paper-scissors playing rock
                # プレイヤーのじゃんけんがグーを出した場合
                elif key[K_0] == 1:
                    timer = 0
                    player_hand = 0
                    change_screen = 13
                    
                # If the player's rock-paper-scissors playing paper
                # プレイヤーのじゃんけんがパーを出した場合
                elif key[K_1] == 1:
                    timer = 0
                    player_hand = 1
                    change_screen = 13

                # If the player's rock-paper-scissors playing scissors
                # プレイヤーのじゃんけんがチョキを出した場合
                elif key[K_2] == 1:
                    timer = 0
                    player_hand = 2
                    change_screen = 13

        ##############################################################
        # Switching the screen of rock, paper, scissors game results
        # じゃんけんゲーム結果の画面切り替え
        ##############################################################
        
        elif change_screen == 13:
            if 1 <= timer and timer <= 5:
                h = 80*timer
                pygame.draw.rect(screen, BLACK, [0, 0, h, 600])
                pygame.draw.rect(screen, BLACK, [800-h, 0, h, 600])
            if timer == 5:
                janken_result(screen)
            if timer >= 6:
                draw_text(screen, "[Press space] Leave the rock, paper, scissors game results", 10, 560, font, COLOR_SCHEME6[timer%10])

            # Click the space key to return to the original screen.
            # spaceキーをクリックすると、元の画面に戻る
            if key[K_SPACE] == 1:
                timer = 0
                change_screen = 4

        ########################################
        # Switching the screen of random color
        # ランダムな色の画面切り替え
        ########################################
        
        elif change_screen == 14:
            if 1 <= timer and timer <= 5:
                h = 80*timer
                pygame.draw.rect(screen, BLACK, [0, 0, h, 600])
                pygame.draw.rect(screen, BLACK, [800-h, 0, h, 600])
            if timer >= 5:
                random_color(screen)
                draw_text(screen, "[Press space] Leave the random color", 150, 560, font, COLOR_SCHEME7[timer%10])

                # Click the space key to return to the original screen.
                # spaceキーをクリックすると、元の画面に戻る
                if key[K_SPACE] == 1:
                    timer = 0
                    change_screen = 4

        #################################
        # Switching the screen of memo
        # メモの画面切り替え
        #################################
        
        elif change_screen == 15:
            if 1 <= timer and timer <= 5:
                h = 80*timer
                pygame.draw.rect(screen, BLACK, [0, 0, h, 600])
                pygame.draw.rect(screen, BLACK, [800-h, 0, h, 600])
            if timer >= 5:
                memo(screen)

                # Set the timer to 0 and return to the original screen.
                # timerを0にして、元の画面に戻る
                timer = 0
                change_screen = 4

        ###############################
        # Switching the screen of BMI
        # BMIの画面切り替え
        ###############################
        
        elif change_screen == 16:
            if 1 <= timer and timer <= 5:
                h = 80*timer
                pygame.draw.rect(screen, BLACK, [0, 0, h, 600])
                pygame.draw.rect(screen, BLACK, [800-h, 0, h, 600])
            if timer >= 5:
                bmi(screen)
                
                # Set the timer to 0 and next to the original screen.
                # timerを0にして、元の画面に戻る
                timer = 0
                change_screen = 4

        ######################################
        # Switching the battle start screen
        # 戦闘開始画面の切り替え
        ######################################
        
        elif change_screen == 17:
            if timer == 1:

                # appearance of enemy
                # 敵の出現
                appearance_of_enemy()

                # Initializing the battle message
                # 戦闘メッセージの初期化
                init_battle_message()
                
            elif timer <= 5:
                background_x = (5-timer)*200
                background_y = (timer-5)*200

                # Use the image from the battle start screen.
                # 戦闘開始用画面の画像を使用する
                screen.blit(imgBackgroundFightEnemy, [background_x, background_y])
                
            elif timer <= 20:
                battle_screen(screen, fontS)

                # An enemy will appear.
                # 敵が出現する
                draw_text(screen, enemy_name+" appear!", 270, 100, font, WHITE)
            else:
                
                # Set timer to 0.
                # timerを0にする。
                timer = 0

                # player's turn
                # プレイヤーの番                
                change_screen = 18

        ##################
        # player's turn
        # プレイヤーの番
        ##################
        
        elif change_screen == 18:

            # Switching battle screen
            # 戦闘画面の切り替え
            battle_screen(screen, fontS)
            
            if timer == 1:
                
                # It's the player's turn
                # プレイヤーの番です
                insert_battle_message("You turn")
                
            if combat_command(screen, font, key) == True:
                
                # If battle_command is 0
                # battle_commandが0の場合
                if battle_command == 0:
                    
                    # Set timer to 0.
                    # timerを0にする。
                    timer = 0

                    # player's attack
                    # プレイヤーの攻撃
                    change_screen = 19
                    
                # If battle_command is 1
                # battle_commandが1の場合
                if battle_command == 1 and recovery_agents > 0:
                    
                    # Set timer to 0.
                    # timerを0にする。
                    timer = 0

                    # Use of recovery medicine
                    # 回復薬の利用
                    change_screen = 26

                # If battle_command is 2
                # battle_commandが2の場合
                if battle_command == 2:

                    # Set timer to 0.
                    # timerを0にする。
                    timer = 0

                    # Can the player escape?
                    # プレイヤーが逃げられるかどうか
                    change_screen = 21

        ####################
        # player's attack
        # プレイヤーの攻撃
        ####################
        
        elif change_screen == 19:
            
            # Switching battle screen
            # 戦闘画面の切り替え
            battle_screen(screen, fontS)
            
            if timer == 1:
                
                # attack the enemy.
                # 敵に攻撃する
                insert_battle_message("You attack!")
                
                # Damage is the result of adding the player's attack power and a random number from 0 to 9.
                # プレイヤーの攻撃力と０から９までの乱数を足し合わせた結果がダメージとなる
                damage = player_attack_power + random.randint(0, 9)
                
            if 2 <= timer and timer <= 4:
                
                # Use the image of the enemy taking damage to create a performance.
                # 敵がダメージを受けた時の画像を利用して、演出する
                screen.blit(imgEffect, [800-timer*100, -100+timer*100])
                
            if timer == 5:

                # Set blinking to 5 when enemy is attacked.
                # 敵が攻撃を受けた時の点滅を５にする
                enemy_flash = 5
                
                # Enemies take some damage.
                # 敵がいくつかのダメージを受ける
                insert_battle_message(str(damage)+" damage!")
                
            if timer == 11:
                
                # Subtract the damage taken from the enemy's current life.
                # 敵の現在のライフから受けたダメージを引く
                enemy_life = enemy_life - damage
                
                # If the enemy's life becomes 0 or less
                # 敵のライフが０以下になった場合
                if enemy_life <= 0:

                    # Reduce the enemy's life to 0.
                    # 敵のライフを0にする
                    enemy_life = 0
                    
                    # Set timer to 0.
                    # timerを0にする。
                    timer = 0

                    # player victory
                    # プレイヤーの勝利
                    change_screen = 24

            if timer == 16:
                
                # Set timer to 0.
                # timerを0にする。
                timer = 0

                # Enemy's turn, enemy's attack
                # 敵の番、敵の攻撃
                change_screen = 20
                
        ################################
        # Enemy's turn, enemy's attack
        # 敵の番、敵の攻撃
        ################################
        
        elif change_screen == 20:

            # Switching battle screen
            # 戦闘画面の切り替え
            battle_screen(screen, fontS)
            
            if timer == 1:

                # Enemy's turn
                # 敵の番
                insert_battle_message("Enemy turn.")
                
            if timer == 5:
                
                # An enemy attacks the player.
                # 敵がプレイヤーに攻撃する
                insert_battle_message(enemy_name + " attack!")

                # Set the value to move the enemy forward to 30.
                # 敵を前方に移動する値を30にする
                enemy_front = 30
                
            if timer == 10:
                
                # Damage is the result of adding the enemy's attack power and a random number from 0 to 10.
                # 敵の攻撃力と0から10までの乱数を足し合わせた結果がダメージとなる
                damage = enemy_attack_power + random.randint(0, 10)

                # Player takes some damage.
                # プレイヤーがいくつかのダメージを受ける
                insert_battle_message(str(damage)+" damage!")

                # Set the screen shaking value to 5.
                # 画面を揺らす値を5にする
                screen_shaking = 5

                # Set the value that moves the enemy forward to 0.
                # 敵を前方にする値を0にする
                enemy_front = 0
                
            if timer == 15:

                # Subtract the damage taken from the player's current life.
                # プレイヤーの現在のライフから受けたダメージを引く
                player_life = player_life - damage

                # If the player's life becomes 0 or less
                # プレイヤーのライフが0以下になった場合
                if player_life <= 0:

                    # Reduce the player's life to 0.
                    # プレイヤーのライフを0にする
                    player_life = 0

                    # Set timer to 0.
                    # timerを0にする。
                    timer = 0
                    
                    # player's loss
                    # プレイヤーの敗北
                    change_screen = 22
                    
            if timer == 20:
                
                # Set timer to 0.
                # timerを0にする。                
                timer = 0

                # player's turn
                # プレイヤーの番      
                change_screen = 18
                
        ###########################
        # Can the player escape?
        # プレイヤーが逃げられるかどうか
        ###########################

        elif change_screen == 21:

            # Switching battle screen
            # 戦闘画面の切り替え
            battle_screen(screen, fontS)
            
            if timer == 1:
                insert_battle_message("Y")
            if timer == 2:
                insert_battle_message("Yo")
            if timer == 3:
                insert_battle_message("You")
            if timer == 4:
                insert_battle_message("You ")
            if timer == 5:
                insert_battle_message("You c")
            if timer == 6:
                insert_battle_message("You ca")
            if timer == 7:
                insert_battle_message("You can")
            if timer == 8:
                insert_battle_message("You can ")
            if timer == 9:
                insert_battle_message("You can  e")
            if timer == 10:
                insert_battle_message("You can  es")
            if timer == 11:
                insert_battle_message("You can  esc")
            if timer == 12:
                insert_battle_message("You can  esca")
            if timer == 13:
                insert_battle_message("You can  escap")
            if timer == 14:
                insert_battle_message("You can  escape")
            if timer == 15:
                insert_battle_message("You can  escape.")
            if timer == 16:

                # If the number is less than 40, you can escape.
                # 40より小さい数字の場合、逃げられる
                if random.randint(0, 99) < 40:
                    
                    # Battle ends
                    # 戦闘終了
                    change_screen = 27
                    
                else:
                    
                    # あなたは逃げられません
                    insert_battle_message("You can't escape.")
                    
            if timer == 22:
                
                # Set timer to 0.
                # timerを0にする。              
                timer = 0

                # Enemy's turn, enemy's attack
                # 敵の番、敵の攻撃
                change_screen = 20
                
        #################
        # player's loss
        # プレイヤーの敗北
        #################
             
        elif change_screen == 22:

            # Switching battle screen
            # 戦闘画面の切り替え
            battle_screen(screen, fontS)
            
            if timer == 1:
                
                # あなたの負けです
                insert_battle_message("You lose.")
                
            if timer == 11:

                # Set timer to 29.
                # timerを29にする。
                timer = 29
                
                # game over
                # ゲームオーバー
                change_screen = 23

        ###############
        # game over
        # ゲームオーバー
        ###############
        
        elif change_screen == 23:
            
            if timer <= 30:

                # Let the list of player turns be 2,4,0,6.
                # プレイヤーのターンのリストを2,4,0,6とする
                PLAYER_TURN = [2, 4, 0, 6]

                # Assign the remainder of the timer value below 30 divided by 4 to the player's animation.
                # 30以下のtimerの値を4で割った余りをプレイヤーのアニメーションに代入する
                player_animation = PLAYER_TURN[timer%4]
                
                if timer == 30:
                    
                    # Animation that disappoints the player
                    # プレイヤーが落胆するアニメーション
                    player_animation = 8
                
                # Draw the hierarchy.
                # 階層を描画する
                draw_hierarchy(screen, fontS)
                
            elif timer == 31:
                
                # ゲームオーバー
                draw_text(screen, "Game over.", 360, 240, font, RED)
                
            elif timer == 50:
                
                # Set the timer to 0 and next to the original screen.
                # timerを0にして、元の画面に戻る
                timer = 0               
                change_screen = 4

        ###################
        # player victory
        # プレイヤーの勝利
        ###################

        elif change_screen == 24:

            # Switching battle screen
            # 戦闘画面の切り替え
            battle_screen(screen, fontS)
            
            if timer == 1:
                
                # あなたの勝ちです
                insert_battle_message("You win!")
                
            if timer == 30:

                # Battle ends
                # 戦闘終了
                change_screen = 27

                # If the enemy's maximum life is greater than the player's maximum life
                # 敵のライフの最大値がプレイヤーのライフの最大値より大きい場合
                if random.randint(0, enemy_lifemax) > random.randint(0, player_lifemax):
                    
                    # Set timer to 0.
                    # timerを0にする。
                    timer = 0

                    # Level up your player
                    # プレイヤーのレベルアップ
                    change_screen = 25

        #######################
        # Level up your player
        # プレイヤーのレベルアップ
        #######################

        elif change_screen == 25:

            # Switching battle screen
            # 戦闘画面の切り替え
            battle_screen(screen, fontS)
            
            if timer == 1:
                
                # player power up
                # プレイヤーのパワーアップ
                insert_battle_message("Power up!")

                # Assign a random number between 10 and 20 to the player's life up value.
                # 10から20までの乱数をプレイヤーのライフアップの値に代入する
                life_power_up = random.randint(10, 20)

                # Assign a random number from 5 to 10 to the player's attack power increase value.
                # 5から10までの乱数をプレイヤーの攻撃力アップの値に代入する
                strong_power_up = random.randint(5, 10)
                
            if timer == 20:
                
                # Player's life up
                # プレイヤーのライフアップ
                insert_battle_message("Life-up + "+str(life_power_up))

                # The player's current maximum life value and the increased life value are added together to determine the player's latest maximum life value.
                # プレイヤーのライフの現在の最大値とライフアップした値を加算した結果がプレイヤーのライフの最新の最大値となる
                player_lifemax = player_lifemax + life_power_up
                
            if timer == 35:
                
                # Increases player's attack power
                # プレイヤーの攻撃力アップ
                insert_battle_message("Attack Power up + "+str(strong_power_up))

                # The player's latest attack power value is the result of adding the player's current attack power value and the increased attack power value.
                # プレイヤーの現在の攻撃力の値と攻撃力アップした値を加算した結果がプレイヤーの最新の攻撃力の値となる
                player_attack_power = player_attack_power + strong_power_up
                
            if timer == 50:
                
                # Battle ends
                # 戦闘終了
                change_screen = 27

        ###########################
        # Use of recovery medicine
        # 回復薬の利用
        ###########################

        elif change_screen == 26:

            # Switching battle screen
            # 戦闘画面の切り替え
            battle_screen(screen, fontS)
            
            if timer == 1:
                
                # A player uses a healing potion.
                # プレイヤーが回復薬を利用する
                insert_battle_message("Recovery!")
                
            if timer == 5:
                
                # Assigns the player's maximum life value to the current life value.
                # プレイヤーのライフの最大値を現在のライフの値に代入する
                player_life = player_lifemax
                
                # Reduces recovery potion by 1.
                # 回復薬を1つ減らす
                recovery_agents = recovery_agents - 1
                
            if timer == 10:

                # Set timer to 0.
                # timerを0にする。
                timer = 0

                # Enemy's turn, enemy's attack
                # 敵の番、敵の攻撃
                change_screen = 20
                            
        ###############
        # Battle ends
        # 戦闘終了
        ###############

        elif change_screen == 27:
            
            # Set the timer to 0 and next to the original screen.
            # timerを0にして、元の画面に戻る
            timer = 0          
            change_screen = 4              

        #####################
        # Data to save
        # セーブするためのデータ
        #####################

        data['player_lifemax'] = player_lifemax
        data['player_life'] = player_life
        data['player_attack_power'] = player_attack_power
        data['recovery_agents'] = recovery_agents
        
        # Update part of the screen.
        # 画面の一部を更新する
        pygame.display.update()

        # Updates 5*speed frames every second.
        # １秒ごとに5*speedフレーム更新する
        clock.tick(5*speed)

# If the file is executed as a script, execute it.
# ファイルがスクリプトとして実行される場合、実行する。            
if __name__ == '__main__':
    main()
