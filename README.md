# Contrôle Caméra TP-Link C210

Cette application web permet de visualiser et de contrôler une caméra TP-Link Tapo C210 sur votre réseau local.

## Prérequis

- Python 3.7 ou supérieur
- Caméra TP-Link Tapo C210 connectée au réseau local
- Connexion RTSP activée sur la caméra
- Docker (optionnel, pour l'exécution en conteneur)

## Installation

1. Clonez ce dépôt ou téléchargez les fichiers
2. Installez les dépendances :
```bash
pip install -r requirements.txt
```

## Utilisation

### Méthode 1 : Exécution via Python

1. Assurez-vous que votre caméra est connectée au réseau et que l'URL RTSP est correcte dans le fichier `app.py`
2. Lancez l'application :
```bash
python app.py
```
3. Ouvrez votre navigateur et accédez à `http://localhost:5000`

### Méthode 2 : Exécution via Docker

1. Construisez l'image Docker :
```bash
docker build -t tapoview .
```

2. Lancez le conteneur :
```bash
docker run -p 5000:5000 tapoview
```

3. Ouvrez votre navigateur et accédez à `http://localhost:5000`

## Fonctionnalités

- Visualisation en direct du flux vidéo de la caméra
- Rotation de l'image à 0°, 90°, 180° et 270°
- Interface web simple et intuitive

## Sécurité

- L'application est configurée pour fonctionner uniquement sur votre réseau local
- Assurez-vous que votre caméra est correctement sécurisée avec un mot de passe fort 
