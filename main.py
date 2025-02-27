from word_grid import *
import argparse


# Initialize parser
parser = argparse.ArgumentParser(description="Generates a word search puzzle")

# Adding optional argument
parser.add_argument("-c", "--cheated", action="store_true", help = "Hightlight words")
parser.add_argument("-f", "--file", type=str, default="words.txt", help = "Path to a custom words file. One word per line.")
parser.add_argument("-s", "--size", type=int, default=20, help = "Sets a custom grid size (Default: 20)")

# Read arguments from command line
args = parser.parse_args()

def main(cheated=False, words_file=None, size=20):

	# generating words from file
	words = []
	file1 = open(words_file, 'r')
	lines = file1.readlines()
	file1.close()

	# appending words to array
	for _ in range(164):
		rando = random.randint(0, len(lines)-1)
		words.append(lines[rando].strip())
		lines.pop(rando)

	# creating the word grid
	grid = WordGrid(size)

	print("┌────────────────────┐")
	print("│ Word Search Puzzle │")
	print("└────────────────────┘")

	grid.cheated = cheated
	grid.generate_with_words(words)

	# printing the words to find
	print("Words:")
	count = 0
	for word in words:
		count += 1
		print(f"{count}. {word}", end=" | ")
	print()

if __name__ == "__main__":
	main(cheated=args.cheated, words_file=args.file, size=args.size)

# Created by Magoninho