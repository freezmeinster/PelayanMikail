import Pyro.core

class Sysinfo(Pyro.core.ObjBase):
    def __init__(self):
        Pyro.core.ObjBase.__init__(self)
    def info(self, name):
        return "Haloo nama saya "+name+""

def main():
    Pyro.core.initServer()
    daemon=Pyro.core.Daemon()
    uri=daemon.connect(Sysinfo(),"host_os")

    print "The daemon runs on port:",daemon.port
    print "The object's uri is:",uri

    daemon.requestLoop()
    
if __name__=="__main__":
    main()
