import random

# 게임을 위한 랜덤 숫자 생성
rn = ["0", "0", "0"]
rn[0] = str(random.randrange(0, 9, 1))
rn[1] = rn[0]
rn[2] = rn[0]
while (rn[0] == rn[1]):
    rn[1] = str(random.randrange(1, 9, 1))
while (rn[0] == rn[2] or rn[1] == rn[2]):
    rn[2] = str(random.randrange(1, 9, 1))

# print(rn)

t_cnt = 0  # 시도횟수
s_cnt = 0  # 스트라이크 갯수
b_cnt = 0  # 볼 갯수

print("숫자야구게임을 시작합니다 !!!")
print("---------------------------")
while (s_cnt < 3):
    num = str(input("숫자 3자리를 입력하세요 : "))

    # 3자리만 입력할 수 있도록 함
    while len(num) != 3 or not num.isdigit() or not all(0 <= int(digit) <= 9 for digit in num):
        print("0~9 사이의 숫자 3자리를 입력해주십시오.")
        num = input("숫자 3자리를 입력하세요 : ")

    s_cnt = 0
    b_cnt = 0

    for i in range(0, 3): # 시도 횟수
        for j in range(0, 3):
            if (num[i] == str(rn[j]) and i == j):
                s_cnt += 1
            elif (num[i] == str(rn[j]) and i != j):
                b_cnt += 1

    if (s_cnt == 0) and (b_cnt == 0):
        print("결과 : OUT")
    else:
        print("결과 : [", s_cnt, "] Strike [", b_cnt, "] Ball")
    t_cnt += 1
print("---------------------------")
print(t_cnt, "번 만에 정답을 맞추셨습니다.")












# 마우스 커서 이미지 불러오기
cursor_image = pygame.image.load("C:/Users/sally/PycharmProjects/pythonProject2/코딧 프로젝트/bat.jpg")
cursor_image = pygame.transform.scale(cursor_image, (24, 24))

# 커서 설정
cursor_data, mask_data = pygame.cursors.compile(cursor_image.get_buffer(), black='X', white='.', xor='o')
cursor = pygame.cursors.Cursor((24, 24), (0, 0), cursor_data, mask_data)
pygame.mouse.set_cursor((24, 24), (0, 0), *cursor)