import numpy as np

def shortest_distances_directed(n, edges, src):
    dist = [np.inf] * n
    dist[src] = 0
    oldDist = dist.copy()

    for i in range(n - 1):
        for (x, y, z) in edges:
            dist[y] = min(dist[y], dist[x] + z)
        if dist != oldDist:
            oldDist = dist.copy()
        else:
            break

    return dist

def find_closest_unbalanced(src, dists, balance):
    minDist, bestPartner = np.inf, src
    n = len(balance)
    for dst in range(src + 1, n):
        if balance[src] * balance[dst] < 0 and dists[dst] <= minDist:
            minDist, bestPartner = dists[dst], dst

    return bestPartner

def vertices_ratio(n, edges):
    # in // out ratio
    balance = [0 for i in range(n)]

    for e in edges:
        balance[e[0]] += 1
        balance[e[1]] -= 1

    return balance

def is_eulerian_directed(n, edges):
    balance = vertices_ratio(n, edges)
    return all(balance[i] == 0 for i in range(n))

def eulerize_directed(n, edges):
    # deja eulerien
    if is_eulerian_directed(n, edges):
        return edges

    balance = vertices_ratio(n, edges)

    # ils doivent tous etre balance

    for v in range(len(balance)):
        if balance[v] != 0:
            dists = shortest_distances_directed(n, edges, v)

        while balance[v] != 0:
            bestPartner = find_closest_unbalanced(v, dists, balance)

            # donator notation (out +, in -)
            if balance[v] > 0:
                while balance[bestPartner] < 0 and balance[v] > 0:
                    edges.append((bestPartner, v, dists[bestPartner]))
                    balance[v] -= 1
                    balance[bestPartner] += 1
            else:
                while balance[bestPartner] > 0 and balance[v] < 0:
                    edges.append((v, bestPartner, dists[bestPartner]))
                    balance[v] += 1
                    balance[bestPartner] -= 1

    return edges