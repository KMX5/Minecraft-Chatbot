#Importiert Module
import webbrowser
import time
import tkinter as tk


#Eingangstext mit erstem Input und Erläuterung
root = tk.Tk()
label1 = tk.Label(root, text="Hallo Spieler. Hier kannst du Informationen zu jedem Minecraft Mob finden." +"\n"
      "Sage dem Programm erst über welches Mob du etwas wissen möchtest. Sag ihm dann was du wissen möchtest"+"\n"
      "Du kannst nach den Leben, dem Spawn, den Drops und der Wahrscheinlichkeit der Drops, Besonderheiten, Lebensweise und der Zähmbarkeit fragen."+"\n"
      "Gib hierfür einfach Leben, Spawn, Drop, Version, Besonderheiten, Lebensweise oder Zähmbarkeit ein."+"\n"
      "Das Programm geht nun im Terminal weiter.")

#Wird in GUI Elemente einbetten
label1.pack()

#Beendet die Schleife dee Fensters
root.mainloop()


#Gibt dem Nutzer 3 Secunden zum lesen des Textes
time.sleep(3)

#Frage nach Mob und eingabe des Benutzers.
eingabe = input("Welches Mob interessiert dich: ")




#Liest Liste aus um zu schauen ob es das eingegebene Mob gibt
with open('mobsl.txt','r') as mobsl:
    r = mobsl.read()
    if eingabe in r:
         #Offnet Datei als Dictionary
      Mob = {}
      datei = open(eingabe +".txt","r")
      for line in datei:
            line = line.strip()
            zuordnung = line.split(" ")
            Mob[zuordnung[0]] = zuordnung[1]
      datei.close()
      


#Fragt den Nutzer nach den eigenschaften der Mobs
     #Öffnet eine Unendliche Schleife und tätigt einen 2.Input
      while True:
            eigenschaft = input("Du kannst nach den Leben, dem Spawn, den Drops und der Wahrscheinlichkeit der Drops,"+"\n"
                         " die Ersterscheinung, Besonderheiten, Lebensweis und der Zähmbarkeit fragen. Du kannst außerdem für mehr Infos "+"\n"
                         "nach einem Link zum Wiki fragen. Was wählst du: ")
            
            #Gib das Schlüsselwort und den Schlüsselbegriff aus
            if eigenschaft in Mob:
                 print("Die Information vom ",eigenschaft,":",Mob[eigenschaft])
                

          #Öffnet bei der Eingabe von "Link" das Minecraft-Wiki
            elif eigenschaft == 'Link':
                 webbrowser.open('https://minecraft.fandom.com/de/wiki/',0)
            

          #Bei Stop wird die Schleife Gestoppt und der Bot verabschiedet sich
            elif eigenschaft == 'Stop':
                 print("Vielen Dank das du unseren Chatbot genutzt hast.")
                 break
                 

          #Bei falscher Eingabe weißt dich auf eine fehler hin 
            else:
                 print("Die Eingabe ist nicht als Information in der Datenbank enthalten. ")
    