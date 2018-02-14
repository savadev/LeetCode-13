"""
Find Median = Find N-st Smallest Number
Time Complexity: O(n)
"""
import math
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        length = len(nums1) + len(nums2)
        if length % 2 == 1:
            return findKthSortedList(nums1, nums2, (length + 1)/2)
        else:
            return (findKthSortedList(nums1, nums2, length/2) \
            + findKthSortedList(nums1, nums2, length/2 + 1)) / 2
    def findKthSortedList(self, nums1, nums2, n):
        # Find N-st number = find it in index n-1
        # Step1: Set base
        if not nums2: # where nums2 == null then Nst is in nums1[n-1]
            return nums1[n-1]
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        if not nums1: # where nums1 and nums2 == null
            return -1

        if n == 1: # the 1st element is what we need, so return the smallest one
            return min(nums1[0], nums2[0])
        if n > 1:
            # Step2: Approaching the base
            # Set any conditions you prefer as long as n is on its way to the base
            cutPointB = math.ceil(n/2)
            cutPointA = n - cutPointB
            if nums1[cutPointA-1] < nums2[cutPointB-1]:
                # drop nums1[cutPointA-1] because nums[cutPointA] >= nums[cutPointB]
                # then find (N-cutPointA)st Number
                return self.findKthSortedList(nums1[cutPointA:], nums2, n - cutPointA)
            elif nums1[cutPointA-1] > nums2[cutPointB-1]:
                return self.findKthSortedList(nums1, nums2[cutPointB:], n - cutPointB)
            else:
                # cutPointA == cutPointB
                return nums1[cutPointA-1]
                #return nums2[cutPointB-1]



if __name__ == "__main__":
    print("To Iterate Is Human; To Recurse, Divine.....FKDIS")
    assert Solution().findMedianSortedArrays((1, 5, 6), (4, 5)) == 5
