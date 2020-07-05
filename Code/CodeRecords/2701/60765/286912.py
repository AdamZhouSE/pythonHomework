#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys
import re
import collections


def solve():
    def isWin(pieces):
        if board[0][0]==board[1][1]==board[2][2]==pieces\
                or board[0][2]==board[1][1]==board[2][0]==pieces \
                or board[0][0] == board[0][1] == board[0][2] == pieces \
                or board[1][0] == board[1][1] == board[1][2] == pieces \
                or board[2][0] == board[2][1] == board[2][2] == pieces \
                or board[0][0] == board[1][0] == board[2][0] == pieces \
                or board[0][1] == board[1][1] == board[2][1] == pieces \
                or board[0][2] == board[1][2] == board[2][2] == pieces\
                :
            print(pieces)
            return True

    # =list(map(int,input().split()))
    # =int(input())

    # n =input()[2:-2].split('],[')
    # target=int(input())
    n = input()[2:-2].split('],[')
    moves = [list(map(int, s.split(','))) for s in n]

    board=[['','',''],['','',''],['','','']]
    for step in range(len(moves)):
        x,y=moves[step]
        if step%2==0:
            board[x][y]='A'
            if isWin('A'):
                return
        else:
            board[x][y] = 'B'
            if isWin('B'):
                return
    if len(moves)==9:
        print('Draw')
    else:
        print('Pending')


solve()