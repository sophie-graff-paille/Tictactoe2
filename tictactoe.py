from tkinter import *
from tkinter import messagebox

# création de la fenêtre
window = Tk()
window.title("Tic Tac So!")
window.geometry("500x600")

# frame pour les boutons du jeu
frame = Frame(window)
frame.pack(pady=5)

# variables globales pour le jeu
clicked = True
count = 0
score_X = 0
score_O = 0

# frame pour l'historique (et l'affichage des scores en temps réel)
frame2 = Frame(window)
frame2.pack(pady=10)

# pour qu'il n'y ait pas de double fonctions
# j'ai choisi de mettre un historique des parties avec un bouton pour l'afficher
# et de ne pas afficher les scores en temps réel

# # labels pour les scores
# label_X = Label(frame2, text="Score X: " + str(score_X), font=("Comic Sans MS", 12))
# label_X.pack(side=LEFT, padx=10)
# label_O = Label(frame2, text="Score O: " + str(score_O), font=("Comic Sans MS", 12))
# label_O.pack(side=LEFT, padx=20)

# historique des parties
def historique(score_X, score_O): # récupère les scores en temps réel
    # affiche l'historique des parties dans une fenêtre d'alerte messagebox
    messagebox.showinfo("Historique des parties", "X a gagné " + str(score_X) + " fois\nO a gagné " + str(score_O) + " fois")

# bouton pour afficher l'historique
btn_historique = Button(window, text="Historique", font=("Comic Sans MS", 20), bg="deeppink", fg="yellow", width=10, height=1, borderwidth=6, command=lambda: historique(score_X=score_X, score_O=score_O))
btn_historique.pack(side=TOP, padx=10)

# fonction qui désactive les boutons après la fin de la partie
def desactiver_boutons():
    btn1.config(state=DISABLED)
    btn2.config(state=DISABLED)
    btn3.config(state=DISABLED)
    btn4.config(state=DISABLED)
    btn5.config(state=DISABLED)
    btn6.config(state=DISABLED)
    btn7.config(state=DISABLED)
    btn8.config(state=DISABLED)
    btn9.config(state=DISABLED)

# fonction qui vérifie si quelqu'un a gagné
def verif_gagnant():
    global winner, score_X, score_O # récupère les variables globales
    winner = False # initialise la variable winner à False

    # vérifie si X a gagné
    if btn1["text"] == "X" and btn2["text"] == "X" and btn3["text"] == "X": # vérifie si les boutons 1, 2 et 3 ont le texte "X"
        # change la couleur du bouton gagnant aux boutons 1, 2 et 3
        btn1.config(bg="tomato")
        btn2.config(bg="tomato")
        btn3.config(bg="tomato")
        winner = True
        score_X += 1
        #label_X.config(text="Score X : " + str(score_X))
        messagebox.showinfo("Tic Tac So!", "X est le gagnant!") # affiche un message d'alerte messagebox
        desactiver_boutons() # désactive les boutons après la fin de la partie pour éviter de pouvoir cliquer dessus
    # on vérifie les autres possibilités de victoire avec les autres boutons et les autres combinaisons
    # on change la couleur des boutons gagnants, on affiche un message d'alerte messagebox et on désactive les boutons
    elif btn4["text"] == "X" and btn5["text"] == "X" and btn6["text"] == "X":
        btn4.config(bg="tomato")
        btn5.config(bg="tomato")
        btn6.config(bg="tomato")
        winner = True
        score_X += 1
        #label_X.config(text="Score X : " + str(score_X))
        messagebox.showinfo("Tic Tac So!", "X est le gagnant!")
        desactiver_boutons()
    elif btn7["text"] == "X" and btn8["text"] == "X" and btn9["text"] == "X":
        btn7.config(bg="tomato")
        btn8.config(bg="tomato")
        btn9.config(bg="tomato")
        winner = True
        score_X += 1
        #label_X.config(text="Score X : " + str(score_X))
        messagebox.showinfo("Tic Tac So!", "X est le gagnant!")
        desactiver_boutons()
    elif btn1["text"] == "X" and btn4["text"] == "X" and btn7["text"] == "X":
        btn1.config(bg="tomato")
        btn4.config(bg="tomato")
        btn7.config(bg="tomato")
        winner = True
        score_X += 1
        #label_X.config(text="Score X : " + str(score_X))
        messagebox.showinfo("Tic Tac So!", "X est le gagnant!")
        desactiver_boutons()
    elif btn2["text"] == "X" and btn5["text"] == "X" and btn8["text"] == "X":
        btn2.config(bg="tomato")
        btn5.config(bg="tomato")
        btn8.config(bg="tomato")
        winner = True
        score_X += 1
        #label_X.config(text="Score X : " + str(score_X))
        messagebox.showinfo("Tic Tac So!", "X est le gagnant!")
        desactiver_boutons()
    elif btn3["text"] == "X" and btn6["text"] == "X" and btn9["text"] == "X":
        btn3.config(bg="tomato")
        btn6.config(bg="tomato")
        btn9.config(bg="tomato")
        winner = True
        score_X += 1
        #label_X.config(text="Score X : " + str(score_X))
        messagebox.showinfo("Tic Tac So!", "X est le gagnant!")
        desactiver_boutons()
    elif btn1["text"] == "X" and btn5["text"] == "X" and btn9["text"] == "X":
        btn1.config(bg="tomato")
        btn5.config(bg="tomato")
        btn9.config(bg="tomato")
        winner = True
        score_X += 1
        #label_X.config(text="Score X : " + str(score_X))
        messagebox.showinfo("Tic Tac So!", "X est le gagnant!")
        desactiver_boutons()
    elif btn3["text"] == "X" and btn5["text"] == "X" and btn7["text"] == "X":
        btn3.config(bg="tomato")
        btn5.config(bg="tomato")
        btn7.config(bg="tomato")
        winner = True
        score_X += 1
        #label_X.config(text="Score X : " + str(score_X))
        messagebox.showinfo("Tic Tac So!", "X est le gagnant!")
        desactiver_boutons()

    # vérifie si O a gagné
    elif btn1["text"] == "O" and btn2["text"] == "O" and btn3["text"] == "O":
        btn1.config(bg="blue")
        btn2.config(bg="blue")
        btn3.config(bg="blue")
        winner = True
        score_O += 1
        #label_O.config(text="Score O : " + str(score_O))
        messagebox.showinfo("Tic Tac So!", "O est le gagnant!")
        desactiver_boutons()
    elif btn4["text"] == "O" and btn5["text"] == "O" and btn6["text"] == "O":
        btn4.config(bg="blue")
        btn5.config(bg="blue")
        btn6.config(bg="blue")
        winner = True
        score_O += 1
        #label_O.config(text="Score O : " + str(score_O))
        messagebox.showinfo("Tic Tac So!", "O est le gagnant!")
        desactiver_boutons()
    elif btn7["text"] == "O" and btn8["text"] == "O" and btn9["text"] == "O":
        btn7.config(bg="blue")
        btn8.config(bg="blue")
        btn9.config(bg="blue")
        winner = True
        score_O += 1
        #label_O.config(text="Score O : " + str(score_O))
        messagebox.showinfo("Tic Tac So!", "O est le gagnant!")
        desactiver_boutons()
    elif btn1["text"] == "O" and btn4["text"] == "O" and btn7["text"] == "O":
        btn1.config(bg="blue")
        btn4.config(bg="blue")
        btn7.config(bg="blue")
        winner = True
        score_O += 1
        #label_O.config(text="Score O : " + str(score_O))
        messagebox.showinfo("Tic Tac So!", "O est le gagnant!")
        desactiver_boutons()
    elif btn2["text"] == "O" and btn5["text"] == "O" and btn8["text"] == "O":
        btn2.config(bg="blue")
        btn5.config(bg="blue")
        btn8.config(bg="blue")
        winner = True
        score_O += 1
        #label_O.config(text="Score O : " + str(score_O))
        messagebox.showinfo("Tic Tac So!", "O est le gagnant!")
        desactiver_boutons()
    elif btn3["text"] == "O" and btn6["text"] == "O" and btn9["text"] == "O":
        btn3.config(bg="blue")
        btn6.config(bg="blue")
        btn9.config(bg="blue")
        winner = True
        score_O += 1
        #label_O.config(text="Score O : " + str(score_O))
        messagebox.showinfo("Tic Tac So!", "O est le gagnant!")
        desactiver_boutons()
    elif btn1["text"] == "O" and btn5["text"] == "O" and btn9["text"] == "O":
        btn1.config(bg="blue")
        btn5.config(bg="blue")
        btn9.config(bg="blue")
        winner = True
        score_O += 1
        #label_O.config(text="Score O : " + str(score_O))
        messagebox.showinfo("Tic Tac So!", "O est le gagnant!")
        desactiver_boutons()
    elif btn3["text"] == "O" and btn5["text"] == "O" and btn7["text"] == "O":
        btn3.config(bg="blue")
        btn5.config(bg="blue")
        btn7.config(bg="blue")
        winner = True
        score_O += 1
        #label_O.config(text="Score O : " + str(score_O))
        messagebox.showinfo("Tic Tac So!", "O est le gagnant!")
        desactiver_boutons()

    # vérifie l'égalité
    elif count == 9 and winner == False:
        messagebox.showinfo("Tic Tac So!", "Match nul!\nPersonne n'a gagné!")
        desactiver_boutons()

# fonction quand on clique sur un bouton
def btn_clic(b):
    global clicked, count # récupère les variables globales
    if b["text"] == " " and clicked == True: # si le bouton est vide et que c'est au tour de X
        b["text"] = "X" # met un X
        clicked = False # c'est au tour de O
        count += 1 # incrémente le compteur
        verif_gagnant() # vérifie si quelqu'un a gagné
    elif b["text"] == " " and clicked == False: # fait la même chose mais pour O
        b["text"] = "O"
        clicked = True
        count += 1
        verif_gagnant()
    else:
        messagebox.showerror("Tic Tac So!", "La case est déjà utilisée !\nChoisissez une autre case.") # sinon affiche une erreur si la case est déjà utilisée

# fonction qui réinitialise le jeu
def rejouer():
    global btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9 # récupère les variables globales
    global clicked, count 
    clicked = True # c'est au tour de X
    count = 0 # le compteur est remis à 0
    # réinitialise tous les boutons
    btn1["text"] = " " 
    btn2["text"] = " "
    btn3["text"] = " "
    btn4["text"] = " "
    btn5["text"] = " "
    btn6["text"] = " "
    btn7["text"] = " "
    btn8["text"] = " "
    btn9["text"] = " "
    # réactive tous les boutons
    btn1.config(bg="black", state=NORMAL)
    btn2.config(bg="black", state=NORMAL)
    btn3.config(bg="black", state=NORMAL)
    btn4.config(bg="black", state=NORMAL)
    btn5.config(bg="black", state=NORMAL)
    btn6.config(bg="black", state=NORMAL)
    btn7.config(bg="black", state=NORMAL)
    btn8.config(bg="black", state=NORMAL)
    btn9.config(bg="black", state=NORMAL)

# fonction pour quitter le jeu
def quitter():
    window.quit()

# création des 9 boutons du jeu
# la commande lambda permet d'envoyer une fonction avec un argument à un bouton (ici, la fonction btn_clic) et écrite en une seule ligne
btn1 = Button(frame, text=" ", font=("Comic Sans MS", 20), bg="black", fg="yellow", height=2, width=6, command=lambda: btn_clic(btn1)) 
btn2 = Button(frame, text=" ", font=("Comic Sans MS", 20), bg="black", fg="yellow", height=2, width=6, command=lambda: btn_clic(btn2))
btn3 = Button(frame, text=" ", font=("Comic Sans MS", 20), bg="black", fg="yellow", height=2, width=6, command=lambda: btn_clic(btn3))
btn4 = Button(frame, text=" ", font=("Comic Sans MS", 20), bg="black", fg="yellow", height=2, width=6, command=lambda: btn_clic(btn4))
btn5 = Button(frame, text=" ", font=("Comic Sans MS", 20), bg="black", fg="yellow", height=2, width=6, command=lambda: btn_clic(btn5))
btn6 = Button(frame, text=" ", font=("Comic Sans MS", 20), bg="black", fg="yellow", height=2, width=6, command=lambda: btn_clic(btn6))
btn7 = Button(frame, text=" ", font=("Comic Sans MS", 20), bg="black", fg="yellow", height=2, width=6, command=lambda: btn_clic(btn7))
btn8 = Button(frame, text=" ", font=("Comic Sans MS", 20), bg="black", fg="yellow", height=2, width=6, command=lambda: btn_clic(btn8))
btn9 = Button(frame, text=" ", font=("Comic Sans MS", 20), bg="black", fg="yellow", height=2, width=6, command=lambda: btn_clic(btn9))

btn1.grid(row=0, column=0)
btn2.grid(row=0, column=1)
btn3.grid(row=0, column=2)
btn4.grid(row=1, column=0)
btn5.grid(row=1, column=1)
btn6.grid(row=1, column=2)
btn7.grid(row=2, column=0)
btn8.grid(row=2, column=1)
btn9.grid(row=2, column=2)

# création des boutons pour rejouer et quitter
btnrejouer = Button(window, text="Rejouer", font=("Comic Sans MS", 20), bg="lime", fg="darkslateblue", height=1, width=6, borderwidth=6, command=rejouer)
btnrejouer.pack(side=LEFT, padx=50, pady=10)

btnquitter = Button(window, text="Quitter", font=("Comic Sans MS", 20), bg="red", fg="aqua", height=1, width=6, borderwidth=6, command=window.quit)
btnquitter.pack(side=RIGHT, padx=50, pady=10)

window.mainloop()