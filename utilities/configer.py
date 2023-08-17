from configparser import ConfigParser


class configread:
    def configreader(self,section, Key):
        config = ConfigParser()
        config.read("C:\\Users\\RUDTIWAR\\Desktop\\assigiment\\BDD_PYTHON\\utilities\\paths.ini")
        return config.get(section, Key)
