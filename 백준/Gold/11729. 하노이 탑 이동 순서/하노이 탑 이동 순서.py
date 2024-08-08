def move_the_block(k, start_point, end_point):
    if k == 1:
        print(start_point, end_point)
    else:
        tmp = [1, 2, 3]
        tmp.remove(start_point)
        tmp.remove(end_point)
        middle_point = tmp[0]

        move_the_block(k-1, start_point, middle_point)
        print(start_point, end_point)
        move_the_block(k-1, middle_point, end_point)

N = int(input())
move_count = 2**N - 1

print(move_count)
move_the_block(N, 1, 3)