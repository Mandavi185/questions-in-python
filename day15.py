class Solution(object):
    def numberOfSubmatrices(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        result = 0
        x_count = [0] * cols
        y_count = [0] * cols

        for i in range(rows):
            # update column counts
            for j in range(cols):
                if grid[i][j] == 'X':
                    x_count[j] += 1
                elif grid[i][j] == 'Y':
                    y_count[j] += 1

            # now check prefix sums
            x = 0
            y = 0
            for j in range(cols):
                x += x_count[j]
                y += y_count[j]

                if x == y and x > 0:
                    result += 1

        return result
