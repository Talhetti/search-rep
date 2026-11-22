from puzzle.base_search import BaseSearch
from puzzle.state import State
from puzzle.result import SearchResult

DEFAULT_DEPTH_LIMIT = 50


class DFS(BaseSearch):

    def __init__(self, depth_limit: int = DEFAULT_DEPTH_LIMIT):
        self.depth_limit = depth_limit

    def search(self, initial: State) -> SearchResult:
        frontier = [initial]
        visited = set()

        nodes_generated = 1
        nodes_expanded = 0
        max_frontier_size = 1

        while frontier:
            max_frontier_size = max(max_frontier_size, len(frontier))

            node = frontier.pop()

            if node in visited:
                continue
            visited.add(node)

            if node.is_goal:
                return SearchResult(
                    solution=node,
                    nodes_expanded=nodes_expanded,
                    nodes_generated=nodes_generated,
                    max_frontier_size=max_frontier_size,
                    depth=node.cost,
                )

            nodes_expanded += 1

            if node.cost < self.depth_limit:
                for child in node.neighbors():
                    if child not in visited:
                        frontier.append(child)
                        nodes_generated += 1

        return SearchResult(
            solution=None,
            nodes_expanded=nodes_expanded,
            nodes_generated=nodes_generated,
            max_frontier_size=max_frontier_size,
        )
