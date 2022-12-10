import time, sys
while True:
    f = open(sys.path[0] + "/data/pingTime", "w")
    f.write(str(time.time()))
    f.close()
    time.sleep(500)