import tensorflow as tf
import os
import argparse


class Chatbot:

    class TestMode:
        ALL='all'
        INTERACTIVE='interactive'
        DAEMON = 'daemon'

    def __init__(self):
        self.args = None
        self.textData = None
        self.model = None
        self.writer = None
        self.saver = None
        self.modelDir = ''
        self.globStep = 0
        self.sess = None

        self.MODEL_DIR_BASE = 'save' + os.sep + 'model'
        self.MODEL_NAME_BASE = 'name'
        self.MODEL_EXT = '.ckpt'
        self.CONFIG_FILENAME = 'params.ini'
        self.CONFIG_VERSION = 0.5
        self.TEST_IN_NAME = 'data' + os.sep + 'test' + os.sep + 'samples.txt'
        self.SENTENCES_PREFIX = ['Q: ', 'A: ']
    @staticmethod
    def parseArgs(args):
        parser=argparse.ArgumentParser()
        globalArgs=parser.add_argument_group('Global Options')
        globalArgs.add_argument('--test',
                                nargs='?',
                                choices=[])
