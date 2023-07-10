class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
      """
      Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
      The overall run time complexity should be O(log (m+n)).

      https://leetcode.com/problems/median-of-two-sorted-arrays/description/
      """
        l = []

        l.extend(nums1)
        l.extend(nums2)
        l.sort()

        if len(l) % 2 != 0:
            index = (len(l) // 2)

            return l[index]
        else:
            index = (len(l) // 2)

            return (l[index] + l[index - 1]) / 2
