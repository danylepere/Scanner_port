import socket
print("=== Mini scanner de Ports ===")
target= input(" IP ou domaine à scanner : ")
port = int(input(" Port à tester, par exemple : 22, 80 ,43 : "))
print(f"Scan de (target) port (port)...")
s = socket.socket(socket.AF_INET, SOCK_STREAM)
s.settimeout(1)
try
    if s.connect_ex(target,port) == 0 :
        print(f"Resultat : Port (port) est OUVERT 🔓")
    else :
        print(f"Resultat : Port (port) est FERMÉ 🔒")
except :
    print(" Erreur : IP ou hôte injoignable ")
s.close()
print(" Scan terminé")
