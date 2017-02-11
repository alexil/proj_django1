# log_with_config.py
import logging
import logging.config
import otherMod2
# module_logger = logging.getLogger("exampleApp.otherMod2")

#----------------------------------------------------------------------
def main():
    """
    Based on http://docs.python.org/howto/logging.html#configuring-logging
    """
    dictLogConfig = {
        "version":1,
        "handlers":{

            "fileHandler":{
                "class":"logging.FileHandler",
                "formatter":"myFormatter",
                "filename":"config2.log"
                },

            "default_1": {
                'level': 'DEBUG',
                # "class": "logging.FileHandler",
                'class': 'logging.handlers.RotatingFileHandler',
                'maxBytes': 1024*1024*5, # 5 MB
                'backupCount': 5,
                'formatter':'standard',
                # "formatter": "myFormatter",
                "filename": "default_2.log"
                },
            "default": {
                'level': 'DEBUG',
                # "class": "logging.FileHandler",
                'class': 'logging.handlers.RotatingFileHandler',
                'maxBytes': 1024 * 1024 * 5,  # 5 MB
                'backupCount': 5,
                'formatter': 'standard',
                # "formatter": "myFormatter",
                "filename": "default_2.log"
            },

        },

        "loggers":{
            "exampleApp":{
                "handlers":["fileHandler"],
                "level":"INFO",
                },
            'root123': {
                'handlers': ['default_1'],
                'level': 'WARN'
            },
            '': {
                'handlers': ['default'],
                'level': 'DEBUG'
            },
            "l2": {
                "handlers": ["fileHandler"],
                "level": "DEBUG",
            }

        },

        "formatters":{
            # format = % (asctime)
            # s - % (name)
            # s - % (levelname)
            # s - % (module)
            # s: % (lineno)
            # d - % (message)
            # s
            "myFormatter":{
                "format":"%(asctime)s - %(levelname)s - %(name)s, %(lineno)s:%(module)s - %(message)s"
                },
            'standard': {
                'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
            },
        },

    }
            
    logging.config.dictConfig(dictLogConfig)

    # logger = logging.getLogger("exampleApp")
    logger = logging.getLogger(__name__)
    print logger.handlers
    logger.info("Program started")
    result = otherMod2.add(7, 8)
    logger.warn("======Done!")


    # logger = logging.getLogger('L2')

    logger.debug(" = = = = =Program started")
    result = otherMod2.add(7, 8)
    logger.debug(" = = = = Done!")

if __name__ == "__main__":
    main()