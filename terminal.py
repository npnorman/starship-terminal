# This file is responsible for running the terminal to access the starship

import systems
import threading

sysloop = systems.SystemLoop()

def runTerminal():
    argv = []
    builtin = {
        #command : function
        "status" : lambda argc, argv : checkSystemStatus(argc, argv),
        "help" : lambda argc, argv: help(argc, argv),
        "diagram" : lambda argc, argv: diagram(argc, argv),
    }

    keepGoing = True
    while keepGoing:
        #get input
        user = input("Starship-System $")

        #lex into tokens
        argv = user.split(" ")
            #remove extra spaces
            #blank tokens disapear

        #parse syntax
        argc = len(argv)

        #variable expansion

        #end terminal
        if user == "quit":
            keepGoing = False
            argc = -1

        #builtin/alias or external
        if (argv[0] == "" or argc == -1):
            pass
        elif (argc > 0 and argv[0] in builtin):
            builtin[argv[0]](argc, argv)
        else:
            print(f"Command {argv[0]} unknown. Use 'quit' to quit and 'help' to learn more.")

#Builtins
def checkSystemStatus(argc, argv):
    power = sysloop.power
    distance = 226
    classLevel = 7
    
    print("System Status: Healthy")
    
    if (argc > 1):
        if ("-" in argv[1]):
            if ("p" in argv[1]):
                print(f"Power Level: {power}%")
            if ("d" in argv[1]):
                print(f"Distance from Earth HQ: {distance} AU")
            if ("c" in argv[1]):
                print(f"Class Level: {classLevel} \"Wanderer\" Starship")
    
    return 0

def help(argc, argv):
    
    helpDict = {
        "status" : "Check the status of the starship: status -[pdc]\n-p Power\n-d Distance\n-c Class Level"
    }
    
    print(f"STARSHIP SYSTEM MANUAL")
    
    if (argc == 1):
        print("Use 'help' <command> to learn more about each command.\nPossible commands:")
        for command in helpDict:
            print(command)
    elif (argc > 1 and argv[1] in helpDict):
        print(helpDict[argv[1]])
    
    return 0

def diagram(argc, argv):
    print("""   *   ** ╓──────────────────┐
 #      # ╣      Main        ├──────────────────────────────────┐           ______
          ╣     Engine       │	          Mess Hall             │          /Turret\\=====+
   #     *╣                  │	                                │         (\\      /)
  *   #   ╣                  ├─────┬─┬────────────────────────┬─┴─────────────────────────╮
*         ╙──────────┬───────┘     ┆ ┆   Barracks             ┆                            ╲
       ╓─────────────┴┐            ┆ ┆                        ┆   Cargo &                   ╲
     # ╣  Shield      │	Engineering┆ ├┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┤   Docking Station            ╲
 *     ╣  Engine      │            ┆ ┆     Rec Room           ┆                               ╲
  *  # ╣              ├┄┄┄┄┄┄┄┄┄┄┄┄┴┄┴┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┬┄┄┄┄┄┄┄┄┴┄┄┄┄┄┄┄┄┬┄┄┄┄┄┄┄┄┄┄┄┄┬┄┄┄┄┄┄┄┄┄┄╲            
       ╣              │	 Officer Quaters and Offices ┆    Medical &    ┆  Guest     ┆ Weapons   ╲
    #* ╙────────────┬─┘                              ┆    Labs         ┆  Quarters  ┆ Cargo      ╲
                    └───────────────┬────────────────┴──┬──────────────┴────────────┴────────────╯
                                    │                   │
                                    │      Cockpit      │
                                    │                   │
                                    └───────────────────┘""")
    
    return 0

if __name__ == "__main__":
    thread = threading.Thread(target=sysloop.systemLoop)
    thread.start()
    
    runTerminal()
    
    thread.join()