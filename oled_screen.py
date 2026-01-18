from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from luma.core.render import canvas
from PIL import ImageFont

class OLED:
    def __init__(self, i2c_addr=0x3C):
        try:
            self.serial = i2c(port=1, address=i2c_addr)
            self.device = ssd1306(self.serial)
            print(f"✅ OLED ({hex(i2c_addr)}) 初始化完成")
        except Exception as e:
            print(f"❌ OLED 初始化失败: {e}")
            self.device = None

    def show_info(self, line1="", line2="", line3=""):
        """
        显示三行文字，自动处理画布
        """
        if self.device is None: return

        with canvas(self.device) as draw:
            # 这里坐标是写死的，你也可以做成参数传进来
            draw.text((0, 0),  str(line1), fill="white")
            draw.text((0, 12), str(line2), fill="white")
            draw.text((0, 24), str(line3), fill="white")

    def clear(self):
        if self.device:
            self.device.clear()