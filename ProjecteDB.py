import sqlite3
db=sqlite3.connect('ProjecteDB.db')
eixir='n'
while eixir!='n':
    canal=input("Vols posar un canal? s/n")
    if(canal=='s'):
        Subscripció_activada=bool(input("El usuari té una subscripció?"))
        IDcan=input("Quina és la ID del canal?")
        if(IDcan!="" and Subscripció_activada!=""):
            db.execute("INSERT INTO Canal VALUES ({Subscripció_activada},{IDcan})")
    capitol=input("Vols posar un capitol? s/n")
    if (canal=='s'):
        IDcap=input("Quina és el ID del capitol?")
        Nomcap=input("Com es diu el captilol")
        Numcap=int(input("Quin número es el capitol?"))
        Durada_del_capitol=int(input("Quant dura el capitol?"))
        if(Durada_del_capitol<0 or Durada_del_capitol>57):
            print("No pot durar mys de 0 min o més de 57 min")
        else:
            if(IDcap!="" and  Nomcap!="" and Numcap>0 ):
                db.execute("INSERT INTO Capitols VALUES ({IDcap},{Durada_del_capitol},{Nomcap},{Numcap})")
    Programes=input("Vols fer un programa? s/n")
    if(Programes=='s'):
        IDpr=input("Quina és la ID del programa?")
        Rating =int(input("Quin rating té?"))
        Expectativa_de_emisió=int(input("Quants anys pensa estar en emisió?"))
        Genere=input("De quin genere es?")
        Edat_general=input("Quina és la edat general")
        Nom_del_programa=input("Com es diu el programa")
        Nºtemp=int(input("Quantes temporades té?"))
        Nºcap=int(input("Quants capitols té?"))
        if(IDpr!="" and Rating!="" and Expectativa_de_emisió>0 and Genere!="" and Edat_general>0 and Nom_del_programa!="" and Nºtemp>3 and Nºcap>20 ):
            db.execute("INSERT INTO Programes VALUES ({IDpr},{Rating},{Expectativa_de_emisió},{Genere},{Descripció},{Edat_general},{Nom_del_programa},{Nºtemp},{Nºcap})")
    Propaganda=input("Vols posar un canal? s/n")
    if(Propaganda=='s'):
        IDprop=input("Quina és la ID de la propaganda?")
        if(IDprop!=""):
            db.execute("INSERT INTO Propaganda VALUES ({IDprop})")
    Temporades=input("Vols posar un canal? s/n")
    if(Temporades=='s'):
        IDtemp=input("Quina és la ID del canal?")
        Numtemp=int(input("Quantes temporades té?"))
        if(IDtemp!="" and Numtemp>0):
            db.execute("INSERT INTO Temporades VALUES ({IDtemp},{Numtemp})")
    Usuaris=input("Vols posar un canal? s/n")
    if(Usuaris=='s'):
        IDus=(input("Quina és la ID del canal?"))
        Registrarse=bool(input("El usuario esta registrado?"))
        if(IDus!="" and Registrarse!=None):
            db.execute("INSERT INTO Canal VALUES ({IDus},{Registrarse})")
        canal=input("Vols eixir ja? s/n")