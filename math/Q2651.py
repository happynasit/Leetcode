class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
      """
      """
        final_time = arrivalTime + delayedTime
        if final_time < 24:
            return final_time
        else:
            return final_time % 12
