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
        if bzoard[0][col] == board[1][col] == board[2][col] != "":
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
        buttons[row][col].config(text=player)
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
            buttons[row][col].config(text="")

# Criando janela principal
root = tk.Tk()
root.title("Jogo da Velha")

buttons = [[None for _ in range(3)] for _ in range(3)]

for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(root, text="", width=10, height=3,
                                      command=lambda r=row, c=col: button_click(r, c))
        buttons[row][col].grid(row=row, column=col)

reset_button = tk.Button(root, text="Reiniciar", command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3)
root.mainloop()
