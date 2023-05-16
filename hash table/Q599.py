class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        """
        https://leetcode.com/problems/minimum-index-sum-of-two-lists/
        Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants 
        represented by strings.
        You need to help them find out their common interest with the least list index sum. If there is a choice tie between 
        answers, output all of them with no order requirement. You could assume there always exists an answer. 
        """
        restaurants = {}
        
        for res in list1:
            if res in list2:
                restaurants[res] = list1.index(res) + list2.index(res)
        
        lst_res = []
        for restaurant in restaurants:
            if restaurants[restaurant] == min(restaurants.values()):
                lst_res.append(restaurant)
        return lst_res
