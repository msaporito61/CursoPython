#!/usr/bin/env python3
import logging

logger = logging.getLogger('Demostracion')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('errores.log')
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)
formato = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formato)
ch.setFormatter(formato)
logger.addHandler(fh)
logger.addHandler(ch)

logger.debug('mensaje debug')
logger.info('mensaje info')
logger.warning('mensaje de alerta')
logger.error('mensaje de error')
logger.critical('mensaje critico')


'''
INFO WARNING sys.stdout
ERROR CRITICAL sys.stderr
DEBUG a definir
'''