import os
import urllib.request as request
import zipfile
from src.TextSummarizer.logging import logger
from src.TextSummarizer.utils.common import get_size
from src.TextSummarizer.entity.__init__ import DataIngestionConfig
from pathlib import Path


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download with info : \n {headers}")
        else:
            logger.info(f"File already exists. {get_size(Path(self.config.local_data_fike))} Skipping download")
            
    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok = True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)