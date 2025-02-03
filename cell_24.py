#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class board:
  status = ""

def initialize(Array_board):
  for x in range(0,8,1):
    for y in range(0,8,1):
      if y == 0 or y == 1:
        Array_board[x][y].status = "B"
      elif y == 6 or y == 7:
        Array_board[x][y].status = "W"
      else:
        Array_board[x][y].status = "E"

def possible_moves(PC, xc, yc):
  if PC == "W":
    print("Possible Moves to Left")
    for i in range(xc,-1,-1):
      if Array_board[i][yc].status == "E":
        print(str(i) + " " + str(yc))
      if Array_board[i][yc].status == "B":
        print(str(i) + " " + str(yc) + "Remove piece")
        break
      if Array_board[i][yc].status == "W":
        break
    print("Possible Movies to Right")
    for i in range(xc,8,1):
      if Array_board[i][yc].status == "E":
        print(str(i) + " " + str(yc))
      if Array_board[i][yc].status == "B":
        print(str(i) + " " + str(yc) + "Remove piece")
        break
      if Array_board[i][yc].status == "W":
        break
  elif PC == "B":
    print("Possible Moves to Left")
    for i in range(xc,-1,-1):
      if Array_board[i][yc].status == "E":
        print(str(i) + " " + str(yc))
      if Array_board[i][yc].status == "W":
        print(str(i) + " " + str(yc) + "Remove piece")
        break
      if Array_board[i][yc].status == "B":
        break
    print("Possbile Moves to Right")
    for i in range(xc,8,1):
      if Array_board[i][yc].status == "E":
        print(str(i) + " " + str(yc))
      if Array_board[i][yc].status == "W":
        print(str(i) + " " + str(yc) + "Remove piece")
        break
      if Array_board[i][yc].status == "B":
        break


Array_board = []
for i in range(0,8,1):
  column = []
  for x in range(0,8,1):
    column.append(board())
  Array_board.append(column)

initialize(Array_board)

Piece_color = "B" # random practice value
xCurrent = 2
yCurrent = 1

possible_moves(Piece_color,xCurrent,yCurrent)

