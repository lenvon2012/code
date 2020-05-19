#!/usr/bin/env python
# coding: utf-8
"""
Created on 2020-5-15

@author: Lenvon
"""
import configparser
import logging
import os
import shutil
import sys
import time


def copytree(src, dst, symlinks=False, ignore=None):
    # for item in os.listdir(src):
    #     s = os.path.join(src, item)
    #     d = os.path.join(dst, item)
    #     logging.info("move %s to %s", s, d)
    #     shutil.move(s, d)

    for files in os.listdir(src):
        s = os.path.join(src, files)
        d = os.path.join(dst, files)
        logging.info("move %s to %s", s, d)
        if os.path.isfile(s):
            shutil.copy2(s, d)
            os.remove(s)
        else:
            if not os.path.isdir(d):
                os.makedirs(d)
            copytree(s, d)
            os.rmdir(s)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        filename='log.log',
                        filemode='a')

    config = configparser.ConfigParser()
    config['default'] = {'source': '', 'target': ''}
    configFile = 'config.ini'
    if not os.path.exists(configFile):
        with open(configFile, 'w') as configfile:
            config.write(configfile)
    config.read(configFile)

    source = config['default']['source']
    target = config['default']['target']
    if not source or not target:
        logging.info('both source and target can not be empty')
        logging.info('\n')
        sys.exit(0)

    target_dir = os.path.join(target, time.strftime('%m%d'))

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    copytree(source, target_dir)
    logging.info("move %s to %s", source, target_dir)
    logging.info('\n')
