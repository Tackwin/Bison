# -*- coding: utf-8 -*-

import time
import Reversi
import math
from random import randint
from playerInterface import *
class Link:
	def __init__(self, i, o, w):
		self.i = i
		self.o = o
		self.w = w

class Node:
	def __init__(self, i, sensor):
		self._in = []
		self._out = []
		self._id = i
		self._sum = 0
		self.activation = 0
		self.sensor = sensor
		self.activated = False

	def add_in(self, l):
		self._in.append(l)
	def add_out(self, l):
		self._out.append(l)

	def set_to(self, x):
		self._sum = x

nodes = {}
nodes[1] = Node(1,True)
nodes[2] = Node(2,True)
nodes[3] = Node(3,True)
nodes[4] = Node(4,True)
nodes[5] = Node(5,True)
nodes[6] = Node(6,True)
nodes[7] = Node(7,True)
nodes[8] = Node(8,True)
nodes[9] = Node(9,True)
nodes[10] = Node(10,True)
nodes[11] = Node(11,True)
nodes[12] = Node(12,True)
nodes[13] = Node(13,True)
nodes[14] = Node(14,True)
nodes[15] = Node(15,True)
nodes[16] = Node(16,True)
nodes[17] = Node(17,True)
nodes[18] = Node(18,True)
nodes[19] = Node(19,True)
nodes[20] = Node(20,True)
nodes[21] = Node(21,True)
nodes[22] = Node(22,True)
nodes[23] = Node(23,True)
nodes[24] = Node(24,True)
nodes[25] = Node(25,True)
nodes[26] = Node(26,True)
nodes[27] = Node(27,True)
nodes[28] = Node(28,True)
nodes[29] = Node(29,True)
nodes[30] = Node(30,True)
nodes[31] = Node(31,True)
nodes[32] = Node(32,True)
nodes[33] = Node(33,True)
nodes[34] = Node(34,True)
nodes[35] = Node(35,True)
nodes[36] = Node(36,True)
nodes[37] = Node(37,True)
nodes[38] = Node(38,True)
nodes[39] = Node(39,True)
nodes[40] = Node(40,True)
nodes[41] = Node(41,True)
nodes[42] = Node(42,True)
nodes[43] = Node(43,True)
nodes[44] = Node(44,True)
nodes[45] = Node(45,True)
nodes[46] = Node(46,True)
nodes[47] = Node(47,True)
nodes[48] = Node(48,True)
nodes[49] = Node(49,True)
nodes[50] = Node(50,True)
nodes[51] = Node(51,True)
nodes[52] = Node(52,True)
nodes[53] = Node(53,True)
nodes[54] = Node(54,True)
nodes[55] = Node(55,True)
nodes[56] = Node(56,True)
nodes[57] = Node(57,True)
nodes[58] = Node(58,True)
nodes[59] = Node(59,True)
nodes[60] = Node(60,True)
nodes[61] = Node(61,True)
nodes[62] = Node(62,True)
nodes[63] = Node(63,True)
nodes[64] = Node(64,True)
nodes[65] = Node(65,True)
nodes[66] = Node(66,True)
nodes[67] = Node(67,True)
nodes[68] = Node(68,True)
nodes[69] = Node(69,True)
nodes[70] = Node(70,True)
nodes[71] = Node(71,True)
nodes[72] = Node(72,True)
nodes[73] = Node(73,True)
nodes[74] = Node(74,True)
nodes[75] = Node(75,True)
nodes[76] = Node(76,True)
nodes[77] = Node(77,True)
nodes[78] = Node(78,True)
nodes[79] = Node(79,True)
nodes[80] = Node(80,True)
nodes[81] = Node(81,True)
nodes[82] = Node(82,True)
nodes[83] = Node(83,True)
nodes[84] = Node(84,True)
nodes[85] = Node(85,True)
nodes[86] = Node(86,True)
nodes[87] = Node(87,True)
nodes[88] = Node(88,True)
nodes[89] = Node(89,True)
nodes[90] = Node(90,True)
nodes[91] = Node(91,True)
nodes[92] = Node(92,True)
nodes[93] = Node(93,True)
nodes[94] = Node(94,True)
nodes[95] = Node(95,True)
nodes[96] = Node(96,True)
nodes[97] = Node(97,True)
nodes[98] = Node(98,True)
nodes[99] = Node(99,True)
nodes[100] = Node(100,True)
nodes[101] = Node(101,False)
nodes[249] = Node(249,False)
nodes[669] = Node(669,False)
nodes[763] = Node(763,False)
nodes[1136] = Node(1136,False)
nodes[1174] = Node(1174,False)
nodes[2068] = Node(2068,False)
nodes[2343] = Node(2343,False)
nodes[2402] = Node(2402,False)
nodes[2601] = Node(2601,False)
links_in = [
1, -0.260870,101,
2, 0.048484,101,
3, -0.172659,101,
4, 0.018541,101,
5, -0.347942,101,
8, -0.030052,101,
9, -0.363558,101,
10, -0.454231,101,
11, -0.109700,101,
13, -0.085174,101,
14, -0.025657,101,
16, -0.018628,101,
19, 0.005172,101,
20, -0.115961,101,
24, 0.061440,101,
29, -0.157787,101,
30, -0.102775,101,
31, -0.314123,101,
32, 0.113403,101,
33, -0.021734,101,
37, -0.062090,101,
38, -0.024684,101,
40, -0.045570,101,
41, -0.166793,101,
43, -0.008690,101,
46, -0.141755,101,
48, -0.034859,101,
54, -0.027719,101,
56, -0.132568,101,
59, -0.056753,101,
60, -0.233930,101,
61, -0.085199,101,
63, 0.044870,101,
64, -0.021529,101,
67, 0.016324,101,
68, -0.015459,101,
71, -0.175299,101,
72, -0.034834,101,
75, 0.013124,101,
76, -0.108271,101,
80, -0.121741,101,
89, -0.048060,101,
91, -0.394640,101,
93, -0.367031,101,
94, -0.027125,101,
96, 0.074275,101,
98, -0.409899,101,
100, -0.394734,101,
2402, -0.260870,101,
27, -0.079533,249,
40, 0.500000,763,
25, -0.328018,763,
71, 0.085085,1174,
13, -0.170511,1174,
8, 0.579390,1174
]
links_out = [
1,-0.260870,101,
2,0.048484,101,
3,-0.172659,101,
4,0.018541,101,
5,-0.347942,101,
8,-0.030052,101,
8,0.579390,1174,
9,-0.363558,101,
10,-0.454231,101,
11,-0.109700,101,
13,-0.085174,101,
13,-0.170511,1174,
14,-0.025657,101,
16,-0.018628,101,
19,0.005172,101,
20,-0.115961,101,
24,0.061440,101,
25,-0.328018,763,
27,-0.079533,249,
29,-0.157787,101,
30,-0.102775,101,
31,-0.314123,101,
32,0.113403,101,
33,-0.021734,101,
37,-0.062090,101,
38,-0.024684,101,
40,-0.045570,101,
40,0.500000,763,
41,-0.166793,101,
43,-0.008690,101,
46,-0.141755,101,
48,-0.034859,101,
54,-0.027719,101,
56,-0.132568,101,
59,-0.056753,101,
60,-0.233930,101,
61,-0.085199,101,
63,0.044870,101,
64,-0.021529,101,
67,0.016324,101,
68,-0.015459,101,
71,-0.175299,101,
71,0.085085,1174,
72,-0.034834,101,
75,0.013124,101,
76,-0.108271,101,
80,-0.121741,101,
89,-0.048060,101,
91,-0.394640,101,
93,-0.367031,101,
94,-0.027125,101,
96,0.074275,101,
98,-0.409899,101,
100,-0.394734,101,
2402,-0.260870,101]

nodes = {}
nodes[1] = Node(1,True)
nodes[2] = Node(2,True)
nodes[3] = Node(3,True)
nodes[4] = Node(4,True)
nodes[5] = Node(5,True)
nodes[6] = Node(6,True)
nodes[7] = Node(7,True)
nodes[8] = Node(8,True)
nodes[9] = Node(9,True)
nodes[10] = Node(10,True)
nodes[11] = Node(11,True)
nodes[12] = Node(12,True)
nodes[13] = Node(13,True)
nodes[14] = Node(14,True)
nodes[15] = Node(15,True)
nodes[16] = Node(16,True)
nodes[17] = Node(17,True)
nodes[18] = Node(18,True)
nodes[19] = Node(19,True)
nodes[20] = Node(20,True)
nodes[21] = Node(21,True)
nodes[22] = Node(22,True)
nodes[23] = Node(23,True)
nodes[24] = Node(24,True)
nodes[25] = Node(25,True)
nodes[26] = Node(26,True)
nodes[27] = Node(27,True)
nodes[28] = Node(28,True)
nodes[29] = Node(29,True)
nodes[30] = Node(30,True)
nodes[31] = Node(31,True)
nodes[32] = Node(32,True)
nodes[33] = Node(33,True)
nodes[34] = Node(34,True)
nodes[35] = Node(35,True)
nodes[36] = Node(36,True)
nodes[37] = Node(37,True)
nodes[38] = Node(38,True)
nodes[39] = Node(39,True)
nodes[40] = Node(40,True)
nodes[41] = Node(41,True)
nodes[42] = Node(42,True)
nodes[43] = Node(43,True)
nodes[44] = Node(44,True)
nodes[45] = Node(45,True)
nodes[46] = Node(46,True)
nodes[47] = Node(47,True)
nodes[48] = Node(48,True)
nodes[49] = Node(49,True)
nodes[50] = Node(50,True)
nodes[51] = Node(51,True)
nodes[52] = Node(52,True)
nodes[53] = Node(53,True)
nodes[54] = Node(54,True)
nodes[55] = Node(55,True)
nodes[56] = Node(56,True)
nodes[57] = Node(57,True)
nodes[58] = Node(58,True)
nodes[59] = Node(59,True)
nodes[60] = Node(60,True)
nodes[61] = Node(61,True)
nodes[62] = Node(62,True)
nodes[63] = Node(63,True)
nodes[64] = Node(64,True)
nodes[65] = Node(65,True)
nodes[66] = Node(66,True)
nodes[67] = Node(67,True)
nodes[68] = Node(68,True)
nodes[69] = Node(69,True)
nodes[70] = Node(70,True)
nodes[71] = Node(71,True)
nodes[72] = Node(72,True)
nodes[73] = Node(73,True)
nodes[74] = Node(74,True)
nodes[75] = Node(75,True)
nodes[76] = Node(76,True)
nodes[77] = Node(77,True)
nodes[78] = Node(78,True)
nodes[79] = Node(79,True)
nodes[80] = Node(80,True)
nodes[81] = Node(81,True)
nodes[82] = Node(82,True)
nodes[83] = Node(83,True)
nodes[84] = Node(84,True)
nodes[85] = Node(85,True)
nodes[86] = Node(86,True)
nodes[87] = Node(87,True)
nodes[88] = Node(88,True)
nodes[89] = Node(89,True)
nodes[90] = Node(90,True)
nodes[91] = Node(91,True)
nodes[92] = Node(92,True)
nodes[93] = Node(93,True)
nodes[94] = Node(94,True)
nodes[95] = Node(95,True)
nodes[96] = Node(96,True)
nodes[97] = Node(97,True)
nodes[98] = Node(98,True)
nodes[99] = Node(99,True)
nodes[100] = Node(100,True)
nodes[101] = Node(101,False)
nodes[249] = Node(249,False)
nodes[669] = Node(669,False)
nodes[763] = Node(763,False)
nodes[1136] = Node(1136,False)
nodes[1174] = Node(1174,False)
nodes[2068] = Node(2068,False)
nodes[2343] = Node(2343,False)
nodes[2402] = Node(2402,False)
nodes[2601] = Node(2601,False)
links_in = [
1, -0.260870,101,
2, 0.048484,101,
3, -0.172659,101,
4, 0.018541,101,
5, -0.347942,101,
8, -0.030052,101,
9, -0.363558,101,
10, -0.454231,101,
11, -0.109700,101,
13, -0.085174,101,
14, -0.025657,101,
16, -0.018628,101,
19, 0.005172,101,
20, -0.115961,101,
24, 0.061440,101,
29, -0.157787,101,
30, -0.102775,101,
31, -0.314123,101,
32, 0.113403,101,
33, -0.021734,101,
37, -0.062090,101,
38, -0.024684,101,
40, -0.045570,101,
41, -0.166793,101,
43, -0.008690,101,
46, -0.141755,101,
48, -0.034859,101,
54, -0.027719,101,
56, -0.132568,101,
59, -0.056753,101,
60, -0.233930,101,
61, -0.085199,101,
63, 0.044870,101,
64, -0.021529,101,
67, 0.016324,101,
68, -0.015459,101,
71, -0.175299,101,
72, -0.034834,101,
75, 0.013124,101,
76, -0.108271,101,
80, -0.121741,101,
89, -0.048060,101,
91, -0.394640,101,
93, -0.367031,101,
94, -0.027125,101,
96, 0.074275,101,
98, -0.409899,101,
100, -0.394734,101,
669, 0.000000,101,
763, 0.000000,101,
2068, 0.000000,101,
2343, 0.000000,101,
2402, -0.260870,101,
2601, 0.000000,101,
6, 0.000000,249,
27, -0.079533,249,
70, 0.000000,669,
95, 0.000000,669,
14, 0.000000,669,
28, 0.000000,669,
24, 0.000000,669,
40, 0.500000,763,
20, 0.000000,763,
99, 0.000000,763,
46, 0.000000,763,
25, -0.328018,763,
71, 0.000000,1136,
75, 0.000000,1174,
71, 0.085085,1174,
13, -0.170511,1174,
8, 0.579390,1174,
66, 0.000000,2068,
36, 0.000000,2343,
1, 0.000000,2402,
23, 0.000000,2601
]
links_out = [
1,-0.260870,101,
1,0.000000,2402,
2,0.048484,101,
3,-0.172659,101,
4,0.018541,101,
5,-0.347942,101,
6,0.000000,101,
6,0.000000,249,
7,0.000000,101,
8,-0.030052,101,
8,0.579390,1174,
9,-0.363558,101,
10,-0.454231,101,
11,-0.109700,101,
12,0.000000,101,
13,-0.085174,101,
13,-0.170511,1174,
14,-0.025657,101,
14,0.000000,669,
15,0.000000,101,
16,-0.018628,101,
17,0.000000,101,
18,0.000000,101,
19,0.005172,101,
20,-0.115961,101,
20,0.000000,763,
21,0.000000,101,
22,0.000000,101,
23,0.000000,101,
23,0.000000,2601,
24,0.061440,101,
24,0.000000,669,
25,0.000000,101,
25,-0.328018,763,
26,0.000000,101,
27,0.000000,101,
27,-0.079533,249,
28,0.000000,669,
29,-0.157787,101,
30,-0.102775,101,
31,-0.314123,101,
32,0.113403,101,
33,-0.021734,101,
34,0.000000,101,
35,0.000000,101,
36,0.000000,101,
36,0.000000,2343,
37,-0.062090,101,
38,-0.024684,101,
39,0.000000,101,
40,-0.045570,101,
40,0.500000,763,
41,-0.166793,101,
42,0.000000,101,
43,-0.008690,101,
44,0.000000,101,
45,0.000000,101,
46,-0.141755,101,
46,0.000000,763,
47,0.000000,101,
48,-0.034859,101,
49,0.000000,101,
50,0.000000,101,
51,0.000000,101,
52,0.000000,101,
53,0.000000,101,
54,-0.027719,101,
55,0.000000,101,
56,-0.132568,101,
59,-0.056753,101,
60,-0.233930,101,
61,-0.085199,101,
62,0.000000,101,
63,0.044870,101,
64,-0.021529,101,
65,0.000000,101,
66,0.000000,101,
66,0.000000,2068,
67,0.016324,101,
68,-0.015459,101,
69,0.000000,101,
70,0.000000,101,
70,0.000000,669,
71,-0.175299,101,
71,0.085085,1174,
71,0.000000,1136,
72,-0.034834,101,
73,0.000000,101,
74,0.000000,101,
75,0.013124,101,
75,0.000000,1174,
76,-0.108271,101,
77,0.000000,101,
78,0.000000,101,
79,0.000000,101,
80,-0.121741,101,
81,0.000000,101,
82,0.000000,101,
83,0.000000,101,
84,0.000000,101,
85,0.000000,101,
86,0.000000,101,
87,0.000000,101,
88,0.000000,101,
89,-0.048060,101,
90,0.000000,101,
91,-0.394640,101,
92,0.000000,101,
93,-0.367031,101,
94,-0.027125,101,
95,0.000000,101,
95,0.000000,669,
96,0.074275,101,
97,0.000000,101,
98,-0.409899,101,
99,0.000000,101,
99,0.000000,763,
100,-0.394734,101,
669,0.000000,101,
763,0.000000,101,
2068,0.000000,101,
2343,0.000000,101,
2402,-0.260870,101,
2601,0.000000,101]


def sig(x):
	#return x / (1 + x) if x > 0 else -x / (x - 1)
	return -1 + 2 / (1 + math.exp(-x))

def at(x, y):
	return y * 10 + x

class Network:
	def __init__(self):
		global nodes
		global links_in
		global links_out
		self._nodes = nodes

		for i in range(0, len(links_in), 3):
			l = Link(links_in[i + 0], links_in[i + 2], links_in[i + 1])
			self._nodes[links_in[i + 2]].add_in(l)

		for i in range(0, len(links_out), 3):
			l = Link(links_out[i + 0], links_out[i + 2], links_out[i + 1])
			self._nodes[links_out[i + 0]].add_out(l)

		for i in range(1, 101):
			self._nodes[i].activated = True

	def oneof(self):
		for i in self._nodes:
			if (not self._nodes[i].activated):
				return True
		return False

	def activate(self, inputs):
		for i, it in self._nodes.items():
			it.activation = 0
			it._sum = 0
			it.activated = False
		for i in range(0, 100):
			it = self._nodes[i + 1]
			it._sum = inputs[i]
			it.activated = True

		while self.oneof():
			for i in self._nodes:
				if i <= 100: continue
				it = self._nodes[i]

				s = 0
				for x in it._in:
					s += self._nodes[x.i]._sum * x.w
					it.activated = it.activated or x.i <= 100 or self._nodes[x.i].activated

				it._sum += s

			for i, it in self._nodes.items():
				if i <= 100: continue
				if (not it.activated): continue
				it.activation = sig(it._sum)

		out = self._nodes[101].activation

		for i in self._nodes:
			if i <= 100: continue
			self._nodes[i]._sum = 0
			self._nodes[i].activated = False

		return out

class myPlayer(PlayerInterface):
	def __init__(self):
		self._board = Reversi.Board(10)
		self._mycolor = None
		self._net = Network()

	def getPlayerName(self):
		return "Genetic Player"

	def getInputs(self):
		inputs = []
		for x in range(0, 10):
			for y in range(0, 10):
				if (self._board._board[x][y] == self._mycolor):
					inputs.append(-1)
				elif (self._board._board[x][y] == 0):
					inputs.append(0)
				else:
					inputs.append(+1)
		return inputs

	def h(self):
		return self._net.activate(self.getInputs())


	def negamax(self, d, p, alpha, beta):
		if (d == 0 or self._board.is_game_over()):
			return (self.h(), (p, -1, -1)) if self._mycolor == p else (-self.h(), (p, -1, -1))

		best = -1
		best_move = (p, -1, -1)
		moves = self._board.legal_moves()

		for it in moves:
			self._board.push(it)
			(current, _) = self.negamax(d - 1, 1 if p == 2 else 2, -beta, -alpha)
			current = -current
			self._board.pop()

			if current > best:
				best = current
				best_move = it

			alpha = max(alpha, current)
			#beta = min(beta, current)
			if (alpha >= beta): break
		
		return (best, best_move)

	def getPlayerMove(self):
		assert(not self._board.is_game_over())

		(_, move) = self.negamax(4, self._mycolor, -1, 1)
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




