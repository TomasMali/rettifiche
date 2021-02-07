
import re
from tkinter import *
from tkinter import messagebox
from functools import partial

import tkinter.ttk
from tkinter.filedialog import askopenfile

window = Tk()
window.wm_title("ALCODA Rec C. python_tomas_new")
#"""""""""""""""""""""""""""" FUNCTIONS """""""""""""""""""""""""""""


fl = []
numero = 0 



#"""""""""""""""""""""""""""" LABELS """""""""""""""""""""""""""""


def loadFields():
    import glob
    with open(glob.glob("file//*")[0], 'r') as f:
         lines = f.readlines()
    if  int(s_info.get()) < 2:
         messagebox.showerror("Error Python", "Attenzione!! La riga 0 e 1 non si possono calcolare!!!")
         return
    if  int(s_info.get()) >= (len(lines)):
         messagebox.showerror("Error Python", "Attenzione!! La riga non esiste!!!")
         return
    target = lines[int(s_info.get())]


    lista = (re.split(r'\t', target)[:-1])

    first = lista[0]
    lista.pop(0)

    fist_as_list = [first[0:6], first[6:19], first[19:27], first[27:28], first[28:29] ]
    fl = fist_as_list + lista


    if len(fl) < 35:
         messagebox.showerror("Error Python", "Attenzione!! Controllare la riga perche mancano dati!!!")
         return

    e1.delete(0,END)
    e1.insert(END, fl[0])
    e2.delete(0,END)
    e2.insert(END, fl[1])
    e3.delete(0,END)
    e3.insert(END, fl[2])
    e4.delete(0,END)
    e4.insert(END, fl[3])
    e5.delete(0,END)
    e5.insert(END, fl[4])
    e6.delete(0,END)
    e6.insert(END, fl[5])
    e7.delete(0,END)
    e7.insert(END, fl[6])
    e8.delete(0,END)
    e8.insert(END, fl[7])  
    e9.delete(0,END)
    e9.insert(END, fl[8])
    e10.delete(0,END)
    e10.insert(END, fl[9])
    e11.delete(0,END)
    e11.insert(END, fl[10])
    e12.delete(0,END)
    e12.insert(END, fl[11])
    e13.delete(0,END)
    e13.insert(END, fl[12])
    e14.delete(0,END)
    e14.insert(END, fl[13])
    e15.delete(0,END)
    e15.insert(END, fl[14])
    e16.delete(0,END)
    e16.insert(END, fl[15])
    e17.delete(0,END)
    e17.insert(END, fl[16])
    e18.delete(0,END)
    e18.insert(END, fl[17])
    e19.delete(0,END)
    e19.insert(END, fl[18])
    e20.delete(0,END)
    e20.insert(END, fl[19])
    e21.delete(0,END)
    e21.insert(END, fl[20])
    e22.delete(0,END)
    e22.insert(END, fl[21])
    e23.delete(0,END)
    e23.insert(END, fl[22])
    e24.delete(0,END)
    e24.insert(END, fl[23])
    e25.delete(0,END)
    e25.insert(END, fl[24])
    e26.delete(0,END)
    e26.insert(END, fl[25])
    e27.delete(0,END)
    e27.insert(END, fl[26])
    e28.delete(0,END)
    e28.insert(END, fl[27])
    e29.delete(0,END)
    e29.insert(END, fl[28])
    e30.delete(0,END)
    e30.insert(END, fl[29])
    e31.delete(0,END)
    e31.insert(END, fl[30])
    e32.delete(0,END)
    e32.insert(END, fl[31])
    e33.delete(0,END)
    e33.insert(END, fl[32])
    e34.delete(0,END)
    e34.insert(END, fl[33])
    e35.delete(0,END)
    e35.insert(END, fl[34])

#"""""""""""""""""""""""""""" LABELS """""""""""""""""""""""""""""

def back():
    loc = int(s_info.get())
    s_info.delete(0,END)
    s_info.insert(END, loc-1)
    loadFields()

def forward():
    loc = int(s_info.get())
    s_info.delete(0,END)
    s_info.insert(END, loc +1)
    loadFields()

def showDetail(nomeCampo, obb, condizioi, rapp):
     nomeCampoEntity.delete(0,END)
     nomeCampoEntity.insert(END, nomeCampo)
     obbEntity.delete(0,END)
     obbEntity.insert(END, obb)
     condizioniEntity.delete(0,END)
     condizioniEntity.insert(END, condizioi)
     rappEntity.delete(0,END)
     rappEntity.insert(END, rapp)

def getFile():
     file = askopenfile(parent=window,mode='rb',title='Choose a file')


#"""""""""""""""""""""""""""" LABELS """""""""""""""""""""""""""""










stepTwo = LabelFrame(window, text=" Controllo delle righe: ", bd=4 )
stepTwo.grid(row=0, columnspan=12, sticky='WE', \
             padx=15, pady=15, ipadx=5, ipady=5)


content = LabelFrame(window, text=" Contenuto della riga: ", bd=4 )
content.grid(row=1, columnspan=12, sticky='WE', \
             padx=15, pady=15, ipadx=5, ipady=5)


l_info = Label(stepTwo, text="Numero riga")
l_info.grid(row=0, column=0 , padx=15, pady=15, ipadx=5, ipady=5)

s_info = IntVar()
s_info = Entry(stepTwo, textvariable=s_info, width=6, bd = 3)
s_info.grid(row=0, column=1 )
s_info.insert(END, 2)



b2 = Button(stepTwo, text="<", width=4, bd = 5, command=back ) 
b2.grid(row=0, column=3 )
b3 = Button(stepTwo, text=">", width=4, bd = 5, command=forward ) 
b3.grid(row=0, column=4 )


b1 = Button(stepTwo, text="Calcola", width=12, bd = 5, command=loadFields ) 
b1.grid(row=0, column=5 )

tkinter.ttk.Separator(stepTwo, orient=VERTICAL).grid(column=6, padx=50 , row=0,sticky='ns')
tkinter.ttk.Separator(stepTwo, orient=VERTICAL).grid(column=6, padx=50 , row=1,sticky='ns')








Label(stepTwo, text="Nome campo: ").grid(row=0, column=7)


nomeCampoEntity = StringVar()
nomeCampoEntity = Entry(stepTwo, textvariable=nomeCampoEntity , width=40)
nomeCampoEntity.grid(row=0, column=8)

Label(stepTwo, text="Obbligatorio: ").grid(row=1, column=9)

obbEntity = StringVar()
obbEntity = Entry(stepTwo, textvariable=obbEntity , width=14)
obbEntity.grid(row=1, column=10)

Label(stepTwo, text="RAPPR: ").grid(row=0, column=9)

rappEntity = StringVar()
rappEntity = Entry(stepTwo, textvariable=rappEntity , width=14)
rappEntity.grid(row=0, column=10)

Label(stepTwo, text="Condizioni: ").grid(row=1, column=7)

condizioniEntity = StringVar()
condizioniEntity = Entry(stepTwo, textvariable=condizioniEntity , width=40)
condizioniEntity.grid(row=1, column=8)









showDetail_par = partial(showDetail, "Valore fisso ALCODA", "SI", "", "X(6)")
l1 = Button(content, text="1", width=3, command = showDetail_par ) 
l1.grid(row=2, column=0)


s1 = StringVar()
e1 = Entry(content, textvariable=s1, width=8)
e1.grid(row=3, column=0)

showDetail_par = partial(showDetail, "Codice accisa del depositario autorizzato", "SI", "", "X(13)")
l2 = Button(content, text="2", width=3, command = showDetail_par ) 
l2.grid(row=2, column=1)

s2 = StringVar()
e2 = Entry(content, textvariable=s2 , width=13)
e2.grid(row=3, column=1)

showDetail_par = partial(showDetail, "Data della movimentazione o del rientro della terza copia (nel formato AAAAMMGG)", "COND", "CN10,CN31,CN42,CN50", "9(8)")
l3 = Button(content, text="3", width=3, command = showDetail_par ) 
l3.grid(row=2, column=2)

s3 = StringVar()
e3 = Entry(content, textvariable=s3 , width=8)
e3.grid(row=3, column=2)


showDetail_par = partial(showDetail, "Tipo record", "SI", "TA17", "X(1)")
l4 = Button(content, text="4", width=3, command = showDetail_par ) 
l4.grid(row=2, column=3)

s4 = StringVar()
e4 = Entry(content, textvariable=s4 , width=2)
e4.grid(row=3, column=3)


showDetail_par = partial(showDetail, "Tipo richiesta", "SI", "TA01, CN53", "X(1)")
l5 = Button(content, text="5", width=3, command = showDetail_par ) 
l5.grid(row=2, column=4)

s5 = StringVar()
e5 = Entry(content, textvariable=s5 , width=2)
e5.grid(row=3, column=4)


showDetail_par = partial(showDetail, "Identificativo registro: Tipo registro Tipo Prodotto", "SI", "CN59,TA15", "X(1)")
l6 = Button(content, text="6", width=3, command = showDetail_par ) 
l6.grid(row=2, column=5)


s6 = StringVar()
e6 = Entry(content, textvariable=s6 , width=2)
e6.grid(row=3, column=5)

showDetail_par = partial(showDetail, "Identificativo registro: Codice Ufficio che ha rilasciato il registro", "SI", "CN60, TA03", "X(8)")
l7 = Button(content, text="7", width=3, command = showDetail_par ) 
l7.grid(row=2, column=6)

s7 = StringVar()
e7 = Entry(content, textvariable=s7 , width=8)
e7.grid(row=3, column=6)


showDetail_par = partial(showDetail, "Identificativo registro: Anno protocollo (formato AAAA) Anno di riferimento del Numero progressivo record/Identificativo univoco annuo", "SI", "CN57", "9(4)")
l8 = Button(content, text="8", width=3, command = showDetail_par ) 
l8.grid(row=2, column=7)

s8 = StringVar()
e8 = Entry(content, textvariable=s8 , width=4)
e8.grid(row=3, column=7)


showDetail_par = partial(showDetail, "Identificativo registro: Numero protocollo Identificativo combinazione prodotti/sezione del Registro Telematico", "SI", "CN51", "X(10)")
l9 = Button(content, text="9", width=3, command = showDetail_par ) 
l9.grid(row=2, column=8)

s9 = StringVar()
e9 = Entry(content, textvariable=s9 , width=10)
e9.grid(row=3, column=8)


showDetail_par = partial(showDetail, "Numero progressivo record Numero progressivo record / Identificativo univoco progressivo annuo", "COND", "CN56, CN11", "9(7)")
l10 = Button(content, text="10", width=3, command = showDetail_par ) 
l10.grid(row=2, column=9)

s10 = StringVar()
e10 = Entry(content, textvariable=s10 , width=7)
e10.grid(row=3, column=9)



""""""""""""""""""""""""""""""""""""""""""""""""""""""""


showDetail_par = partial(showDetail, "Codice prodotto", "COND", "CN01, CN28, CN33, CN39, CN43, CN61, TA20", "X(18)")
l11 = Button(content, text="11", width=3, command = showDetail_par ) 
l11.grid(row=4, column=0)

s11 = StringVar()
e11 = Entry(content, textvariable=s11 , width=18)
e11.grid(row=5, column=0)


showDetail_par = partial(showDetail, "Quantità in chilogrammi", "COND", "CN26, CN63", "9(11)V9(5)")
l12 = Button(content, text="12", width=3, command = showDetail_par ) 
l12.grid(row=4, column=1)

s12 = StringVar()
e12 = Entry(content, textvariable=s12 , width=17)
e12.grid(row=5, column=1)



showDetail_par = partial(showDetail, "Quantità in litri anidri", "COND", "CN16, CN63", "9(11)V9(5)")
l13 = Button(content, text="13", width=3, command = showDetail_par ) 
l13.grid(row=4, column=2)

s13 = StringVar()
e13 = Entry(content, textvariable=s13 , width=17)
e13.grid(row=5, column=2)


""""""""""""""""""""""""""""""""""""""""""""""""""""""""

showDetail_par = partial(showDetail, "Quantità in litri idrati", "COND", "CN15, CN63", "9(11)V9(5)")
l14 = Button(content, text="14", width=3, command = showDetail_par ) 
l14.grid(row=4, column=3)

s14 = StringVar()
e14 = Entry(content, textvariable=s14, width=17)
e14.grid(row=5, column=3)

showDetail_par = partial(showDetail, "Mosto ottenuto in litri: lettura iniziale", "COND", "CN14", "9(10)")
l15 = Button(content, text="15", width=3, command = showDetail_par ) 
l15.grid(row=4, column=4)

s15 = StringVar()
e15 = Entry(content, textvariable=s15 , width=10)
e15.grid(row=5, column=4)

showDetail_par = partial(showDetail, "Mosto ottenuto in litri: lettura finale", "COND", "CN14", "9(10)")
l16 = Button(content, text="16", width=3, command = showDetail_par ) 
l16.grid(row=4, column=5)

s16 = StringVar()
e16 = Entry(content, textvariable=s16 , width=10)
e16.grid(row=5, column=5)


showDetail_par = partial(showDetail, "Ettogradi", "COND", "CN17, CN63", "9(11)V9(5)")
l17 = Button(content, text="17", width=3, command = showDetail_par ) 
l17.grid(row=4, column=6)

s17 = StringVar()
e17 = Entry(content, textvariable=s17 , width=16)
e17.grid(row=5, column=6)


showDetail_par = partial(showDetail, "Grado plato / Grado alcolico", "COND", "CN17, CN63", "9(2)V9(5)")
l18 = Button(content, text="18", width=3, command = showDetail_par ) 
l18.grid(row=4, column=7)

s18 = StringVar()
e18 = Entry(content, textvariable=s18 , width=8)
e18.grid(row=5, column=7)


showDetail_par = partial(showDetail, "Tipo stoccaggio", "COND", "CN01, CN62, TA16 ", "X(1)")
l19 = Button(content, text="19", width=3, command = showDetail_par ) 
l19.grid(row=4, column=8)

s19 = StringVar()
e19 = Entry(content, textvariable=s19 , width=2)
e19.grid(row=5, column=8)

showDetail_par = partial(showDetail, "Volume nominale confezioni", "COND", "CN06", "9(3)V9(5)")
l20 = Button(content, text="20", width=3, command = showDetail_par ) 
l20.grid(row=4, column=9)

s20 = StringVar()
e20 = Entry(content, textvariable=s20 , width=9)
e20.grid(row=5, column=9)


""""""""""""""""""""""""""""""""""""""""""""""""""""""""
showDetail_par = partial(showDetail, "Numero delle confezioni ", "COND", "CN06", "9(7)")
l21 = Button(content, text="21", width=3, command = showDetail_par ) 
l21.grid(row=6, column=0)

s21 = StringVar()
e21 = Entry(content, textvariable=s21 , width=7)
e21.grid(row=7, column=0)


showDetail_par = partial(showDetail, "Tipo documento / verbale", "COND", "CN11, CN41, TA05", "X(3)")
l22 = Button(content, text="22", width=3, command = showDetail_par ) 
l22.grid(row=6, column=1)

s22 = StringVar()
e22 = Entry(content, textvariable=s22 , width=4)
e22.grid(row=7, column=1)


showDetail_par = partial(showDetail, "Numero documento / verbale", "COND", "CN11, CN21, CN37, CN44, CN49", "X(21)")
l23 = Button(content, text="23", width=3, command = showDetail_par ) 
l23.grid(row=6, column=2)

s23 = StringVar()
e23 = Entry(content, textvariable=s23 , width=21)
e23.grid(row=7, column=2)


showDetail_par = partial(showDetail, "Data emissione/convalida documento/verbale (nel formato AAAAMMGG)", "COND", "CN11, CN21", "9(8)")
l24 = Button(content, text="24", width=3, command = showDetail_par ) 
l24.grid(row=6, column=3)

s24 = StringVar()
e24 = Entry(content, textvariable=s24 , width=8)
e24.grid(row=7, column=3)


showDetail_par = partial(showDetail, "Numero del DAA cumulativo, del DAS collettivo o del X-E", "COND", "CN04", "X(21)")
l25 = Button(content, text="25", width=3, command = showDetail_par ) 
l25.grid(row=6, column=4)

s25 = StringVar()
e25 = Entry(content, textvariable=s25 , width=21)
e25.grid(row=7, column=4)



showDetail_par = partial(showDetail, "Provenienza / destinazione della merce (sigla paese comunitario) ", "COND", "CN09, CN40, TA06", "X(2)")
l26 = Button(content, text="26", width=3, command = showDetail_par ) 
l26.grid(row=6, column=5)

s26 = StringVar()
e26 = Entry(content, textvariable=s26, width=2)
e26.grid(row=7, column=5)


showDetail_par = partial(showDetail, "Mittente / Destinatario del prodotto. Per maggiori informazioni consultare il processo di valorizzazione di questo campo, disponibile sul sito internet dell'Agenzia", "COND", "CN05, CN21, CN29", "X(16)")
l27 = Button(content, text="27", width=3, command = showDetail_par ) 
l27.grid(row=6, column=6)

s27 = StringVar()
e27 = Entry(content, textvariable=s27, width=16)
e27.grid(row=7, column=6)

showDetail_par = partial(showDetail, "Tipo movimentazione ", "COND", "CN23, CN38, CN58, TA07", "X(1)")
l28 = Button(content, text="28", width=3, command = showDetail_par ) 
l28.grid(row=6, column=7)

s28 = StringVar()
e28 = Entry(content, textvariable=s28, width=2)
e28.grid(row=7, column=7)

showDetail_par = partial(showDetail, "Causale di movimentazione  ", "COND", "CN11, CN34, CN38, TA21(C), TA21(S)", "9(3)")
l29 = Button(content, text="29", width=3, command = showDetail_par ) 
l29.grid(row=6, column=8)

s29 = StringVar()
e29 = Entry(content, textvariable=s29, width=3)
e29.grid(row=7, column=8)


""""""""""""
showDetail_par = partial(showDetail, "Codice posizione fiscale", "COND", "CN11, CN27, CN48, TA22", "9(3)")
l30 = Button(content, text="30", width=3, command = showDetail_par ) 
l30.grid(row=8, column=0)

s30 = StringVar()
e30 = Entry(content, textvariable=s30, width=3)
e30.grid(row=9, column=0)

showDetail_par = partial(showDetail, "Accisa erariale a debito / Accisa sospesa", "COND", "CN07, CN09, CN24, CN48", "9(9)V9(2)")
l31 = Button(content, text="31", width=3, command = showDetail_par ) 
l31.grid(row=8, column=1)

s31 = StringVar()
e31 = Entry(content, textvariable=s31, width=12)
e31.grid(row=9, column=1)

showDetail_par = partial(showDetail, "Note", "COND", "CN22", "X(800)")
l32 = Button(content, text="note", width=4, command = showDetail_par ) 
l32.grid(row=8, column=2)

s32 = StringVar()
e32 = Entry(content, textvariable=s32, width=20)
e32.grid(row=9, column=2)


showDetail_par = partial(showDetail, "Numero progressivo DAA per l’ARC di riferimento", "COND", "CN35", "9(2)")
l33 = Button(content, text="33", width=3, command = showDetail_par ) 
l33.grid(row=8, column=3)

s33 = StringVar()
e33 = Entry(content, textvariable=s33, width=2)
e33.grid(row=9, column=3)


showDetail_par = partial(showDetail, "Numero identificativo locale del Draft DAA", "COND", "CN36", "X(22)")
l34 = Button(content, text="34", width=3, command = showDetail_par ) 
l34.grid(row=8, column=4)

s34 = StringVar()
e34 = Entry(content, textvariable=s34, width=22)
e34.grid(row=9, column=4)


showDetail_par = partial(showDetail, "Progressivo dettagli del DAA univoco ", "COND", "CN36", "9(3)")
l35 = Button(content, text="35", width=3, command = showDetail_par ) 
l35.grid(row=8, column=5)

s35 = StringVar()
e35 = Entry(content, textvariable=s35, width=3)
e35.grid(row=9, column=5)



window.mainloop()