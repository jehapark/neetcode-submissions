class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hashset = {i: [] for i in range(numCourses)} 
        for crs, pre in prerequisites:
            hashset[crs].append(pre)

        output = []
        visiting, cycle = set(), set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visiting:
                return True

            cycle.add(crs)
            for pre in hashset[crs]:
                if not dfs(pre):
                    return False
            
            cycle.remove(crs)
            visiting.add(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        
        return output