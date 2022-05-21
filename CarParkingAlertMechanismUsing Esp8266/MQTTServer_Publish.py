from umqtt.simple import MQTTClient
import ubinascii

class MQTTConfig:
    #@staticmethod
    def _main_(mqtt_broker="192.168.0.104", clientid="ubinascii.hexlify(machine.unique_id())",message=""):
      print(clientid)
      print(mqtt_broker)
      c = MQTTClient(clientid, mqtt_broker)
      print('clientid--->',clientid)
      print('brokeris----->',mqtt_broker)
      c.connect()
      c.publish(b"foo_topic", message)
      print('Message Published')
      c.disconnect()

  #  _main_("192.168.0.104", ubinascii.hexlify(machine.unique_id()),"Hi There")