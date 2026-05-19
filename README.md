# Awesome NVIDIA Isaac 🤖

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Updated](https://img.shields.io/badge/Updated-weekly-blue)](https://github.com/robotlearning123/awesome-nvidia-isaac/pulls)

> **The canonical resource for the NVIDIA Isaac Platform** —
> GPU-accelerated robotics simulation, learning, and deployment.
>
> Covers **Isaac Lab · Isaac Sim · Newton · GR00T · Cosmos · Isaac ROS · Omniverse** and the full physical AI stack.

📦 **Looking for legacy Isaac Gym (Preview)?** → see [`isaac-gym.md`](isaac-gym.md)

---

## ⚡ Quick Links — by Intent

| I want to… | Go to |
|---|---|
| 🚀 Start with Isaac Lab in 5 minutes | [§0 Getting Started](#-getting-started) |
| 🦾 Train a humanoid policy (GR00T / HOVER) | [§2 Humanoid](#humanoid) |
| 🐕 Train quadruped locomotion | [§2 Quadruped](#quadruped--legged) |
| 🤖 Build manipulation skills | [§2 Manipulation](#manipulation) |
| 🔄 Migrate from Isaac Gym to Isaac Lab | [§0 Migration](#-getting-started) |
| ⚡ Switch physics backend (Newton / PhysX / MuJoCo) | [§1 Core Platforms](#%EF%B8%8F-core-platforms) |
| 🌍 Generate synthetic data with Cosmos | [§3 Foundation Models](#foundation-models--world-models) |
| 📰 Latest research papers (auto-updated) | [§4 Research](#-research) |
| 🏭 Deploy to real robots | [§5 Production & Sim2Real](#%EF%B8%8F-production--sim2real) |
| ⭐ See who uses Isaac | [§6 Showcase](#-showcase) |

---

## 📚 Contents

- [§0 Getting Started](#-getting-started)
- [§1 Core Platforms](#%EF%B8%8F-core-platforms)
- [§2 Robots by Application](#-robots-by-application)
- [§3 Algorithms & Models](#-algorithms--models)
- [§4 Research](#-research)
- [§5 Production & Sim2Real](#%EF%B8%8F-production--sim2real)
- [§6 Showcase](#-showcase)
- [§7 Community](#-community)
- [Contributing](#contributing)
- [Latest Research (auto-updated)](#-latest-research-auto-updated)

---

## 📚 Getting Started

### 🏛️ Official

- **[Isaac Lab Documentation](https://isaac-sim.github.io/IsaacLab/)** — Full framework docs, tutorials, API reference
- **[Isaac Lab GitHub](https://github.com/isaac-sim/IsaacLab)** — Source, releases, examples
- **[Isaac Sim Documentation](https://docs.isaacsim.omniverse.nvidia.com/)** — Simulator setup, scenes, sensors
- **[Isaac Sim GitHub](https://github.com/isaac-sim/IsaacSim)** — Open-source simulator
- **[NVIDIA Isaac Platform Hub](https://developer.nvidia.com/isaac)** — Top-level entry point
- **[Install Isaac Sim + Isaac Lab on DGX Spark](https://build.nvidia.com/spark/isaac)** — Reference install
- **[Isaac Lab on NGC](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/isaac-lab)** — Container images
- **[NVIDIA Developer Blog · Isaac tag](https://developer.nvidia.com/blog/tag/isaac/)** — Latest official tutorials

### 🌐 Community Starters

- **5-Minute Hello World** — *(coming soon in this repo)*
- **Migration: Isaac Gym → Isaac Lab** — *(coming soon in this repo)*

---

## 🏛️ Core Platforms

### Frameworks (Robot Learning)

#### 🏛️ Official

- **[Isaac Lab](https://github.com/isaac-sim/IsaacLab)** `[OFFICIAL]` — Modular GPU-accelerated robot learning framework. **Latest stable: 2.3.2** (2026-02). **Latest beta: 3.0.0** (2026-03 GTC, built on Sim 6.0, multi-backend physics). 150K+ FPS for parallel training. Foundation of GR00T training pipeline.
- **[Isaac Lab Release Notes](https://isaac-sim.github.io/IsaacLab/main/source/refs/release_notes.html)** `[OFFICIAL]` — Authoritative version history
- **[Isaac Lab-Arena](https://developer.nvidia.com/isaac/lab-arena)** `[OFFICIAL]` — Large-scale policy evaluation framework (CES 2026), co-developed with Lightwheel. Connects to LIBERO, RoboCasa benchmarks.
- **[Isaac Teleop](https://developer.nvidia.com/isaac)** `[OFFICIAL]` — Unified teleoperation + data collection across sim and real (GA at GTC 2026). XR headsets, body trackers, MANUS gloves.

### Simulators

#### 🏛️ Official

- **[Isaac Sim](https://github.com/isaac-sim/IsaacSim)** `[OFFICIAL]` — Open-source robotics simulator on Omniverse. **Latest stable: 5.1.0**. **6.0 Early Developer Release** (GTC 2026) — multi-physics-backend, NuRec integration, Robot Inspector tools.
- **[Isaac Sim Documentation](https://docs.isaacsim.omniverse.nvidia.com/)** `[OFFICIAL]`
- **[Omniverse NuRec](https://blogs.nvidia.com/blog/gtc-2026-virtual-worlds-physical-ai/)** `[OFFICIAL]` — 3D Gaussian splatting libraries for converting sensor data into interactive simulations (GA at GTC 2026)
- **[Isaac Gym (Legacy)](https://developer.nvidia.com/isaac-gym)** `[OFFICIAL]` `[DEPRECATED]` — Preview 4 final · See [`isaac-gym.md`](isaac-gym.md) for legacy resources

### Physics Engines

#### 🏛️ Official

- **[Newton](https://github.com/newton-physics/newton)** `[OFFICIAL]` `[NEW]` — GPU-accelerated physics engine built on NVIDIA Warp + OpenUSD. **1.0 GA at GTC 2026** (2026-03-17). Linux Foundation project co-developed with **Google DeepMind + Disney Research**. Includes MuJoCo Warp, Kamino solvers. Up to **475× faster** vs MJX for manipulation.
- **[Newton — Announcement Blog](https://developer.nvidia.com/blog/announcing-newton-an-open-source-physics-engine-for-robotics-simulation/)** `[OFFICIAL]`
- **[NVIDIA PhysX](https://github.com/NVIDIA-Omniverse/PhysX)** `[OFFICIAL]` — Default rigid-body physics in Isaac Sim/Lab
- **[NVIDIA Warp](https://github.com/NVIDIA/warp)** `[OFFICIAL]` — Python GPU computing framework underpinning Newton + Isaac Lab data pipelines
- **[MuJoCo Warp](https://github.com/google-deepmind/mujoco_warp)** `[OFFICIAL]` — MuJoCo on Warp (NVIDIA + Google DeepMind), 70× speedup

### Foundation / Asset Layer

#### 🏛️ Official

- **[NVIDIA Omniverse](https://www.nvidia.com/en-us/omniverse/)** `[OFFICIAL]` — Collaboration + simulation platform underlying Isaac Sim
- **[OpenUSD](https://openusd.org/)** `[OFFICIAL]` — Universal Scene Description (Pixar/NVIDIA)

### ROS / Edge

#### 🏛️ Official

- **[Isaac ROS](https://github.com/NVIDIA-ISAAC-ROS)** `[OFFICIAL]` — CUDA-accelerated ROS 2 packages (NITROS). **Latest: 4.4** (2026-02-19) with DGX Spark + JetPack 7.1 support.
- **[Isaac ROS Documentation](https://nvidia-isaac-ros.github.io/)** `[OFFICIAL]`
- **[NVIDIA Jetson Thor](https://developer.nvidia.com/embedded/jetson-thor)** `[OFFICIAL]` — Edge robot computing platform (Blackwell GPU)

---

## 🤖 Robots by Application

### Humanoid

#### 🏛️ Official

- **[Isaac GR00T N1.7](https://github.com/NVIDIA/Isaac-GR00T)** `[OFFICIAL]` `[GR00T]` — Humanoid robot foundation model with Cosmos-Reason2-2B + Qwen3-VL VLM backbone. Apache 2.0 licensed. Pretrained on 20K hours EgoScale human video data. Early Access at GTC 2026.
- **[Isaac GR00T (Developer Hub)](https://developer.nvidia.com/isaac/gr00t)** `[OFFICIAL]` `[GR00T]`
- **[GR00T N1 Paper (arXiv 2503.14734)](https://arxiv.org/abs/2503.14734)** `[OFFICIAL]` — Dual-system architecture for generalist humanoid robots
- **[GR00T N1.5 Research Page](https://research.nvidia.com/labs/gear/gr00t-n1_5/)** `[OFFICIAL]` `[GR00T]` — Enhanced VLM, FLARE loss, DreamGen integration
- **[GR00T N2 (Preview)](https://nvidianews.nvidia.com/news/nvidia-and-global-robotics-leaders-take-physical-ai-to-the-real-world)** `[OFFICIAL]` `[GR00T]` — Next-gen, year-end 2026 target. #1 on MolmoSpaces / RoboArena.
- **[HOVER](https://github.com/NVlabs/HOVER)** `[OFFICIAL]` — Neural whole-body controller for humanoids, built on Isaac Lab. Sim-to-real for Unitree H1.
- **[Isaac Lab Mimic](https://developer.nvidia.com/isaac/lab)** `[OFFICIAL]` — Imitation learning extension for Isaac Lab

#### 🌐 Community

- **[HumanoidVerse](https://github.com/LeCAR-Lab/HumanoidVerse)** — Multi-simulator framework for humanoid robot learning
- **[ASAP](https://agile.human2humanoid.com/)** — Aligning Simulation and Real-World Physics for Agile Humanoid Whole-Body Skills (LeCAR Lab, 2025)
- **[HIMLoco](https://junfeng-long.github.io/HIMLoco/)** — Hierarchical Imitation Learning for Robust Humanoid Locomotion (2024)
- **[Humanoid-Gym](https://github.com/roboterax/humanoid-gym)** — Zero-shot sim-to-real RL for humanoid robots
- **[agibot_x1_train](https://github.com/AgibotTech/agibot_x1_train)** — Training framework for AgiBot X1

### Quadruped / Legged

#### 🏛️ Official

- **[Legged Robotics (NVIDIA Reference Envs)](https://github.com/isaac-sim/IsaacLab/tree/main/source/isaaclab_tasks)** `[OFFICIAL]` — Quadruped tasks in Isaac Lab

#### 🌐 Community

- **[Legged Gym (RSL)](https://github.com/leggedrobotics/legged_gym)** — Massively parallel deep RL for legged locomotion (ETH RSL, CoRL 2021)
- **[Agile But Safe (ABS)](https://github.com/LeCAR-Lab/ABS)** — Collision-Free High-Speed Legged Locomotion (RSS 2024)
- **[Rapid Locomotion via RL](https://github.com/Improbable-AI/rapid-locomotion-rl)** — RSS 2022
- **[rl-mpc-locomotion](https://github.com/silvery107/rl-mpc-locomotion)** — RL + MPC for legged robots

### Manipulation

#### 🏛️ Official

- **[Isaac Manipulator](https://developer.nvidia.com/isaac/manipulator)** `[OFFICIAL]` — Reference workflows for robotic arms
- **[Isaac GR00T-Mimic Blueprint](https://developer.nvidia.com/isaac/gr00t)** `[OFFICIAL]` — Synthetic manipulation motion generation
- **[Cosmos Policy](https://www.therobotreport.com/nvidia-adds-cosmos-policy-world-foundation-models/)** `[OFFICIAL]` `[NEW]` — Post-trained Cosmos Predict-2 for manipulation. SOTA on LIBERO + RoboCasa.

#### 🌐 Community

- **[RLAfford](https://github.com/hyperplane-lab/RLAfford)** — End-to-end Affordance Learning with RL (ICRA 2023) — Isaac Gym
- **[Factory](https://research.nvidia.com/publication/2022-05_factory-fast-contact-robotic-assembly)** `[OFFICIAL]` — Fast Contact for Robotic Assembly (NVIDIA, RSS 2022) — Isaac Gym
- **[ASE: Adversarial Skill Embeddings](https://research.nvidia.com/labs/toronto-ai/ASE/)** `[OFFICIAL]` — NVIDIA Toronto AI Lab (SIGGRAPH 2022) — Isaac Gym
- **[DexterousHands](https://github.com/PKU-MARL/DexterousHands)** — Bimanual dexterous manipulation benchmark on Isaac Gym
- **[RoboDuet](https://github.com/locomanip-duet/RoboDuet)** — Whole-body Legged Loco-Manipulation (Isaac Gym Preview 4, 2024)

### Mobile / Wheeled

#### 🏛️ Official

- **[Nova Carter](https://developer.nvidia.com/isaac/perceptor)** `[OFFICIAL]` — Reference autonomous mobile robot

### Aerial / Drones

#### 🌐 Community

- **[Isaac Lab Drone Envs](https://github.com/isaac-sim/IsaacLab/tree/main/source/isaaclab_tasks)** — Multirotor / thruster support added in Lab 2.3.2

### Underwater / Marine

#### 🌐 Community

- **[OceanSim](https://github.com/umfieldrobotics/OceanSim)** — Underwater simulation on Isaac Sim + Omniverse (verified Isaac Sim)
- **[MarineGym](https://arxiv.org/abs/2410.14117)** — Accelerated training for underwater vehicles *(paper claims Isaac Sim; verify before adding to live repo)*

### Space Robotics

#### 🌐 Community

- **[Space Robotics Bench](https://github.com/AndrejOrsula/space_robotics_bench)** — Space-domain benchmark (verified Isaac Sim per official docs)

### Surgical Robotics

#### 🏛️ Official

- **[Isaac for Surgical Robotics](https://www.2minutemedicine.com/nvidia-gtc-2026-unveils-isaac-gr00t-foundation-model-for-surgical-robotics/)** `[OFFICIAL]` `[NEW]` — GR00T extended for surgical robotics (GTC 2026)

### Agriculture / Industrial Verticals

#### 🌐 Community

- **[Aigen](https://www.aigen.io/)** — Agricultural robots using Cosmos + Isaac Sim, Jetson Orin edge inference (cited in [NVIDIA Robotics Week blog](https://blogs.nvidia.com/blog/national-robotics-week-2026/))

---

## 🧠 Algorithms & Models

### RL Frameworks

#### 🏛️ Official

- **[RSL-RL](https://github.com/leggedrobotics/rsl_rl)** `[OFFICIAL-ADJACENT]` — Robotics Systems Lab RL (ETH Zürich) — official Isaac Lab integration
- **[skrl](https://github.com/Toni-SM/skrl)** `[OFFICIAL-ADJACENT]` — Modular and reusable library for RL, native Isaac Lab support

#### 🌐 Community

- **[RL Games](https://github.com/Denys88/rl_games)** — High-performance RL natively used with Isaac Gym/Lab

### Imitation Learning

#### 🏛️ Official

- **[Isaac Lab Mimic](https://developer.nvidia.com/isaac/lab)** `[OFFICIAL]` — Imitation learning workflows
- **[Isaac Teleop](https://developer.nvidia.com/isaac)** `[OFFICIAL]` — Demonstration data capture (XR headsets, MANUS gloves)

### Foundation Models / World Models

#### 🏛️ Official

- **[NVIDIA Cosmos 3.0](https://www.nvidia.com/en-us/ai/cosmos/)** `[OFFICIAL]` `[NEW]` — World Foundation Models platform. **2M+ downloads**. Unifies vision + reasoning + action + simulation.
- **[Cosmos GitHub](https://github.com/nvidia-cosmos)** `[OFFICIAL]`
- **[Cosmos Predict 2.5](https://github.com/nvidia-cosmos)** `[OFFICIAL]` — Generates realistic future world states from multimodal inputs
- **[Cosmos Reason 2](https://github.com/nvidia-cosmos)** `[OFFICIAL]` — Spatiotemporal reasoning, embodied decision-making via long chain-of-thought
- **[Cosmos Transfer 2.5](https://github.com/nvidia-cosmos)** `[OFFICIAL]` — Photorealistic simulation grounded in physics
- **[Cosmos Policy](https://github.com/nvidia-cosmos)** `[OFFICIAL]` — Manipulation policy training on Predict-2
- **[Cosmos: World Simulation Paper (arXiv 2511.00062)](https://arxiv.org/abs/2511.00062)** `[OFFICIAL]`
- **[GR00T N1.7 / N2](https://github.com/NVIDIA/Isaac-GR00T)** — see [Humanoid](#humanoid) section

### Synthetic Data

#### 🏛️ Official

- **[Physical AI Data Factory Blueprint](https://nvidianews.nvidia.com/news/nvidia-announces-open-physical-ai-data-factory-blueprint-to-accelerate-robotics-vision-ai-agents-and-autonomous-vehicle-development)** `[OFFICIAL]` `[NEW]` — Open reference architecture: Cosmos Curator + Transfer + Reason/Evaluator + NVIDIA OSMO
- **[GR00T-Dreams Blueprint](https://developer.nvidia.com/isaac/gr00t)** `[OFFICIAL]` — Synthetic trajectory generation
- **[GR00T-Mimic Blueprint](https://developer.nvidia.com/isaac/gr00t)** `[OFFICIAL]` — Manipulation motion generation

### Multi-Agent

#### 🌐 Community

- **[Safe Multi-Agent Isaac Gym Benchmark](https://github.com/chauncygu/Safe-Multi-Agent-Isaac-Gym)** — Multi-agent RL benchmark
- **[TimeChamber](https://github.com/inspirai/TimeChamber)** — Massively parallel multi-agent training

### Sim2Real

#### 🌐 Community

- **[BayesSimIG](https://arxiv.org/pdf/2107.04527.pdf)** — Domain randomization
- See also: HOVER (Unitree H1 sim-to-real), ASAP

---

## 🔬 Research

> 🤖 **Latest research papers are auto-curated and posted weekly** by a research bot
> (see [`.research-bot.yaml`](.research-bot.yaml)). Scroll to the bottom for the
> [auto-updated section](#-latest-research-auto-updated).

### Core Papers (Hall of Fame)

- **[Isaac Gym: High Performance GPU-Based Physics Simulation for RL](https://arxiv.org/abs/2108.10470)** — NeurIPS 2021 (the founding paper)
- **[GR00T N1: An Open Foundation Model for Generalist Humanoid Robots](https://arxiv.org/abs/2503.14734)** — 2025
- **[World Simulation with Video Foundation Models for Physical AI (Cosmos)](https://arxiv.org/abs/2511.00062)** — 2025

### Benchmarks & Leaderboards

#### 🏛️ Official / Industry-Standard

- **[Isaac Lab-Arena](https://developer.nvidia.com/isaac/lab-arena)** `[OFFICIAL]` — Standardized policy evaluation
- **[LIBERO](https://github.com/Lifelong-Robot-Learning/LIBERO)** — Lifelong robot learning benchmark (NeurIPS 2023). Used by Cosmos Policy + Isaac Lab-Arena.
- **[RoboCasa](https://robocasa.ai/)** — Large-scale household robotics simulation framework
- **[RoboCasa GR-1 Tabletop Tasks](https://github.com/robocasa/robocasa-gr1-tabletop-tasks)** — Official GR00T N1 evaluation tasks built on RoboCasa
- **[RoboArena](https://github.com/robo-arena/roboarena)** — Distributed real-world evaluation of generalist robot policies (CoRL 2025, [arXiv 2506.18123](https://arxiv.org/abs/2506.18123))

### Conference Tutorials

- **[ICRA · CoRL · IROS · RSS](https://www.icra2026.org/)** — Track Isaac-related workshops yearly
- **[NVIDIA GTC](https://www.nvidia.com/gtc/)** — Annual robotics keynotes and deep-dive sessions

---

## 🏗️ Production & Sim2Real

### 🏛️ Official

- **[Physical AI Data Factory Blueprint](https://nvidianews.nvidia.com/news/nvidia-announces-open-physical-ai-data-factory-blueprint-to-accelerate-robotics-vision-ai-agents-and-autonomous-vehicle-development)** `[OFFICIAL]` — Reference architecture for sim-to-real data pipelines
- **[Jetson Thor](https://developer.nvidia.com/embedded/jetson-thor)** `[OFFICIAL]` — Edge robot computing (Blackwell)
- **[Jetson Orin](https://developer.nvidia.com/embedded/jetson-orin)** `[OFFICIAL]` — Lower-tier edge computing
- **[NVIDIA NGC Catalog](https://catalog.ngc.nvidia.com/)** `[OFFICIAL]` — Pretrained models + containers

### 🌐 Industry Integrations (Case Studies)

- **ABB RobotStudio + Omniverse** — HyperReality release expected 2026
- **FANUC + Isaac Sim** — Digital twins for factory automation
- **PTC Onshape + Isaac Sim** — Cloud-native design-to-simulation workflow
- **CoreWeave** — Isaac Lab for robot learning pipelines
- **Alibaba Cloud** — Full NVIDIA physical AI stack integration

---

## ⭐ Showcase

### 🏛️ NVIDIA Partner Robot Developers (110+ partners)

**Humanoid pioneers**: Agility Robotics · Boston Dynamics · Figure AI · 1X Technologies · Mentee Robotics · NEURA Robotics · Disney Research (BDX Droids, Olaf)

**Industrial robotics**: ABB · AGIBOT · FANUC · KUKA · Universal Robots · YASKAWA · Hexagon · Techman Robot · Solomon · Franka Robotics · Comau

**Surgical / medical**: CMR Surgical · Medtronic

**Autonomous platforms**: Skild AI · Foretellix · Uber · World Labs

### 🎓 Academic Adopters

ETH Zürich Robotic Systems Lab · Stanford University · Technical University of Munich (TUM) · Peking University · National University of Singapore (NUS) · Toyota Research Institute

### 💼 Notable Community Projects

See sections above (Humanoid, Quadruped, Manipulation) for community-built repos using NVIDIA Isaac.

---

## 🌐 Community

### Official Channels

- **[NVIDIA Developer Forums · Isaac Sim](https://forums.developer.nvidia.com/c/omniverse/simulation/69)** `[OFFICIAL]`
- **[NVIDIA Developer Forums · Isaac ROS](https://forums.developer.nvidia.com/c/robotics-edge-computing/isaac/isaac-ros/600)** `[OFFICIAL]`
- **[NVIDIA Developer Forums · Isaac Gym (legacy)](https://forums.developer.nvidia.com/c/robotics-edge-computing/isaac/isaac-gym/322)** `[OFFICIAL]`
- **[NVIDIA Developer Blog · Isaac tag](https://developer.nvidia.com/blog/tag/isaac/)** `[OFFICIAL]`
- **[NVIDIA Omniverse YouTube](https://www.youtube.com/c/NVIDIAOmniverse)** `[OFFICIAL]`
- **[NVIDIA AI YouTube](https://www.youtube.com/c/NVIDIAAI)** `[OFFICIAL]`

### Learning Resources

- **[NVIDIA DLI · Robotics Courses](https://www.nvidia.com/en-us/training/)** `[OFFICIAL]` — Deep Learning Institute curriculum
- **[NVIDIA GTC On-Demand](https://www.nvidia.com/en-us/on-demand/)** `[OFFICIAL]` — Historical conference sessions
- **[Tutorials by j3soon](https://tutorial.j3soon.com/robotics/)** — Community-maintained Isaac tutorials

---

## Contributing

Contributions welcome! Please read **[CONTRIBUTING.md](CONTRIBUTING.md)** for the quality criteria:

- **GitHub projects**: ⭐ ≥ 50 OR paper-backed OR NVIDIA official · 12-month commit activity · clear license · readable README
- **Papers**: published OR major conference accepted · code/model/data at least partially open
- **Tutorials/blogs**: official or verifiable author · contains code or video · still works within last 6 months
- **Showcase entries**: public evidence of NVIDIA Isaac use (product, paper, video)

Use the [issue templates](.github/ISSUE_TEMPLATE/) to suggest a resource or report a broken link.

---

## License

[MIT](LICENSE) — Free to use, fork, share. Attribution appreciated.

## Acknowledgments

Thanks to all contributors of the original [`awesome-isaac-gym`](isaac-gym.md) (2021–2026) and to NVIDIA for building the Isaac Platform.

---

## 🧠 Latest Research (auto-updated)

<!-- The section below is automatically updated by the research bot. Do not edit by hand. -->
