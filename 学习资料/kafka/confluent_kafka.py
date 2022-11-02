from kafka import KafkaProducer

'''ip地址：端口号,server也可为一个字符串列表，代表一个服务器集群'''
server_name = "110.42.193.168:9092"
'''
producer在创建时还有很多参数，比如：
retries(int):发送失败时的重发次数，默认值0
request_timeout_ms(int):客户端请求超时，单位:ms,默认值30000
更多请见官方文档
'''
producer = KafkaProducer(bootstrap_servers=server_name)
