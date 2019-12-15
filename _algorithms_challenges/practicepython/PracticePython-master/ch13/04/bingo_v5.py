import random

bingo = [i for i in range(16)]
random.shuffle(bingo)   #將排序打亂

bingo_4x4 = [[bingo[i + 4 * j] for i in range(4)]for j in range(4)]

for row in bingo_4x4:
    print(row)

print()

print("這是一個 4 X 4 賓果遊戲，")

bingo_flag = False

for i in range(16):
    input_num = int(input("請輸入1~16的數字: "))
    for index in range(16):
        if input_num == bingo[index]:
            row = index // 4
            col = index % 4
            bingo_4x4[row][col] = -1
    print()

    #判斷獲勝條件
    for a in range(4):
        if bingo_4x4[a][0] == -1 & bingo_4x4[a][1] == -1 & bingo_4x4[a][2] == -1 & bingo_4x4[a][3] == -1:
            bingo_flag = True
            break
    for a in range(4):
        if bingo_4x4[0][a] == -1 & bingo_4x4[1][a] == -1 & bingo_4x4[2][a] == -1 & bingo_4x4[3][a] == -1:
            bingo_flag = True
            break
    for a in range(4):
        if bingo_4x4[a][0] == -1 & bingo_4x4[a-1][1] == -1 & bingo_4x4[a-2][2] == -1 & bingo_4x4[a-3][3] == -1:
            bingo_flag = True
            break
    for a in range(4):
        if bingo_4x4[0][a] == -1 & bingo_4x4[1][a-1] == -1 & bingo_4x4[2][a-2] == -1 & bingo_4x4[3][a-3] == -1:
            bingo_flag = True
            break
    if bingo_flag == True:
        print("Bingo!!!")
        break
