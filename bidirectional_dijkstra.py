#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/5/27 10:49
# @Author  : Xavier Ma
# @Email   : xavier_mayiming@163.com
# @File    : bidirectional_dijkstra.py
# @Statement : The bidirectional Dijkstra's algorithm
import heapq


def reverse_graph(graph):
    # reverse the graph
    reversed_graph = {}
    for node1 in graph:
        for node2, weight in graph[node1].items():
            if node2 not in reversed_graph:
                reversed_graph[node2] = {}
            reversed_graph[node2][node1] = weight
    return reversed_graph


def main(graph, source, target):
    """
    The main function of the bidirectional Dijkstra's algorithm
    :param graph: {node1: {node2: weight, node3: weight, ...}, ...}
    :param source: the source node
    :param target: the target node
    :return:
    """
    dist_f = {node: float('inf') for node in graph.keys()}
    dist_b = {node: float('inf') for node in graph.keys()}
    dist_f[source] = 0
    dist_b[target] = 0
    path_f = {source: [source]}
    path_b = {target: [target]}
    queue_f = []
    heapq.heappush(queue_f, (0, [source]))
    queue_b = []
    heapq.heappush(queue_b, (0, [target]))
    visited_f = set()
    visited_b = set()
    mu = float('inf')
    best_path = None
    reversed_graph = reverse_graph(graph)
    length_f = length_b = 0

    while queue_f or queue_b:
        if queue_f:
            length, path = heapq.heappop(queue_f)
            length_f = length
            node1 = path[-1]
            path_f[node1] = path
            if node1 not in visited_f:
                visited_f.add(node1)
                for node2, weight in graph[node1].items():
                    temp_length = length + weight
                    if temp_length < dist_f[node2]:
                        dist_f[node2] = temp_length
                        temp_path = path.copy()
                        temp_path.append(node2)
                        heapq.heappush(queue_f, (temp_length, temp_path))
                    if node2 in visited_b and dist_f[node1] + graph[node1][node2] + dist_b[node2] < mu:
                        mu = dist_f[node1] + graph[node1][node2] + dist_b[node2]
                        best_path = path_f[node1] + list(reversed(path_b[node2]))
        if queue_b:
            length, path = heapq.heappop(queue_b)
            length_b = length
            node1 = path[-1]
            path_b[node1] = path
            if node1 not in visited_b:
                visited_b.add(node1)
                for node2, weight in reversed_graph[node1].items():
                    temp_length = length + weight
                    if temp_length < dist_b[node2]:
                        dist_b[node2] = temp_length
                        temp_path = path.copy()
                        temp_path.append(node2)
                        heapq.heappush(queue_b, (temp_length, temp_path))
                    if node2 in visited_f and dist_f[node2] + reversed_graph[node1][node2] + dist_b[node1] < mu:
                        mu = dist_f[node2] + reversed_graph[node1][node2] + dist_b[node1]
                        best_path = path_f[node2] + list(reversed(path_b[node1]))
        if length_f + length_b >= mu:
            return {'length': mu, 'path': best_path}


if __name__ == '__main__':
    test_graph = {
        0: {1: 62, 2: 44, 3: 67},
        1: {0: 62, 2: 32, 4: 52},
        2: {0: 44, 1: 33, 3: 32, 4: 52},
        3: {0: 67, 2: 32, 4: 54},
        4: {1: 52, 2: 52, 3: 54}
    }
    s = 0
    d = 4
    print(main(test_graph, s, d))
