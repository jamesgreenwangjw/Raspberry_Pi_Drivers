import RPi.GPIO as GPIO

class BreathingLED:
    def __init__(self, pin, frequency=200):
        self.pin = pin
        self.freq = frequency
        self.pwm = None
        
        # 初始化
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin, self.freq)
        self.pwm.start(0) # 默认全黑

    def set_brightness(self, duty_cycle):
        """
        设置亮度 (0.0 - 100.0)
        """
        if duty_cycle > 100: duty_cycle = 100
        if duty_cycle < 0: duty_cycle = 0
        self.pwm.ChangeDutyCycle(duty_cycle)

    def stop(self):
        if self.pwm:
            self.pwm.stop()
            GPIO.output(self.pin, GPIO.LOW)