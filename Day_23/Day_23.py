#!/usr/bin/python3
from itertools import combinations
import networkx as nx

def main():
    part_1()
    part_2()

def part_2():
    graph = nx.Graph()
    with open("Day_23_input.txt", 'r', encoding="utf-8") as file:
        for line in file:
            computers = line.strip().split("-")
            graph.add_edge(computers[0], computers[1])
    cliques = nx.find_cliques(graph)
    res = sorted(sorted(cliques, key=len, reverse=True)[0])
    print(res)

def part_1():
    graph = nx.Graph()
    with open("Day_23_input.txt", 'r', encoding="utf-8") as file:
        for line in file:
            computers = line.strip().split("-")
            graph.add_edge(computers[0], computers[1])
    cliques = []
    for clique in nx.find_cliques(graph):
        if len(clique) >= 3 and any(node[0] == "t" for node in clique):
            cliques.append(clique)
    
    count = 0
    visited = []
    for clique in cliques:
        for nodes in combinations(clique, 3):
            if any(node[0] == "t" for node in nodes) and sorted(nodes) not in visited:
                count += 1
                visited.append(sorted(nodes))
    print(count)
    


if __name__ == "__main__":
    main()