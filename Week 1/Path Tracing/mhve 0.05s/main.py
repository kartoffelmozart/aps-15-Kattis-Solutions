dir_to_vec = {
    'down': (1,0),
    'left': (0,-1),
    'up': (-1,0),
    'right': (0,1)
}

snake = [(0,0)]

while 1:
    try:
        vec = dir_to_vec[input()]
        snake.append((snake[-1][0]+vec[0] , snake[-1][1]+vec[1]))
    except EOFError:
        break
    
northmost = min(snake , key=lambda seg:seg[0])[0]
eastmost = max(snake , key=lambda seg:seg[1])[1]
southmost = max(snake , key=lambda seg:seg[0])[0]
westmost = min(snake , key=lambda seg:seg[1])[1]

for i,seg in enumerate(snake):
    snake[i] = (seg[0] - northmost, seg[1] - westmost)

inner_board_size = (southmost - northmost + 1 , eastmost - westmost + 1)

board = [['#'] * (inner_board_size[1] + 2)]
for _ in range(inner_board_size[0]):
    board.append(['#'] + [' ' for _ in range(inner_board_size[1])] + ['#'])
board.append(['#'] * (inner_board_size[1] + 2))

for i,seg in enumerate(snake):
    if board[seg[0] + 1][seg[1] + 1] == 'S': continue
    board[seg[0] + 1][seg[1] + 1] = 'S' if i == 0 else 'E' if i == len(snake) - 1 else '*'
    
output = '\n'.join([''.join(line) for line in board])
print(output)