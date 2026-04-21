# cn_project
# SDN Bandwidth Analysis using Mininet

## 1. Problem Statement

The objective of this project is to design and implement a Software Defined Networking (SDN) topology using Mininet and analyze network performance in terms of bandwidth and connectivity.

The project demonstrates:

* Creation of a custom network topology
* Establishment of communication between hosts
* Measurement of bandwidth using iperf
* Verification of connectivity using ping

---

## 2. Objective

* To simulate a simple SDN network using Mininet
* To understand topology creation and link configuration
* To measure network performance using standard tools
* To analyze packet forwarding behavior in SDN

---

## 3. Topology Description

The network consists of:

* 2 Hosts → h1, h2
* 1 Switch → s1
* Links between:

  * h1 ↔ s1
  * h2 ↔ s1

Each link has:

* Bandwidth: 10 Mbps

### Topology Diagram (Conceptual)

h1 ---- s1 ---- h2

---

## 4. Tools and Technologies Used

* Mininet (Network Emulator)
* Python 3
* Open vSwitch
* iperf (Bandwidth testing)
* ping (Connectivity testing)

---

## 5. Project Structure

```
project-folder/
│── ba.py              # Main topology script
│── README.md          # Documentation
│── screenshots/       # Proof of execution (optional but recommended)
```

---

## 6. Setup Instructions

### Step 1: Start Mininet Environment (VM or Ubuntu)

Ensure Mininet is installed:

```
sudo apt update
sudo apt install mininet
```

---

### Step 2: Run the Topology Script

```
sudo python3 ba.py
```

---

## 7. Execution Steps

1. Run the script
2. Network will be created automatically
3. Hosts and switch will be initialized
4. Connectivity test will run
5. Bandwidth test will run using iperf

---

## 8. Expected Output

When the script is executed, the following outputs are expected:

### Network Creation

```
*** Creating network
*** Adding controller
*** Adding hosts: h1 h2
*** Adding switch: s1
*** Adding links
```

---

### Ping Test (Connectivity Check)

```
*** Ping: testing ping reachability
h1 -> h2
h2 -> h1
*** Results: 0% dropped
```

---

### Iperf Test (Bandwidth Measurement)

```
*** Iperf: testing TCP bandwidth between h1 and h2 ***
[ ID] Interval       Transfer     Bandwidth
[  4] 0.0-10.0 sec   ~10-12 MBytes  ~9-10 Mbits/sec
```

---

## 9. Proof of Execution

The following should be included in the GitHub repository:

* Screenshot of Mininet running
* Ping test output
* Iperf results

### Flow Table Verification

Run:

```
sudo ovs-ofctl dump-flows s1
```

Expected:

* Flow entries showing packet forwarding rules

---

## 10. Controller Used

The project uses the default Open vSwitch controller.

Note:
Ryu controller was initially attempted, but due to Python environment compatibility issues (Python 3.12 and setuptools conflicts), it was not used in the final implementation.

Since the project focuses on topology creation and bandwidth analysis, the default controller is sufficient for achieving the objectives.

---

## 11. Code Explanation (Summary)

The Python script performs the following:

* Creates Mininet network
* Adds controller
* Adds hosts and switch
* Configures links with bandwidth
* Starts network
* Runs:

  * pingAll()
  * iperf()
* Stops network

---

## 12. Sample Commands Used

```
sudo python3 ba.py
sudo ovs-ofctl dump-flows s1
```

---

## 13. Conclusion

This project successfully demonstrates:

* SDN topology creation using Mininet
* Host communication validation using ping
* Bandwidth analysis using iperf
* Basic understanding of SDN concepts and traffic flow

---

## 14. References

* Mininet Official Documentation
* Open vSwitch Documentation
* SDN Concepts (Course Material)

---
## 15. Performance Analysis

### 15.1 Connectivity Analysis (Ping)

The `pingAll()` test verifies basic reachability between hosts.

Observed result:

* 0% packet loss between h1 and h2

Interpretation:

* The switch successfully forwards packets between hosts
* Flow rules are correctly installed in the switch
* There are no link failures or misconfigurations

---

### 15.2 Bandwidth Analysis (Iperf)

The `iperf` test measures TCP throughput between h1 and h2.

Observed result:

* Bandwidth ≈ 9–10 Mbps

Interpretation:

* The configured link bandwidth is 10 Mbps
* Measured throughput is close to the theoretical maximum
* Slight reduction (~5–10%) is due to:

  * TCP overhead
  * Protocol headers
  * Mininet virtualization overhead

---

### 15.3 Flow Behavior Analysis

Flow table entries (using `ovs-ofctl dump-flows s1`) show:

* Packet forwarding rules installed dynamically
* Match fields based on MAC/IP addresses
* Actions forwarding packets to correct ports

Interpretation:

* The switch operates using flow-based forwarding (SDN principle)
* Controller installs rules after initial packet-in events
* Subsequent packets are handled efficiently without controller intervention

---

### 15.4 Latency Considerations

* Initial packets may experience slightly higher delay due to controller interaction
* Once flow rules are installed, latency decreases significantly
* In this simple topology, latency remains minimal

---

### 15.5 Network Efficiency

* High efficiency observed (≈90–95% of link capacity)
* No congestion due to single-flow traffic
* Performance is stable under current topology

---

### 15.6 Limitations

* Only a single switch topology is used
* No congestion or multiple traffic flows tested
* No advanced QoS or traffic shaping applied
* Default controller limits advanced SDN behavior

---

### 15.7 Possible Improvements

* Add multiple hosts to test congestion
* Introduce custom controller (Ryu/POX) for intelligent routing
* Implement QoS policies
* Measure latency using advanced tools

---

### 15.8 Conclusion of Analysis

The network performs efficiently with minimal packet loss and near-maximum bandwidth utilization.
The results validate correct topology design, proper link configuration, and effective packet forwarding in the SDN environment.
