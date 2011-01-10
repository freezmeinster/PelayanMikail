import Pyro.core
nguk = Pyro.core.getProxyForURI("PYROLOC://localhost:7766/host_os")
print nguk.info("Irmen")
