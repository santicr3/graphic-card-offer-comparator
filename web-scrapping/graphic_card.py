class GraphicCard:
    def __init__(self, model, price, vram_size, vram_type, hdmi, dp, consume):
        self.model = model
        self.price = price
        self.vram_size = vram_size
        self.vram_type = vram_type
        self.hdmi = hdmi
        self.dp = dp
        self.consume = consume

    def validate():
        if not isinstance(self.model, str) or not self.model:
            print('Model is not an string')
            return False
        if not isinstance(self.vram_type, str) or not self.vram_type:
            print('Vram type is not an string')
            return False
        if not isinstance(self.vram_size, int) or not self.vram_size:
            print('Vram size is not a number')
            return False
        if not isinstance(self.hdmi, int) or not self.hdmi:
            print("HDMI's number is not a number")
            return False
        if not isinstance(self.dp, int) or not self.dp:
            print("DP's number is not a number")
            return False
        if not isinstance(self.consume, int) or not self.consume:
            print("Consume is not a number")
            return False
        return True

    def formatToString():
        return f"{self.model or None},{self.price or None},{self.vram_size or None},{self.vram_type or None},{self.ports or None},{self.consume or None}"









            
