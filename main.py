import tkinter as tk
import psutil
import os
from PIL import Image, ImageTk

#Ferme l’app avec button
def close_app():
   screen_app.destroy() 

#Ferme l’app avec q
def quit(event):
   screen_app.destroy() 

#Retourne sur le bureau sans fermer l’app
def return_desktop():
   pass

#Redemarre le raspberry
def reboot():
   os.system("sudo reboot")

#Eteint le raspberry
def shutdown():
   os.system("sudo shutdown now")

#Affiche les stats du CPU
def cpu_stat():
   cpu_usage = psutil.cpu_percent(interval=1)
   cpu_label.config(text=f"CPU Usage : {cpu_usage}%")
   screen_app.after(1000, cpu_stat)

#Affiche les stats du réseau
def network_stat():
   net_io = psutil.net_io_counters()
   net_label.config(text=f"Bytes Sent: {net_io.bytes_sent}, Bytes Received: {net_io.bytes_recv}")
   screen_app.after(1000, network_stat)

#Affiche le nombre d’app lancé
def proc_stat():
   proc_count = len(psutil.pids())
   proc_label.config(text=f"Number of running processes : {proc_count}")
   screen_app.after(1000, proc_stat)

#Affiche les 5 derniers accès SSH
def ssh_stat():
   ssh_usage = "test"
   ssh_label.config(text=f"SSH Monitoring : {ssh_usage}")
   screen_app.after(1000, ssh_stat)

#Définition des parametres de fenetre
screen_app = tk.Tk()
screen_app.title("Monitoring Raspberry")
screen_app.attributes("-fullscreen", True)
screen_app.overrideredirect(True)
screen_app.geometry("1280x1024")

#Chargement image et convertion pour Tkinter
img_logo_path = "logo.png"
img_logo = Image.open(img_logo_path)
img_logo = img_logo.resize((150, 200))
logo = ImageTk.PhotoImage(img_logo)

#Chargement des labels TK
#Logo
img_logo_label = tk.Label(screen_app, image=logo)
img_logo_label.image = logo # Référence pour éviter que l’image soit rez par le garbage collector
img_logo_label.pack()
#Button quit
close_button = tk.Button(screen_app, text="Quit", command=close_app)
close_button.pack()
#Button desktop
close_button = tk.Button(screen_app, text="Return Desktop", command=return_desktop)
close_button.pack()
#Button reboot
close_button = tk.Button(screen_app, text="Reboot", command=reboot)
close_button.pack()
#Button shutdown
close_button = tk.Button(screen_app, text="Shutdown", command=shutdown)
close_button.pack()
#Exit app with q keyboard cap
screen_app.bind('<q>', quit)
#Affichage des stats ssh
ssh_label = tk.Label(screen_app, text="Waiting...")
ssh_log = ssh_stat()
ssh_label = tk.Label(screen_app, text=f"{ssh_log}")
ssh_label.pack()
#Affichage des stats cpu
cpu_label = tk.Label(screen_app, text="Waiting...")
cpu_log = cpu_stat()
cpu_label = tk.Label(screen_app, text=f"{cpu_stat}")
cpu_label.pack()
#Affichage des stats proc
proc_label = tk.Label(screen_app, text="Waiting...")
proc_log = proc_stat()
proc_label = tk.Label(screen_app, text=f"{proc_stat}")
proc_label.pack()
#Affichage des stats network
net_label = tk.Label(screen_app, text="Waiting...")
net_log = network_stat()
net_label = tk.Label(screen_app, text=f"{network_stat}")
net_label.pack()

#Boucle principale
screen_app.mainloop()
