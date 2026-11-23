"""Script de demonstração — útil para depurar manualmente."""

from puzzle.state import State
from algorithms.bfs import BFS
from algorithms.dfs import DFS
from algorithms.a_star import AStar


def print_result(name: str, result):
    print(f"\n{'='*40}")
    print(f"Algoritmo : {name}")
    if result.found:
        print(f"Solução   : {' → '.join(result.actions)}")
        print(f"Custo     : {result.path_cost}")
        print(f"Profund.  : {result.depth}")
    else:
        print("Solução   : NÃO ENCONTRADA")
    print(f"Expandidos: {result.nodes_expanded}")
    print(f"Gerados   : {result.nodes_generated}")
    print(f"Fronteira : {result.max_frontier_size} (máx)")


if __name__ == "__main__":
    initial_states = [
        State((2, 8, 3, 1, 6, 4, 7, 0, 5)),
        State((1, 2, 3, 4, 5, 6, 0, 7, 8)),
        State((1, 2, 3, 0, 4, 6, 7, 5, 8)),
        State((4, 1, 3, 2, 5, 6, 7, 8, 0)),
        State((2, 3, 6, 1, 4, 8, 7, 0, 5)),
    ]

    for initial in initial_states:
        print("\nEstado inicial:")
        print(initial)

        print_result("BFS",  BFS().search(initial))
        print_result("DFS",  DFS().search(initial))
        print_result("A*",   AStar().search(initial))
