import os
import tarfile
import pandas as pd
import kagglehub
import re
from loguru import logger

class DatasetLoader:
    def __init__(self, dataset_ref="breandan/french-reddit-discussion", download_dir="data"):
        self.dataset_ref = dataset_ref
        self.download_dir = download_dir
        if not os.path.exists(self.download_dir):
            os.makedirs(self.download_dir)

        self.csv_file_path = os.path.join(self.download_dir, "cleaned_data.csv")
        self.xml_file = None
        self.cleaned_xml_path = None

    def _download_and_extract(self):
        logger.debug("Downloading dataset...")
        download_path = kagglehub.dataset_download(self.dataset_ref)

        archive_path = os.path.join(download_path, "spf.tar.gz")

        with tarfile.open(archive_path, "r:gz") as tar:
            tar.extractall(path=download_path)

        for root, dirs, files in os.walk(download_path):
            for file in files:
                if file.endswith(".xml"):
                    self.xml_file = os.path.join(root, file)
                    break
            if self.xml_file:
                break

        if not self.xml_file:
            raise FileNotFoundError("No XML file found after extraction.")

        self.cleaned_xml_path = self.xml_file.replace(".xml", "_cleaned.xml")

    def _clean_xml(self):
        def clean_invalid_xml_chars(text):
            return re.sub(r"[^\x09\x0A\x0D\x20-\uD7FF\uE000-\uFFFD]", "", text)

        with open(self.xml_file, "r", encoding="utf-8", errors="ignore") as infile:
            raw_content = infile.read()

        cleaned_content = clean_invalid_xml_chars(raw_content)

        with open(self.cleaned_xml_path, "w", encoding="utf-8") as outfile:
            outfile.write(cleaned_content)

    def _load_csv(self):
        if os.path.exists(self.csv_file_path):
            logger.debug(f"Cleaned CSV file already exists at: {self.csv_file_path}")
            return pd.read_csv(self.csv_file_path)
        else:
            logger.debug(f"Cleaned CSV file does not exist at: {self.csv_file_path}")
            return None

    def load(self):
        df = self._load_csv()

        if df is not None:
            return df

        self._download_and_extract()
        self._clean_xml()

        df = pd.read_xml(self.cleaned_xml_path)

        df.to_csv(self.csv_file_path, index=False)
        logger.debug(f"\nCleaned data saved to {self.csv_file_path}")

        return df
