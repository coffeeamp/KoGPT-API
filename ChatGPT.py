from PyKakao import KoGPT

# KoGPT API 인스턴스 생성
GPT = KoGPT(service_key = "YOUR_KEY")

prompt = ''

def chatbot(text):
    global prompt
    # 문장을 input()을 활용하여 입력받기
    prompt += "Q:" + text + "A:"
    max_tokens = 128
    
    result = GPT.generate(prompt, max_tokens, temperature=0.3, top_p=1)
    answer = result['generations'][0]['text']
    q = answer.find("Q")
    answer = answer[:q-1]
    prompt += answer
    print(answer)
    return answer
