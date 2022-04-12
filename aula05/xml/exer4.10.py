from lxml import etree
import time
import psutil

def main():
    root = etree.Element("stats")

    for i in range(1, 61):
        currTime = time.time()
        cpuUsage = psutil.cpu_percent(interval=1)
        availableRam = psutil.virtual_memory()[1]
        netIoCounters = psutil.net_io_counters()
        packetsReceived = netIoCounters.packets_recv
        packetsSent = netIoCounters.packets_sent

        value = etree.SubElement(root, "value")
        value.set("time", str(int(currTime)))
        cpu = etree.SubElement(value, "cpu")
        cpu.text = str(cpuUsage)
        ram = etree.SubElement(value, "ram")
        ram.text = str(availableRam)
        network = etree.SubElement(value, "network")
        packetsReceived = etree.SubElement(network, "packetsReceived")
        packetsReceived.text = str(packetsReceived)
        packetsSent = etree.SubElement(network, "packetsSent")
        packetsSent.text = str(packetsSent)

    with open('rand.xml', 'w') as f:
        f.write(etree.tostring(root, pretty_print=True).decode())

main()