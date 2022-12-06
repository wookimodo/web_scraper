# 웹 스크래핑 코드
# 텔레그램 push
# django DB 저장하기

import requests
from bs4 import BeautifulSoup # BeautifulSoup 객체를 만들어서 select 사용할 것임.
import telegram
import env_info # 베이스 기준으로 바로 import 가능
from hotdeal.models import Deal


TLGM_BOT_API = env_info.TLGM_BOT_API
tlgm_bot = telegram.Bot(TLGM_BOT_API)
# 데이터를 가져옴
url = "https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu"
res = requests.get(url)
# res.text -> 해당 url의 html 가져옴
# "html.parser" -> html문서를 가져왔기 때문에.
# BeautifulSoup 객체는 요소값을 지정할 수 있음. 패턴을 찾아서 잘 가져와야 함.
soup = BeautifulSoup(res.text, "html.parser")
# print(soup)
# select는 매칭되는 모든 요소를 리스트로 가져옴. 각 요소가 리스트로 반환됨.
items = soup.select("tr.list1, tr.list0")
# 변수 설정 : img_url, title, link, replay_count, up_count
# .strip() 은 혹시 모를 공백 제거.
# IndexError 예외처리해줘야함

# 버전에 따라 다르긴 하지만, run()함수로 싸줘야 실행이 됨.
def run():
  for item in items:
    try:
      img_url = item.select("img.thumb_border")[0].get("src").strip()
      title = item.select("a font.list_title")[0].text.strip()
      # "a font.list_title"를 싸고 있는 태그의 href요소를 가져와라.
      link = item.select("a font.list_title")[0].parent.get("href").strip()
      link = "https://www.ppomppu.co.kr/zboard/" + link.replace("/zboard/", "").lstrip('/')
      reply_count = item.select("td span.list_comment2 span")[0].text.strip()
      up_count = item.select("td.eng.list_vspace")[-2].text.strip()
      up_count = up_count.split("-")[0]
      up_count = int(up_count)
      
      
      if up_count >= 3:
        # if(Deal.objects.filter(link__iexact=link).count()==0) -> DB에 저장되어 있는 link 수가 0이라면, 즉 없다면. 중복제거하기 위해서.
        # 텔레그램 봇으로 push
        # link__iexact : 대소문자 구분없이
        # link__iexact 여기서 link는 컬럼명.
        
        if(Deal.objects.filter(link__iexact=link).count()==0):
          chat_id = env_info.chat_id
          message = f"{title}"
          # tlgm_bot.sendMessage(chat_id, 전송_message)
          tlgm_bot.sendMessage(chat_id, message)
          # image_url=img_url 여기서 앞의 image_url은 Deal에서 정의돼있는 컬럼명, 뒤의 image_url은 여기서 긁어온 데이터.
          Deal(img_url=img_url, title=title, link=link, reply_count=reply_count, up_count=up_count).save()

        
    except Exception as e:
      continue