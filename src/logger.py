import logging
import os
from datetime import datetime

LOG_FILE=f"logs/log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
logs_path = os.path.dirname(LOG_FILE)
os.makedirs(logs_path, exist_ok=True)
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='[%(asctime)s] %(lineno)d %(name)s-%(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

