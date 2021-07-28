# -*- coding: utf-8 -*-

import configparser
from winreg import OpenKey, HKEY_CURRENT_USER, QueryValueEx
from chardet.universaldetector import UniversalDetector

# Judge cfg file encoding and read it.|判断文件编码方式并读取。


class P3dCfgOpr(configparser.ConfigParser):

    def __init__(self, cfgAddr='E:/scenery.cfg') -> None:
        super().__init__()
        self.cfgAddr = cfgAddr
        self.__getCfgEncoding()
        self.read(self.cfgAddr, self.__cfgEncoding)

    def __getCfgEncoding(self) -> None:
        __cfgFileDetector = UniversalDetector()
        __cfgFile = open(self.cfgAddr, 'rb')

        for _line in __cfgFile:
            __cfgFileDetector.feed(_line)
            if __cfgFileDetector.done:
                break

        __cfgFile.close()
        __cfgFileDetector.close()
        self.__cfgEncoding = __cfgFileDetector.result['encoding']
        __cfgFileDetector.reset()


class P3dInfoSrc():

    def __init__(self, version='v5') -> None:
        self.version = version
        pass

    @staticmethod
    def getInstedVerList():
        try:
            __key = OpenKey(HKEY_CURRENT_USER, r'Software\Lockheed Martin')
        except:
            return []
        else:
            __key.Close()

        __allVerList = ['v2', 'v3', 'v4', 'v5']
        __instedVerList = []

        for k in __allVerList:
            try:
                __key = OpenKey(HKEY_CURRENT_USER,
                                r'Software\Lockheed Martin\Prepar3D ' + f'{k}')
                if QueryValueEx(__key, 'Installed')[0] != 1:
                    raise Exception('Installed Value is Not 1!')
            except:
                continue
            else:
                __key.Close()
                __instedVerList.append(k)

        return __instedVerList

    def getInstAddr():
        pass


#sceneryCfg1 = P3dCfgOpr()
#sceneryCfg2 = P3dCfgOpr('E:/scenery2.cfg')
#print(sceneryCfg1.sections(), sceneryCfg2.sections())
# print(sceneryCfg1.sections())
