"""
Shared logging configuration for the ML Scorer service.
"""
import logging


def setup_logging():
    """
    Configure logging with consistent format across the application.
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger(__name__)
