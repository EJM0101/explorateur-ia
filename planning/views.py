from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import heapq
from collections import deque, defaultdict

# A* et Dijkstra
def a_star(graph, start, goal, heuristic=None):
    if heuristic is None:
        heuristic = lambda x, y: 0

    open_set = [(0 + heuristic(start, goal), 0, start, [])]
    visited = set()

    while open_set:
        est_total, cost, current, path = heapq.heappop(open_set)
        if current in visited:
            continue
        visited.add(current)
        path = path + [current]
        if current == goal:
            return path
        for neighbor, weight in graph[current]:
            if neighbor not in visited:
                est = cost + weight + heuristic(neighbor, goal)
                heapq.heappush(open_set, (est, cost + weight, neighbor, path))
    return []

# BFS (non pondéré)
def bfs(graph, start, goal):
    queue = deque([[start]])
    visited = set()
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == goal:
            return path
        if node in visited:
            continue
        visited.add(node)
        for neighbor, _ in graph[node]:
            if neighbor not in visited:
                queue.append(path + [neighbor])
    return []

# Heuristique A* simple (distance de nom)
def lettre_distance(a, b):
    return abs(len(a) - len(b))

@csrf_exempt
def index(request):
    chemin = []
    algo = 'a_star'
    noeuds = []
    edges_input = ""
    start, end = "", ""
    invalides = []

    if request.method == 'POST':
        algo = request.POST.get('algo')
        edges_input = request.POST.get('edges', '')
        start = request.POST.get('start', '').strip()
        end = request.POST.get('end', '').strip()

        graph = defaultdict(list)
        noeuds_set = set()

        for line in edges_input.strip().splitlines():
            parts = line.strip().split()
            if len(parts) >= 3:
                try:
                    a = parts[0].strip()
                    b = parts[1].strip()
                    w = float(parts[2].strip())
                    graph[a].append((b, w))
                    graph[b].append((a, w))
                    noeuds_set.update([a, b])
                except ValueError:
                    invalides.append(line)
            else:
                invalides.append(line)

        noeuds = sorted(list(noeuds_set))

        if algo == 'a_star':
            chemin = a_star(graph, start, end, lettre_distance)
        elif algo == 'dijkstra':
            chemin = a_star(graph, start, end)  # heuristique 0
        elif algo == 'bfs':
            chemin = bfs(graph, start, end)

    return render(request, 'planning/index.html', {
        'algo': algo,
        'chemin': chemin,
        'edges': edges_input,
        'start': start,
        'end': end,
        'noeuds': noeuds,
        'invalides': invalides
    })