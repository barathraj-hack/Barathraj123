# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import random
import time

def get_temp():
    return random.randint(0, 100)

def get_humidity():
    return random.randint(0, 100)

def check_temp(temp):
    if temp > 90:
        print("Temperature is too high")
        return True
    else:
        return False

def check_humidity(humidity):
    if humidity > 70:
        print("Humidity is too high")
        return True
    else:
        return False

def main():
    while True:
        temp = get_temp()
        humidity = get_humidity()
        if check_temp(temp) or check_humidity(humidity):
            print("ALARM")
        else:
            print("Everything is fine")
        time.sleep(1)

if __name__ == "__main__":
    main()



