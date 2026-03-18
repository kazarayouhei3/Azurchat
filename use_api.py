import os
import sys
from openai import OpenAI
import sqlite3
import json
def get_base_path():
    # 打包后
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    # 开发环境
    return os.path.dirname(os.path.abspath(__file__))

def resource_path(*paths):
    return os.path.join(get_base_path(), *paths)

class Chat():

    def __init__(self, role="hipper"):

        self.role = role

        self.username, self.model = self.load_username()
        print(self.username, self.model)
        api_key, base_url = self.load_api_from_db(self.username)

        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url
        )

        persona_file = resource_path(f"prompt/{self.role}.txt")
        self.persona_text = self.load_persona_from_txt(persona_file)

        self.SYSTEM_PROMPT = f"""
            {self.persona_text}
            """

        self.messages = [
            {"role": "system", "content": self.SYSTEM_PROMPT}
        ]

    def load_username(self):

        try:
            with open("config.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                return data.get("username"), data.get("model")
        except:
            return None

    def load_persona_from_txt(self, path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    def load_api_from_db(self, username):

        conn = sqlite3.connect("chat.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT api, url FROM users WHERE username=?",
            (username,)
        )

        result = cursor.fetchone()

        conn.close()

        if result:
            return result[0], result[1]
        else:
            return None, None

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

