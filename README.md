# ai_hw01_8queens

本项目采用 回溯法 (Backtracking) 求解八皇后（N皇后）问题。在 VS Code 中打开终端（Terminal -> New Terminal）。
2. 执行测试命令：
进入 hw01 目录，运行 pytest 测试。
# 进入作业目录
cd hw01
pytest tests/test_8queens.py -v
显示 3 passed，说明代码逻辑正确，能通过所有校验（解数正确性、返回格式正确性）如果出现报错，通常是因为逻辑错误（如递归终止条件设置不当），导致返回空列表或解的数量不符。
造 Bug：我故意将递归终止条件从 if row == n: 修改为 if row == n-1:。这会导致程序少遍历最后一行，永远无法凑齐 N 个皇后，导致测试断言失败（AssertionError: assert 0 == 2）修 Bug：通过 AI 辅助分析，发现错误在于递归终止条件。将 n-1 还原为 n，即可完成最后一行的放置，修复后所有测试用例通过。
