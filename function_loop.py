#function loop
import time


global clk
clk = 0

def loop():
    global clk
    clk += 1
    print(clk)
    time.sleep(1)
    loop()

loop()
