import os
from openai import OpenAI

# 初始化AI问答环境

client = OpenAI(
    api_key = "d193273f-5fd9-4ad7-8bdd-c23397145fdc",
    base_url = "https://ark.cn-beijing.volces.com/api/v3",
)
# 模型名称
model_name="ep-20250201132243-cswlp"
# 初始系统提示
system_prompt="你是一个友好的助手，请用简短的语言回答问题，每次回复不要超过50个字"
# 回答结尾提示信息
end_prompt_information="——AI自动回复，输入stop即可停止"

# 获取回答
def answer_message(user_id,message):
    try:
        completion = client.chat.completions.create(
            model=model_name,  # 模型名称
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": message},
            ],
        )

        # 获取回答
        ans=completion.choices[0].message.content
        return f"{ans}    {end_prompt_information}"
    except Exception as e:
        print("调用API失败");
        return "抱歉，AI似乎出了点问题，请稍后再试"

#print(answer_message("XXRKSJLYC","你好啊"))