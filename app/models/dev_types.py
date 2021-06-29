import enum
import random
from enum import Enum


class RANDOM_ATTR(enum.EnumMeta):
    @property
    def RANDOM(self):
        return random.choice([DevType.emeter, DevType.zigbee, DevType.lora, DevType.gsm])


class DevType(str, Enum, metaclass=RANDOM_ATTR):
    emeter = 'emeter'
    zigbee = 'zigbee'
    lora = 'lora'
    gsm = 'gsm'
