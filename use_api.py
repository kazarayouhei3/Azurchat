import os
import sys
from openai import OpenAI

def get_base_path():
    # 打包后
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    # 开发环境
    return os.path.dirname(os.path.abspath(__file__))

def resource_path(*paths):
    return os.path.join(get_base_path(), *paths)

class Chat():
    def __init__(self, role="hipper",model="deepseek-chat",api_key="",base_url="https://api.deepseek.com"):
        self.role = role
        persona_file = resource_path(f"{self.role}.txt")
        self.persona_text = self.load_persona_from_txt(persona_file)
        self.SYSTEM_PROMPT = f"""
            你必须始终扮演以下角色设定，不允许偏离。
            {self.persona_text}
            请保持角色语气，不要解释你是AI。
            """
        self.messages = [
            {"role": "system", "content": self.SYSTEM_PROMPT}
        ]
        self.client = OpenAI(
                    api_key=api_key,
                    base_url=base_url
        )

    def load_persona_from_txt(self, path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()


    def chat(self, user_text):
           # 1️⃣ 加入用户输入
           self.messages.append({
               "role": "user",
               "content": user_text
           })

           # 2️⃣ 请求
           response = self.client.chat.completions.create(
               model=self.model,
               messages=self.messages
           )

           reply = response.choices[0].message.content

           # 3️⃣ 保存 AI 回复
           self.messages.append({
               "role": "assistant",
               "content": reply
           })

           # 4️⃣ 返回给 UI
           return reply

    # ========= 生成开场白 =========
    def generate_opening(self):
        response = self.client.chat.completions.create(
            model="deepseek-chat",
            messages=self.messages + [
                {
                    "role": "user",
                    "content": "现在开始对话，请用角色语气主动说第一句话。"
                }
            ]
        )

        opening = response.choices[0].message.content

        self.messages.append({
            "role": "assistant",
            "content": opening
        })

        return opening

    # ========= 重置对话 =========
    def reset(self):
        self.messages = [
            {"role": "system", "content": self.SYSTEM_PROMPT}
        ]
