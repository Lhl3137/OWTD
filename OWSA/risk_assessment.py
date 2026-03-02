import json
from typing import List, Dict, Any
import requests

API_KEY = ""  # 配置API密钥
API_BASE_URL = "" # 配置API地址

def _auth_headers() -> Dict[str, str]:
    return {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

def generate_final_report(
    oilwell_detections: List[Dict[str, Any]],
    initial_description: str,
) -> str:
    prompt = f"""生成一份专业的油井安全评估报告。请仔细阅读以下信息，并按照指示完成报告：

1. 油井检测结果：
- 检测到的油井数量：{len(oilwell_detections)}
- 油井位置信息：{json.dumps(oilwell_detections, ensure_ascii=False)}

2. 图像全局信息：
{initial_description}

在撰写报告时，请遵循以下指南：
1. 油井分布情况分析：根据提供的油井分布信息，分析油井的分布特点，并明确列出每口油井的具体坐标。
2. 场景环境描述：详细描述油井所在的场景环境，包括地理、气候、周边设施等情况。
3. 潜在的安全隐患或需要注意的问题：基于油井分布和场景环境，分析可能存在的安全隐患或需要特别注意的问题。
4. 建议的后续行动：针对潜在的安全隐患，提出具体的建议后续行动，如检查、维护、改进等。
请确保报告内容丰富、全面、专业，使用清晰、简洁的语言，避免使用行话或复杂的术语。

将生成的安全评估报告以标准HTML格式输出
"""

    data = {
        "model": "Qwen/Qwen3-235B-A22B-Instruct-2507",
        "messages": [
            {
                "role": "user",
                "content": prompt,
            }
        ],
    }

    response = requests.post(
        f"{API_BASE_URL}/chat/completions",
        headers=_auth_headers(),
        json=data,
    )
    return response.json()["choices"][0]["message"]["content"]

