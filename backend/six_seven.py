from gpiozero import Servo
import time
import asyncio

class SixSeven:
  def __init__(self, servo_pin_1=17, servo_pin_2=27):
    self.servo_1 = Servo(servo_pin_1)
    self.servo_2 = Servo(servo_pin_2)

  async def six_seven(self):
    for _ in range(3):
      self.servo_1.min()
      self.servo_2.min()
      time.sleep(0.25)
      self.servo_1.max()
      self.servo_2.max()
      time.sleep(0.25)