# car_sim
在树莓派上，运行car_sub_mqtt.py
pub 消息时使用字典形式

例如：

control_topic = 'control'
client = mqtt.Client()
client.username_pw_set(username='caoyong', password='admin123')
client.connect('192.168.22.70', 61883, 600)  # 600为keepalive的时间间隔
push_new = {'0': 1, 'time': time.time(),
            'push_rtmp': 0,
            'camera_up_down': {'angle': 45},
            'camera_left_right': {'angle': 90},
            'car_left_right': {'angle': 45},
            'car_up_down': {'car_status': 1, 'speed': 'high'},
            'cat_stop': 1
            }

client.publish(control_topic, payload=json.dumps(push_new), qos=0)
具体字段代表的含义
push_rtmp 0 开启推流 反之 关闭推流
voice 0 开启声音传输，反之关闭
camera_up_down 摄像头舵机上下转动，0~90°，angle 转动的角度
camera_left_right 摄像头舵机左右转动 0~360° angle 转动的角度
car_up_down car_status 1 前进 2 后退 speed 默认high 任意值 low
car_left_right 车舵机 左右转 angle 角度 0~180
cat_stop 停车 每次调用前进与后退时 务必调用停车
