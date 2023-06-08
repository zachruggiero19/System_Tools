import sys
import process_watchClass
import network_Checker

class main:
    def option_Check():
        while True:
            print("Welcome to the process monitor")
            print("Please select an option")
            print("1. Monitor new processes")
            print("2. Monitor closing processes")
            print("3. Monitor ip addresses")
            print("4. Monitor mac addresses")
            print("5. Exit")
            option = input("Please enter your option: ")
            if option == "1":
                process_watchClass.ProcessMonitor.new_process()
                input("Press enter to continue")
                return
            elif option == "2":
                process_watchClass.ProcessMonitor.closing_process()
                return
            elif option == "3":
                network_Checker.NetworkMonitor.ip_checker()
                return
            elif option == "4":
                network_Checker.NetworkMonitor.mac_checker()
                input("Press enter to continue")
                return
            elif option == "5": 
                sys.exit()
            else:
                print("Invalid option, please try again")
                return

    option_Check()
input("Please enter yes or no if you'd like to continue")
if "yes", "y"
    main()
if "no", "n"
    exit
else
    print("Please  enter a proper response")
    
    
        
