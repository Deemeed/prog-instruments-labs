import logging
import os
from datetime import datetime


def setup_logging():
    if not os.path.exists('logs'):
        os.makedirs('logs')

    log_filename = f"logs/student_system_{datetime.now().strftime('%Y-%m-%d')}.log"

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_filename, encoding='utf-8'),
            logging.StreamHandler()
        ]
    )

    logger = logging.getLogger('StudentSystem')
    logger.info("=" * 50)
    logger.info("System started")
    logger.info("=" * 50)

    return logger