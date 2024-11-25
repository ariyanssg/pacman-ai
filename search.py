import util
import time  # For measuring execution time

class SearchProblem:
    """
    This class outlines the structure of a search problem.
    """
    def getStartState(self):
        util.raiseNotDefined()

    def isGoalState(self, state):
        util.raiseNotDefined()

    def getSuccessors(self, state):
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        util.raiseNotDefined()


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.
    """
    from util import Stack
    start_time = time.perf_counter()

    stack = Stack()
    visited = set()
    stack.push((problem.getStartState(), []))  # (state, path)

    while not stack.isEmpty():
        state, path = stack.pop()

        if state in visited:
            continue

        visited.add(state)

        if problem.isGoalState(state):
            end_time = time.perf_counter()
            print(f"DFS Execution Time: {end_time - start_time:.5f} seconds")
            return path

        for successor, action, _ in problem.getSuccessors(state):
            if successor not in visited:
                stack.push((successor, path + [action]))

    return []


def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    from util import Queue
    start_time = time.perf_counter()

    queue = Queue()
    visited = set()
    queue.push((problem.getStartState(), []))  # (state, path)

    while not queue.isEmpty():
        state, path = queue.pop()

        if state in visited:
            continue

        visited.add(state)

        if problem.isGoalState(state):
            end_time = time.perf_counter()
            print(f"BFS Execution Time: {end_time - start_time:.5f} seconds")
            return path

        for successor, action, _ in problem.getSuccessors(state):
            if successor not in visited:
                queue.push((successor, path + [action]))

    return []


def uniformCostSearch(problem):
    """
    Search the node of least total cost first.
    """
    from util import PriorityQueue
    start_time = time.perf_counter()

    pq = PriorityQueue()
    visited = {}
    pq.push((problem.getStartState(), [], 0), 0)  # (state, path, cost)

    while not pq.isEmpty():
        state, path, cost = pq.pop()

        if state in visited and visited[state] <= cost:
            continue

        visited[state] = cost

        if problem.isGoalState(state):
            end_time = time.perf_counter()
            print(f"UCS Execution Time: {end_time - start_time:.5f} seconds")
            return path

        for successor, action, step_cost in problem.getSuccessors(state):
            new_cost = cost + step_cost
            if successor not in visited or visited[successor] > new_cost:
                pq.push((successor, path + [action], new_cost), new_cost)

    return []


def nullHeuristic(state, problem=None):
    """
    A trivial heuristic for A* search.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    from util import PriorityQueue
    start_time = time.perf_counter()

    pq = PriorityQueue()
    visited = {}
    pq.push((problem.getStartState(), [], 0), 0)  # (state, path, cost)

    while not pq.isEmpty():
        state, path, cost = pq.pop()

        if state in visited and visited[state] <= cost:
            continue

        visited[state] = cost

        if problem.isGoalState(state):
            end_time = time.perf_counter()
            print(f"A* Execution Time: {end_time - start_time:.5f} seconds")
            return path

        for successor, action, step_cost in problem.getSuccessors(state):
            new_cost = cost + step_cost
            priority = new_cost + heuristic(successor, problem)
            if successor not in visited or visited[successor] > new_cost:
                pq.push((successor, path + [action], new_cost), priority)

    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
ucs = uniformCostSearch
astar = aStarSearch
