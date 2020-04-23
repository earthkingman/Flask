from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
import requests # http 요청을 보내는 모듈
from time import sleep
import json # 효율적으로 데이터를 저장하고 교환하는데 사용하는 텍스트 데이터 포맷


# 플라스크 객체 생성
app = Flask(__name__)


def send_message(msg): # 카카오톡 메시지 보내기

    header = {"Authorization" : "Bearer j4DrLb7D3d5GES_28QR6bH6a6MIZ1LQat_bAcworDKYAAAFxi71fHA"}
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    post = {
        "object_type": "text",
        "text": msg,
        "link": {
            "web_url": "https://developers.kakao.com",
            "mobile_web_url": "https://developers.kakao.com"
        },
        "button_title": "바로 확인"
    }
    data = {"template_object" : json.dumps(post)}
    return requests.post(url, headers=header, data=data)

def get_mask_stock(adr): # 마스크 재고 확인

    global url
    stock_msg = ''
    params = {'address' : adr}
    # config
    url = 'https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByAddr/json'
    json_obj = requests.get(url,params=params).json()

    for store in json_obj['stores']:
        if store['remain_stat']:
            stock_msg += store['name'] + ' ' + store['remain_stat'] + ' ' + store['stock_at'] + '\n'
    return stock_msg

# @app.route('/coronamap')
# def coronamap():
    
#     return render_template('coronamap.html')


@app.route('/corona',methods=['GET','POST'])
def corona():

    if request.method == 'GET':
         return render_template('coronamap.html')

    if request.method == 'POST':
        data = request.form['data']
        str(data)
        print("받은 데이타 "+data)
        send_message(get_mask_stock(data))
        return data #리턴을 하고 안하고에 따라서 오류가 발생하고 안한다  프론트에서 ajax 요청을하고 서버에서 응답을 하는데 서버에서 return으로 응답을 해줘야 
        #TypeError: The view function did not return a valid response. The function either returned None or ended without a return statement. 오류가 안뜬다.
  
     
if __name__ == "__main__":              
    app.run( port="3000", debug=True)


