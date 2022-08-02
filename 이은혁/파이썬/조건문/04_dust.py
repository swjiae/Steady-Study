dust=7

# dust 변수에 들어있는 값을 

if 150<dust:
    print("졸라나쁨")
elif 80 < dust and dust <= 150:
    print("나쁨")
elif 30 < dust and dust <= 80:
    print("보통")
else:
    print("졸라좋음")

my_level=1631
if my_level>=1490:
    print("'아브렐슈드'는 1490 이상만이 도전 가능합니다.")
elif my_level>=1475:
    print("'쿠크세이튼'은 1475 이상만이 도전 가능합니다.")
elif my_level>=1430:
    print("'비아키스'는 1430 이상만이 도전 가능합니다.")
elif my_level>=1415:
    print("'발탄'은 1415 이상만이 도전 가능합니다.")
else:
    print("아직 레벨이 낮습니다.")