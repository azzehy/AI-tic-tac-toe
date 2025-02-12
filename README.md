# 🎩 Tic-Tac-Toe with AI

This is a **Python-based Tic-Tac-Toe game** that lets you play against an AI with different difficulty levels.

---

## 🎮 How to Play?
1. **Run the script**  
   ```bash
   python tic_tac_toe.py
   ```
2. **Choose the AI difficulty level:**
   - 🥽 **Beginner (1)** - Plays random moves.
   - 🟡 **Intermediate (2)** - Blocks and tries to win.
   - 🔴 **Pro (3)** - Uses the **Minimax Algorithm** (Hard to beat!).

3. **Play against the AI!**  
   - Enter a number (1-9) to mark your move.
   - The AI will respond according to its difficulty level.
   - The game ends when there is a winner or a tie.

---

## 🧠 AI Difficulty Levels

| Level        | Strategy Description |
|-------------|---------------------|
| **Beginner**  | Chooses random moves. |
| **Intermediate**  | Tries to win if possible, otherwise blocks the player. |
| **Pro**  | Uses **Minimax Algorithm** to make optimal moves (Hard to beat!). |

---

## 🧙️‍♂️ Pro AI & Minimax Algorithm

The **Pro AI** is powered by the **Minimax Algorithm**, which allows it to play optimally by evaluating every possible move.

### 🔮 **How Minimax Works?**
1. The AI **simulates** all possible moves.
2. It assigns a **score** to each possible outcome:
   - **+1** if AI wins
   - **-1** if the player wins
   - **0** for a tie
3. It chooses the **move with the highest score**.
4. The algorithm uses **recursion** and **backtracking** to explore future game states.

### 🎨 Minimax Algorithm Diagram
![Minimax](https://github.com/user-attachments/assets/4fbced8b-51dc-467c-9b3e-7ae5025f6225)
### 🔧 **Implementation Overview:**
- **`pro_ai()`** loops through **available moves**, uses Minimax to find the **best possible move**, and plays it.
- **`minimax(board, is_maximizing)`** recursively explores the game tree to determine the best move for AI.
- **`check_winner_ai()`** detects if the game is won.

### 🌌 Minimax Flowchart
![Flowchart-for-minimax-algorithm](https://github.com/user-attachments/assets/b836b9c9-7f6c-439f-96ed-653248e7cf80)

---

## 🏠 Features
✅ Two-player mode (Human vs AI)  
✅ 3 AI Difficulty Levels (Beginner, Intermediate, Pro)  
✅ Win, Block, and Strategy Implementation  
✅ Text-based UI  

---

## 🛠 Requirements
- Python 3.x  
- No external libraries needed (uses `random` for AI moves).  

---

## 🚀 Future Improvements
🔹 Add a **GUI** using Tkinter or Pygame  
🔹 Improve AI with **Machine Learning**  
🔹 Add **Multiplayer Mode**  

---

## 📜 License
This project is open-source and free to use.

---

Enjoy playing! 😃

