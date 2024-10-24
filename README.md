# Awesome NVIDIA Isaac Gym 🤖

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated collection of resources related to **NVIDIA Isaac Gym**, a high-performance GPU-based physics simulation environment for robot learning.

## 🎯 Quick Links

- [Official Website](https://developer.nvidia.com/isaac-gym)

- [Documentation](https://docs.nvidia.com/isaac/isaac/doc/index.html)

- [Community Forum](https://forums.developer.nvidia.com/c/agx-autonomous-machines/isaac/isaac-gym/322)

- [Latest Release Info](#-latest-releases)

---

## 📋 Contents

- [Latest Releases](#-latest-releases)

- [Getting Started](#-getting-started)

- [Official Resources](#-official-resources)

- [Learning Materials](#-learning-materials)

  - [Tutorials](#tutorials)

  - [Workshops](#workshops)

  - [Video Guides](#video-guides)

- [Research Papers](#-research-papers)

  - [Core Papers](#core-papers)

  - [Robot Manipulation](#robot-manipulation)

  - [Locomotion & Control](#locomotion--control)

  - [Simulation & Learning](#simulation--learning)

- [Tools & Libraries](#-tools--libraries)

  - [RL Frameworks](#rl-frameworks)

  - [Community Projects](#community-projects)

- [Applications & Examples](#-applications--examples)

- [Community Resources](#-community-resources)

---

## 🚀 Latest Releases

- **February 2024**: Isaac Lab - A unified and modular framework for robot learning ([Website](https://isaac-sim.github.io/IsaacLab/main/index.html))
- **February 2024**: PhysX 5 SDK release ([GitHub](https://github.com/NVIDIA-Omniverse/PhysX))
- **February 2022**: Isaac Gym Preview 4 (1.3.0)
- **October 2021**: Isaac Gym Preview 3
- **June 2021**: [NVIDIA Isaac Sim on Omniverse Open Beta](https://developer.nvidia.com/blog/nvidia-isaac-sim-on-omniverse-now-available-in-open-beta/)

- **March 23, 2022:** GTC 2022 Session — [Isaac Gym: The Next Generation — High-performance Reinforcement Learning in Omniverse](https://www.nvidia.com/gtc/session-catalog/?search=Isaac#/session/1638331324610001KvlV).

- **Isaac Gym Overview:** [Isaac Gym Session](https://www.nvidia.com/en-us/on-demand/session/gtcsiliconvalley2019-s9918/).
- **GTC Spring 2021:** [Isaac Gym: End-to-End GPU-Accelerated Reinforcement Learning](https://www.nvidia.com/en-us/on-demand/session/gtcspring21-s32037/).

---

## 🎓 Getting Started

1. **Installation & Setup**

   - [Official Isaac Gym Download](https://developer.nvidia.com/isaac-gym)

   - [Quick Start Guide](https://docs.nvidia.com/isaac/isaac/doc/setup.html)

   - [Environment Setup](https://docs.nvidia.com/isaac/isaac/doc/setup.html#environment-setup)

2. **Basic Concepts**

   - [Introduction to Isaac Gym](https://developer.nvidia.com/blog/introducing-isaac-gym-rl-for-robotics/)

   - [Core Components Overview](https://docs.nvidia.com/isaac/isaac/doc/index.html)

   - [Basic Tutorials](https://www.youtube.com/playlist?list=PL3jK4xNnlCVf1SzxjCm7ZxDBNl9QYyV8X)

## 📚 Official Resources

### Core Documentation

- [Isaac SDK Documentation](https://docs.nvidia.com/isaac/isaac/doc/index.html)
- [OmniIsaacGymEnvs Repository](https://github.com/NVIDIA-Omniverse/OmniIsaacGymEnvs)
- [Official Blog Posts](https://developer.nvidia.com/blog/tag/isaac/)

### Learning Resources

- [Video Tutorials](https://www.youtube.com/playlist?list=PL3jK4xNnlCVf1SzxjCm7ZxDBNl9QYyV8X)
- [Developer Blog](https://developer.nvidia.com/blog/tag/isaac/)
- [NVIDIA Omniverse Channel](https://www.youtube.com/c/NVIDIAOmniverse)

## 📖 Learning Materials

### Tutorials

Comprehensive tutorial series from RSS 2021 Workshop:
1. [Introduction & Getting Started](https://youtu.be/nleDq-oJjGk)
2. [Environments, Training & Tips](https://youtu.be/1RSugmJ4_gs)
3. Academic Labs Series:
   - [University of Toronto](https://youtu.be/nXM5_mwUFOI)
   - [IMLab](https://youtu.be/VrTVUpDM7K8)
   - [Stanford University](https://youtu.be/RhjRrUK2abs)
   - [Soft-Body Simulation](https://youtu.be/i4fGVc6lImo)
   - [ETH Zurich](https://youtu.be/Afi17BnSuBM)
4. [New Frontiers in GPU Accelerated RL](https://youtu.be/WhaybakLTXE)

### Video Guides
- [Robot Import Guide](https://youtu.be/pxPFr58gHmQ)
- [Simulator Basics](https://www.youtube.com/watch?v=b12M_kCW82o)
- [Advanced Features](https://youtu.be/XcvMCs9NJfM)
- [Community Demonstrations](https://youtu.be/vpHR0qiH-GY)

- **[From Point Clouds to Material Graphs: Explore the Latest in Omniverse Create 2021.3](https://youtu.be/t9nVWhnOgbE)**
- **[Robot Autonomy with the Digital Twin in Isaac Sim](https://youtu.be/vOEdzxR-_Iw)**
- **[Can We Simulate a Real Robot?](https://youtu.be/phTnbmXM06g)** — A journey through finding a high-quality physics simulator for a robot quadruped.
- **[Teaching Robots to Walk with Reinforcement Learning](https://youtu.be/6qbW7Ki9NUc)** — Robot simulation adventure, covering reinforcement learning with the Bittle robot.
- **[Robot Dog Learns to Walk — Bittle Reinforcement Learning Part 3](https://youtu.be/A0tPe7-R8z0)** — Further progress in training robot quadrupeds to walk.


- **[Isaac Sim GTC 2021 — Sim-to-Real](https://www.nvidia.com/en-us/on-demand/session/gtcspring21-s31824/):** Session on sim-to-real transfer using Isaac Sim.
- **[Isaac Sim Video Tutorials](https://www.youtube.com/playlist?list=PL3jK4xNnlCVf1SzxjCm7ZxDBNl9QYyV8X):** Official video tutorials.
- **[Training Your JetBot in NVIDIA Isaac Sim](https://developer.nvidia.com/blog/training-your-jetbot-in-isaac-sim/):** Guide on training JetBot using Isaac Sim.
- **[Training Your NVIDIA JetBot to Avoid Collisions Using NVIDIA Isaac Sim](https://developer.nvidia.com/blog/training-your-nvidia-jetbot-to-avoid-collisions-using-nvidia-isaac-sim/):** Blog post on collision avoidance training.
- **[Introducing NVIDIA Isaac Gym: End-to-End Reinforcement Learning for Robotics](https://developer.nvidia.com/blog/introducing-isaac-gym-rl-for-robotics/):** Introduction to Isaac Gym.
- **[Accelerating Robotics Simulation with NVIDIA Omniverse Isaac Sim](https://developer.nvidia.com/blog/accelerating-robotics-simulation-with-nvidia-omniverse-isaac-sim/):** Blog post on using Omniverse with Isaac Sim.
- **[Developing Robotics Applications in Python with NVIDIA Isaac SDK](https://developer.nvidia.com/blog/developing-robotics-applications-in-python-with-isaac-sdk/):** Guide on using Isaac SDK with Python.
- **[Building an Intelligent Robot Dog with the NVIDIA Isaac SDK](https://developer.nvidia.com/blog/building-intelligent-robot-dog-with-isaac-sdk/):** Tutorial on building a robot dog.
- **[NVIDIA Omniverse YouTube Channel](https://www.youtube.com/c/NVIDIAOmniverse/videos?&ab_channel=NVIDIAOmniverse):** Official channel with various tutorials and demos.

### Blogs

- **[A Brief Introduction to NVIDIA Omniverse](https://zhuanlan.zhihu.com/p/462305733)**

---

## 📑 Research Papers

### Core Papers
- [Isaac Gym: High Performance GPU-Based Physics Simulation](https://arxiv.org/abs/2108.10470) (NeurIPS 2021)
  - [Project Page](https://sites.google.com/view/isaacgym-nvidia)
  - [OpenReview Discussion](https://openreview.net/forum?id=fgFBtYgJQX_)

### Robot Manipulation

- **[RLAfford](https://github.com/hyperplane-lab/RLAfford):** Official implementation of "RLAfford: End-to-end Affordance Learning with Reinforcement Learning", ICRA 2023.
- **[Masked Visual Pre-training for Robotics (MVP)](https://github.com/ir413/mvp):** Repository for the MVP project.
- **[Factory: Fast Contact for Robotic Assembly](https://sites.google.com/nvidia.com/factory):** RSS 2022.
  - [Paper](http://doi.acm.org/10.1145/3450626.3459670)
  - [Code](https://github.com/NVIDIA-Omniverse/IsaacGymEnvs)
- **[ASE: Adversarial Skill Embeddings](https://nv-tlabs.github.io/ASE/):** SIGGRAPH 2022.
  - [Paper](https://arxiv.org/abs/2205.01906)
  - [Code](https://github.com/NVIDIA-Omniverse/IsaacGymEnvs)
- **[Data-Driven Operational Space Control (OSCAR)](https://cremebrule.github.io/oscar-web/):** Adaptive and robust robot manipulation.
  - [Paper](https://arxiv.org/abs/2110.00704)
  - [Code](https://github.com/nvlabs/oscar)
- **[DefGraspSim](https://sites.google.com/nvidia.com/defgraspsim):** Simulation-based grasping of deformable objects.
  - [Paper](https://arxiv.org/pdf/2107.05778.pdf)
  - [Video](https://youtu.be/Caj0AtsKKVI)
  - [Code](https://github.com/NVlabs/deformable_object_grasping)
- **[In-Hand Object Pose Tracking](https://sites.google.com/view/in-hand-object-pose-tracking/):** ICRA 2021.
  - [Paper](https://arxiv.org/pdf/2002.12160.pdf)
- **[STORM: Fast Joint-Space MPC for Reactive Manipulation](https://sites.google.com/view/manipulation-mpc):** CoRL 2021.
  - [Paper](https://arxiv.org/pdf/2104.13542.pdf)
  - [Code](https://github.com/NVlabs/storm)
- **[Transferring Dexterous Manipulation from GPU Simulation to Real-World TriFinger](https://s2r2-ig.github.io/):**
  - [Paper](https://arxiv.org/pdf/2108.09779.pdf)
  - [Code](https://github.com/pairlab/leibnizgym)
- **[Causal Reasoning in Simulation for Robot Manipulation Policies](https://sites.google.com/view/crest-causal-struct-xfer-manip):** ICRA 2021.
  - [Paper](https://arxiv.org/pdf/2103.16772.pdf)
- **[Reactive Long Horizon Task Execution](https://www.youtube.com/playlist?list=PL-oD0xHUngeLfQmpngYkGFZarstfPOXqX):** IROS 2021.
  - [Paper](https://arxiv.org/pdf/2011.08694.pdf)

### Localization & Control

- **[Learning to Walk in Minutes Using Massively Parallel Deep RL](https://leggedrobotics.github.io/legged_gym/):** CoRL 2021.
  - [Paper](https://arxiv.org/pdf/2109.11978.pdf)
  - [Code](https://github.com/leggedrobotics/legged_gym)
- **[Dynamics Randomization Revisited](https://www.pair.toronto.edu/understanding-dr/):** A case study for quadrupedal locomotion.
  - [Paper](https://arxiv.org/abs/2011.02404)
  - [Video](https://youtu.be/ckdHWWpfSpk)
- **[GLiDE: Generalizable Quadrupedal Locomotion](https://www.pair.toronto.edu/glide-quadruped/):**
  - [Paper](https://arxiv.org/abs/2104.09771)
- **[Learning a Contact-Adaptive Controller](https://sites.google.com/view/learn-contact-controller/home):** For robust, efficient legged locomotion.
  - [Paper](https://arxiv.org/abs/2009.10019)
  - [Video](https://youtu.be/JJOmFZKpYTo)
  - [Blog](https://developer.nvidia.com/blog/contact-adaptive-controller-locomotion/)
- **[Learning a State Representation and Navigation](https://arxiv.org/pdf/2103.04351.pdf):** In cluttered and dynamic environments.

### Others

- **[BayesSimIG](https://arxiv.org/pdf/2107.04527.pdf):** Scalable parameter inference for adaptive domain randomization with Isaac Gym.
  - [Code](https://github.com/NVlabs/bayes-sim-ig)
- **[Isaac Gym: High Performance GPU-Based Physics Simulation](https://sites.google.com/view/isaacgym-nvidia):** NeurIPS 2021.
  - [Paper](https://arxiv.org/abs/2108.10470)
  - [OpenReview](https://openreview.net/forum?id=fgFBtYgJQX_)
- **[Learning to Swim](https://arxiv.org/abs/2410.00120v1):** Reinforcement learning for 6-DOF control of thruster-driven AUVs.
- **[MarineGym: Accelerated Training for Underwater Vehicles with High-Fidelity RL Simulation](https://arxiv.org/abs/2410.14117):** Based on Issac Sim
- **[space_robotics_bench](https://github.com/AndrejOrsula/space_robotics_bench)** Space Robotics Bench


## 🛠 Tools & Libraries

### RL Frameworks

- [RL Games](https://github.com/Denys88/rl_games) - Compatible RL algorithms
- [ElegantRL](https://github.com/AI4Finance-Foundation/ElegantRL)
- [skrl](https://github.com/Toni-SM/skrl) - Modular RL library
- [Minimal Stable PPO](https://github.com/ToruOwO/minimal-stable-PPO)

---

### Community Projects

- **[IsaacGymEnvs](https://github.com/NVIDIA-Omniverse/IsaacGymEnvs):** Official Isaac Gym RL environments.
- **[isaacgym_hammering](https://github.com/LiCHOTHU/isaacgym_hammering):** Hammering task implementation.
- **[isaacgym-utils](https://github.com/iamlab-cmu/isaacgym-utils):** Utilities by CMU's Intelligent Autonomous Manipulation Lab.
- **[isaacgym_sandbox](https://github.com/kploeger/isaacgym_sandbox):** Sandbox for Isaac Gym experiments.
- **[thormang3-gogoro-PPO](https://github.com/guichristmann/thormang3-gogoro-PPO):** Two-wheeled vehicle control using PPO.
- **[Bez_IsaacGym](https://github.com/utra-robosoccer/Bez_IsaacGym):** Environments for humanoid robot Bez.
- **[DexterousHands](https://github.com/PKU-MARL/DexterousHands):** Dual dexterous hand manipulation tasks.
- **[legged_gym_isaac](https://github.com/chengxuxin/legged_gym_isaac):** Legged robots in Isaac Gym.
- **[shifu](https://github.com/42jaylonw/shifu):** Environment builder for any robot.
- **[Rofunc](https://github.com/Skylark0924/Rofunc):** Python package for robot learning from demonstration.
- **[Dofbot Reacher](https://github.com/j3soon/OmniIsaacGymEnvs-DofbotReacher):** Sim2Real environment for Dofbot.
- **[UR10 Reacher](https://github.com/j3soon/OmniIsaacGymEnvs-UR10Reacher):** Sim2Real environment for UR10.
- **[TimeChamber](https://github.com/inspirai/TimeChamber):** Massively parallel self-play framework.
- **[RL-MPC-Locomotion](https://github.com/silvery107/rl-mpc-locomotion):** Deep RL for quadruped locomotion.
- **[Isaac_Underwater](https://github.com/leonlime/isaac_underwater):** Water and underwater tests using NVIDIA Isaac Sim.
- **[VRKitchen2.0-IndoorKit](https://github.com/yizhouzhao/VRKitchen2.0-IndoorKit):** Omniverse IndoorKit Extension.

---

## Conference Sessions and Talks

- **[Isaac Gym and Omniverse: High Performance Reinforcement Learning Evolved [A31118]](https://events.rainfocus.com/widget/nvidia/nvidiagtc/sessioncatalog?search=A31118)**
- **[Learning Challenging Tasks for Quadrupedal Robots: From Simulation to Reality [A31308]](https://events.rainfocus.com/widget/nvidia/nvidiagtc/sessioncatalog?search=A31308)**
- **[Sim-to-Real in Isaac Sim](https://www.nvidia.com/en-us/on-demand/session/gtcspring21-s31824/)**
- **[Isaac Gym: End-to-End GPU-Accelerated Reinforcement Learning](https://www.nvidia.com/en-us/on-demand/session/gtcspring21-s32037/)**
- **[Bridging Sim2Real Gap: Simulation Tuning for Training Deep Learning Robotic Perception Models](https://www.nvidia.com/en-us/on-demand/session/gtcspring21-s31649/)**
- **[Reinforcement Learning and Intralogistics](https://www.nvidia.com/en-us/on-demand/session/gtcspring21-e31467/)**
- **[Building Robotics Applications Using NVIDIA Isaac SDK](https://www.nvidia.com/en-us/on-demand/session/gtcfall20-a21856/)**
- **[NVIDIA Isaac Sim — Amazing Robot Models and Tasks](https://www.nvidia.com/en-us/on-demand/session/gtcsj20-d2s43/)**
- **[Omniverse View 2021.2 — Application Tour](https://www.nvidia.com/en-us/on-demand/session/omniverse2020-om1315/)**
- **[ISAAC SIM Introduction and Live Demo](https://www.nvidia.com/en-us/on-demand/session/omniverse2020-om1314/)**
- **[NVIDIA On-Demand ISAAC SIM Sessions](https://www.nvidia.com/en-us/on-demand/search/?facet.mimetype[]=event%20session&layout=list&page=1&q=isaac%20sim&sort=relevance)**

---

## 🌟 Contributing

Contributions are welcome! Please read our [contribution guidelines](CONTRIBUTING.md) before submitting a pull request.

## 📄 License

This repository is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

Special thanks to all contributors and the NVIDIA Isaac team for making these resources available to the robotics community.
