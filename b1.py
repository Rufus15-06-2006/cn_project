from mininet.net import Mininet
from mininet.node import OVSController
from mininet.link import TCLink
import time

def run_test(bw):
    print(f"\n===== Running test with bandwidth = {bw} Mbps =====")

    net = Mininet(controller=OVSController, link=TCLink)

    c0 = net.addController('c0', controller=OVSController)

    h1 = net.addHost('h1')
    h2 = net.addHost('h2')
    s1 = net.addSwitch('s1')

    net.addLink(h1, s1, bw=bw)
    net.addLink(h2, s1, bw=bw)

    net.start()

    print("\n*** Ping Test ***")
    net.pingAll()

    time.sleep(1)

    print("\n*** iPerf Test ***")
    h1.cmd('iperf -s &')
    time.sleep(2)
    result = h2.cmd('iperf -c 10.0.0.1')
    print(result)

    net.stop()


if __name__ == '__main__':
    run_test(10)
    run_test(5)
