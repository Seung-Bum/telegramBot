import requests
import json
from bs4 import BeautifulSoup
# 채팅방 주소: t.me/pika_231216_bot.

bot_token = "6929602386:AAGrxMLCsdXYGssgnpcoQe_6avoBOQmmtXk"
chat_id = "6685064774"


def get_update():
    # 쳇봇에 입력된 내용이 업데이트 되있으면 내용을 가져오는 api
    url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
    res = requests.get(url)
    if res.status_code == 200:
        return json.loads(res.text)


def send_message(message=None):
    # message가 없을 경우 입력 실행
    if not message:
        message = "다시 입력해주세요."
    # 탤레그램 채팅방으로 메시지를 발송
    data = {"chat_id": chat_id, "text": message}
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    res = requests.get(url, data=data)
    if res.status_code == 200:
        return json.loads(res.text)


keyword = input("keyword: ")
url = f"https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query={keyword}"

res = requests.get(url)

if res.status_code == 200:
    html = res.text
    soup = BeautifulSoup(html, "html.parser")
    new_title = soup.select(".news_tit")

    title_list = []

    for title in new_title:
        print(title.text)
        print(title["href"])
        title_list.append(f"{title.text}\n{title['href']}")
        print()

    # 각 라인을 join 앞의 글자를 기준으로 합침
    message = "\n\n".join(title_list)
    send_message(message)
