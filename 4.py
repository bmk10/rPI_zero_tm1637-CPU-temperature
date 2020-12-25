import os
import time

import tm1637


def measure_temp():
        temp = os.popen("vcgencmd measure_temp").readline()
        return (temp.replace("temp=",""))

def measure_temp2():
        temp = os.popen("vcgencmd measure_temp").readline()
        temp = temp.replace("'C","") 
        return (temp.replace("temp=",""))

def measure_temp3():
        temp = os.popen("vcgencmd measure_temp").readline()
        temp = temp.replace("'C","")
        temp = temp.replace("\n","")
#        temp = temp.replace("\n","")

#        return int(temp.replace("temp=",""))
        return float(temp.replace("temp=",""))

def measure_temp4():
        temp = os.popen("vcgencmd measure_temp").readline()
        temp = temp.replace("'C","")
        temp = temp.replace("\n","")
        temp = temp.replace("temp=","")
        temp = float(temp)
        temp = int(temp)
        return temp

def measure_temp5():
        temp = os.popen("vcgencmd measure_temp").readline()
        temp = temp.replace("'C","")
        temp = temp.replace("\n","")
#        return int(temp.replace("temp=",""))
        return (temp.replace("temp=",""))

tm = tm1637.TM1637(clk=21, dio=20)

# all LEDS on "88:88"
tm.write([127, 255, 127, 127])

# all LEDS off
tm.write([0, 0, 0, 0])

# show "0123"
tm.write([63, 6, 91, 79])

# show "COOL"
tm.write([0b00111001, 0b00111111, 0b00111111, 0b00111000])

# show "HELP"
tm.show('help')

# display "dEAd", "bEEF"
tm.hex(0xdead)
tm.hex(0xbeef)

# show "12:59"
tm.numbers(12, 59)

# show "-123"
tm.number(-123)

# show temperature '24*C'
tm.temperature(24)

#tm.temperature(measure_temp())
while True:
        print(measure_temp4())
        print(measure_temp5())
        floatstr = str(measure_temp3())
        floatstr = floatstr.replace(".","")
        print(len(floatstr))
        tm.show(floatstr)
        time.sleep(1)
