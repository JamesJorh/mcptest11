# API客户端调试示例
import requests

def fetch_data():
    response = requests.get('https://api.example.com/data')
    return response.json()