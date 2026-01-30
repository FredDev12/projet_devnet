from netmiko import ConnectHandler
import time
from datetime import datetime

# ⚡ VOS IDENTIFIANTS VALIDÉS
DEVICE = {
    "host": "devnetsandboxiosxec8k.cisco.com",
    "username": "betukumesukabamba",
    "password": "1f6_Zr-tK928F",
    "device_type": "cisco_ios",
    "port": 22,
    "name": "Catalyst 8000 Always-On"
}

class Logger:
    """Classe pour gérer la journalisation dans la console et dans un fichier"""
    
    def __init__(self, filename="projet_devnet_resultats.md"):
        self.filename = filename
        self.log_buffer = []
        self.start_time = datetime.now()
        
        with open(self.filename, "w", encoding="utf-8") as f:
            f.write(f"# Rapport du Projet DevNet - {self.start_time.strftime('%d/%m/%Y %H:%M:%S')}\n\n")
            f.write("## ℹInformations de la session\n")
            f.write(f"- **Date d'exécution**: {self.start_time.strftime('%d/%m/%Y %H:%M:%S')}\n")
            f.write(f"- **Device cible**: {DEVICE['name']}\n")
            f.write(f"- **Host**: {DEVICE['host']}\n")
            f.write(f"- **Utilisateur**: {DEVICE['username']}\n")
            f.write(f"- **Port**: {DEVICE['port']}\n\n")
            f.write("---\n\n")
    
    def log(self, message, level="INFO"):
        """Ajoute un message au log"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        formatted_message = f"[{timestamp}] {level}: {message}"
        
        print(formatted_message)
        
        self.log_buffer.append(formatted_message)
        
        with open(self.filename, "a", encoding="utf-8") as f:
            if message.startswith("#"):
                f.write(f"\n{message}\n")
            elif message.startswith("##"):
                f.write(f"\n{message}\n")
            elif "**" in message or message.strip().startswith("-"):
                f.write(f"{message}\n")
            else:
                f.write(f"{message}\n")
    
    def save_output(self, section_title, content):
        """Sauvegarde une sortie spécifique dans le fichier"""
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(f"\n## {section_title}\n\n")
            f.write("```\n")
            f.write(content)
            f.write("\n```\n\n")
    
    def finalize(self):
        """Finalise le rapport"""
        end_time = datetime.now()
        duration = end_time - self.start_time
        
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write("\n---\n\n")
            f.write("## Résumé de l'exécution\n")
            f.write(f"- **Début**: {self.start_time.strftime('%H:%M:%S')}\n")
            f.write(f"- **Fin**: {end_time.strftime('%H:%M:%S')}\n")
            f.write(f"- **Durée totale**: {duration.total_seconds():.2f} secondes\n")
            f.write(f"- **Messages enregistrés**: {len(self.log_buffer)}\n\n")
            f.write("> Rapport généré automatiquement par le projet DevNet\n")

def connect_to_device(logger):
    """Connexion au device"""
    logger.log(f"Connexion à {DEVICE['name']}")
    logger.log(f"Host: {DEVICE['host']}")
    logger.log(f"Utilisateur: {DEVICE['username']}")
    logger.log("=" * 50)
    
    try:
        connection = ConnectHandler(
            host=DEVICE["host"],
            username=DEVICE["username"],
            password=DEVICE["password"],
            device_type=DEVICE["device_type"],
            port=DEVICE["port"],
            timeout=30,
            banner_timeout=30,
            auth_timeout=30,
            global_delay_factor=2,
        )
        
        logger.log("Connecté avec succès!")
        return connection
        
    except Exception as e:
        logger.log(f"Erreur de connexion: {e}", level="ERROR")
        return None

def safe_send_command(conn, command, description="", logger=None):
    """Exécute une commande avec gestion d'erreur"""
    if description and logger:
        logger.log(f" {description}")
    
    if logger:
        logger.log(f"Commande: {command}")
    
    try:
        output = conn.send_command(command, delay_factor=2)
        return output.strip()
    except Exception as e:
        error_msg = f" Erreur avec '{command}': {e}"
        if logger:
            logger.log(error_msg, level="WARNING")
        return ""

def parse_hostname(running_config):
    """Extrait le hostname de la configuration"""
    for line in running_config.splitlines():
        line = line.strip()
        if line.startswith("hostname"):
            return line.split()[1] if len(line.split()) > 1 else "Inconnu"
    return "Inconnu"

def parse_version_info(show_version):
    """Extrait les informations de version"""
    version = "Inconnue"
    model = "Inconnu"
    uptime = "Inconnu"
    
    lines = show_version.splitlines()
    for i, line in enumerate(lines):
        line_lower = line.lower()
        
        if "version" in line_lower and version == "Inconnue":
            version = line.strip()
        
        if "uptime" in line_lower:
            uptime = line.strip()
            
            if i + 1 < len(lines) and lines[i + 1].strip():
                uptime += " " + lines[i + 1].strip()
        
        if "software (" in line_lower and model == "Inconnu":
            
            parts = line.split("(")
            if len(parts) > 1:
                model = parts[1].replace(")", "").strip()
    
    return version, model, uptime

def analyze_interfaces(interfaces_output):
    """Analyse la sortie de 'show ip interface brief'"""
    interfaces = []
    
    for line in interfaces_output.splitlines():
        line = line.strip()
        if not line or line.startswith("Interface") or line.startswith("--"):
            continue
        
        parts = line.split()
        if len(parts) >= 4:
            interface = {
                "name": parts[0],
                "ip_address": parts[1] if parts[1] != "unassigned" else "N/A",
                "status": parts[-2],
                "protocol": parts[-1]
            }
            interfaces.append(interface)
    
    return interfaces

def count_interface_types(interfaces):
    """Compte les types d'interfaces"""
    counts = {
        "GigabitEthernet": 0,
        "FastEthernet": 0,
        "Loopback": 0,
        "Vlan": 0,
        "Tunnel": 0,
        "Other": 0
    }
    
    for intf in interfaces:
        name = intf["name"]
        if name.startswith("Gi"):
            counts["GigabitEthernet"] += 1
        elif name.startswith("Fa"):
            counts["FastEthernet"] += 1
        elif name.startswith("Lo"):
            counts["Loopback"] += 1
        elif name.startswith("Vl"):
            counts["Vlan"] += 1
        elif name.startswith("Tu"):
            counts["Tunnel"] += 1
        else:
            counts["Other"] += 1
    
    return counts

def parse_routing_table(routes_output):
    """Analyse la table de routage"""
    routes = []
    current_protocol = ""
    
    for line in routes_output.splitlines():
        line = line.strip()
        if not line:
            continue
        
        if line.startswith("Codes:"):
            continue
        
        if "Gateway of last resort" in line:
            continue
        
        if line and line[0].isalpha() and line[0].isupper():
            parts = line.split()
            if len(parts) >= 2:
                route = {
                    "type": parts[0],
                    "network": parts[1],
                    "via": parts[2] if len(parts) > 2 else "direct",
                    "interface": parts[-1] if len(parts) > 3 else "N/A"
                }
                routes.append(route)
    
    return routes

def collect_device_inventory(conn, logger):
    """Collecte toutes les informations du device"""
    inventory = {}
    
    logger.log("\n## 1. Informations du Routeur/Switch")
    logger.log("### Configuration en cours")
    
    running_config = safe_send_command(conn, "show running-config", "Récupération de la configuration", logger)
    inventory["running_config"] = running_config
    logger.save_output("Configuration Running", running_config[:5000])  # Limité à 5000 caractères
    
    hostname = parse_hostname(running_config)
    inventory["hostname"] = hostname
    logger.log(f"**Hostname**: {hostname}")
    
    logger.log("### Version du système")
    show_version = safe_send_command(conn, "show version", "Récupération des informations de version", logger)
    inventory["show_version"] = show_version
    logger.save_output("Show Version", show_version)
    
    version, model, uptime = parse_version_info(show_version)
    inventory["version"] = version
    inventory["model"] = model
    inventory["uptime"] = uptime
    
    logger.log(f"**Version**: {version[:100]}...")
    logger.log(f"**Modèle**: {model}")
    logger.log(f"**Uptime**: {uptime}")
    
    logger.log("\n## 2. Analyse des Interfaces")
    logger.log("### Statut des interfaces")
    
    interfaces_output = safe_send_command(conn, "show ip interface brief", "Récupération du statut des interfaces", logger)
    inventory["interfaces_output"] = interfaces_output
    logger.save_output("Show IP Interface Brief", interfaces_output)
    
    interfaces = analyze_interfaces(interfaces_output)
    inventory["interfaces"] = interfaces
    
    up_count = sum(1 for i in interfaces if i['status'] == 'up' and i['protocol'] == 'up')
    down_count = len(interfaces) - up_count
    
    logger.log(f"**Total d'interfaces**: {len(interfaces)}")
    logger.log(f"**Interfaces UP/UP**: {up_count}")
    logger.log(f"**Interfaces DOWN**: {down_count}")
    
    counts = count_interface_types(interfaces)
    logger.log("**Répartition par type**:")
    for intf_type, count in counts.items():
        if count > 0:
            logger.log(f"- {intf_type}: {count}")
    
    logger.log("\n**Interfaces UP (détail)**:")
    for intf in interfaces:
        if intf["status"] == "up" and intf["protocol"] == "up":
            logger.log(f"- {intf['name']}: IP={intf['ip_address']}, Status={intf['status']}/{intf['protocol']}")
    
    logger.log("\n## 3. Table de Routage")
    logger.log("### Routes disponibles")
    
    routes_output = safe_send_command(conn, "show ip route", "Récupération de la table de routage", logger)
    inventory["routes_output"] = routes_output
    logger.save_output("Show IP Route", routes_output[:5000]) 
    
    routes = parse_routing_table(routes_output)
    inventory["routes"] = routes
    
    route_types = {}
    for route in routes:
        route_type = route["type"]
        route_types[route_type] = route_types.get(route_type, 0) + 1
    
    logger.log(f"**Total de routes**: {len(routes)}")
    logger.log("**Répartition par type**:")
    
    type_names = {
        'C': 'Connected',
        'S': 'Static', 
        'R': 'RIP',
        'O': 'OSPF',
        'D': 'EIGRP',
        'B': 'BGP'
    }
    
    for rtype, count in sorted(route_types.items()):
        name = type_names.get(rtype, f'Type {rtype}')
        logger.log(f"- {rtype} ({name}): {count}")
    
    logger.log("\n## 4. Informations Supplémentaires")
    
    logger.log("### Utilisation mémoire")
    memory = safe_send_command(conn, "show memory statistics", "Récupération des statistiques mémoire", logger)
    if memory and "Invalid" not in memory:
        inventory["memory"] = memory
        logger.save_output("Show Memory Statistics", memory)
        logger.log("Statistiques mémoire récupérées")
    
    logger.log("### Utilisation CPU")
    cpu = safe_send_command(conn, "show processes cpu sorted", "Récupération de l'utilisation CPU", logger)
    if cpu and "Invalid" not in cpu:
        inventory["cpu"] = cpu
        logger.save_output("Show Processes CPU (extrait)", cpu[:3000])
        logger.log("Statistiques CPU récupérées")
    
    logger.log("### Configuration startup")
    startup = safe_send_command(conn, "show startup-config", "Vérification de la configuration sauvegardée", logger)
    if startup:
        inventory["startup_config"] = startup
        if "NVRAM" in startup:
            logger.log("Configuration sauvegardée dans NVRAM")
        else:
            logger.log("Pas de configuration sauvegardée dans NVRAM")
    
    logger.log("\n## 5. Commandes Supplémentaires (Bonus)")
    
    logger.log("### Table ARP")
    arp_table = safe_send_command(conn, "show arp", "Récupération de la table ARP", logger)
    if arp_table and "Invalid" not in arp_table:
        inventory["arp_table"] = arp_table
        logger.save_output("Show ARP (extrait)", arp_table[:2000])
    
    logger.log("### Voisins CDP")
    cdp_neighbors = safe_send_command(conn, "show cdp neighbors", "Récupération des voisins CDP", logger)
    if cdp_neighbors and "Invalid" not in cdp_neighbors:
        inventory["cdp_neighbors"] = cdp_neighbors
        logger.save_output("Show CDP Neighbors", cdp_neighbors[:2000])
    
    logger.log("### Horloge système")
    clock = safe_send_command(conn, "show clock", "Récupération de l'heure système", logger)
    if clock:
        inventory["clock"] = clock
        logger.log(f"**Heure système**: {clock}")
    
    return inventory

def generate_summary_report(inventory, logger):
    """Génère un rapport de synthèse"""
    logger.log("\n## Rapport de Synthèse")
    logger.log("### Résumé des informations collectées")
    
    summary = f"""
### SYNTHÈSE DU DEVICE

**Identifiant**: {inventory.get('hostname', 'Inconnu')}
**Modèle**: {inventory.get('model', 'Inconnu')}
**Uptime**: {inventory.get('uptime', 'Inconnu')}

### INTERFACES
- **Total**: {len(inventory.get('interfaces', []))}
- **UP/UP**: {sum(1 for i in inventory.get('interfaces', []) if i['status'] == 'up' and i['protocol'] == 'up')}
- **DOWN**: {sum(1 for i in inventory.get('interfaces', []) if i['status'] != 'up' or i['protocol'] != 'up')}

### ROUTAGE
- **Routes totales**: {len(inventory.get('routes', []))}

### CONFIGURATION
- **Running config**: {'Récupérée (' + str(len(inventory.get('running_config', ''))) + ' caractères)' if inventory.get('running_config') else 'Non récupérée'}
- **Startup config**: {'Récupérée' if inventory.get('startup_config') else 'Non récupérée'}

### STATISTIQUES
- **Mémoire**: {'Analysée' if inventory.get('memory') else 'Non analysée'}
- **CPU**: {'Analysé' if inventory.get('cpu') else 'Non analysé'}
- **ARP Table**: {'Récupérée' if inventory.get('arp_table') else 'Non récupérée'}
- **Voisins CDP**: {'Récupérés' if inventory.get('cdp_neighbors') else 'Non récupérés'}
"""
    
    logger.log(summary)
    
    # Sauvegarder le résumé
    with open("resume_execution.txt", "w", encoding="utf-8") as f:
        f.write("="*60 + "\n")
        f.write("RÉSUMÉ DE L'EXÉCUTION DU PROJET DEVNET\n")
        f.write("="*60 + "\n\n")
        f.write(f"Device: {inventory.get('hostname', 'Inconnu')}\n")
        f.write(f"Date: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
        f.write(f"Host: {DEVICE['host']}\n")
        f.write(f"Utilisateur: {DEVICE['username']}\n\n")
        
        f.write("STATISTIQUES:\n")
        f.write(f"- Interfaces: {len(inventory.get('interfaces', []))}\n")
        f.write(f"- Routes: {len(inventory.get('routes', []))}\n")
        f.write(f"- Version: {inventory.get('version', 'Inconnue')[:50]}...\n")
        f.write(f"- Modèle: {inventory.get('model', 'Inconnu')}\n\n")
        
        f.write("FICHIERS GÉNÉRÉS:\n")
        f.write(f"- Rapport complet: projet_devnet_resultats.md\n")
        f.write(f"- Résumé: resume_execution.txt\n")
        f.write(f"- Fichiers de sortie dans le dossier 'outputs/' si créé\n")

def main():
    # Initialiser le logger
    logger = Logger()
    
    print("\n" + "="*60)
    print("🎓 PROJET DEVNET - CATALYST 8000 SANDBOX")
    print("="*60)
    print(f"Session: {DEVICE['username']}")
    print(f"Device: {DEVICE['name']}")
    print(f"Rapport: projet_devnet_resultats.md")
    print("="*60)
    
    # Connexion
    conn = connect_to_device(logger)
    if not conn:
        logger.finalize()
        return
    
    try:
        # Collecte complète des données
        logger.log("\n" + "="*60)
        logger.log("COLLECTE DES DONNÉES EN COURS...")
        logger.log("="*60)
        
        inventory = collect_device_inventory(conn, logger)
        
        # Générer le rapport de synthèse
        generate_summary_report(inventory, logger)
        
        logger.log("\n" + "="*60)
        logger.log("PROJET TERMINÉ AVEC SUCCÈS ! ")
        logger.log("="*60)
        
        # Afficher les fichiers générés
        print(f"\nFICHIERS GÉNÉRÉS :")
        print(f"  1. projet_devnet_resultats.md - Rapport complet au format Markdown")
        print(f"  2. resume_execution.txt - Résumé de l'exécution")
        print(f"\nDONNÉES COLLECTÉES :")
        print(f"  - Configuration running: {len(inventory.get('running_config', ''))} caractères")
        print(f"  - Version système: {inventory.get('version', 'Inconnue')[:50]}...")
        print(f"  - Interfaces analysées: {len(inventory.get('interfaces', []))}")
        print(f"  - Routes trouvées: {len(inventory.get('routes', []))}")
        
    except Exception as e:
        logger.log(f"\nErreur pendant l'exécution: {e}", level="ERROR")
        import traceback
        error_details = traceback.format_exc()
        logger.save_output("Erreur détaillée", error_details)
        
    finally:
        # Fermer la connexion
        if conn:
            conn.disconnect()
            logger.log(f"\nConnexion fermée proprement")
        
        # Finaliser le rapport
        logger.finalize()
        
        # Message final
        print(f"\nLe rapport complet a été sauvegardé dans 'projet_devnet_resultats.md'")
        print(f" Durée totale: {datetime.now() - logger.start_time}")

if __name__ == "__main__":
    main()