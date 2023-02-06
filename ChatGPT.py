from PyKakao import KoGPT

# KoGPT API 인스턴스 생성
GPT = KoGPT(service_key = "94c513ac26370fe7d8e48c4a3c8baeec")

# 문장을 input()을 활용하여 입력받기
prompt = input("문장을 입력하세요: ")
max_tokens = 128
result = GPT.generate(prompt, max_tokens, temperature=0.7, top_p=0.8)


# 문장이 끝이 안나면 이전 .까지 자르고 다시 .을 붙여서 출력
if result['generations'][0]['text'].split(".")[-1] != "":
    print(result['generations'][0]['text'].split(".")[0] + '.')
else:
    print(result['generations'][0]['text'])