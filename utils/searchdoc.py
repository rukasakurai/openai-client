import os
import requests
import json

# オプションの例
# options = {
#     "history": [
#       {
#           "user": "就業規則とは何ですか？",
#           "bot": "就業規則は、労働者の労働条件や待遇の基準を定めるものであり、労働基準法に基づいて作成されます。就業規則は労働者に周知される必要があり、配付や掲示、電子媒体での記録などの方法で労働者に周知されます。就業規則の効力発生時期は、労働者に周知された日とされます。[001018385-2.pdf][001018385-0.pdf]"
#       },
#       {
#           "user": "先ほどの補足をして"
#       }
#   ],
#     "approach": "rrr",
#     "overrides": {
#         "gptModel": "gpt-3.5-turbo",
#         "temperature": "0.0",
#         "top": 5,
#         "semanticRanker": True,
#         "semanticCaptions": True
#     }
# }
def searchdoc_api(apim_endpoint, options):
    # エンドポイント URL（ローカルホストを仮定）
    url = apim_endpoint + 'docsearch'

    # POST リクエストのヘッダー
    headers = {
        "Content-Type": "application/json"
    }

    # POST リクエストのボディ
    body = {
        "history": options['history'],
        "approach": options['approach'],
        "overrides": options['overrides']
    }

    # POST リクエストを送信
    response = requests.post(url, headers=headers, data=json.dumps(body))

    # レスポンスの解析
    if response.status_code > 299 or not response.ok:
        try:
            parsed_response = response.json()
            error_message = parsed_response.get('error', 'Unknown error')
        except json.JSONDecodeError:
            error_message = 'Unknown error'
        raise Exception(error_message)

    return response.json()