import tkinter as tk
from tkinter import messagebox
import random

CARD_VALUES = list(range(1, 11))  # Cards from 1 to 10

class BlackjackGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🎴 Professional Blackjack")
        self.root.geometry("650x450")
        self.root.config(bg="#0B132B")  # Dark background
        self.root.resizable(False, False)

        # Initialize game variables
        self.user_cards = []
        self.computer_cards = []
        self.game_over = False

        # -------- HEADER --------
        header = tk.Label(
            root,
            text="♠️ Blackjack Game ♣️",
            font=("Helvetica", 22, "bold"),
            bg="#1C2541",
            fg="#5BC0BE",
            pady=10,
        )
        header.pack(fill="x", pady=(10, 5))

        # -------- MAIN FRAME --------
        self.main_frame = tk.Frame(root, bg="#1C2541", padx=20, pady=20)
        self.main_frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Input for player cards
        tk.Label(
            self.main_frame,
            text="Enter your starting cards (1–10, space-separated):",
            font=("Arial", 11),
            bg="#1C2541",
            fg="#FFFFFF",
        ).grid(row=0, column=0, sticky="w", columnspan=2)

        self.entry_cards = tk.Entry(self.main_frame, font=("Arial", 12), width=25)
        self.entry_cards.grid(row=1, column=0, sticky="w", pady=5)

        self.btn_deal = tk.Button(
            self.main_frame,
            text="🎲 Deal",
            bg="#5BC0BE",
            fg="black",
            font=("Arial", 11, "bold"),
            command=self.start_game,
        )
        self.btn_deal.grid(row=1, column=1, padx=10)

        # Labels for cards and totals
        self.lbl_player = tk.Label(self.main_frame, text="Your Cards: [] | Sum: 0",
                                   bg="#1C2541", fg="#FFFFFF", font=("Arial", 12))
        self.lbl_player.grid(row=2, column=0, columnspan=2, sticky="w", pady=(10, 0))

        self.lbl_computer = tk.Label(self.main_frame, text="Computer Cards: [] | Sum: ?",
                                     bg="#1C2541", fg="#FFFFFF", font=("Arial", 12))
        self.lbl_computer.grid(row=3, column=0, columnspan=2, sticky="w")

        # Result label
        self.lbl_result = tk.Label(self.main_frame, text="", bg="#1C2541",
                                   fg="#FFD700", font=("Arial", 13, "bold"), pady=10)
        self.lbl_result.grid(row=4, column=0, columnspan=2, sticky="w")

        # Buttons for actions
        btn_frame = tk.Frame(self.main_frame, bg="#1C2541", pady=10)
        btn_frame.grid(row=5, column=0, columnspan=2)

        self.btn_hit = tk.Button(btn_frame, text="Hit", command=self.hit,
                                 bg="#3A506B", fg="#FFFFFF", font=("Arial", 11, "bold"),
                                 width=10, state="disabled")
        self.btn_hit.grid(row=0, column=0, padx=5)

        self.btn_stand = tk.Button(btn_frame, text="Stand", command=self.stand,
                                   bg="#3A506B", fg="#FFFFFF", font=("Arial", 11, "bold"),
                                   width=10, state="disabled")
        self.btn_stand.grid(row=0, column=1, padx=5)

        self.btn_reset = tk.Button(btn_frame, text="Play Again", command=self.reset_game,
                                   bg="#5BC0BE", fg="black", font=("Arial", 11, "bold"), width=12)
        self.btn_reset.grid(row=0, column=2, padx=5)

    # ---------- GAME LOGIC ----------
    def start_game(self):
        raw = self.entry_cards.get().strip()
        if not raw:
            messagebox.showwarning("Input Required", "Please enter your starting cards (e.g. 7 4).")
            return

        try:
            self.user_cards = list(map(int, raw.split()))
        except ValueError:
            messagebox.showerror("Invalid Input", "Enter only numbers between 1–10.")
            return

        if any(c not in CARD_VALUES for c in self.user_cards):
            messagebox.showerror("Invalid Card", "Cards must be between 1 and 10.")
            return

        self.computer_cards = [random.choice(CARD_VALUES)]
        self.update_labels()

        # Enable action buttons
        self.btn_hit.config(state="normal")
        self.btn_stand.config(state="normal")
        self.lbl_result.config(text="Game started! You can Hit or Stand.")

    def hit(self):
        if self.game_over:
            return
        new_card = random.choice(CARD_VALUES)
        self.user_cards.append(new_card)
        self.update_labels()

        if sum(self.user_cards) > 21:
            self.end_game()

    def stand(self):
        if self.game_over:
            return
        # Computer draws one more card
        self.computer_cards.append(random.choice(CARD_VALUES))
        self.update_labels()
        self.end_game()

    def end_game(self):
        self.game_over = True
        self.btn_hit.config(state="disabled")
        self.btn_stand.config(state="disabled")

        player_total = sum(self.user_cards)
        comp_total = sum(self.computer_cards)
        result = ""

        if player_total > 21:
            result = "You Lose! (Busted over 21)"
        elif comp_total > 21:
            result = "You Win! (Computer busted)"
        elif player_total > comp_total:
            result = "You Win! (Higher total)"
        elif player_total < comp_total:
            result = "You Lose! (Lower total)"
        else:
            result = "It's a Draw!"

        self.lbl_result.config(text=result)
        self.update_labels()
        messagebox.showinfo("Game Result", result)

    def update_labels(self):
        self.lbl_player.config(
            text=f"Your Cards: {self.user_cards} | Sum: {sum(self.user_cards)}"
        )

        # Show all computer cards if game over
        if self.game_over:
            self.lbl_computer.config(
                text=f"Computer Cards: {self.computer_cards} | Sum: {sum(self.computer_cards)}"
            )
        else:
            # Only show first card before stand
            shown = [self.computer_cards[0]] if self.computer_cards else []
            self.lbl_computer.config(
                text=f"Computer Cards: {shown} | Sum: ?"
            )

    def reset_game(self):
        self.user_cards = []
        self.computer_cards = []
        self.entry_cards.delete(0, tk.END)
        self.lbl_player.config(text="Your Cards: [] | Sum: 0")
        self.lbl_computer.config(text="Computer Cards: [] | Sum: ?")
        self.lbl_result.config(text="")
        self.btn_hit.config(state="disabled")
        self.btn_stand.config(state="disabled")
        self.game_over = False


# -------- RUN THE GAME --------
if __name__ == "__main__":
    root = tk.Tk()
    app = BlackjackGUI(root)
    root.mainloop()
