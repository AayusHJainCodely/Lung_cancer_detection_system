import smbus
import time
import random
from adafruit_ina260 import INA260
import board
import busio

# MCP4725 default address
MCP4725_ADDR = 0x60


bus = smbus.SMBus(1)  


i2c_bus = busio.I2C(board.SCL, board.SDA)


ina260 = INA260(i2c_bus, addr=0x40)

def set_dac_voltage(mvoltage):
    """
    Sets the DAC output voltage of MCP4725.
    mvoltage: Voltage value in millivolts (0 to 3300).
    """
    # Calculate the 12-bit DAC value
    dac_value = int(mvoltage * 4095 / 3300)
    
    # Split the 12-bit value into two bytes (MSB and LSB)
    msb = (dac_value >> 4) & 0xFF
    lsb = (dac_value << 4) & 0xFF
    
   
    bus.write_i2c_block_data(MCP4725_ADDR, 0x40, [msb, lsb])

def read_current():
    """
    Reads the current value from the INA260 sensor.
    Returns the current in Amperes.
    """
    return ina260.current

# Example usage
try:
    while True:
        # Generate random voltages V1 and V2 such that 0 <= V1 < V2 <= 1
        v1 = random.uniform(0, 1) * 1000  # Convert to millivolts
        v2 = random.uniform(v1 / 1000, 1) * 1000  # Ensure V2 is greater than V1

        
        set_dac_voltage(v1)
        print(f"Set DAC output to V1: {v1 / 1000}V")
        time.sleep(1)

        
        current_v1 = read_current()
        print(f"Current at V1 ({v1 / 1000}V): {current_v1:.3f} A")

      
        set_dac_voltage(v2)
        print(f"Set DAC output to V2: {v2 / 1000}V")
        time.sleep(1)

      
        current_v2 = read_current()
        print(f"Current at V2 ({v2 / 1000}V): {current_v2:.3f} A")

        time.sleep(2)

except KeyboardInterrupt:
    print("Program terminated")