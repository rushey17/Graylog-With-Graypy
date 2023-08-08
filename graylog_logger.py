import logging
import graypy

def setup_logger():
    # Create a GraylogHandler instance
    graylog_handler = graypy.GELFUDPHandler(host='graylog_server_ip', port=12201)
    
    # Create and configure the logger
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.DEBUG)
    
    # Create a formatter and add it to the handler
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    graylog_handler.setFormatter(formatter)
    
    # Add the GraylogHandler to the logger
    logger.addHandler(graylog_handler)
    
    return logger
