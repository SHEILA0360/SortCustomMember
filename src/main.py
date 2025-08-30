import os

# api.jsonのパスを指定
api_path = os.path.join(os.path.dirname(__file__), '../api.json')

# api.jsonを読み取って表示
with open(api_path, 'r', encoding='utf-8') as f:
    api_key = f.read().strip()

# API周りの設定
region = "jp"
players =[
    {"mame"}
]