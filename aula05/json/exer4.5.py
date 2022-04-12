import json
import random
import time
import psutil

def main():
    fout = open("rand.json", "w")

    data = {
        "stats": []
    }
    
    for i in range(1, 61):
        currTime = time.time()
        cpuUsage = psutil.cpu_percent(interval=1)
        netIoCounters = psutil.net_io_counters()
        packetsReceived = netIoCounters.packets_recv
        packetsSent = netIoCounters.packets_sent
        tempData = {
            "time": int(currTime),
            "cpu": cpuUsage,
            "network": {
                "received": packetsReceived,
                "sent": packetsSent
            }
        }
        data["stats"].append(tempData)

    fout.write(json.dumps(data))
    fout.close()

main()