from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Controller
from mininet.log import setLogLevel, info
from mininet.link import TCLink
import time

# -------------------------------
# Custom Topologies
# -------------------------------

class SingleSwitchTopo(Topo):
    def build(self):
        s1 = self.addSwitch('s1')
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')

        self.addLink(h1, s1, cls=TCLink, bw=10)
        self.addLink(h2, s1, cls=TCLink, bw=10)


class LinearTopo(Topo):
    def build(self):
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')

        self.addLink(h1, s1, cls=TCLink, bw=10)
        self.addLink(s1, s2, cls=TCLink, bw=5)
        self.addLink(s2, h2, cls=TCLink, bw=10)


class TreeTopo(Topo):
    def build(self):
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')

        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')

        self.addLink(s1, s2, cls=TCLink, bw=5)

        self.addLink(h1, s1, cls=TCLink, bw=10)
        self.addLink(h2, s1, cls=TCLink, bw=10)

        self.addLink(h3, s2, cls=TCLink, bw=10)
        self.addLink(h4, s2, cls=TCLink, bw=10)


# -------------------------------
# Bandwidth Test Function
# -------------------------------

def runTest(topo, name):
    info("\n===== Running Test:", name, "=====\n")

    net = Mininet(topo=topo, controller=Controller, link=TCLink)
    net.start()

    h1, h2 = net.get('h1', 'h2')

    # Start iperf server
    h1.cmd('iperf -s &')
    time.sleep(2)

    # Run client test
    result = h2.cmd('iperf -c ' + h1.IP() + ' -t 5')

    print("\n--- Result for", name, "---")
    print(result)

    # Cleanup
    h1.cmd('killall iperf')
    net.stop()


# -------------------------------
# Main Execution
# -------------------------------

if __name__ == '__main__':
    setLogLevel('info')

    runTest(SingleSwitchTopo(), "Single Switch Topology")
    runTest(LinearTopo(), "Linear Topology")
    runTest(TreeTopo(), "Tree Topology")

