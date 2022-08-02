import random

# menu = ['새마을식당','홍콩비밀반점','초원삼겹살']
# lunch = random.choice(menu) # 이 코드는 random 모듈을 불러와 choice 함수를 사용한 것이다.
# print(f'오늘 점심은 {lunch}입니다.')

numbers = range(1,46)
lucky = random.sample(numbers, 6)
print(f'오늘의 행운 번호는 {sorted(lucky)} 입니다')