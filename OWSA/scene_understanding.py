import base64
from typing import Dict
import requests

API_KEY = ""  # 配置API密钥
API_BASE_URL = "" # 配置API地址

def _auth_headers() -> Dict[str, str]:
    return {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

def get_initial_description(image_path: str) -> str:
    with open(image_path, "rb") as image_file:
        image_base64 = base64.b64encode(image_file.read()).decode("utf-8")

    data = {
        "model": "Qwen/Qwen2.5-VL-72B-Instruct",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": (
                            "提取这张图片中的所有内容和信息。在提取信息时，请关注以下方面的细节："
                            "场景：描述图片呈现的整体场景，例如室内、室外、自然景观、城市街道等。"
                            "物体：列举图片中出现的所有物体，并明确其具体数量。"
                            "具体位置：说明每个物体在图片中的具体位置。"
                            "颜色：指出重要物体或场景的主要颜色。"
                            "确保涵盖上述各个方面的内容，尽量提供丰富、全面的描述。"
                        ),
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_base64}",
                        },
                    },
                ],
            }
        ],
    }

    response = requests.post(
        f"{API_BASE_URL}/chat/completions",
        headers=_auth_headers(),
        json=data,
    )
    return response.json()["choices"][0]["message"]["content"]

