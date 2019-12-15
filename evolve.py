"""
2-input XOR example -- this is most likely the simplest possible example.
"""

from __future__ import print_function
import neat
import Reversi
import math
import random
import GeneticPlayer

def play_game(player1, player2):
	b = Reversi.Board(10)

	player1.newGame(b._BLACK)
	player2.newGame(b._WHITE)

	players = [player1, player2]
	colors = [b._BLACK, b._WHITE]

	player_index = 0

	while not b.is_game_over():
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

	(n_white, n_black) = b.get_nb_pieces()

	return n_white < n_black

# 2-input XOR inputs and expected outputs.
xor_inputs = [(0.0, 0.0), (0.0, 1.0), (1.0, 0.0), (1.0, 1.0)]
xor_outputs = [   (0.0,),     (1.0,),     (1.0,),     (0.0,)]


def eval_genomes(genomes, config):
	for _, g in genomes:
		g.fitness = 0

	for genome_i, genome_p in genomes:
		net = neat.nn.FeedForwardNetwork.create(genome_p, config)
		p1 = GeneticPlayer.myPlayer(net)
		for genome_j, genome_o in genomes:
			if (genome_j <= genome_i):
				continue
			
			net_opponent = neat.nn.FeedForwardNetwork.create(genome_o, config)
			p2 = GeneticPlayer.myPlayer(net_opponent)

			p1_win = play_game(p1, p2)
			genome_p.fitness = genome_p.fitness + (1 if p1_win else 0)
			genome_o.fitness = genome_o.fitness + (0 if p1_win else 1)



# Load configuration.
config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
					neat.DefaultSpeciesSet, neat.DefaultStagnation,
					'config-feedforward')

# Create the population, which is the top-level object for a NEAT run.
p = neat.Population(config)

# Add a stdout reporter to show progress in the terminal.
p.add_reporter(neat.StdOutReporter(False))

# Run until a solution is found.
winner = p.run(eval_genomes, 10)

# Display the winning genome.
print('\nBest genome:\n{!s}'.format(winner))
