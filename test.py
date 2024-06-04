from minesweeper import * 

field=Minesweeper()
field.print()

mines=[]

for i in range(field.height):
    for j in range(field.width):
        if field.board[i][j]:
            mines.append((i,j))

#print(mines)

print(field.board[2][2])
ai=MinesweeperAI()
ai.add_knowledge((7,7), 3)
ai.add_knowledge((7,6), 2)
ai.add_knowledge((7,5), 2)
ai.add_knowledge((6,6), 3)
print(ai.make_safe_move())
print(ai.make_random_move())
#print(ai.mines)


