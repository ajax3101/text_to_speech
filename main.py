
import json
import os
import time
import requests




def text_to_speech(text="Привет!"):
    headers = {"Authorization": f"Bearer {os.getenv(API_Key)}"}
    url ="https://api.edenai.run/v2/audio/text_to_speech"

    payload={
        "providers": "google", 
        "language": "ru-RU", 
        "option":"FEMALE",
        "google": "ru-RU-Standard-A", 
        "text": f"{text}"
        }
    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)
    unix_time = int(time.time())

    with open(f'{unix_time}.json', 'w') as file:
        json.dump(result, file, indent=4, ensure_ascii=False)

    #print(result['google']['audio'])



def main():
    text_to_speech(text="Благодаря масштабированию бизнес сможет увеличить продажи, прибыль и клиентскую базу, сгенерировать новые идеи. А еще это возможность стать более устойчивыми и конкурентоспособными, – говорят в Google Украина. – Поэтому Google стремится помочь украинскому бизнесу расширить возможности благодаря экспорту услуг и товаров на новые рынки")


if __name__ == "__main__":
    main()