import pandas as pd
import numpy as np
import os
import time

output_dir = "/usr/src/app/shared_data"
os.makedirs(output_dir, exist_ok=True)

while True:

    data = {
        'id': np.arange(1, 101),
        'valor': np.random.rand(100) * 100,
        'categoria': np.random.choice(['A', 'B', 'C', 'D'], 100)
    }
    
    df = pd.DataFrame(data)
    
    
    timestamp = int(time.time())
    csv_path = f"{output_dir}/dados_aleatorios_{timestamp}.csv"
    df.to_csv(csv_path, index=False)
    
    print(f"Arquivo gerado: {csv_path}")
    time.sleep(30)  