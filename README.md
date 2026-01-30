# Projet DevNet – Collecte d’Informations Cisco Catalyst 8000

> Script Python d’automatisation réseau permettant de collecter, analyser et documenter les informations système et réseau d’un routeur **Cisco Catalyst 8000** via SSH (DevNet Sandbox).

![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Cisco](https://img.shields.io/badge/Cisco-DevNet-blue.svg)

---

## Description

Ce projet automatise la collecte d’informations réseau sur un **Cisco Catalyst 8000** à partir du **Cisco DevNet Sandbox**.  
Il se connecte via SSH et exécute des commandes Cisco IOS XE afin de produire un **rapport détaillé au format Markdown**.

Les informations collectées incluent :

- Informations système (hostname, version IOS, modèle, uptime)
- État des interfaces réseau (UP / DOWN)
- Table de routage
- Utilisation mémoire et CPU
- Table ARP et voisins CDP
- Configuration running et startup

---

## Démarrage rapide

### Prérequis

- Python **3.8+**
- Compte Cisco DevNet
- Accès au **Catalyst 8000 Always-On Sandbox**
- Connexion Internet stable

---

## Installation

### 1 Cloner le projet

```bash
git clone https://github.com/FredDev12/projet_devnet.git
cd projet_devnet
````

### 2 Créer un environnement virtuel (recommandé)

```bash
python3 -m venv venv
source venv/bin/activate   # Windows : venv\Scripts\activate
```

### 3 Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## Configuration

### 1. Obtenir les identifiants DevNet

Depuis [https://devnetsandbox.cisco.com](https://devnetsandbox.cisco.com) :

1. Sélectionner **Catalyst 8000 Always-On**
2. Ouvrir la réservation active
3. Aller dans l’onglet **I/O**
4. Copier le **username** et le **password**

---

### 2. Configurer le script

Modifier le fichier `projet.py` :

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

---

### 3. (Optionnel) Tester la connexion SSH

```bash
python config.py
```

Ce script permet de :

* Vérifier la connexion SSH
* Tester des commandes Cisco
* Valider les identifiants
* Sauvegarder les accès localement (**à ne jamais commit**)

---

## Utilisation

### Lancer la collecte

```bash
python projet.py
```

---

## Fichiers générés

| Fichier                      | Description                       |
| ---------------------------- | --------------------------------- |
| `projet_devnet_resultats.md` | Rapport complet horodaté          |
| `resume_execution.txt`       | Résumé synthétique de l’exécution |

---

## Structure du projet

```text
projet_devnet/
├── projet.py                   # Script principal
├── config.py                   # Test de connexion SSH
├── requirements.txt            # Dépendances
├── README.md                   # Documentation
├── sandbox_credentials.txt     # Identifiants (IGNORÉ)
├── projet_devnet_resultats.md  # Rapport généré
└── resume_execution.txt        # Résumé généré
```

---

## Commandes Cisco utilisées

### Informations système

```text
show running-config
show version
```

### Réseau

```text
show ip interface brief
show ip route
```

### Performance

```text
show memory statistics
show processes cpu sorted
```

### Connectivité

```text
show arp
show cdp neighbors
show clock
```

---

## Exemple de résultats

```text
Hostname: Cat8kv_AO_Sandbox
Version IOS: Cisco IOS XE Software, Version 17.15.04c
Interfaces:
  - Total : 3
  - UP/UP : 1
  - DOWN  : 2
Routes détectées : 7
```

> **Note** : Le Catalyst 8000 du sandbox ne possède pas d’interfaces FastEthernet,
> ce qui explique un comptage FastEthernet = 0 (comportement normal).

---

## Dépannage

### Erreur d’authentification

```text
Authentication failed
```

**Solution** :

* Rafraîchir la réservation DevNet (F5)
* Vérifier l’onglet **I/O**
* Créer une nouvelle réservation si nécessaire

---

### Timeout SSH

```text
TimeoutError: Connection timed out
```

**Solution** :

* Vérifier la connexion Internet
* Augmenter `global_delay_factor` dans le script

---

## Sécurité

**Ne jamais commit** :

* `sandbox_credentials.txt`
* des identifiants en clair

Ajoute dans `.gitignore` :

```text
sandbox_credentials.txt
```

---

## Ressources

* Cisco DevNet Sandbox
  [https://devnetsandbox.cisco.com](https://devnetsandbox.cisco.com)
* Netmiko Documentation
  [https://github.com/ktbyers/netmiko](https://github.com/ktbyers/netmiko)
* Cisco IOS XE Commands
  [https://www.cisco.com](https://www.cisco.com)

---

## Cas d’usage

* Documentation réseau automatique
* Audit et inventaire d’équipements
* Apprentissage DevNet / NetDevOps
* Base pour automatisation réseau avancée

---

## Licence

Projet fourni à **des fins éducatives**.
Libre d’utilisation pour l’apprentissage.

---

### 👤 Auteur

**Betukumesu Kabamba Frederic** et **Iness Mufuka**
Cours **DevNet – Automatisation Réseau**
Janvier 2026
Cisco Catalyst 8000 Sandbox

```
