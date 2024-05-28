import json

def init_config_data():
    try:
        with open("/Users/lythk/Documents/Coding/KickzAE | Managment Bot/Utils/config.json", "r") as chrome_controller_config:
            controller_config_raw = chrome_controller_config.read()
            
        config_json = json.loads(controller_config_raw)
        config_json["Global_Variables"]["Bot_Config"] = json.loads(controller_config_raw)

        return True
    except:
        return False

init_config_data()

with open("/Users/lythk/Documents/Coding/KickzAE | Managment Bot/Utils/config.json", "r") as chrome_controller_config:
        controller_config_raw = chrome_controller_config.read()
        config_json = json.loads(controller_config_raw)

print(config_json["Global_Variables"]["Bot_Config"])