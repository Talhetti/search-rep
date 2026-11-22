import heapq
import itertools
from puzzle.base_search import BaseSearch
from puzzle.state import State, GOAL_STATE
from puzzle.result import SearchResult


class AStar(BaseSearch):

    def heuristic(self, state: State) -> int:
        total = 0
        for index, tile in enumerate(state.tiles):
            if tile == 0:
                continue
            goal_index = GOAL_STATE.index(tile)
            row, col = divmod(index, 3)
            goal_row, goal_col = divmod(goal_index, 3)
            total += abs(row - goal_row) + abs(col - goal_col)
        return total

    def search(self, initial: State) -> SearchResult:
        counter = itertools.count()
        frontier = [(self.heuristic(initial), next(counter), initial)]
        best_cost = {initial: 0}

        nodes_generated = 1
        nodes_expanded = 0
        max_frontier_size = 1

        while frontier:
            max_frontier_size = max(max_frontier_size, len(frontier))

            _, _, node = heapq.heappop(frontier)

            if node.cost > best_cost.get(node, float("inf")):
                continue

            if node.is_goal:
                return SearchResult(
                    solution=node,
                    nodes_expanded=nodes_expanded,
                    nodes_generated=nodes_generated,
                    max_frontier_size=max_frontier_size,
                    depth=node.cost,
                )

            nodes_expanded += 1

            for child in node.neighbors():
                if child.cost < best_cost.get(child, float("inf")):
                    best_cost[child] = child.cost
                    f_score = child.cost + self.heuristic(child)
                    heapq.heappush(frontier, (f_score, next(counter), child))
                    nodes_generated += 1

        return SearchResult(
            solution=None,
            nodes_expanded=nodes_expanded,
            nodes_generated=nodes_generated,
            max_frontier_size=max_frontier_size,
        )
