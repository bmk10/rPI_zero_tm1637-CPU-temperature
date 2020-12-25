# rPI_zero_tm1637-CPU-temperature
temperature - SPECIAL EDITION, MORE precision PRINTED For . trailing number. 
<br />
[sipplettle]:<br/>
<code>
  while True:
        print(measure_temp4())
        print(measure_temp5())
        floatstr = str(measure_temp3())
        len1 = len(floatstr) 
        floatstr = floatstr.replace(".","")
        len2 = len(floatstr)
        bShowColin = False
        if(len1 != len2):
             bShowColin = True 
        
        print(str(len1) + " " + str(len2))
        tm.show(floatstr,bShowColin)
        time.sleep(1)
  </code>
  <BR />
  <img src="https://github.com/bmk10/rPI_zero_tm1637-CPU-temperature/blob/main/nano.JPG?raw=true" />
  
  <br />
  <br />
 REPLACE  measure_temp FUNCTIONS with own LINUX Commands FOR GPIO or other extraction methods VERY easy.
  <br />
  <br />
<img src="https://github.com/bmk10/rPI_zero_tm1637-CPU-temperature/blob/main/command1.JPG?raw=true" />
<br />
<img src="https://github.com/bmk10/rPI_zero_tm1637-CPU-temperature/blob/main/command2.JPG?raw=true" />
