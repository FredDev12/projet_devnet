# 📊 Rapport du Projet DevNet - 30/01/2026 15:42:15

## ℹ️ Informations de la session
- **Date d'exécution**: 30/01/2026 15:42:15
- **Device cible**: Catalyst 8000 Always-On
- **Host**: devnetsandboxiosxec8k.cisco.com
- **Utilisateur**: betukumesukabamba
- **Port**: 22

---

🚀 Connexion à Catalyst 8000 Always-On
📍 Host: devnetsandboxiosxec8k.cisco.com
👤 Utilisateur: betukumesukabamba
==================================================
✅ Connecté avec succès!

============================================================
🗂️  COLLECTE DES DONNÉES EN COURS...
============================================================

## 1. Informations du Routeur/Switch

### Configuration en cours
📌 Récupération de la configuration
Commande: show running-config

## Configuration Running

```
Building configuration...

Current configuration : 6557 bytes
!
! Last configuration change at 13:37:40 UTC Fri Jan 30 2026
!
version 17.15
service timestamps debug datetime msec
service timestamps log datetime msec
service password-encryption
platform qfp utilization monitor load 80
platform sslvpn use-pd
platform console virtual
!
hostname Cat8kv_AO_Sandbox
!
boot-start-marker
boot-end-marker
!
!
vrf definition Mgmt-vrf
 !
 address-family ipv4
 exit-address-family
 !
 address-family ipv6
 exit-address-family
!
aaa new-model
!
!
aaa group server tacacs+ labtac
 server name sandboxtacacs
 ip tacacs source-interface GigabitEthernet1
!
aaa authentication login default group labtac local
aaa authentication login netconf-authn group labtac local
aaa authorization exec default group labtac local if-authenticated 
aaa authorization exec netconf-authz group labtac local 
aaa authorization commands 1 default group labtac local if-authenticated 
aaa authorization commands 15 default group labtac local if-authenticated 
!
!
aaa session-id common
!
!
!
!
!
!
!
!
!
!
!
!
no ip domain lookup
ip domain name lab.devnetsandbox.local
!
!
!
login on-success log
!
!
subscriber templating
!
!
!
crypto pki trustpoint TP-self-signed-2996086467
 enrollment selfsigned
 subject-name cn=IOS-Self-Signed-Certificate-2996086467
 revocation-check none
 rsakeypair TP-self-signed-2996086467
 hash sha512
!
crypto pki trustpoint SLA-TrustPoint
 enrollment pkcs12
 revocation-check crl
 hash sha512
!
!
crypto pki certificate chain TP-self-signed-2996086467
 certificate self-signed 01
  30820330 30820218 A0030201 02020101 300D0609 2A864886 F70D0101 0D050030 
  31312F30 2D060355 04030C26 494F532D 53656C66 2D536967 6E65642D 43657274 
  69666963 6174652D 32393936 30383634 3637301E 170D3236 30313035 30393333 
  33375A17 0D333630 31303530 39333333 375A3031 312F302D 06035504 030C2649 
  4F532D53 656C662D 5369676E 65642D43 65727469 66696361 74652D32 39393630 
  38363436 37308201 22300D06 092A8648 86F70D01 01010500 0382010F 00308201 
  0A028201 0100E71D 5A4B848E 9846F9F2 5D461752 1F06D9F7 390D076B 560F61E2 
  D5D7901F 1FC34185 744C210A 24EC0D3A D157AC06 4520F49A F96FDBD3 72CBF2F2 
  2590E10F 42FDBC48 0CC3DA6C D54789CB F4870366 6A81B01D 928E6A7D 07A95A9C 
  D5C92EC0 3505CB74 DB1F9BC7 099DB5D7 6B635C1B 6D2FC3E1 521CAF16 2E68DA72 
  8384942A 669E423A 63647E2D 25386756 5F818C54 578E35D5 C68114E9 9DC13D94 
  E6E1F774 8F6F8F2C 5CAF5285 FAFDE66B 1F009971 12FEC0FA 61DA67A9 E8A57B14 
  2AA96EBA 3BBA9D8A 4236878E 3A176BE1 C1769A75 88FEB578 80D0C00D 82293585 
  F55D4808 DC575AF0 4BC92859 301409D8 87E0C89F 7938DF46 8595D697 5C3ACECB 
  4BC026C4 A1BB0203 010001A3 53305130 1D060355 1D0E0416 0414CF56 B094E61F 
  50C20319 949CF0AB 82419585 10CA301F 0603551D 23041830 168014CF 56B094E6 
  1F50C203 19949CF0 AB824195 8510CA30 0F060355 1D130101 FF040530 030101FF 
  300D0609 2A864886 F70D0101 0D050003 82010100 280CE4EC 501AD195 F8A58947 
  E93964CA B17DCBC0 4521ADB7 8AB7AF7F 45E768F7 40E03BDC 033EF179 0B1EF4EA 
  956B973A 01C24188 9209202D 57A8343B BA3A043D E34FC094 123653CC 39071992 
  B843010E 2B0D6EC4 A92217F8 ECDC4DD5 D869A892 FBC3336F 7412047B 73EA50F0 
  0EA48ED0 8E364A64 D49C4421 B1013CD5 5C82F628 134098AE 4E8C65AB 2F57867C 
  73A4B8C3 B058DD41 DDB98883 EBF23D4F 9754A011 95D6794C 10701EC5 09DDBE6D 
  8AE86BBC 76E97E33 BF6E970D C0D5F00D DB1B5FF0 60A436D2 5890502C 50511737 
  EB539CC8 03E32259 C88C944A B145B545 DB584D10 9891DCEC 635604B6 69233937 
  C5124A4F BB879376 342E0040 5C914576 66B51089
  	quit
crypto pki certificate chain SLA-TrustPoint
 certificate ca 01
  30820321 30820209 A0030201 02020101 300D0609 2A864886 F70D0101 0B050030 
  32310E30 0C060355 040A1305 43697363 6F312030 1E060355 04031317 43697363 
  6F204C69 63656E73 696E6720 526F6F74 20434130 1E170D31 33303533 30313934 
  3834375A 170D3338 30353330 31393438 34375A30 32310E30 0C060355 040A1305 
  43697363 6F312030 1E060355 04031317 43697363 6F204C69 63656E73 696E6720 
  526F6F74 20434130 82012230 0D06092A 864886F7 0D010101 05000382 010F0030 
  82010A02 82010100 A6BCBD96 131E05F7 145EA72C 2CD686E6 17222EA1 F1EFF64D 
  CBB4C798 212AA147 C655D8D7 9471380D 8711441E 1AAF071A 9CAE6388 8A38E520 
  1C394D78 462EF239 C659F715 B98C0A59 5BBB5CBD 0CFEBEA3 700A8BF7 D8F256EE 
  4AA4E80D DB6FD1C9 60B1FD18 FFC69C96 6FA68957 A2617DE7 104FDC5F EA2956AC 
  7390A3EB 2B5436AD C847A2C5 DAB553EB 69A9A535 58E9F3E3 C0BD23CF 58BD7188 
  68E69491 20F320E7 948E71D7 AE3BCC84 F10684C7 4BC8E00F 539BA42B 42C68BB7 
  C7479096 B4CB2D62 EA2F505D C7B062A4 6811D95B E8250FC4 5D5D5FB8 8F27D191 
  C55F0D76 61F9A4CD 3D992327 A8BB03BD 4E6D7069 7CBADF8B DF5F4368 95135E44 
  DFC7C6CF 04DD7FD1 02030100 01A34230 40300E06 03551D0F 0101FF04 04030201 
  06300F06 03551D13 0101FF04 05300301 01FF301D 0603551D 0E041604 1449DC85 
  4B3D31E5 1B3E6A17 606AF333 3D3B4C73 E8300D06 092A8648 86F70D01 010B0500 
  03820101 00507F24 D3932A66 86025D9F E838AE5C 6D4DF6B0 49631C78 240DA905 
  604EDCDE FF4FED2B 77FC460E CD636FDB DD44681E 3A5673AB 9093D3B1 6C9E3D8B 
  D9898
```

**Hostname**: Cat8kv_AO_Sandbox

### Version du système
📌 Récupération des informations de version
Commande: show version

## Show Version

```
Cisco IOS XE Software, Version 17.15.04c
Cisco IOS Software [IOSXE], Virtual XE Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 17.15.4c, RELEASE SOFTWARE (fc2)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2025 by Cisco Systems, Inc.
Compiled Fri 26-Sep-25 09:24 by mcpre


Cisco IOS-XE software, Copyright (c) 2005-2025 by cisco Systems, Inc.
All rights reserved.  Certain components of Cisco IOS-XE software are
licensed under the GNU General Public License ("GPL") Version 2.0.  The
software code licensed under GPL Version 2.0 is free software that comes
with ABSOLUTELY NO WARRANTY.  You can redistribute and/or modify such
GPL code under the terms of GPL Version 2.0.  For more details, see the
documentation or "License Notice" file accompanying the IOS-XE software,
or the applicable URL provided on the flyer accompanying the IOS-XE
software.


ROM: IOS-XE ROMMON

Cat8kv_AO_Sandbox uptime is 2 minutes
Uptime for this control processor is 4 minutes
System returned to ROM by reload
System image file is "bootflash:packages.conf"
Last reload reason: Reload Command



This product contains cryptographic features and is subject to United
States and local country laws governing import, export, transfer and
use. Delivery of Cisco cryptographic products does not imply
third-party authority to import, export, distribute or use encryption.
Importers, exporters, distributors and users are responsible for
compliance with U.S. and local country laws. By using this product you
agree to comply with applicable laws and regulations. If you are unable
to comply with U.S. and local laws, return this product immediately.

A summary of U.S. laws governing Cisco cryptographic products may be found at:
http://www.cisco.com/wwl/export/crypto/tool/stqrg.html

If you require further assistance please contact us by sending email to
export@cisco.com.

License Level: 
License Type: Perpetual
Next reload license Level: 

Addon License Level: 
Addon License Type: Subscription
Next reload addon license Level: 

The current throughput level is 20000 kbps 


Smart Licensing Status: Smart Licensing Using Policy

cisco C8000V (VXE) processor (revision VXE) with 1655530K/3075K bytes of memory.
Processor board ID 9YB8GCIXM3M
Router operating mode: Autonomous
3 Gigabit Ethernet interfaces
32768K bytes of non-volatile configuration memory.
3959732K bytes of physical memory.
11526144K bytes of virtual hard disk at bootflash:.

Configuration register is 0x2102
```

**Version**: Cisco IOS XE Software, Version 17.15.04c...
**Modèle**: X86_64_LINUX_IOSD-UNIVERSALK9-M, Version 17.15.4c, RELEASE SOFTWARE
**Uptime**: Uptime for this control processor is 4 minutes System returned to ROM by reload

## 2. Analyse des Interfaces

### Statut des interfaces
📌 Récupération du statut des interfaces
Commande: show ip interface brief

## Show IP Interface Brief

```
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet1       10.10.20.148    YES NVRAM  up                    up      
GigabitEthernet2       unassigned      YES NVRAM  administratively down down    
GigabitEthernet3       unassigned      YES NVRAM  administratively down down
```

**Total d'interfaces**: 3
**Interfaces UP/UP**: 1
**Interfaces DOWN**: 2
**Répartition par type**:
- GigabitEthernet: 3

**Interfaces UP (détail)**:
- GigabitEthernet1: IP=10.10.20.148, Status=up/up

## 3. Table de Routage

### Routes disponibles
📌 Récupération de la table de routage
Commande: show ip route

## Show IP Route

```
Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area 
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2, m - OMP
       n - NAT, Ni - NAT inside, No - NAT outside, Nd - NAT DIA
       i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, * - candidate default, U - per-user static route
       H - NHRP, G - NHRP registered, g - NHRP registration summary
       o - ODR, P - periodic downloaded static route, l - LISP
       a - application route
       + - replicated route, % - next hop override, p - overrides from PfR
       & - replicated local route overrides by connected

Gateway of last resort is 10.10.20.254 to network 0.0.0.0

S*    0.0.0.0/0 [1/0] via 10.10.20.254
      10.0.0.0/8 is variably subnetted, 2 subnets, 2 masks
C        10.10.20.0/24 is directly connected, GigabitEthernet1
L        10.10.20.148/32 is directly connected, GigabitEthernet1
```

**Total de routes**: 7
**Répartition par type**:
- C (Connected): 1
- D (EIGRP): 1
- E1 (Type E1): 1
- H (Type H): 1
- L (Type L): 1
- N1 (Type N1): 1
- S* (Type S*): 1

## 4. Informations Supplémentaires

### Utilisation mémoire
📌 Récupération des statistiques mémoire
Commande: show memory statistics

## Show Memory Statistics

```
Tracekey : 1#09df4bb29cead05ad42b2df3f4fab952  

                Head    Total(b)     Used(b)     Free(b)   Lowest(b)  Largest(b)
Processor  7DC71D56E048   2089388040   206066312   1883321728   1694866800   1301677300
reserve P  7DC71D56E0A0      102404          92      102312      102312      102312
 lsmpi_io  7DC7077B01A8     3149400     3148576         824         824         412
Dynamic heap limit(MB) 376 	 Use(MB) 0
```

Statistiques mémoire récupérées

### Utilisation CPU
📌 Récupération de l'utilisation CPU
Commande: show processes cpu sorted

## Show Processes CPU (extrait)

```
CPU utilization for five seconds: 1%/0%; one minute: 1%; five minutes: 1%
 PID Runtime(ms)     Invoked      uSecs   5Sec   1Min   5Min TTY Process 
 424         117         367        318  0.63%  0.15%  0.03% 435 SSH Process      
   9          73          24       3041  0.15%  0.04%  0.00%   0 Check heaps      
 199          25        4932          5  0.07%  0.01%  0.00%   0 IP ARP Retry Age 
 128          47        9939          4  0.07%  0.02%  0.00%   0 L2 LISP Punt Pro 
 129          57        9938          5  0.07%  0.02%  0.01%   0 SIS Punt Process 
 200          38        4932          7  0.07%  0.01%  0.00%   0 IP GARP Retry Ag 
 145          43           7       6142  0.07%  0.01%  0.00%   0 Per-minute Jobs  
 121          16        1674          9  0.07%  0.00%  0.00%   0 100ms check      
 125          20         410         48  0.07%  0.01%  0.00%   0 IOSXE-RP Punt Se 
 570          21         827         25  0.07%  0.00%  0.00%   0 ONEP Network Ele 
  80          20         183        109  0.07%  0.00%  0.00%   0 SASRcvWQWrk1     
  11           0           1          0  0.00%  0.00%  0.00%   0 DiscardQ Backgro 
  10           1           4        250  0.00%  0.00%  0.00%   0 Pool Manager     
  12           0           2          0  0.00%  0.00%  0.00%   0 Timers           
   3           2           4        500  0.00%  0.00%  0.00%   0 iosp_dmiauthd_10 
  16           0           1          0  0.00%  0.00%  0.00%   0 CEF MIB API      
  13           0         140          0  0.00%  0.00%  0.00%   0 WATCH_AFS        
  14           0           2          0  0.00%  0.00%  0.00%   0 ATM AutoVC Perio 
  19           0           2          0  0.00%  0.00%  0.00%   0 ARP Input        
   8           0           1          0  0.00%  0.00%  0.00%   0 RO Notify Timers 
  21           1          37         27  0.00%  0.00%  0.00%   0 IPC Event Notifi 
  15           0           2          0  0.00%  0.00%  0.00%   0 ATM VC Auto Crea 
  17           0           1          0  0.00%  0.00%  0.00%   0 VACS Background  
  24           0           4          0  0.00%  0.00%  0.00%   0 IPC Dynamic Cach 
  25           0          37          0  0.00%  0.00%  0.00%   0 IPC Service NonC 
  26           0           1          0  0.00%  0.00%  0.00%   0 IPC Zone Manager 
  27           0         176          0  0.00%  0.00%  0.00%   0 IPC Periodic Tim 
  18           0           1          0  0.00%  0.00%  0.00%   0 SENSOR-MGR event 
  29           1           1       1000  0.00%  0.00%  0.00%   0 IPC Process leve 
   7           0           1          0  0.00%  0.00%  0.00%   0 EDDRI_MAIN       
  31           1          11         90  0.00%  0.00%  0.00%   0 IPC Check Queue  
  32           0           1          0  0.00%  0.00%  0.00%   0 IPC Seat RX Cont 
   6          81          14       5785  0.00%  0.00%  0.00%   0 RF Slave Main Th 
  20           3         193         15  0.00%  0.00%  0.00%   0 ARP Background   
  22           1         176  
```

Statistiques CPU récupérées

### Configuration startup
📌 Vérification de la configuration sauvegardée
Commande: show startup-config
⚠️ Pas de configuration sauvegardée dans NVRAM

## 5. Commandes Supplémentaires (Bonus)

### Table ARP
📌 Récupération de la table ARP
Commande: show arp

## Show ARP (extrait)

```
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  10.10.20.148            -   0050.56bf.30eb  ARPA   GigabitEthernet1
Internet  10.10.20.254            2   0050.56bf.85d9  ARPA   GigabitEthernet1
```


### Voisins CDP
📌 Récupération des voisins CDP
Commande: show cdp neighbors

## Show CDP Neighbors

```
% CDP is not enabled
```


### Horloge système
📌 Récupération de l'heure système
Commande: show clock
**Heure système**: *13:40:47.750 UTC Fri Jan 30 2026

## 📋 Rapport de Synthèse

### Résumé des informations collectées

### 📊 SYNTHÈSE DU DEVICE

**Identifiant**: Cat8kv_AO_Sandbox
**Modèle**: X86_64_LINUX_IOSD-UNIVERSALK9-M, Version 17.15.4c, RELEASE SOFTWARE
**Uptime**: Uptime for this control processor is 4 minutes System returned to ROM by reload

### 🔌 INTERFACES
- **Total**: 3
- **UP/UP**: 1
- **DOWN**: 2

### 🗺️ ROUTAGE
- **Routes totales**: 7

### 💾 CONFIGURATION
- **Running config**: Récupérée (6617 caractères)
- **Startup config**: Récupérée

### 📈 STATISTIQUES
- **Mémoire**: Analysée
- **CPU**: Analysé
- **ARP Table**: Récupérée
- **Voisins CDP**: Récupérés


============================================================
✅ PROJET TERMINÉ AVEC SUCCÈS ! 🎉
============================================================

🔒 Connexion fermée proprement

---

## 📈 Résumé de l'exécution
- **Début**: 15:42:15
- **Fin**: 15:43:00
- **Durée totale**: 45.65 secondes
- **Messages enregistrés**: 74

> Rapport généré automatiquement par le projet DevNet
