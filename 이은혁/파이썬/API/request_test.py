import requests
url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1021'
response = requests.get(url).json()
# response = requests.get("https://api.agify.io/?name=jun").json()
for i in range(6):
    print(response.get(f'drwtNo{i+1}'), end=" ")
print(response.get('bnusNo'))