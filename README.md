  # Racer AI

A 2D top-down racing game built with Python and pygame, and an AI that learns
to drive it using a genetic algorithm written from scratch.

## Features

- Car physics with acceleration, friction, braking and speed-dependent steering
- Hand-crafted track with tyre-stack obstacles and pixel-perfect collision (pygame masks)
- Track layout stored as data (`track.json`): start position, checkpoints, obstacles

## Getting started

Requires Python 3.10+.

```bash
git clone https://github.com/doruk-akcali/racer-ai.git
cd racer-ai
pip install pygame-ce
python CarGame.py
```

## Controls

| Key | Action |
|---|---|
| ↑ | Accelerate |
| ↓ | Brake / reverse |
| ← → | Steer |

## Project structure

| File | Purpose |
|---|---|
| `CarGame.py` | Game loop: input, update, collision, drawing |
| `Car.py` | Car physics and rendering |
| `Track.py` | Track image, collision mask and track data |
| `assets/` | Images and `track.json` |

## Roadmap

- [x] Playable car with physics
- [x] Track with obstacles and crash detection
- [ ] Distance sensors
- [ ] Neural network "brain"
- [ ] Genetic algorithm: selection, crossover, mutation
- [ ] Training visualisation and saving the best driver
