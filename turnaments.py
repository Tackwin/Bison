import Reversi
import math
import BetterRandom
import GeneticPlayer
import random
import time

random.seed(100)

def play_game(player1, player2):
	b = Reversi.Board(10)

	player1.newGame(b._BLACK)
	player2.newGame(b._WHITE)

	players = [player1, player2]
	colors = [b._BLACK, b._WHITE]

	player_index = 0

	while not b.is_game_over():
		#print(b)
		current_player = players[player_index]
		current_color = colors[player_index]
		other_player = players[(player_index + 1) % len(players)]

		move = current_player.getPlayerMove()
		(x,y) = move
		if not b.is_valid_move(current_color, x, y):
			print("Problem: illegal move")
			break
		b.push([current_color, x, y])
		other_player.playOpponentMove(x, y)

		player_index = (player_index + 1) % 2

		if random.random() < 0.1:
			toreturn=""
			for l in b._board:
				for c in l:
					toreturn += b._piece2str(c)
				toreturn += "\n"

			p = player1 if isinstance(player1, GeneticPlayer.myPlayer) else player2

			toreturn += str(p._net.activate(p.getInputs())) + "\n\n"

			f = open("output/test.txt", "a")
			f.write(toreturn)
			f.close()



	(n_white, n_black) = b.get_nb_pieces()

	return n_white < n_black



current_milli_time = lambda: int(round(time.time() * 1000))



# n = int(input("n: "))
n = 1

player_kind = []

# next_file = input()
# while not next_file == "":
# 	player_kind.append(__import__(next_file).myPlayer)
# 	next_file = input()
# 
# players = [None] * (2 ** n)
# 
# for i in range(len(players)):
# 	players[i] = random.choice(player_kind)()

players = [BetterRandom.myPlayer(), GeneticPlayer.myPlayer()]



def run_turnament(players):
	for i in range(n):
		n_games = len(players) // 2
		for it in range(n_games):

			p_1 = players[it + 0]
			p_2 = players[it + 1]

			if play_game(p_1, p_2):
				del players[it + 1]
			else:
				del players[it + 0]



def winrate(players, n):
	N = 1
	n_win = 0.0
	avg_time = 0.0
	for i in range(n):
		start = current_milli_time()
		if not play_game(players[0], players[1]):
			n_win = n_win + 1.0
		if N > 1 and play_game(players[1], players[0]):
			n_win = n_win + 1.0
		end = current_milli_time()
		

		avg_time += end - start
		print("Winrate: ", n_win / ((i + 1) * N), "(", n_win, ", ", (i + 1) * N, ") in ", avg_time / ((i + 1) * N))

# run_turnament(players)
winrate(players, 1000)

print("Winner is: ", players[0].getPlayerName())

