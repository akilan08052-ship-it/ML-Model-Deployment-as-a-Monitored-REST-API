import logging
from logging.handlers import RotatingFileHandler
import sys



def setup():
    LOG_FILE="app/logs/app.log"

    logging.basicConfig(
        level=logging.INFO,
        format=(
            "%(asctime)s |"
            "%(levelname)s | "
            "%(name)s | "
            "%(message)s"
            
        ),
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler(LOG_FILE)
        ]
    )
    file_handler = RotatingFileHandler( LOG_FILE, maxBytes=5 * 1024 * 1024,  backupCount=3, encoding="utf-8" )
    return logging.getLogger("app")
