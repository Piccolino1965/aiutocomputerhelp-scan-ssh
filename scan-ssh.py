#---------------------ScanSSH.py------------------------------
# aiutocomputerhelp 2024
#------------------------------------------------------------- 

import socket
import paramiko
import sys
import logging
# Configura il logging di paramiko per mostrare solo errori critici
logging.getLogger("paramiko").setLevel(logging.CRITICAL)
# Funzione per controllare i servizi SSH su un dato indirizzo IP
def check_service(ip, port):
    try:
        # Crea un socket TCP per tentare la connessione alla porta
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1) #per una lan è gia troppo, per internet senza grossissimi problemi , anche. (alzate a 2 se c'e' molto ritardo)
        result = sock.connect_ex((ip, port))
        print(f"Controllo Porta {port}")
       
        # Verifica se la porta è aperta
        if result == 0:
            try:
                # Controllo se la porta è un servizio SSH usando paramiko
                transport = paramiko.Transport((ip, port))
                transport.start_client(timeout=2)
                print(f"Servizio SSH rilevato sulla porta {port}. Target acquisito.")
                transport.close()
                sys.exit()
                return True  # Interrompe la scansione
            except paramiko.ssh_exception.SSHException:
                # Messaggio semplificato per SSHException
                print(f"Porta {port} aperta ma non è SSH (nessun banner SSH rilevato)")
            except (OSError, Exception) as e:
                print(f"Errore imprevisto su porta {port}: {e}")
               
            finally:
                sock.close()
        else:
            print(f"Porta {port} chiusa o non accessibile")
    except (socket.timeout, ConnectionRefusedError, OSError) as e:
        print(f"Nessun servizio sulla porta {port}: {e}")
    except Exception as e:
        print(f"Errore imprevisto durante la connessione alla porta {port}: {e}")
    return False  # Continua la scansione
# Funzione principale per gestire la scansione di due range di porte
def scan_ports(ip, range1, range2=None):
    for port in range1:
        if check_service(ip, port):
            break    # Trovare ssh O= Ok - Interrompe la scansione se viene trovato SSH
    if range2:
        for port in range2:
            if check_service(ip, port):
                break     # Interrompe la scansione se viene trovato SSH
# Esempio di utilizzo
target_ip = "x.x.x.x"         # Sostituisci con l'indirizzo IP target o nome Host
range1 = range(18, 85)        # Potete aggiungere quanti range di porte
range2 = range(10998, 11004)  # dovete modificare anche _ports(ip, range1, range2=None , range3=Nome) etc etc
scan_ports(target_ip, range1, range2)
#—————————————————
