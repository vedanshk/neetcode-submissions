class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows = len(board)
        cols = len(board[0])
        visited = set()

        def dfs(row, col, word_index):
            # Base case: matched all letters
            if word_index == len(word):
                return True

            # Bounds check + letter match check + visited check
            if (row < 0 or row >= rows or
                col < 0 or col >= cols or
                board[row][col] != word[word_index] or
                (row, col) in visited):
                return False

            # Mark this cell as used for this path
            visited.add((row, col))

            # Try all 4 neighbors for the next letter
            found = (dfs(row + 1, col, word_index + 1) or
                     dfs(row - 1, col, word_index + 1) or
                     dfs(row, col + 1, word_index + 1) or
                     dfs(row, col - 1, word_index + 1))

            # Backtrack: unmark this cell so other paths can use it
            visited.remove((row, col))

            return found

        # Try starting the search from every cell
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False




        