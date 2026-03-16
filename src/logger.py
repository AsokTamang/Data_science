import logging
import os
from pathlib import Path


dir=Path(__file__).parent  #current working dir
file_path = os.path.join(dir,"loggings.log")  #created the logfile
logging.basicConfig(level=logging.INFO,
                    format="{asctime} - {levelname} - {message}",datefmt = "%Y-%m-%d %H:%M",
                    filename= file_path,
                    style="{"
                    )
logger=logging.getLogger(__name__)