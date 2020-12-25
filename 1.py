import tm1637
from machine import Pin
tm = tm1637.TM1637(clk=Pin(5), dio=(4))

tm.temperature(24)

