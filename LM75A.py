#lm75a.py
import smbus2
from smbus2 import SMBus
import sys

def lm75a(address):

    if 1 < len(sys.argv):
        address = int(sys.argv[1], 16)

    try:
        bus = SMBus(1)
        raw = bus.read_word_data(address, 0)& 0xffff
        raw = ((raw << 8) & 0xffff) + (raw >> 8)
        temperature = (raw / 32.0) / 8.0

        return temperature
        
    except Exception as e: print(e)
    
    finally:
        bus.close()