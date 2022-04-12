import csv
import random
import time
from numpy import ravel_multi_index
import psutil
from lxml import etree

def main():
    config = etree.parse("conf.xml").getroot()

    fout = open("rand.csv", "w")

    monitor_cpu = config.findall("./monitor/cpu")[0].attrib["active"] == "true"
    monitor_ram = config.findall("./monitor/ram")[0].attrib["active"] == "true"
    monitor_network = config.findall("./monitor/network")[0].attrib["active"] == "true"

    print(monitor_cpu)
    print(monitor_ram)
    print(monitor_network)

    fields = ["time"]
    if monitor_cpu: fields.append("cpu")
    if monitor_ram: fields.append("ram")
    if monitor_network: fields += ["packetsReceived", "packetsSent"]

    writer = csv.DictWriter(fout, fieldnames=fields, extrasaction="ignore")

    writer.writeheader()

    for i in range(1, 61):
        currTime = time.time()
        cpuUsage = psutil.cpu_percent(interval=1)
        availableRam = psutil.virtual_memory()[1]
        netIoCounters = psutil.net_io_counters()
        packetsReceived = netIoCounters.packets_recv
        packetsSent = netIoCounters.packets_sent
        writer.writerow({ "time": currTime, 
                            "cpu": cpuUsage, 
                            "ram": availableRam,
                            "packetsReceived": packetsReceived,
                            "packetsSent": packetsSent })

    fout.close()

main()