# rPI_zero_tm1637-CPU-temperature
temperature - SPECIAL EDITION, MORE precision PRINTED For . trailing number. <br/>
bShowColin = THE 2 DOT LEDs IN THE MIDDLE, THAT NEED PROBABLY SOME C REGISTER INSTRUCTION TO TURN OFF AND ON, BUT REALLY COOL TO CONTROL MANUALLY FIRST!.br / =]<BR />
<br />
[sipplettle]:<br/>
  <img src="https://github.com/bmk10/rPI_zero_tm1637-CPU-temperature/blob/main/init_and_shell_bash_kernal.JPG?raw=true" />
  <br/>
  <br/>
<code><br/>
  while True:<br/>
        print(measure_temp4())<br/>
        print(measure_temp5())<br/>
        floatstr = str(measure_temp3())<br/>
        len1 = len(floatstr) <br/>
        floatstr = floatstr.replace(".","")<br/>
        len2 = len(floatstr)<br/>
        bShowColin = False<br/>
        if(len1 != len2):<br/>
             bShowColin = True <br/>
        
        print(str(len1) + " " + str(len2))<br/>
        tm.show(floatstr,bShowColin)<br/>
        time.sleep(1)<br/>
  </code><br/>
  
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
