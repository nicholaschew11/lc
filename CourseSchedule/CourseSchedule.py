class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        courseMap = {i:[] for i in range(numCourses)}
        visited = set()

        for i, j in prerequisites:
            courseMap[i].append(j)

        for i in range(numCourses):
            if not self.dfs(courseMap, visited, i): return False

        return True

    def dfs(self, graph, visited, course):
        
        if graph[course] == []:
            return True

        if course in visited:
            return False

        visited.add(course)

        for i in graph[course]:
            if not self.dfs(graph, visited, i):
                return False

        visited.remove(course)
        graph[course] = []
        return True