from oled import OLED_1inch3
import time

class PicoRunner:

    def __init__(self):
        self.score = 0
        self.speed = 1
        self.floor_artifacts = [
            {"type": "/", "x1": 112, "y1": 2, "x2": 120, "y2": 6},
            {"type": "/", "x1": 124, "y1": 9, "x2": 126, "y2": 2},
            {"type": "/", "x1": 135, "y1": 3, "x2": 142, "y2": 5}
        ]
        self.obstacles = []
        self.oled = OLED_1inch3()
        self.oled.fill(self.oled.balck)
        self.oled.show()
    
    def start(self):
        self.oled.rect(0, 0, 128, 64, self.oled.white)
        self.draw_character(50, 20)
        while(True):
            self.score += 1
            self.scroll()
            self.draw_floor()
            self.display_score()
            self.oled.show()
            time.sleep(.05)

    def draw_character(self, x, y):
        self.oled.pixel(x+1, y, self.oled.white)
        self.oled.pixel(x, y+1, self.oled.white)
        self.oled.pixel(x+2, y+1, self.oled.white)
        self.oled.pixel(x+1, y+2, self.oled.white)
        self.oled.pixel(x+1, y+3, self.oled.white)
        self.oled.pixel(x+1, y+4, self.oled.white)

    def draw_floor(self):
        self.oled.line(0, 48, 128, 48, self.oled.white)
        self.oled.fill_rect(1, 49, 126, 14, self.oled.balck)
        for artifact in self.floor_artifacts:
            if artifact["type"] == "/":
                self.oled.line(artifact["x1"], 48+artifact["y1"], artifact["x2"], 48+artifact["y2"], self.oled.white)

    def display_score(self):
        self.oled.fill_rect(100, 5, 27, 8, self.oled.balck)
        if self.score < 10:
            self.oled.text(str(self.score), 116, 5, self.oled.white)
        elif self.score < 100:
            self.oled.text(str(self.score), 108, 5, self.oled.white)
        else:
            self.oled.text(str(self.score), 100, 5, self.oled.white)

    def scroll(self):
        for artifact in self.floor_artifacts:
            if artifact["type"] != "":
                artifact["x1"] -= self.speed
                artifact["x2"] -= self.speed
