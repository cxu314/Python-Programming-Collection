# Python-Programming-Collection

## 1. Graph

A directed un-weighted in the Graph class implementation.

### Examples

```
from graph import *

# create an empty node
node = Node({})

# create a graph with a list of nodes
node_list = []
node_list.append(Node({'A':['B','C']}))
node_list.append(Node({'B':['C','D']}))
node_list.append(Node({'C':['D']}))
node_list.append(Node({'D':['C']}))
Graph(node_list)

# add nodes to a graph
g = Graph()
for node in node_list:
    g.add(node)

# find paths
g.find_path_dfs("A", "D")
g.find_all_paths("A", "D")
g.find_shortest_path("A", "D")

# check if there is a path between nodes
g.has_route("C", "B")
```


## 2. Object Oriented Search Engine Implementation

A reusable library of a hash table implementation.

### Examples

The following examples all create a hashtable, then set the value associated with the key "parrt" and the value 99.

```
from htable_oo import HashTable

#create a hash table
table = HashTable(5) 

#put an association with key 'parrt' and value 99 into the table
table.put('parrt', 99) 

#print the hash table
print(table.buckets_str())

#print all associations in the hash table
str(table)
```

## 3. Prefix and Suffix Search

Given a prefix or a suffix find all matching words in a given list of words.

### Examples

Git clone the repository and run the code in the terminal.
The following examples all create with reading the list of words from standard input.
`words_list.txt` is a txt file each line of which is a word. 

1. Return usage instructions of the application.

```
python fix_search.py -h
```

2. Return a list of words with the prefix "abacul".

```
python fix_search.py -p "abacul" < words_list.txt
```

3. Return a list of words with the suffix "abacul".

```
python fix_search.py -s "abacul" < words_list.txt
```

## 4. Palindrome

A program that takes a word or a sentence and determines whereather is it palindrome or not.

### Examples

Git clone the repository and run the code in the terminal.

1. Return yes for a palindrome.

```
python palindrome.py "A nut for a jar of tuna"
```

2. Return no for a non-palindrome.

```
python palindrome.py "Call me maybe"
```

## 5. Telephone Keypad

A program that given a "phone number" prints a sorted list of all possible words generated from a telephone keypad.

`words_list.txt` is a txt file each line of which is a word. 

### Examples

Git clone the repository and run the code in the terminal.

1. Return "abt", "abu", "abv", "act", "bat", "cat", and "cav" for "228".

```
python telephone_keypad.py "228" < words_list.txt
```

2. Return None if there are no possible words.

```
python telephone_keypad.py "6502227795" < words_list.txt
```

## 6. Project Order

A program that iven a list of project and a list of dependencies 
(which is a list of pairs of projects, where the second project is dependent on the first), determines a build order which allows the projects to be built. 

All of the project’s dependencies must be built before the project is. 
If there is no build order, then the code will indicate so.

Input:
Projects: a, b, c, d, e, f
Dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
Output:
	f, e, a, b, d, c


## 7. Game Ranking System

Game ranking system implementation.

### Rules

You have been asked to implement the ranking system. All players have a rank determining their playing strength which gets updated after every game played. There are 25 regular ranks, and an extra rank, Legend, above that. The ranks are numbered in decreasing order, 25 being the lowest rank, 1 the second highest rank, and Legend the highest rank.

Each rank has a certain number of stars that one needs to gain before advancing to the next rank. If a player wins a game, she gains a star. If before the game the player was on rank 6-25, and this was the third or more consecutive win, she gains an additional bonus star for that win. When she has all the stars for her rank (see list below) and gains another star, she will instead gain one rank and have one star on the new rank.

For instance, if before a winning game the player had all the stars on her current rank, she will after the game have gained one rank and have 1 or 2 stars (depending on whether she got a bonus star) on the new rank. If on the other hand she had all stars except one on a rank, and won a game that also gave her a bonus star, she would gain one rank and have 1 star on the new rank.

If a player on rank 1-20 loses a game, she loses a star. If a player has zero stars on a rank and loses a star, she will lose a rank and have all stars minus one on the rank below. However, one can never drop below rank 20 (losing a game at rank 20 with no stars will have no effect).

If a player reaches the Legend rank, she will stay legend no matter how many losses she incurs afterwards.

The number of stars on each rank are as follows:

Rank 25-21: 2 stars
Rank 20-16: 3 stars
Rank 15-11: 4 stars
Rank 10-1: 5 stars
A player starts at rank 25 with no stars.

### Examples

Git clone the repository and run the code in the terminal.

1. Return 25.

```
python ranking.py WW
```

2. Return 24.

```
python ranking.py WWW
```

3. Return 24.

```
python ranking.py WLWLWLWL
```

4. Return 19.

```
python ranking.py WWWWWWWWWLLWW
```

5. Return 18.

```
python ranking.py WWWWWWWWWLWWL
```

## 8. Animated Compass Needle
Animate the needle taking the shortest path from the current needle direction to the correct direction.

### Rules

The aim of this project is developing animated compass needle. The API is simple: the compass needle is currently in some direction (between 0 and 359 degrees, with north being 0, east being 90), and is being animated by giving the degrees to spin it. If the needle is pointing north, and you give the compass an input of 90, it will spin clockwise (positive numbers mean clockwise direction) to stop at east, whereas an input of -45 would spin it counterclockwise to stop at north west.

### Examples

Git clone the repository and run the code in the terminal.

1. Return 90.

```
python compas.py 315 45
```

2. Return 90.

```
python compas.py 180 270
```

3. Return -135.

```
python compas.py 45 270
```
