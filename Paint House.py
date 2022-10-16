#Time Complexity:: Average: O(m*n)
#Space Complexity:: O(1)
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
#Paint House

costs = [[17,2,17],[16,16,5],[14,3,19]]

for i in range(len(costs)-2,-1,-1):
    costs[i][0] += min(costs[i+1][1], costs[i+1][2])
    costs[i][1] += min(costs[i+1][0], costs[i+1][2])
    costs[i][2] += min(costs[i+1][0], costs[i+1][1])

print(min(costs[0]))