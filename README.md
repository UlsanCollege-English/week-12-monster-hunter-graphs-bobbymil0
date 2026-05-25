[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/80z-ZS6n)
# Week 12: Monster Hunter Graphs

## Student

Name: Bobby Nepali

Student ID: 2412077

## Summary

This assignment builds a monster sighting network as a graph so the Hunter Guild can understand where threats are connected. It creates both unweighted and weighted maps, summarizes the route network, finds the most dangerous hub, and orders priority reports for urgent response.

## Approach

- `build_hunter_map`: Use a set-based adjacency collection to build an undirected graph and avoid duplicate neighbors.
- `build_weighted_hunter_map`: Create a two-way danger map, validate positive weights, and keep the lowest weight for duplicate routes.
- `map_summary`: Count locations as nodes and count each undirected route once by normalizing edge direction.
- `most_connected_location`: Select the node with the highest neighbor count and break ties with alphabetical order.
- `priority_hunt_order`: Use `heapq` to order sighting locations from most urgent to least urgent.

## Complexity

### `build_hunter_map`

- Time: O(E)
- Space: O(V + E)
- Why: Each route is processed once and neighbor sets store unique connections.

### `build_weighted_hunter_map`

- Time: O(E)
- Space: O(V + E)
- Why: Each weighted edge is inserted bidirectionally and duplicate route weights are compared.

### `map_summary`

- Time: O(V + E)
- Space: O(E)
- Why: The function iterates through every node and neighbor, counting unique undirected edges.

### `most_connected_location`

- Time: O(V log V)
- Space: O(1)
- Why: Sorting the node keys ensures deterministic tie-breaking, then degrees are compared.

### `priority_hunt_order`

- Time: O(N log N)
- Space: O(N)
- Why: `heapq.heapify` and repeated pops order reports by priority with heap operations.

## Edge-Case Checklist

- [x] Empty graph
- [x] One route
- [x] Duplicate routes
- [x] Disconnected locations
- [x] Tie for most connected location
- [x] Positive weighted routes
- [x] Invalid zero or negative danger score
- [x] Empty priority report list

## Tests

Paste the result of your test run.

```bash
PYTHONPATH=. pytest -q
```

Result:

```text
All tests passed.
```

## Assistance & Sources

AI used? Yes

If yes, what did it help with?

- Clarifying function behavior and writing README explanations.

Other sources used:

- None

