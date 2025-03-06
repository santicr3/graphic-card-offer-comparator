import re
import os

def consume_clean(consume):
    words = consume.lower().split("[ ,.:] ?")
    consume = next((word for word in words if re.search(r'\d+\s?W(?!\S)', word, re.IGNORECASE)), '')
    if(consume):
        consume = re.search(r'\d+', consume).group()
    else:
        consume = ''
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

def vram_type_clean(type): 
    new_type = re.search(r'GDDR\d+', type)
    if(new_type):
        return new_type.group()

def add_to_file(data_lines, cols):
    if not os.path.exists('results/data.csv'):
        with open('results/data.csv', 'w') as f:
            f.write(cols + '\n') 
            for data_str in data_lines:
                f.write(data_str + '\n')
    else:
        with open('results/data.csv', 'a+') as f:                
            for data_str in data_lines:
                f.write(data_str + '\n')