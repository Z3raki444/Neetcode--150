board = [["5","3",".",".","7",".",".",".","."]
,        ["6",".",".","1","9","5",".",".","."]
,        [".","9","8",".",".",".",".","6","."]
,        ["8",".",".",".","6",".",".",".","3"]
,        ["4",".",".","8",".","3",".",".","1"]
,        ["7",".",".",".","2",".",".",".","6"]
,        [".","6",".",".",".",".","2","8","."]
,        [".",".",".","4","1","9",".",".","5"]
,        [".",".",".",".","8",".",".","7","9"]]


nums = set()
for i in range(9):
    for j in range(9):
        if board[i][j] != '.':
            if board[i][j] + 'row' + str(i) in nums or board[i][j] + 'col' + str(j) in nums or board[i][j] + 'box' + str(i//3) + str(j//3) in nums:
                print(False)
                exit()
            nums.add(board[i][j] + 'row' + str(i))
            nums.add(board[i][j] + 'col' + str(j))
            nums.add(board[i][j] + 'box' + str(i//3) + str(j//3))
print(True)

print(nums)