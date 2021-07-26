import configparser
from chardet.universaldetector import UniversalDetector


class readCfg(configparser.ConfigParser):

    def __init__(self, cfgAddr='E:/scenery.cfg') -> None:
        super().__init__()
        _detector = UniversalDetector()
        _cfgFile = open(cfgAddr, 'rb')

        for line in _cfgFile:
            _detector.feed(line)
            if _detector.done:
                _cfgFile.close()
                _detector.close()
                break

        self.read(cfgAddr, _detector.result['encoding'])
        _detector.reset()


sceneryCfg1 = readCfg()
sceneryCfg2 = readCfg('E:/scenery2.cfg')
print(sceneryCfg1.sections(), sceneryCfg2.sections())
print(sceneryCfg1.sections())
