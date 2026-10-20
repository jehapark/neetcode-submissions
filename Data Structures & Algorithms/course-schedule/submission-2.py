class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjMap = { i : [] for i in range(numCourses) }
        for crs, pre in prerequisites:
            adjMap[crs].append(pre)

        courseSet = set()
        def dfs(course):
            if course in courseSet:
                return False
            if adjMap[course] == []:
                return True

            courseSet.add(course)
            for crs in adjMap[course]:
                if not dfs(crs): return False
            courseSet.remove(course)
            adjMap[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course): return False
        return True