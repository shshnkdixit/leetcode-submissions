class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7

        dp_right = [[0] * n for _ in range(m)]
        dp_down = [[0] * n for _ in range(m)]

        # Robot starts at (0, 0)
        if m == 1 and n == 1:
            return 1

        # Initial possible moves
        if n > 1:
            dp_right[0][1] = 1

        if m > 1:
            dp_down[1][0] = 1

        for r in range(m):
            for c in range(n):

                # Destination reached
                if r == m - 1 and c == n - 1:
                    return (dp_right[r][c] +
                            dp_down[r][c]) % MOD

                # Starting cell is already occupied
                if r == 0 and c == 0:
                    continue

                right = dp_right[r][c]
                down = dp_down[r][c]

                if grid[r][c] == 1:
                    # Mirror redirects RIGHT to DOWN
                    if right and r + 1 < m:
                        dp_down[r + 1][c] = (
                            dp_down[r + 1][c] + right
                        ) % MOD

                    # Mirror redirects DOWN to RIGHT
                    if down and c + 1 < n:
                        dp_right[r][c + 1] = (
                            dp_right[r][c + 1] + down
                        ) % MOD

                else:
                    # Empty cell: robot can move RIGHT or DOWN
                    total = (right + down) % MOD

                    if c + 1 < n:
                        dp_right[r][c + 1] = (
                            dp_right[r][c + 1] + total
                        ) % MOD

                    if r + 1 < m:
                        dp_down[r + 1][c] = (
                            dp_down[r + 1][c] + total
                        ) % MOD

        return 0