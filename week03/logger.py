import json
import logging
import logging.handlers
import os
import time


class Logger(object):
    def __init__(self, file_name):
        sl_formatter = logging.Formatter('%(asctime)s%(message)s')
        sl_handler = logging.StreamHandler()
        sl_handler.setFormatter(sl_formatter)

        sl_logger = logging.getLogger('stream_logger')
        sl_logger.setLevel(logging.INFO)
        sl_logger.addHandler(sl_handler)

        if file_name != " ":
            fl_formatter = logging.Formatter('%(message)s')
            if not os.path.isdir('./logs'):
                os.mkdir('./logs')
            fl_handler = logging.handlers.RotatingFileHandler(
                f'logs/{file_name}', maxBytes=20)
            fl_handler.setFormatter(fl_formatter)
            fl_logger = logging.getLogger('file_logger')
            fl_logger.setLevel(logging.INFO)
            fl_logger.addHandler(fl_handler)
            self.fl_logger = fl_logger
        else:
            self.fl_logger = None
        self.sl_logger = sl_logger

    def log(self, ip, port, result):
        msg = f'ip={ip}'
        if port != 0:
            msg = f' {msg} port={port}'
        msg = f' {msg} result={result}'
        self.sl_logger.info(msg)
        if self.fl_logger is not None:            
            if port != 0:
              d = {'ip': ip,'prot':port,"open":result}        
            else:
              d = {'ip': ip,"connected":result[0],'delay':result[1]}
            self.fl_logger.info(json.dumps(d))
