# Flappy Bird Clone

This project is a simple Flappy Bird clone implemented in Python using the Pygame library. The game features a bird that the player can control to navigate through pipes, simulating the popular mobile game Flappy Bird.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Project Structure](#project-structure)
- [Contributing](#contributing)

## Features

- Bird character with flapping animation
- Randomly generated pipes
- Gravity and jumping mechanics
- Bird rotation based on velocity

## Requirements

- Python 3.x
- Pygame library

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/flappy-bird-clone.git
   ```

2. Navigate to the project directory:
   ```
   cd flappy-bird-clone
   ```

3. Install the required Pygame library:
   ```
   pip install pygame
   ```

## How to Play

Run the game by executing the main Python script:

```
python 3.py
```

- Press any key to make the bird jump
- Navigate the bird through the gaps in the pipes
- The game ends if the bird collides with a pipe or the ground

## Project Structure

The project consists of three Python scripts, each building upon the previous one:

1. `1.py`: Sets up the basic game window and draws the bird with a flapping animation.
2. `2.py`: Adds pipe generation and movement.
3. `3.py`: Implements full game mechanics including gravity, jumping, and bird rotation.

### Image Files

The game requires the following image files in an `images` folder:

- `bird_wing_up.png`
- `bird_wing_down.png`
- `background.png`
- `pipe_body.png`
- `pipe_end.png`

Ensure these images are present in the `images` folder before running the game.

## Contributing

Contributions to improve the game are welcome. Please feel free to fork the repository, make changes, and submit pull requests.

Some ideas for improvements:
- Add score tracking
- Implement game over screen
- Add sound effects
- Create a start menu
