# Projet Airflow pour le Traitement des Fichiers CSV

Ce projet utilise Apache Airflow pour automatiser le traitement des fichiers CSV contenant des données immobilières. Le processus calcule la moyenne des prix des biens et déplace les fichiers traités vers un dossier spécifique.

## Structure du Projet

- `airflow_job.py`: Script Airflow définissant le DAG pour le traitement des fichiers CSV.
- `read_csv.py`: Script Python pour le traitement des fichiers CSV.
- `toProcess/`: Dossier contenant les fichiers CSV à traiter.
- `already_processed/`: Dossier où les fichiers CSV traités sont déplacés.
- `result/`: Dossier où les résultats du traitement sont stockés sous forme de fichiers CSV.

## Prérequis

- Python 3.x
- Apache Airflow
- Pandas
- Virtualenv (recommandé)

## Installation

1. **Cloner le dépôt:**

   ```sh
   git clone https://github.com/votre_utilisateur/votre_projet.git
   cd votre_projet
   ```

2. **Créer et activer un environnement virtuel:**

   ```sh
   python -m venv airflow-env
   source airflow-env/bin/activate
   ```

3. **Installer les dépendances:**

   ```sh
   pip install apache-airflow pandas
   ```

## Configuration d'Airflow

1. **Initialiser Airflow:**

   ```sh
   airflow db init
   ```

2. **Démarrer Airflow:**

   ```sh
   airflow standalone
   ```

3. **Copier le fichier `airflow_job.py` dans le dossier `dags` d'Airflow:**

   ```sh
   cp /path/to/your/project/airflow_job.py ~/airflow/dags/
   ```

## Utilisation

1. **Ajouter les fichiers CSV à traiter dans le dossier `toProcess`:**

   Placez vos fichiers CSV dans le dossier `toProcess`.

2. **Exécuter le DAG Airflow:**

   - Accédez à l'interface web d'Airflow (par défaut à `http://localhost:8080`).
   - Activez le DAG nommé `process_csv`.
   - Lancez le DAG manuellement ou attendez qu'il soit exécuté automatiquement selon la planification.

3. **Vérifier les résultats:**

   - Les fichiers CSV traités seront déplacés vers le dossier `already_processed`.
   - Les résultats seront sauvegardés dans le dossier `result` sous forme de fichiers CSV contenant la moyenne des prix.

     ![Alt text](<Capture d’écran 1.png>)
     ![Alt text](<Capture d’écran 2.png>)
