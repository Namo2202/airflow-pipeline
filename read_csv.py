import pandas as pd
import os
import shutil
from datetime import datetime

to_process_dir = '/mnt/d/Booster Data IA/toProcess'
processed_dir = '/mnt/d/Booster Data IA/already_processed'
result_dir = '/mnt/d/Booster Data IA/result'


os.makedirs(to_process_dir, exist_ok=True)
os.makedirs(processed_dir, exist_ok=True)
os.makedirs(result_dir, exist_ok=True)

for filename in os.listdir(to_process_dir):
    if filename.endswith('.csv'):
        file_path = os.path.join(to_process_dir, filename)
  
        df = pd.read_csv(file_path)
        
        avg_price = df['price'].mean()
        
        result_filename = f'result_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
        result_path = os.path.join(result_dir, result_filename)
        df_result = pd.DataFrame({'avg_price': [avg_price]})
        df_result.to_csv(result_path, index=False)
   
        shutil.move(file_path, os.path.join(processed_dir, filename))
