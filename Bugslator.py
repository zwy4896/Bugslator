#################################
#       Bugslator by Wuyang     #
#           @2017/2/11          #
#              v1.1             #
#################################
import urllib.parse as up
import urllib.request as ur
import hashlib
import json
import random

url = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
tolang = input("请输入目标语言:")   #目标语言 zh为中文 en为英文
word = input("请输入要翻译的内容:")   #需要翻译的句子或单词
#key和appid在注册成为百度翻译开放平台开发者后由系统生成
key = 'XXXXXXXXXXXX'
appid = 'XXXXXXXXXXXXX'

salt = random.randint(32768, 65536)    #生成随机数
fromlang = 'auto'    # 源语言 auto为自动识别
#加密算法
sign0 = appid + word + str(salt) + key
sign = (hashlib.md5(sign0.encode(encoding='utf-8'))).hexdigest()

data = {}
data['q'] = word
data['from'] = fromlang
data['to'] = tolang
data['appid'] = appid
data['salt'] = salt
data['sign'] = sign


data = up.urlencode(data).encode('utf-8')

response = ur.urlopen(url, data)
html = response.read().decode('utf-8')

target = json.loads(html)    #处理json格式的返回结果
print("翻译结果：%s" % (target['trans_result'][0]['dst']))
