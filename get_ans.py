import os
from openai import OpenAI

# 初始化AI问答环境

client = OpenAI(
    api_key = "YOUR_API_KEY",
    base_url = "YOUR_BASE_URL",
)
# 模型名称
model_name="YOUR_MODEL_NAME"
# 初始系统提示
system_prompt="你是一个友好的助手，请用简短的语言回答问题，每次回复不要超过50个字"
# 回答结尾提示信息
end_prompt_information="——AI自动回复"

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
