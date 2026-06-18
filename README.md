# Manim Animations

A collection of mathematical, scientific, and creative animations built using the Manim Community Edition.

This repository documents my journey learning Manim while exploring mathematical visualization, animation design, and creative coding.

---

## Showcase

Rendered animations are available in the `renders` directory.

### Included Animations

* Graph Animation
* Black Hole Animation
* Football Goal Animation

---

## Project Structure

```text
manim-animations/
│
├── animations/
│   ├── graph_animation.py
│   └── ...
│
├── renders/
│   ├── graph_animation.mp4
│   └── ...
│
└── README.md
```

---

## Requirements

Before running any animation, install:

* Python 3.13+
* FFmpeg
* MiKTeX
* Manim Community Edition

---

## Installation

### Clone the Repository

```git clone https://github.com/Taaviikivii/manim-animation.git
   cd manim-animation```

### Create and Activate a Virtual Environment

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### Install Manim

```powershell
pip install manim
```

### Verify Installation

```powershell
python -m manim --version
```

---

## Running an Animation

Render a scene using:

```powershell
python -m manim -pql animations\graph_animation.py GraphAnimation
```

### Quality Presets

Low Quality (Fast)

```powershell
python -m manim -pql animations\graph_animation.py GraphAnimation
```

Medium Quality

```powershell
python -m manim -pqm animations\graph_animation.py GraphAnimation
```

High Quality

```powershell
python -m manim -pqh animations\graph_animation.py GraphAnimation
```

---

## Output

Manim automatically generates rendered files inside the `media` directory.

Selected final renders are included in the `renders` directory for easy viewing.

---

## Learning Goals

This project focuses on:

* Mathematical visualization
* Animation design
* Creative coding
* Scientific communication
* Python programming

---
