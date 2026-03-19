import os
import sys
from openai import OpenAI
import sqlite3
import json

from db import get_user_api


def get_base_path():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))


def resource_path(*paths):
    return os.path.join(get_base_path(), *paths)


# ⭐ 角色映射（中文 → prompt文件名）
ROLE_MAP = {
    "希佩尔": "hipper",
    "企业": "enterprise",
    "塔什干": "tashkent"
}


class Chat:

    def __init__(self, role="hipper"):
        # ⭐ 统一角色（防中文路径问题）
        self.role = ROLE_MAP.get(role, role)

        # ===== 用户配置 =====
        self.username, self.model = self.load_username()
        if not self.username or not self.model:
            raise Exception("config.json 未正确配置 username / model")

        api_key, base_url = get_user_api(self.username)
        if not api_key:
            raise Exception("数据库未配置 API key")

        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url
        )

        # ===== 加载 persona =====
        persona_file = resource_path(f"prompt/{self.role}.txt")

        if not os.path.exists(persona_file):
            raise Exception(f"找不到角色 prompt 文件: {persona_file}")

        self.persona_text = self.load_persona_from_txt(persona_file)

        self.SYSTEM_PROMPT = self.persona_text

        # ⭐ 上下文（每个 Chat 实例独立）
        self.messages = [
            {"role": "system", "content": self.SYSTEM_PROMPT}
        ]

    # =============================
    # 加载用户配置
    # =============================
    def load_username(self):
        try:
            with open("config.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                return data.get("username"), data.get("model")
        except:
            return None, None  # ⭐ 修复 bug

    # =============================
    # 加载角色 prompt
    # =============================
    def load_persona_from_txt(self, path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    # =============================
    # ⭐ 核心聊天
    # =============================
    def chat(self, user_text):
        # 1️⃣ 用户输入
        self.messages.append({
            "role": "user",
            "content": user_text
        })

        # 2️⃣ 请求 AI
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages
        )

        reply = response.choices[0].message.content

        # 3️⃣ 保存 AI 回复（上下文记忆关键）
        self.messages.append({
            "role": "assistant",
            "content": reply
        })

        # ⭐ 限制上下文长度（防爆token）
        if len(self.messages) > 20:
            self.messages = [self.messages[0]] + self.messages[-18:]

        return reply