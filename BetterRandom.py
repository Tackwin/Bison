# -*- coding: utf-8 -*-

import time
import Reversi
from random import randint
from playerInterface import *

class myPlayer(PlayerInterface):

	def __init__(self):
		self._board = Reversi.Board(10)
		self._mycolor = None

	def getPlayerName(self):
		return "Random Player"

	def getPlayerMove(self):
		assert(not self._board.is_game_over())
		moves = [m for m in self._board.legal_moves()]
		move = moves[randint(0,len(moves)-1)]
		self._board.push(move)
		(c,x,y) = move
		assert(c==self._mycolor)
		return (x,y) 

	def playOpponentMove(self, x,y):
		assert(self._board.is_valid_move(self._opponent, x, y))
		self._board.push([self._opponent, x, y])

	def newGame(self, color):
		self._board = Reversi.Board(10)
		self._mycolor = color
		self._opponent = 1 if color == 2 else 2

	def endGame(self, winner):
		self._ended = True




