class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
      """
      You are given a positive integer arrivalTime denoting the arrival time of a 
      train in hours, and another positive integer delayedTime denoting the amount 
      of delay in hours.
      """
        final_time = arrivalTime + delayedTime
        if final_time < 24:
            return final_time
        else:
            return final_time % 12
