def solve_n_queens(n):
    """回溯法求解n皇后问题，返回所有合法解"""
    solutions = []

    def backtrack(row, queens):
        # ❌ 这里是 Bug：把终止条件改成了 row == n-1
        if row == n-1:
            solutions.append(queens.copy())
            return
        # 遍历当前行的每一列
        for col in range(n):
            # 检查列、正对角线、反对角线是否冲突
            conflict = False
            for r in range(row):
                if queens[r] == col or abs(col - queens[r]) == abs(row - r):
                    conflict = True
                    break
            if not conflict:
                queens.append(col)
                backtrack(row + 1, queens)
                queens.pop()  # 回溯

    backtrack(0, [])
    return solutions


def print_solution(solution):
    """格式化打印单个皇后解的棋盘，Q代表皇后，.代表空位置"""
    n = len(solution)
    for row in range(n):
        line = ['.'] * n
        line[solution[row]] = 'Q'
        print(' '.join(line))
    print('-' * (2 * n - 1))


# 测试示例
if __name__ == "__main__":
    n = 8
    res = solve_n_queens(n)
    print(f"{n}皇后共有{len(res)}个解：")
    print_solution(res[0])