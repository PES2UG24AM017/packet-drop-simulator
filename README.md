# Packet Drop Simulator using SDN (Mininet + POX)

## Problem Statement

The objective of this project is to simulate packet loss in a Software Defined Network (SDN) using Mininet and an OpenFlow controller (POX). The project demonstrates how SDN flow rules (match–action) can be used to control network behavior by allowing or blocking specific traffic.


## Objectives

* Build a virtual network using Mininet
* Implement an SDN controller using POX
* Design flow rules to control packet forwarding
* Simulate packet drop for selected traffic
* Compare normal and failure scenarios


## Tools & Technologies

* Mininet (Network Emulator)
* POX Controller (SDN Controller)
* OpenFlow Protocol
* Ubuntu Linux


## Installation

### Install Mininet

```bash
sudo apt update
sudo apt install mininet -y
```

### Clone POX Controller

```bash
git clone https://github.com/noxrepo/pox.git
cd pox
```

## Setup & Execution Steps

### Step 1: Start Normal Controller

```bash
cd ~/pox
./pox.py forwarding.l2_learning
```

### Step 2: Start Mininet Topology

```bash
sudo mn --topo single,3 --controller=remote
```

### Step 3: Test Normal Network

```bash
pingall
```

### Step 4: Start Packet Drop Controller

```bash
cd ~/pox
./pox.py drop_controller
```

### Step 5: Start Mininet Again

```bash
sudo mn --topo single,3 --controller=remote
```

### Step 6: Test Packet Drop

```bash
h1 ping h2
```


## Test Scenarios

### Scenario 1: Normal (Allowed Traffic)

* Controller: `forwarding.l2_learning`
* All hosts communicate successfully
* Output: **0% packet loss**

**Explanation:**
The controller dynamically learns MAC addresses and installs forwarding rules, allowing all packets to be delivered successfully.


### Scenario 2: Failure (Blocked Traffic)

* Controller: `drop_controller`
* Communication between hosts is blocked
* Output: **100% packet loss**

**Explanation:**
The controller installs a flow rule to drop packets from a specific port, preventing communication between hosts.

## Expected Output

* **Normal Scenario:**

  * All hosts should communicate successfully
  * Output shows **0% packet loss**

* **Packet Drop Scenario:**

  * Communication between selected hosts fails
  * Output shows **100% packet loss**
  * “Destination Host Unreachable” messages appear


## Observations

* Normal network allows full communication between hosts
* Packet drop scenario blocks communication completely
* SDN controller successfully controls traffic using flow rules
* Flow tables reflect the installed rules


## Conclusion

This project demonstrates how Software Defined Networking (SDN) can be used to dynamically control network behavior. By applying flow rules, packet transmission can be allowed or blocked, enabling flexible and programmable network management.

---

## References

* Mininet Documentation
* POX Controller Documentation
* OpenFlow SDN Concepts

---
