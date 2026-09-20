import tkinter as tk
from tkinter import messagebox

# Variáveis globais
player = "X"
board = [["" for _ in range(3)] for _ in range(3)]

# Função para verificar vencedor
def check_winner():
    # Linhas
    for row in board:
        if row[0] == row[1] == row[2] != "":
            return True
    # Colunas
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "":
            return True
    # Diagonais
    if board[0][0] == board[1][1] == board[2][2] != "":
        return True
    if board[0][2] == board[1][1] == board[2][0] != "":
        return True
    return False

# Função para verificar empate
def check_draw():
    for row in board:
        if "" in row:
            return False
    return True

# Função chamada ao clicar em um botão
def button_click(row, col):
    global player
    if board[row][col] == "":
        board[row][col] = player
        buttons[row][col].config(text=player,
                                 fg="blue" if player == "X" else "red",
                                 font=("Arial", 20, "bold"))
        if check_winner():
            messagebox.showinfo("Fim de jogo", f"Jogador {player} venceu!")
            reset_game()
        elif check_draw():
            messagebox.showinfo("Fim de jogo", "Empate!")
            reset_game()
        else:
            player = "O" if player == "X" else "X"

# Função para resetar o jogo
def reset_game():
    global player, board
    player = "X"
    board = [["" for _ in range(3)] for _ in range(3)]
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="", fg="black")

# Criando janela principal
root = tk.Tk()
root.title("Jogo da Velha")
root.configure(bg="#f0f0f0")

buttons = [[None for _ in range(3)] for _ in range(3)]

for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(root, text="", width=6, height=3,
                                      font=("Arial", 18, "bold"),
                                      bg="#ffffff",
                                      command=lambda r=row, c=col: button_click(r, c))
        buttons[row][col].grid(row=row, column=col, padx=5, pady=5)

reset_button = tk.Button(root, text="Reiniciar", command=reset_game,
                         font=("Arial", 14), bg="#d9d9d9")
reset_button.grid(row=3, column=0, columnspan=3, pady=10)

root.mainloop()
