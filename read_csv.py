import pandas as pd
import os
import shutil
from datetime import datetime

# Définir les chemins
to_process_dir = '/mnt/d/Booster Data IA/toProcess'
processed_dir = '/mnt/d/Booster Data IA/already_processed'
result_dir = '/mnt/d/Booster Data IA/result'

# Créer les dossiers si nécessaire
os.makedirs(to_process_dir, exist_ok=True)
os.makedirs(processed_dir, exist_ok=True)
os.makedirs(result_dir, exist_ok=True)

# Traiter chaque fichier dans le dossier toProcess
for filename in os.listdir(to_process_dir):
    if filename.endswith('.csv'):
        file_path = os.path.join(to_process_dir, filename)
        
        # Lire le fichier CSV
        df = pd.read_csv(file_path)
        
        # Calculer la moyenne des prix
        avg_price = df['price'].mean()
        
        # Sauvegarder le résultat dans un nouveau fichier CSV
        result_filename = f'result_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
        result_path = os.path.join(result_dir, result_filename)
        df_result = pd.DataFrame({'avg_price': [avg_price]})
        df_result.to_csv(result_path, index=False)
        
        # Déplacer le fichier original vers le dossier already_processed
        shutil.move(file_path, os.path.join(processed_dir, filename))
