# Projet DevNet - Collecte d'Informations Catalyst 8000

> Un script Python pour collecter et analyser les informations de configuration et de performance d'un routeur Cisco Catalyst 8000 via SSH.

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## Description

Ce projet automatise la collecte d'informations sur un équipement réseau Cisco Catalyst 8000 à partir du sandbox DevNet de Cisco. Il se connecte via SSH et exécute diverses commandes pour récupérer :

- Informations système (hostname, version, uptime)
- État des interfaces réseau
- Table de routage
- Utilisation mémoire et CPU
- Table ARP et voisins CDP
- Configuration en cours et sauvegardée

Les résultats sont générés dans un rapport Markdown avec horodatage et statistiques détaillées.

## Démarrage rapide

### Prérequis

- Python 3.8 ou supérieur
- Accès à la [sandbox Cisco DevNet](https://devnetsandbox.cisco.com)
- Réservation active du "Catalyst 8000 Always-On"
- Connexion Internet stable

### Installation

1. **Cloner ou télécharger le projet**
   ```bash
   cd /home/fred/Documents/cours/DevNet/tp/projet_devnet
   ```

2. **Créer un environnement virtuel (optionnel mais recommandé)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Sur Windows: venv\Scripts\activate
   ```

3. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

### 1. Obtenir les identifiants

Depuis le [portail DevNet Sandbox](https://devnetsandbox.cisco.com) :

1. Sélectionnez "Catalyst 8000 Always-On"
2. Cliquez sur votre réservation active
3. Allez dans l'onglet **I/O**
4. Notez le **username** et **password**

### 2. Configurer le script

Éditez [projet.py](projet.py) et mettez à jour le dictionnaire `DEVICE` avec vos identifiants :

```python
DEVICE = {
    "host": "devnetsandboxiosxec8k.cisco.com",
    "username": "VOS_IDENTIFIANTS",
    "password": "VOTRE_MOT_DE_PASSE",
    "device_type": "cisco_ios",
    "port": 22,
    "name": "Catalyst 8000 Always-On"
}
```

### 3. (Optionnel) Valider la connexion

Utilisez le script de test pour vérifier votre connexion SSH :

```bash
python config.py
```

Ce script :
- Teste la connexion SSH directe avec Paramiko
- Valide les identifiants
- Teste quelques commandes Cisco
- Peut sauvegarder vos identifiants dans `sandbox_credentials.txt`

## Utilisation

### Exécuter la collecte

```bash
python projet.py
```

### Résultat

Le script génère deux fichiers :

| Fichier | Description |
|---------|-------------|
| `projet_devnet_resultats.md` | Rapport complet avec toutes les informations collectées |
| `resume_execution.txt` | Résumé textuel de l'exécution |

### Exemple de sortie console

```
============================================================
PROJET DEVNET - CATALYST 8000 SANDBOX
============================================================
Session: betukumesukabamba
Device: Catalyst 8000 Always-On
Rapport: projet_devnet_resultats.md
============================================================

Connecté avec succès!

 COLLECTE DES DONNÉES EN COURS...
============================================================
[...collecte des informations...]

 PROJET TERMINÉ AVEC SUCCÈS !
```

## Structure du projet

```
projet_devnet/
├── projet.py                      # Script principal
├── config.py                      # Utilitaire de test de connexion
├── requirements.txt               # Dépendances Python
├── README.md                      # Ce fichier
├── sandbox_credentials.txt        # Identifiants (généré, à ignorer)
├── projet_devnet_resultats.md    # Rapport (généré)
└── resume_execution.txt          # Résumé (généré)
```

## Fonctionnalités principales

### Collecte d'informations système

```python
# Informations du routeur
show running-config
show version

# État réseau
show ip interface brief
show ip route
```

### Statistiques système

```python
# Performance
show memory statistics
show processes cpu sorted

# Connectivité
show arp
show cdp neighbors
show clock
```

### Génération de rapport

- Analyse automatique des données
- Statistiques et comptage d'interfaces/routes
- Export en Markdown avec mise en forme
- Horodatage de chaque exécution
- Logging dans la console et en fichier

## Modules utilisés

| Module | Version | Utilisation |
|--------|---------|------------|
| **netmiko** | 4.2.0 | Connexion SSH et exécution de commandes Cisco |
| **paramiko** | 3.4.0 | Protocole SSH (dépendance de Netmiko) |

## Exemple de rapport généré

Le rapport [projet_devnet_resultats.md](projet_devnet_resultats.md) contient :

```markdown
# Rapport du Projet DevNet - 30/01/2026 15:42:15

## Informations de la session
- Device cible: Catalyst 8000 Always-On
- Host: devnetsandboxiosxec8k.cisco.com

## 1. Informations du Routeur/Switch
- Hostname: Cat8kv_AO_Sandbox
- Version: Cisco IOS XE Software, Version 17.15.04c

## 2. Analyse des Interfaces
- Total: 3
- UP/UP: 1
- DOWN: 2

...
```

## Dépannage

### Erreur d'authentification

```
 ERREUR D'AUTHENTIFICATION: Les identifiants sont incorrects ou ont expiré.
```

**Solution** :
- Vérifiez vos identifiants dans le portail DevNet
- Rafraîchissez la réservation (F5)
- Créez une nouvelle réservation si nécessaire

### Timeout ou connexion refusée

```
Erreur: TimeoutError: Connection timed out
```

**Solution** :
- Vérifiez votre connexion Internet
- Vérifiez que le host est correct
- Augmentez le `global_delay_factor` dans le code

### Commandes invalides

Certaines commandes peuvent ne pas être disponibles selon la version. Le script les ignore automatiquement avec un message d'avertissement.

## Ressources

- [DevNet Sandbox - Cisco](https://devnetsandbox.cisco.com)
- [Documentation Netmiko](https://github.com/ktbyers/netmiko)
- [Cisco IOS Commands Reference](https://www.cisco.com/c/en/us/support/docs/ios-nx-os-software/ios-software/216806-understand-show-commands-output.html)
- [Automatisation réseau avec Python](https://www.networktocode.com/blog/)

## Cas d'usage

- **Documentation réseau** : Collecter automatiquement la configuration des équipements
- **Analyse d'infrastructure** : Générer des rapports sur l'état du réseau
- **Automatisation** : Base pour des scripts de provisioning ou d'audit
- **Formation** : Apprentissage de l'automatisation réseau avec Python

## Notes importantes

- **Sécurité** : Les identifiants sont stockés en clair. Ne pas commiter `sandbox_credentials.txt` ou les identifiants en dur dans le code en production.
- **Restrictions** : Ce script est configuré pour le sandbox Cisco public. Adaptez le code pour votre infrastructure.
- **Délais** : Les commandes Cisco peuvent être lentes. Un délai global est appliqué pour éviter les timeouts.

## Contribution

Ce projet est un travail académique. Les améliorations et suggestions sont les bienvenues !

## Licence

Ce projet est fourni à titre éducatif. Utilisez-le librement à des fins d'apprentissage.

---

**Créé pour** : Cours DevNet - Automatisation réseau  
**Date** : Janvier 2026  
**Platform** : Cisco Catalyst 8000 Sandbox
**Auteur** : Betukumesu Kabamba Frederic
