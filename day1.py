# Robots collision
class Solution(object):
    def survivedRobotsHealths(self, positions, healths, directions):
        n = len(positions)

        robots = sorted([(positions[i], healths[i], directions[i], i) for i in range(n)])
        stack = []
        healths = healths[:]
        for pos, h, d, i in robots:
            if d == 'R':
                stack.append(i)
            else:
                while stack and healths[i] > 0:
                    j = stack[-1]
                    if healths[j] < healths[i]:
                        stack.pop()
                        healths[i] -= 1
                        healths[j] = 0
                    elif healths[j] > healths[i]:
                        healths[j] -= 1
                        healths[i] = 0
                    else:
                        stack.pop()
                        healths[i] = 0
                        healths[j] = 0

        return [healths[i] for i in range(n) if healths[i] > 0]        
        
