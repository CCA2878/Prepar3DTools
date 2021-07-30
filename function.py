# -*- coding: utf-8 -*-

import configparser
from winreg import OpenKey, HKEY_CURRENT_USER, QueryValueEx
from chardet.universaldetector import UniversalDetector


class P3dInfoSrc():

    def __init__(self, version = 'v5') -> None:
        self.version = version

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

    def getInstPath(self):  # 成功则返回路径，失败返回None
        try:
            __key = OpenKey(HKEY_CURRENT_USER,r'Software\Lockheed Martin\Prepar3D ' + f'{self.version}')
        except:
            return None
        else:
            try:
                __value = QueryValueEx(__key, 'AppPath')[0]
            except:
                __key.Close()
                return None
            else:
                return __value



class P3dCfgOpr(configparser.ConfigParser):# Judge cfg file encoding and read it.|判断文件编码方式并读取。

    def __init__(self, cfgPath='E:/scenery.cfg') -> None:
        super().__init__()
        self.cfgPath = cfgPath
        self.__getCfgEncoding()
        self.read(self.cfgPath, self.__cfgEncoding)

    def __getCfgEncoding(self) -> None:
        __cfgFileDetector = UniversalDetector()
        __cfgFile = open(self.cfgPath, 'rb')

        for _line in __cfgFile:
            __cfgFileDetector.feed(_line)
            if __cfgFileDetector.done:
                break

        __cfgFile.close()
        __cfgFileDetector.close()
        self.__cfgEncoding = __cfgFileDetector.result['encoding']
        __cfgFileDetector.reset()


class GUIOpr():

    def __init__(self) -> None:
        self.infoSrc = P3dInfoSrc()
        self.CfgOpr = P3dCfgOpr()


                #sceneryCfg1 = P3dCfgOpr()
                #sceneryCfg2 = P3dCfgOpr('E:/scenery2.cfg')
                #print(sceneryCfg1.sections(), sceneryCfg2.sections())
                # print(sceneryCfg1.sections())
