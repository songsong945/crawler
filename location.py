import json
from urllib.request import urlopen, quote
import xlrd

def getlnglat(address):
    url = 'http://api.map.baidu.com/geocoder/v2/'
    output = 'json'
    ak = '0XyetZluX2PavwFSkd1Yku8Zz0D0unQP' # 浏览器端密钥
    address = quote(address) # 由于本文地址变量为中文，为防止乱码，先用quote进行编码
    uri = url + '?' + 'address=' + address  + '&output=' + output + '&ak=' + ak 
    req = urlopen(uri)
    res = req.read().decode() 
    temp = json.loads(res)
    lat = temp['result']['location']['lat']
    lng = temp['result']['location']['lng']
    print(str(lat)+" "+str(lng))

def run():
    readbook = xlrd.open_workbook(r'location2.xlsx')
    rtable = readbook.sheets()[0]
    nrows = rtable.nrows
    values = rtable.col_values(0)
    for value in values:
        getlnglat(value)

if __name__=='__main__':
    run()