from flask import Flask,request,jsonify
import requests

app = Flask(__name__)


def fetch_conversion_factor(curr_currency,req_currency):
    url = "https://api.currencyapi.com/v3/latest?apikey=cur_live_e4MFWmQOY2WTmuU3dSVyXcwNxXeZ0xXfjGoKkyEG"
    res = requests.get(url)
    # print(res)
    print(curr_currency,"   ",req_currency)
    print("hello...........................")
    res = res.json()
    curr_value = res['data'][curr_currency]['value']
    req_value = res['data'][req_currency]['value']
    factor = req_value / curr_value
    print(factor)
    return factor


@app.route('/',methods=['POST'])

def index():
    data = request.get_json()
    # print(data)
    # https://api.currencyapi.com/https://api.currencyapi.com/v3/latest?apikey=cur_live_e4MFWmQOY2WTmuU3dSVyXcwNxXeZ0xXfjGoKkyEG
    amount = data['queryResult']['parameters']['unit-currency']['amount']
    curr_currency = data['queryResult']['parameters']['unit-currency']['currency']
    need_currency = data['queryResult']['parameters']['currency-name']
    print(amount,"  ",curr_currency,"   ",need_currency)
    cf = fetch_conversion_factor(curr_currency,need_currency)
    print("cf : ",cf)
    result = amount * cf
    result = round(result,2)
    print("result : ",result)
    response = {
        "fulfillmentText" : '{} {} is {} {}'.format(amount,curr_currency,result,need_currency)
    }
    print(response)
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True,port=5000)
