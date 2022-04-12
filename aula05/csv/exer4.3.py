import csv
import random
import time
import psutil

def main():
    fout = open("rand.csv", "w")
    fields = ["time","cpuUsage", "packetsReceived", "packetsSent"]
    writer = csv.DictWriter(fout, fieldnames=fields)

    writer.writeheader()

    for i in range(1, 61):
        currTime = time.time()
        cpuUsage = psutil.cpu_percent(interval=1)
        netIoCounters = psutil.net_io_counters()
        packetsReceived = netIoCounters.packets_recv
        packetsSent = netIoCounters.packets_sent
        writer.writerow({ "time": currTime, 
                            "cpuUsage": cpuUsage, 
                            "packetsReceived": packetsReceived,
                            "packetsSent": packetsSent })

    fout.close()

main()