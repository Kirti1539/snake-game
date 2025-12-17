# 🐍 Hand-Controlled Snake Game (Computer Vision + Pygame)

## Project Overview

This project is a modern version of the classic **Nokia Snake Game**, controlled entirely using **real-time hand gestures** captured via a webcam. Instead of keyboard input, the snake’s direction is determined by hand movement.

## Key Features

- Real-time hand tracking using a webcam
- Hand gesture-based direction control
- Classic snake gameplay mechanics
- Screen wrap-around (no wall death)
- No game-over condition (endless mode)
- Prevents direct reverse movement (UP → DOWN not allowed)
- Food generation and snake growth
- Live score display
- Controlled snake speed for smooth gameplay

## Project Structure
nokia snake game real time hand movement
│
├── run.py
├── step1.py
├── step2.py
├── step3.py
├── game/
│ ├── snake.py
│ ├── food.py
│ └── main_game.py
├── vision/
│ ├── direction.py
│ └── detector.py

### File Descriptions

- `run.py`: Main entry point. Captures webcam frames, computes hand direction, and runs the game loop.
- `step1.py`, `step2.py`, `step3.py`: Incremental development steps; help understand project evolution.
- `game/`: Contains game logic.
  - `snake.py`: Snake movement, growth, direction logic, wrap-around.
  - `food.py`: Food generation and rendering.
  - `main_game.py`: Game engine that updates the snake, food, score, and renders the frame.
- `vision/`: Computer vision logic.
  - `direction.py`: Computes hand movement direction using wrist and index finger landmarks.
  - `detector.py`: Processes webcam frames, applies MediaPipe, and returns snake direction.

## Workflow

1. Webcam captures frames.
2. Hand landmarks detected.
3. Index finger relative to wrist determines movement direction.
4. Direction sent to the snake.
5. Snake moves, eats food, grows, and updates score.
6. Game renders updated frame.
7. Loop continues endlessly.

## How to Run

```bash
# Activate virtual environment
venv310\Scripts\activate

# Run the game
python run.py
