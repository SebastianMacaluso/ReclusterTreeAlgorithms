import logging


def get_logger(name=__file__, level=logging.DEBUG):
    logger = logging.getLogger(name)

    if getattr(logger, "_init_done__", None):
        logger.setLevel(level)
        return logger

    logger._init_done__ = True
    logger.propagate = False
    logger.setLevel(level)

    formatter = logging.Formatter("%(asctime)s:%(levelname)s::%(message)s")
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    handler.setLevel(0)

    del logger.handlers[:]
    logger.addHandler(handler)

    return logger



# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)
# logging.debug("test")