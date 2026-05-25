"""Week 12: Monster Hunter Graphs.

Complete each function using Python 3.11+.

Rules:
- Standard library only.
- Use type hints.
- Keep public function docstrings.
- Run tests with: pytest -q
"""

import heapq


def build_hunter_map(edges: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Build an undirected adjacency list from route pairs.

    Each tuple represents a two-way route between two monster sighting
    locations.

    Args:
        edges: A list of route pairs, such as
            [("Old Theater", "Train Station")].

    Returns:
        A dictionary where each key is a location and each value is a list
        of neighboring locations.

    Rules:
        - Add both directions for each route.
        - Include every location that appears in the input.
        - Do not duplicate neighbors if the same route appears more than once.
    """
    graph: dict[str, set[str]] = {}

    for start, end in edges:
        graph.setdefault(start, set()).add(end)
        graph.setdefault(end, set()).add(start)

    return {location: list(neighbors) for location, neighbors in graph.items()}


def build_weighted_hunter_map(
    edges: list[tuple[str, str, int]]
) -> dict[str, dict[str, int]]:
    """Build an undirected weighted graph from route triples.

    Each tuple represents a two-way route with a positive danger score.

    Args:
        edges: A list of route triples, such as
            [("Old Theater", "Train Station", 4)].

    Returns:
        A nested dictionary where graph[start][end] is the danger score.

    Rules:
        - Add both directions for each route.
        - Danger scores must be positive integers.
        - If danger score is 0 or negative, raise ValueError.
        - If the same route appears more than once, keep the lowest score.
    """
    graph: dict[str, dict[str, int]] = {}

    for start, end, danger in edges:
        if danger <= 0:
            raise ValueError("Danger scores must be positive integers")

        graph.setdefault(start, {})
        graph.setdefault(end, {})

        existing_forward = graph[start].get(end)
        existing_backward = graph[end].get(start)
        best_score = danger

        if existing_forward is not None:
            best_score = min(existing_forward, best_score)

        if existing_backward is not None:
            best_score = min(existing_backward, best_score)

        graph[start][end] = best_score
        graph[end][start] = best_score

    return graph


def map_summary(graph: dict[str, list[str]]) -> dict[str, int]:
    """Return the number of locations and undirected routes.

    Args:
        graph: An undirected adjacency list.

    Returns:
        A dictionary with:
            - "locations": number of locations
            - "routes": number of undirected routes

    Example:
        {
            "A": ["B", "C"],
            "B": ["A"],
            "C": ["A"],
        }

        returns {"locations": 3, "routes": 2}
    """
    locations = len(graph)
    seen_edges: set[tuple[str, str]] = set()

    for origin, neighbors in graph.items():
        for neighbor in neighbors:
            edge = (origin, neighbor) if origin <= neighbor else (neighbor, origin)
            seen_edges.add(edge)

    routes = len(seen_edges)
    return {"locations": locations, "routes": routes}


def most_connected_location(graph: dict[str, list[str]]) -> str | None:
    """Return the location with the most neighbors.

    Args:
        graph: An undirected adjacency list.

    Returns:
        The location with the most neighbors.
        If the graph is empty, return None.
        If there is a tie, return the alphabetically first location.
    """
    if not graph:
        return None

    best_location: str | None = None
    best_degree = -1

    for location in sorted(graph):
        degree = len(graph[location])
        if degree > best_degree:
            best_degree = degree
            best_location = location

    return best_location


def priority_hunt_order(reports: list[tuple[int, str]]) -> list[str]:
    """Return monster sighting locations from most urgent to least urgent.

    Lower priority number means more urgent.

    Args:
        reports: A list of tuples in the form (priority, location).

    Returns:
        A list of locations ordered from lowest priority number to highest.

    Requirement:
        Use heapq.
    """
    heap = list(reports)
    heapq.heapify(heap)

    ordered: list[str] = []
    while heap:
        _, location = heapq.heappop(heap)
        ordered.append(location)

    return ordered
