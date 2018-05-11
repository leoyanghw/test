#!/bin/python
import TencentYoutuyun
import json
appid='10130422'
secret_id = 'AKID7CD6rYXXoyyoU3fpEVcKyOjuBTuI8qzx'
secret_key = 'ymZI856HIXgfT9e1pcImBSYo0Uq482qU'
userid= '345393041'

end_point = TencentYoutuyun.conf.API_YOUTU_END_POINT       


youtu = TencentYoutuyun.YouTu(appid, secret_id, secret_key, userid, end_point)

ret = youtu.carclassify('http://www.buttoncar.com/wp-content/uploads/2018/04/WechatIMG276.jpeg',1)
jsret = json.dumps(ret)
f=open('result.txt','w+')
f.write(jsret)
f.close()
print ret



