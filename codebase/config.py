# Project configuration values

from pathlib import Path

# Project directory paths
PROJECT_ROOT = Path(__file__).parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# Data file paths
UFC_DATASET = RAW_DATA_DIR / "ufc-master.csv"
RANKINGS_DATASET = RAW_DATA_DIR / "ufc-rankings.csv"

# Model parameters
RANDOM_STATE = 42
TEST_SIZE = 0.2
TARGET_VARIABLE = "winner"

# Feature engineering parameters
LOOKBACK_WINDOW = 3  # Number of previous fights to consider
RELEVANT_STATS = [
    "strikes_landed",
    "strikes_attempted",
    "takedowns_landed",
    "takedowns_attempted",
    "significant_strikes"
]
