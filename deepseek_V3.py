
from openai import OpenAI

def V3(prompt,apikey):
    client = OpenAI(api_key=apikey, base_url="https://api.deepseek.com")
    response = client.chat.completions.create(
        model='deepseek-chat',
        messages=[
            {'role': 'user', 'content':prompt}
        ],
        stream=False
        #temperature=1.0
        #可以设置temperature值,默认1.0,设置格式如上
        #如下是官方文档给出的建议参考数据
        #代码生成/数学解题:0.0
        #数据抽取/分析:1.0
        #通用对话:1.3
        #翻译:1.3
        #创意类写作/诗歌创作:1.5
)
    
    print(response.choices[0].message.content)

if __name__ == '__main__':
    prompt = input('>>>')
    apikey = 'sk-d7b2be184ea6488abc485a1d5ed8a41'
    V3(prompt,apikey)