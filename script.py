import time
import board
import busio
import adafruit_htu21d
import adafruit_dht

# Create I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create sensor objects
htu21d = adafruit_htu21d.HTU21D(i2c)
dht11_sensor = adafruit_dht.DHT11(board.D4)

def read_sensors():
    try:
        # Read HTU21D sensor
        htu_temp = htu21d.temperature
        htu_hum = htu21d.relative_humidity

        # Read DHT11 sensor
        dht_temp = dht11_sensor.temperature
        dht_hum = dht11_sensor.humidity

        # Display readings on terminal
        print(f"HTU21D: Temp={htu_temp:.2f}C Hum={htu_hum:.2f}%")
        print(f"DHT11: Temp={dht_temp:.2f}C Hum={dht_hum:.2f}%")

    except RuntimeError as error:
        # Handle errors from sensors
        print(f"RuntimeError: {error.args[0]}")
    except Exception as error:
        print(f"Exception: {error}")
        raise error

def main():
    while True:
        read_sensors()
        time.sleep(2)  # Read every 2 seconds

if __name__ == "__main__":
    main()