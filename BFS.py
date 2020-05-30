import queue, os
from random import choices, choice
from time import sleep, time
from copy import deepcopy

def GetStartPoint(maze):	
	return maze[0].index("O")

def GenerateMaze():
	size = int(input("Storlek: "))
	maze = [["#"]*size]
	maze[0][choice([i for i in range(1, size-1)])] = "O"
	for i in range(size-1):
		s = ""
		if i == size-2:
			s = "#"*size
		else:
			s = choices(["#", " "], weights = [10, 30], k = size)
			s[0] = "#"
			s[size-1] = "#"
		maze.append(list(s))
	maze[-1][choice([i for i in range(1, size-1)])] = "X"
	return maze

def HasFoundGoal(maze, path):	
	i = 0
	j = GetStartPoint(maze)

	i += path.count("D")
	i -= path.count("U")
	j += path.count("R")
	j -= path.count("L")

	if maze[i][j] == "X":
		return True
	return False

def IsValid(maze, path, coord):
	i = 0
	j = GetStartPoint(maze)

	i += path.count("D")
	i -= path.count("U")
	j += path.count("R")
	j -= path.count("L")


	if i < 0 or i >= len(maze) or j < 0 or j >= len(maze):
		return False
	if maze[i][j] == "#":
		return False
	elif [i, j] in coord:
		return False

	#sleep(0.25)
	#os.system("cls")
	#DrawMaze(maze, path)
	coord.append([i, j])
	return True

def DrawMaze(maze, path):
	newMaze = deepcopy(maze)
	if len(path) > 0:
		i = 0
		j = GetStartPoint(maze)

		for c in path:
			if c == "U":
				i -= 1
			elif c == "D":
				i += 1
			elif c == "L":
				j -= 1
			elif c == "R":
				j += 1
			newMaze[i][j] = "+"
		for row in newMaze:
			print("".join(col for col in row))
	else:
		print("Found No Path!")
		for row in maze:
			print("".join(col for col in row))

t1 = time()
maze = GenerateMaze()
paths = queue.Queue()
paths.put("")
add = ""
hasFoundPath = False
coord = []
os.system("cls")
t2 = time()
while True:
	add = paths.get()
	for c in ["U", "D", "L", "R"]:
		if len(add) > 0:
			if add[-1] == "D" and c == "U" or add[-1] == "U" and c == "D" or add[-1] == "L" and c == "R" or add[-1] == "R" and c == "L":
				continue
		put = add + c
		if IsValid(maze, put, coord):
			paths.put(put)
	if HasFoundGoal(maze, add):
		True
		break
	elif paths.empty():
		add = ""
		break
t3 = time()
DrawMaze(maze, add)
t4 = time()
print(f"Total Tid: {round(t4-t1, 5)}s")
print(f"SökTid: {round(t3-t2, 5)}s")