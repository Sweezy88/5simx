import asyncio
import requests
from config import token as key

session = requests.Session()
headers={'Authorization': f'Bearer {key}', 'Accept': 'application/json'}

def balance():
    resp = session.get('https://5sim.net/v1/user/profile', headers = headers)
    if resp.status_code == 200:
        json = resp.json()
        print("Hesap:",json["email"], "\nHesap Bakiyesi:", json["balance"])
    elif resp.status_code == 401:
        print('API key hatalı.')
    session.close()

def buy(c, s):
  resp = session.get(f'https://5sim.net/v1/user/buy/activation/{c}/any/{s}')
  if resp.status_code == 200:
    try:
      json = resp.json()
    except:
      session.close()
      print('Kullanılabilir numara yok.')
      return
    print(f'Numara: {json["phone"]} ({json["price"]} RUB)\n',
          f'({json["country"]} - {json["product"]})\n\n')


  elif resp.status_code == 401:
    print('API key hatalı.')
    print(resp.text)
  elif resp.status == 400:
    print({'not enough user balance': 'Bakiye yetersiz.',
                                 'not enough rating': 'Puan yetersiz.',
                                 'bad country': 'Ülke geçersiz.',
                                 'no product': f'`{country}/{service}` için numara bulunamadı.',
                                 'server offline': '5sim.net yanıt vermedi.'}.get(text, 'Bilinmeyen bir hata oluştu.'))

  else:
    print('Bilinmeyen bir hata oluştu.')
    session.close()

buy("algeria", "tg")
