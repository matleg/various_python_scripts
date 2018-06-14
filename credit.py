from tkinter import *


tab = []


def calc():
    mt = eval(montant.get())
    t = eval(taux.get())
    ms = eval(mensualites.get())

    mois = 1
    annee = 1 + mois / 12
    rb = mt * (t / 12 + 1)
    rs = rb - ms

    liste0 = [annee, mois, rb, rs]

    calc2(liste0, t, ms)


def calc2(ls, tau, mens):
    liste = []
    liste.append(ls)
    print(liste)
    for i in range(400):
        ms = 1 + i
        aee = ms / 12
        remb = (liste[i][3]) * (tau / 12 + 1)
        rest = remb - mens
        lili = [round(ms), round(aee), round(remb), round(rest)]
        liste.append(lili)
        print(liste[i])
        if rest < 0:
            print("\n")
            print("coût total " + str(ms * mens) + "   coût crédit = " + str(ms * mens - liste[0][2]))
            print("\n")

            break


# création fenêtre
fen = Tk()

tex1 = Label(fen, text="montant emprunte")
tex1.grid(row=0)

montant = Entry(fen)
montant.grid(row=0, column=1)

tex2 = Label(fen, text="taux interet")
tex2.grid(row=1)

taux = Entry(fen)
taux.grid(row=1, column=1)

tex3 = Label(fen, text="mensualites")
tex3.grid(row=2)

mensualites = Entry(fen)
mensualites.grid(row=2, column=1)

bou1 = Button(fen, text="calculer", command=calc)
bou1.grid(row=3)

fen.mainloop()

liste = []

##
##
### plot results
##plt.figure()
##plt.plot(t, S, label='Living')
##plt.plot(t, Z, label='Zombies')
##plt.xlabel('Days from outbreak')
##plt.ylabel('Population')
##plt.title('Zombie Apocalypse - No Init. Dead Pop.; No New Births.')
##plt.legend(loc=0)
