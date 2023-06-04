import wmi
import sys


class ProcessMonitor:
    def new_process():
        c = wmi.WMI()
        process_watcher = c.Win32_Process.watch_for("creation")
        count = 0

        log_file = open("process_log.txt", "w")

        while True:
            while count < 5:
                new_process = process_watcher()
                sys.stdout 
                log_file.write("New process %s created, its PID is %s\n" % (new_process.Caption, new_process.ProcessId)) 
                print("New process %s created, its PID is %s\n" % (new_process.Caption, new_process.ProcessId))    
                count += 1  
         
            log_file.close()
            return

    def closing_process():
        c = wmi.WMI()
        process_watcher2 = c.Win32_Process.watch_for("deletion")
        count = 0

        closing_log = open("closing_log.txt", "w")

        while True:
            while count < 20:
                closing_process = process_watcher2()
                sys.stdout 
                closing_log.write("Process %s closed, its PID was %s\n" % (closing_process.Caption, closing_process.ProcessId)) 
                print("Process %s closed, its PID was %s\n" % (closing_process.Caption, closing_process.ProcessId))    
                count += 1  
         
            closing_log.close()
            return
    

