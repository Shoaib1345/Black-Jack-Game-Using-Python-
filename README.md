# 🎴 Professional Blackjack (Blackjet Game)

A simple yet professional **Blackjack (21)** game built using **Python** and **Tkinter**.  
This GUI version is based on the original console-based `blackjet()` script and includes an improved, modern interface with clear instructions and smooth gameplay.

---

## 🧩 Features

✅ **User-Friendly GUI**
- Clean dark-themed interface.
- Organized layout using Tkinter frames and labels.

✅ **Core Blackjack Gameplay**
- Enter your starting cards.
- Draw additional cards ("Hit") or stop ("Stand").
- Computer draws automatically.
- Automatic winner calculation.

✅ **Smart Game Logic**
- Same rules as traditional Blackjack (21).
- Detects bust (>21), higher hand wins, or draw.

✅ **Replay Option**
- Instantly start a new game using the **Play Again** button.

---

## 🖥️ Preview

**Main Interface:**
```

## 🎴 Professional Blackjack

Enter your starting cards: 7 4
[ Deal ] [ Hit ] [ Stand ] [ Play Again ]
-----------------------------------------

Your Cards: [7, 4] | Sum: 11
Computer Cards: [8] | Sum: ?
Result: Game started! You can Hit or Stand.

````

---

## 🧰 Requirements

Before running the project, make sure you have:

- **Python 3.8+**
- **Tkinter** (comes pre-installed with Python on Windows, macOS, and most Linux systems)

To check if Tkinter is installed:
```bash
python -m tkinter
````

If a small empty window opens, Tkinter is ready to use.

---

## 🚀 How to Run

1. Clone or download this repository:

   ```bash
   git clone https://github.com/yourusername/blackjack-tkinter.git
   ```

2. Navigate to the project folder:

   ```bash
   cd blackjack-tkinter
   ```

3. Run the program:

   ```bash
   python blackjack_gui.py
   ```

---

## 🎮 How to Play

1. **Enter your cards**
   Type your starting cards (numbers between 1–10) separated by spaces, e.g.:

   ```
   7 5
   ```

2. **Click “Deal”**
   The game starts. The computer gets one random card.

3. **Choose your move**

   * **Hit:** Draw another card (you get a random card).
   * **Stand:** Stop drawing; computer draws its second card.

4. **Result shown automatically**
   The program compares totals and displays:

   * ✅ You Win
   * ❌ You Lose
   * ⚖️ It's a Draw

5. **Play Again**
   Click “Play Again” to reset and start a new round.

---

## 🧠 Game Logic Summary

| Condition                 | Result                    |
| ------------------------- | ------------------------- |
| Player sum > 21           | You lose (busted)         |
| Computer sum > 21         | You win (computer busted) |
| Player sum > Computer sum | You win                   |
| Player sum < Computer sum | You lose                  |
| Equal sums                | Draw                      |

---

## 🧑‍💻 Project Structure

```
📂 blackjack-tkinter/
├── blackjack_gui.py      # Main program file
├── README.md             # Project documentation
```

---

## 🪄 Future Enhancements

* 🎨 Add card image graphics for more realism
* 🃏 Animate card draws using Canvas
* 🌐 Multiplayer support or AI difficulty levels
* 💾 Save high scores or game history

---

## 📜 Author

**Shoaib Ahmed**
🎓 2nd Year AI Student at Aror University
📧 Email: [shoaibahmedprogramming@gmail.com](mailto:shoaibahmedprogramming@gmail.com)
💼 LinkedIn: [linkedin.com/in/shoaib-ahmed-tech](https://linkedin.com/in/shoaib-ahmed-tech)



Would you like me to also create a **GitHub-ready folder structure with `requirements.txt` and a short description section for your GitHub page** (so you can upload this project easily)?
`
