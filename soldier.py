import pygame

import Screen

SOLDIER_IMG = pygame.image.load('soldier.png')
NIGHT_SOLDIER_IMG = pygame.image.load('soldier_nigth.png')
SOLDIER_MIDBOTTOM_X = 0
SOLDIER_MIDBOTTOM_Y = 0
NIGHT_SOLDIER_MIDBOTTOM_X =0
NIGHT_SOLDIER_MIDBOTTOM_Y =0
flag_lst=[[(21,46),(21,47),(21,48),(21,49)],[(22,46),(22,47),(22,48),(22,49)],[(23,46),(23,47),(23,48),(23,49)]]
def body_lst(x_s,y_s):
    lst=[]
    for i in range(0,3):
        lst.append([])
        lst[i].append((y_s//25, x_s//25+i))
        lst[i].append((y_s//25+1, x_s//25+i))
    return lst
def legs_lst(x_s,y_s):
    lst=[]
    for i in range(3,4):
        lst.append((x_s//25, y_s//25+i))
        lst.append((x_s//25+1, y_s//25+i))
    return lst
def touch_flag(body,flag):
    for i in range(len(body)):
        for j in range(len(body[i])):
            if body[i][j] in flag[i]:
                return True
    return False
def mine_extension():
    mine=Screen.MINE_POSITIONS
    mine_lst=[]
    for i in range (20):
        mine_lst.append([])
        mine_lst[i].append((mine[i][0]//25,mine[i][1]//25-1))
        mine_lst[i].append((mine[i][0]//25, mine[i][1]//25))
        mine_lst[i].append((mine[i][0]//25, mine[i][1]//25 + 1))
    return mine_lst
def touch_mine(legs,mine):

    for i in mine:
        for j in range(3):
            now=i[j]
            leg1=legs[0]
            leg2=legs[1]
            if i[j] == legs[0] or i[j] == legs[1] :
                return True
    return False
