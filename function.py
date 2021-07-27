# -*- coding: utf-8 -*-

import configparser
from chardet.universaldetector import UniversalDetector

# Judge cfg file encoding and read it.|判断文件编码方式并读取。
class P3dCfgOpr(configparser.ConfigParser):

    def __init__(self, cfgAddr='E:/scenery.cfg') -> None:
        super().__init__()
        _cfgFileDetector = UniversalDetector()
        _cfgFile = open(cfgAddr, 'rb')

        for _line in _cfgFile:
            _cfgFileDetector.feed(_line)
            if _cfgFileDetector.done:
                _cfgFile.close()
                _cfgFileDetector.close()
                break

        self.read(cfgAddr, _cfgFileDetector.result['encoding'])
        _cfgFileDetector.reset()


sceneryCfg1 = P3dCfgOpr()
sceneryCfg2 = P3dCfgOpr('E:/scenery2.cfg')
print(sceneryCfg1.sections(), sceneryCfg2.sections())
print(sceneryCfg1.sections())
