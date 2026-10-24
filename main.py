board = []
for i in range(4):
    row = []
    for j in range(4):
        row.append("-")
    board.append(row)

for row in board:
    print("".join(row))