import os
import sys
import logging
import pandas as pd

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import init_logger

class Dataset:
    """
    POIDataset class for loading and preprocessing POI data.
    """
    def __init__(self, args:dict):
        self.args = args

    @classmethod
    def load_data(cls, data_path:str, file_name:str, encoding:str="utf-8"):
        _, file_ext = os.path.splitext(os.path.join(data_path, file_name))
        
        if file_ext == ".csv":
            df = pd.read_csv(os.path.join(data_path, file_name), names=["MAC", "SRCMAC", "TIME", "RISS"], encoding=encoding)
        
        elif file_ext in [".xls", ".xlsx"]:
            df = pd.read_excel(os.path.join(data_path, file_name))
        
        else:
            raise ValueError(f"Unsupported file extension: {file_ext}")

        logging.info(f"Loaded {file_name} from {data_path}. {df.shape[0]} rows and {df.shape[1]} columns.")
        
        return df


if __name__ == "__main__":
    init_logger()
    
    df = Dataset.load_data(data_path="data/gyeongju", file_name="GY_raw_20240329_20240331.csv")
    print(df.head())