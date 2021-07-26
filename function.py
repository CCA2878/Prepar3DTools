import configparser
from chardet.universaldetector import UniversalDetector

def readCfg(cfgAddr = 'E:/scenery.cfg'):
    _detector = UniversalDetector()
    _cfg = configparser.ConfigParser()
    _cfgFile = open(cfgAddr, 'rb')

    for line in _cfgFile:
        _detector.feed(line)
        if _detector.done:
            _cfgFile.close()
            _detector.close()
            break

    _cfg.read(cfgAddr, _detector.result['encoding'])
    _detector.reset()
    return _cfg

sceneryCfg1 = readCfg()
sceneryCfg2 = readCfg('E:/scenery2.cfg')
print(sceneryCfg1.sections(), sceneryCfg2.sections())