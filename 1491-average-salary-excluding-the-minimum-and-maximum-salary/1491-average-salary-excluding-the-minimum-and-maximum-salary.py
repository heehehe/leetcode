class Solution:
    def average(self, salary: List[int]) -> float:
        return sum([s for s in salary if s != max(salary) and s!= min(salary)]) / (len(salary) - 2)