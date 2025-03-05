import re

def consume_clean(consume):
    words = consume.lower().split("[ ,.:] ?")
    consume = next((word for word in words if re.search(r'\d+w', word, re.IGNORECASE)), None)
    consume = re.search(r'\d+', consume).group()
    return consume

def ports_clean(ports):
    hdmi_pattern = re.compile(r'HDMI\s*(\d+)', re.IGNORECASE)
    dp_pattern = re.compile(r'DisplayPort\s*(\d+)', re.IGNORECASE)
    
    hdmi_match = hdmi_pattern.search(ports)
    dp_match = dp_pattern.search(ports)
   
    return [
        (int(hdmi_match.group(1)) if hdmi_match else 1),
        (int(dp_match.group(1)) if dp_match else 1)    ]

def vram_size_clean(size):
    new_siez = re.search(r'\d+', size)
    if(new_siez):
        return new_siez.group()
