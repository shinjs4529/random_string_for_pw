import random
import string

random_strings = []
user_count = 19

for _ in range(user_count):
    first_char = random.choice(string.ascii_lowercase.replace('l', ''))  # 영어 소문자, 'l' 제외
    rest_chars = ''.join(random.choices(string.digits, k=4))  # 자연수 0~9
    random_string = first_char + rest_chars
    random_strings.append(random_string)

# 결과를 텍스트 파일로 저장
with open('random_strings.txt', 'w') as file:
    for idx, s in enumerate(random_strings, start=1):
        file.write(f"{s}\n")
        # 5번째 줄마다 줄바꿈 추가
        if idx % 5 == 0:
            # 10번째 줄마다 인덱스 표시
            if idx % 10 == 0:
                file.write(f"---{idx}---\n")
            else:
                file.write("\n")

print("텍스트 파일로 저장되었습니다: random_strings.txt")
