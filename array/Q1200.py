class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
      """
      https://leetcode.com/problems/minimum-absolute-difference/
      
      Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.


      """
        arr.sort()
        
        min_value = arr[1] - arr[0]
        pairs = [[arr[0], arr[1]]]
        
        for i in range(1, len(arr)-1):
            pair = []
            if min(min_value, arr[i+1] - arr[i]) < min_value:
                min_value = arr[i+1] - arr[i]
                pairs = []
            if arr[i+1] - arr[i] == min_value:
                pairs.append([arr[i], arr[i + 1]])
        return pairs
        
