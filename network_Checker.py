import sys
import wmi


class NetworkMonitor:
    def ip_checker():
        c = wmi.WMI()
        
        network_log = open("network_log.txt", "w")
        for interface in c.Win32_NetworkAdapterConfiguration(IPEnabled=1):
            sys.stdout
            network_log.write("IP Address: %s\n" % interface.IPAddress[0])
            print(interface.Description, interface.IPAddress[0])

        network_log.close()
        print("Network log created")
        #sys.exit()
    def mac_checker():
        c = wmi.WMI()
        
        network_log = open("network_log.txt", "w")
        for interface in c.Win32_NetworkAdapterConfiguration(IPEnabled=1):
            sys.stdout
            network_log.write("MAC Address: %s\n" % interface.MACAddress)
            print(interface.Description, interface.MACAddress)

        network_log.close()
        print("Network log created")
        return
        #sys.exit()
        
          