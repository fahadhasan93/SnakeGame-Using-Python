
# Snake Game

A simple Snake game implemented in Python using Pygame.

## Requirements
- Python 3.x
- Pygame

## Installation
1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## How to Play
1. Run the game:
```bash
python snake_game.py
```

2. Controls:
- Use arrow keys to control the snake's direction
- Collect red food to grow and increase your score
- Avoid hitting the walls or yourself

## Gameplay / Features
- Grid-based movement (configurable via constants at top of `snake_game.py`)
- Snake grows when eating food; food color changes as score increases
- Speed increases with score
- Collision detection (walls and self)
- Simple Game Over screen with score

## Configuration
Open `snake_game.py` at the top to change:
- WINDOW_SIZE
- GRID_SIZE
- initial speed (Game.speed)

## Troubleshooting
- If you see "ModuleNotFoundError: No module named 'pygame'": ensure the venv is activated and run `python3 -m pip show pygame` to confirm installation.
- If building pygame fails on Linux, install the system SDL/dev packages (see Requirements) then reinstall pygame.

## Screenshots

Game UI (in-play)
A view of the main game while playing: shows the snake on the grid, current food item, and the score in the corner.
![Game UI](https://github.com/user-attachments/assets/219bb6f0-02bc-4199-8441-9017c1ad8fde)


