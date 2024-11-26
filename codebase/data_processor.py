import pandas as pd
from config import *

class UFCDataProcessor:
    def __init__(self):
        self.fights_data = None
        self.rankings_data = None
    
    def load_data(self):
        """Load both UFC Master Dataset and rankings data"""
        self.fights_data = pd.read_csv(UFC_DATASET_PATH)
        self.rankings_data = pd.read_csv(RANKINGS_PATH)
        return self
    
    def clean_fights_data(self):
        """Basic cleaning of fights dataset"""
        # Remove rows with missing crucial information
        # Convert date columns
        # Handle weight classes
        pass
    
    def merge_rankings(self):
        """Merge rankings data with fights data"""
        pass
    
    def save_processed_data(self):
        """Save processed datasets"""
        pass
