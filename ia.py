from tkinter import *
import random
from tkinter import messagebox

# cette ia est vraiment, vraiment facile à battre!!

# création de la fenêtre
window = Tk()
window.title("Tic Tac So!")
window.geometry("400x450")

# frame pour les boutons du jeu
frame = Frame(window)
frame.pack(pady=20)

# fonction qui permet à l'ordinateur de jouer
def ia(board, signe):
    # récupère les coordonnées des cases vides
    cases_vide = []
    for i in range(3): # pour chaque ligne
        for j in range(3): # pour chaque colonne
            if board[i][j] == 0: # si la case est vide
                cases_vide.append([i, j]) # ajoute les coordonnées de la case vide
    # choisit une case vide au hasard
    choix = random.choice(cases_vide)
    # place le signe de l'ordinateur dans la case choisie
    board[choix[0]][choix[1]] = signe
    return board
    
# fonction qui vérifie si l'ordinateur a gagné
def verif_gagnant(board, signe):
    # vérifie si l'ordinateur a gagné sur une ligne
    for i in range(3):
        if board[i][0] == signe and board[i][1] == signe and board[i][2] == signe:
            return True
    # vérifie si l'ordinateur a gagné sur une colonne
    for j in range(3):
        if board[0][j] == signe and board[1][j] == signe and board[2][j] == signe:
            return True
    # vérifie si l'ordinateur a gagné sur une diagonale
    if board[0][0] == signe and board[1][1] == signe and board[2][2] == signe:
        return True
    if board[0][2] == signe and board[1][1] == signe and board[2][0] == signe:
        return True
    # sinon, l'ordinateur n'a pas gagné
    return False

# fonction qui vérifie si la partie est terminée
def fin_partie(board):
    # vérifie si il y a un gagnant
    if verif_gagnant(board, 1) or verif_gagnant(board, 2):
        return True
    # vérifie si il y a une égalité
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return False
    return True

# fonction qui permet de rejouer
def rejouer():
    global board
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # réinitialise le plateau de jeu
    # affiche le plateau de jeu
    afficher_plateau(board)

# fonction qui permet de jouer
def btn_clic(i, j):
    global board
    # vérifie si la case est vide
    if board[i][j] == 0:
        # place le signe du joueur dans la case
        board[i][j] = 1
        # vérifie si la partie est terminée
        if fin_partie(board):
            # affiche le plateau de jeu
            afficher_plateau(board)
            # affiche un message de fin de partie
            if verif_gagnant(board, 1):
                messagebox.showinfo("Tic Tac So!", "Vous avez gagné !")
            elif verif_gagnant(board, 2):
                messagebox.showinfo("Tic Tac So!", "L'ordinateur a gagné !")
            else:
                messagebox.showinfo("Tic Tac So!", "Il y a égalité !")
        else:
            # affiche le plateau de jeu
            afficher_plateau(board)
            # permet à l'ordinateur de jouer
            board = ia(board, 2)
            # vérifie si la partie est terminée
            if fin_partie(board):
                # affiche le plateau de jeu
                afficher_plateau(board)
                # affiche un message de fin de partie
                if verif_gagnant(board, 1):
                    messagebox.showinfo("Tic Tac So!", "Vous avez gagné !")
                elif verif_gagnant(board, 2):
                    messagebox.showinfo("Tic Tac So!", "L'ordinateur a gagné !")
                else:
                    messagebox.showinfo("Tic Tac So!", "Il y a égalité !")
            else:
                # affiche le plateau de jeu
                afficher_plateau(board)
    else:
        messagebox.showerror("Tic Tac So!", "La case est déjà utilisée !\nChoisissez une autre case.")

# création du menu
menu = Menu(window)
window.config(menu=menu)

# création du menu "Jeu"
jeu = Menu(menu, tearoff=0)
menu.add_cascade(label="Jeu", menu=jeu)
jeu.add_command(label="Rejouer", command=rejouer)
jeu.add_separator()
jeu.add_command(label="Quitter", command=window.quit)

# création du plateau de jeu
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# création des boutons
btn = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(3):
    for j in range(3):
        btn[i][j] = Button(frame, text=" ", font=("Comic Sans MS", 20), width=6, height=2, command=lambda i=i, j=j: btn_clic(i, j))
        btn[i][j].grid(row=i, column=j)

# fonction qui permet d'afficher le plateau de jeu
def afficher_plateau(board):
    # affiche le plateau de jeu
    for i in range(3): # pour chaque ligne
        for j in range(3): # pour chaque colonne
            if board[i][j] == 0: # si la case est vide
                btn[i][j]["text"] = " " # affiche une case vide
            elif board[i][j] == 1: # si la case est occupée par le joueur
                btn[i][j]["text"] = "X" # affiche le signe du joueur
            else: # si la case est occupée par l'ordinateur
                btn[i][j]["text"] = "O" # affiche le signe de l'ordinateur

# fonction qui permet de quitter le jeu en détruisant la fenêtre
def quitter():
    window.destroy()

# # création du bouton pour quitter le jeu
# btn_quitter = Button(window, text="Quitter", font=("Comic Sans MS", 20), width=3, height=1, command=quitter)
# btn_quitter.pack(pady=10)

window.mainloop()