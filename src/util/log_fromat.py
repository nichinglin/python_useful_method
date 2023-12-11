import logging

class LogFormat:
    def __init__(self, level="info"):
        if(level == "debug"):
            level = logging.DEBUG
        elif(level == "info"):
            level = logging.INFO
        elif(level == "warning"):
            level = logging.WARNING
        elif(level == "error"):
            level = logging.ERROR
        elif(level == "critical"):
            level = logging.CRITICAL
        else:
            level = logging.INFO

        logging.basicConfig(
            level=level, # DEBUG, INFO, WARNING, ERROR, CRITICAL
            format="%(asctime)s [%(levelname)s]: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        logging.info("Log format done!")

    def log_level_test(self):
        logging.debug("This is a debug message.")
        logging.info("This is a debug message.")
        logging.warning("This is a debug message.")
        logging.error("This is a debug message.")
        logging.critical("This is a debug message.")

    
if __name__ == "__main__":
    log_format = LogFormat()
    log_format.log_level_test()