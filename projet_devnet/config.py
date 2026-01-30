import paramiko
import socket
from getpass import getpass

def test_ssh_direct():
    """Test SSH direct avec paramiko"""
    print("🔍 TEST DE CONNEXION SSH DIRECT")
    print("=" * 60)
    
    host = "devnetsandboxiosxec8k.cisco.com"
    port = 22
    
    # Demander les identifiants
    print(f"Host: {host}:{port}")
    username = input("Username (de l'onglet I/O): ").strip()
    password = getpass("Password (de l'onglet I/O): ").strip()
    
    print(f"\n🔄 Connexion avec: {username}@{host}")
    
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        ssh.connect(
            hostname=host,
            port=port,
            username=username,
            password=password,
            timeout=15,
            look_for_keys=False,
            allow_agent=False,
            banner_timeout=15,
            auth_timeout=15
        )
        
        print("✅ CONNEXION SSH RÉUSSIE !")
        
        # Tester une commande Cisco
        print("\n🧪 Test de commande 'show version'...")
        stdin, stdout, stderr = ssh.exec_command("show version", timeout=10)
        output = stdout.read().decode('utf-8', errors='ignore')
        
        if output:
            print("✅ Commande exécutée avec succès")
            print("\n📄 Extrait de la sortie:")
            lines = output.split('\n')
            for i, line in enumerate(lines[:10]):  # 10 premières lignes
                if line.strip():
                    print(f"  {line}")
            
            # Chercher des infos spécifiques
            for line in lines:
                if 'uptime' in line.lower():
                    print(f"\n⏰ Uptime: {line.strip()}")
                    break
                if 'Version' in line:
                    print(f"📦 {line.strip()}")
        
        ssh.close()
        return True, username, password
        
    except paramiko.AuthenticationException:
        print("\n❌ ERREUR D'AUTHENTIFICATION")
        print("Les identifiants sont incorrects ou ont expiré.")
        return False, None, None
        
    except Exception as e:
        print(f"\n⚠️ Erreur: {type(e).__name__}: {e}")
        return False, None, None

def quick_netmiko_test(username, password):
    """Test rapide avec Netmiko"""
    print("\n" + "=" * 60)
    print("⚡ TEST NETMIKO RAPIDE")
    print("=" * 60)
    
    from netmiko import ConnectHandler
    
    device = {
        "host": "devnetsandboxiosxec8k.cisco.com",
        "username": username,
        "password": password,
        "device_type": "cisco_ios",
        "port": 22,
        "timeout": 30,
        "global_delay_factor": 2,
    }
    
    try:
        print("Connexion en cours...")
        conn = ConnectHandler(**device)
        
        print(f"✅ Connecté! Prompt: {conn.find_prompt()}")
        
        # Tester quelques commandes
        commands = [
            ("show version | include Version", "Version"),
            ("show clock", "Heure"),
            ("show ip interface brief | count", "Nombre d'interfaces"),
        ]
        
        for cmd, desc in commands:
            try:
                output = conn.send_command(cmd, delay_factor=2)
                print(f"\n📊 {desc}:")
                print(f"  {output[:200]}..." if len(output) > 200 else f"  {output}")
            except:
                print(f"  Commande '{cmd}' non disponible")
        
        conn.disconnect()
        print("\n🎉 Test Netmiko réussi!")
        return True
        
    except Exception as e:
        print(f"❌ Échec Netmiko: {e}")
        return False

def main():
    print("🔄 OBTENTION DE NOUVEAUX IDENTIFIANTS")
    print("=" * 60)
    print("""
INSTRUCTIONS:
1. Retournez sur https://devnetsandbox.cisco.com
2. Cliquez sur votre réservation "Catalyst 8000 Always-On"
3. Rafraîchissez la page (F5)
4. Cliquez sur l'onglet "I/O"
5. Copiez les NOUVEAUX username et password
""")
    
    input("Appuyez sur Entrée quand vous avez les nouveaux identifiants...")
    
    # Test SSH direct
    success, username, password = test_ssh_direct()
    
    if success and username and password:
        print("\n" + "=" * 60)
        print("🎯 IDENTIFIANTS VALIDÉS!")
        print("=" * 60)
        print(f"Username: {username}")
        print(f"Password: {password}")
        print(f"Host: devnetsandboxiosxec8k.cisco.com:22")
        
        # Sauvegarder pour plus tard
        save = input("\n💾 Sauvegarder dans un fichier? (o/n): ").lower()
        if save == 'o':
            with open("sandbox_credentials.txt", "w") as f:
                f.write(f"host=devnetsandboxiosxec8k.cisco.com\n")
                f.write(f"port=22\n")
                f.write(f"username={username}\n")
                f.write(f"password={password}\n")
                f.write(f"device_type=cisco_ios\n")
            print("✅ Identifiants sauvegardés dans sandbox_credentials.txt")
        
        # Tester Netmiko
        use_netmiko = input("\n🔧 Tester avec Netmiko? (o/n): ").lower()
        if use_netmiko == 'o':
            quick_netmiko_test(username, password)
    
    else:
        print("\n" + "=" * 60)
        print("🚨 PROBLÈME NON RÉSOLU")
        print("=" * 60)
        print("""
Solutions alternatives:

OPTION 1 - Nouvelle réservation:
1. Retournez au catalogue sandbox
2. Cliquez sur "Catalyst 8000 Always-On"
3. Cliquez sur "Launch" pour une NOUVELLE réservation
4. Attendez 1-2 minutes
5. Récupérez les NOUVEAUX identifiants

OPTION 2 - Sandbox CSR1000v (plus stable):
   Host: sandbox-iosxe-latest-1.cisco.com
   Username: developer
   Password: C1sco12345
   Port: 22

OPTION 3 - Vérifier votre connexion:
   ssh -v {username}@devnetsandboxiosxec8k.cisco.com
""")

if __name__ == "__main__":
    main()