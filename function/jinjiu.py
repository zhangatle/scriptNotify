import os

import requests

goodsId = [116, 117]
authorization_token = os.environ["JINJIU_TOKEN"] if os.environ.get(
    'JINJIU_TOKEN') else "JYJwx eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJKWUp3eCAiOiJhZjE1NmU0Ni0zZjMxLTRjZTctODgxOS04YTA3YTliZjJjMDIifQ.vCi48AxTpsKSHWC45XnYsjWDKZNYJ0qnMx12BI3kjLgX0u8BlLnZCTuLv_AveloQ_tJgDvnReK16OhQbNrJDEw"

for item in goodsId:
    headers = {
        "authorization": authorization_token
    }
    try:
        response = requests.get(f"https://jjw.jingjiu.com/app-jingyoujia/app/jingyoujia/goodsInfo/{item}",
                                headers=headers)
        res_json = response.json()
        goodsInventory = res_json["data"]["goodsInventory"]
        goodsName = res_json["data"]["goodsName"]
        print(f"{goodsName} : {goodsInventory}")
        if goodsInventory > 0:
            print("abc")
            # Assuming there's a Functions class with a sendBark method for notification
            # Replace this line with the appropriate notification function in your Python environment.
            # Functions.sendBark(f"{goodsName} 有库存了，请前往购买， 库存 {goodsInventory}")
    except:
        print("error")
