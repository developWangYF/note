import redis
r = redis.Redis(host='110.42.193.168', port=6379, decode_responses=True, charset='UTF-8', encoding='UTF-8')

r.set('name1', 'chenge')   
#添加
r.set('name2', '辰哥')   
#添加
print(r.get('name1'))   
#获取
print(r.get('name2'))