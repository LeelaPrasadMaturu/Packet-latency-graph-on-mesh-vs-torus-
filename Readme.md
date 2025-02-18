# Network-on-Chip (NoC) Packet Latency Analysis: Mesh vs. Torus

This repository contains the implementation and analysis of packet latency versus injection rates for **Mesh** and **Torus** topologies in Network-on-Chip (NoC) architectures. The project leverages the **BookSim** simulator to model and compare the performance of these two topologies under varying injection rates.

---

## Overview

The goal of this project is to analyze and visualize how packet latency behaves in **Mesh** and **Torus** topologies as injection rates increase. The results are plotted to compare the performance of both topologies, highlighting their strengths and limitations.

---

## Key Concepts

### Network-on-Chip (NoC)
NoC is a communication subsystem used in system-on-chip (SoC) designs. It provides a scalable and efficient way to manage data transfer between multiple processing units and memory components.

### Mesh Topology
- In a **Mesh** topology, processors and memory units are connected in a grid-like structure.
- Each node is directly connected to its neighbors, forming a crossbar-like architecture.
- As injection rates increase, packet latency tends to rise due to congestion in the network.

### Torus Topology
- A **Torus** topology is an extension of the Mesh topology.
- In addition to direct connections, the edges of the mesh are connected, forming a ring-like structure.
- This reduces hop counts and can improve latency under certain conditions, but it also introduces new challenges in routing.

---

## Project Details

### Simulation Setup
- The simulation is performed using the **BookSim** simulator.
- The configuration was modified to extend the maximum computation cycles from **500** to **50,000** to ensure accurate measurement of packet latencies at higher injection rates.

### Observations
- **Mesh Topology**: 
  - Packet latency increases exponentially with lower injection rates too.
  - The topology struggles to handle congestion as injection rates approach saturation.
- **Torus Topology**:
  - A sudden spike in packet latency is observed at an injection rate of **0.8**.
  - This indicates a threshold beyond which the topology experiences significant congestion.

---

## What is Packet Latency?
Packet latency refers to the time it takes for a data packet to travel from its source (sender) to its destination (receiver) in a network. It is a critical performance metric in network communication systems, including Network-on-Chip (NoC) architectures, as it directly impacts the efficiency and responsiveness of the system.

## BOOKSIM Repository Structure
https://github.com/booksim/booksim2.git
