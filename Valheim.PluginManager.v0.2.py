# Import modules
import re
import os
import winreg
import platform
clear = lambda: os.system('cls')

# -------------------------------------------------------------
#Check Valheim folder
def ValheimLocation():
    Valheim_dirs=[]
    location = winreg.HKEY_LOCAL_MACHINE
    if (platform.architecture()[0] == "64bit"):
        soft = winreg.OpenKeyEx(location,r"SOFTWARE\\Wow6432Node\\Valve\\Steam")
    else:
        soft = winreg.OpenKeyEx(location,r"SOFTWARE\\Valve\\Steam")
    installpath = winreg.QueryValueEx(soft,"InstallPath")
    if soft:
        winreg.CloseKey(soft)
    Steamvdf=(installpath[0]+"\steamapps\libraryfolders.vdf")
    with open(Steamvdf, 'r') as fp:
        lines = fp.readlines()
        for line in lines:
            if line.find("path") != -1:
                Valheim_dirs.append(re.findall('"([^"]*)"', line))
    for dir in Valheim_dirs:
            Valheim_check=os.path.exists(dir[1]+"\steamapps\common\Valheim")
            if Valheim_check == True:
                Valheim_dir=(dir[1]+"\steamapps\common\Valheim")
                break
    Valheim_plugins_dir=(Valheim_dir+"\BepInEx\plugins")
    BepinEx_check=os.path.exists(Valheim_plugins_dir)
    if BepinEx_check == True:
        print (" ")
        print ("Valheim plugins folder location:", Valheim_plugins_dir)
        print ("------------------------")
        return(Valheim_plugins_dir)
    else:
        print (" ")
        print ("! ERROR ! Valheim plugins folder not found")
        print ("------------------------")
        return False

# -------------------------------------------------------------
# List enabled plugins
def listenable(Valheim_plugins_dir):
    modson_list = []
    for root, dirs, files in os.walk(Valheim_plugins_dir):
        for file in files:
            if (file.endswith('.dll')):
                modson_list.append(os.path.join(root,file))
            elif (file.endswith('.disable')):
                pass
    modson_list.sort()
    print("Numer of enabled plugins:",len(modson_list))
    print("------------------------")
    if len(modson_list)>0:
        for i in range(len(modson_list)):
            nr=i+1
            print("[",nr,end=" ] ")
            print(modson_list[i])
            #print("\n".join(modson_list))
        print(" ")
    else:
        pass
    return(modson_list)

# -------------------------------------------------------------
# List disabled plugins
def listdisable(Valheim_plugins_dir):
    modsoff_list = []
    for root, dirs, files in os.walk(Valheim_plugins_dir):
        for file in files:
            if (file.endswith('.disable')):
                modsoff_list.append(os.path.join(root,file))
            elif (file.endswith('.dll')):
                pass
    modsoff_list.sort()
    print("Numer of disabled plugins:",len(modsoff_list))
    print("------------------------")
    if len(modsoff_list)>0:
        for i in range(len(modsoff_list)):
            nr=i+1
            print("[",nr,end=" ] ")
            print(modsoff_list[i])
            #print("\n".join(modson_list))
        print(" ")
    else:
        pass
    return(modsoff_list)

# -------------------------------------------------------------
# Enable plugin
def enableplugin():
    modsoff_list=listdisable(Valheim_plugins_dir)
    if len(modsoff_list)==0:
            clear()
            print (" ")
            print("No plugins to enable\n")
            input("Press Enter to continue...")
            clear()
    else:
        pluginID = input('Enter your choice: ').split(",")
        if ''.join(pluginID) == "all":
            clear()
            print (" ")
            for offID in range (len(modsoff_list)):
                mod = modsoff_list[offID-1]
                base = os.path.splitext(mod)[0]
                os.rename(mod, base + '.dll')
                print(modsoff_list[offID-1], "- Plugin enabled")
            print(" ")
            input("Press Enter to continue...")
            clear()
            return()
        else:            
            try:
                intpluginID = [int(pluginID) for pluginID in pluginID]
                if ((max(intpluginID)) > len(modsoff_list)):
                    clear()
                    print (" ")
                    print('Wrong input. Please enter "all" to enable all plugins, or a comma-separated numbers from 1 to',(len(modsoff_list)),"\n")
                    input("Press Enter to continue...")
                    clear()
                    return()
                elif((min(intpluginID)) == 0):
                    clear()
                    print (" ")
                    print('Wrong input. Please enter "all" to enable all plugins, or a comma-separated numbers from 1 to',(len(modsoff_list)),"\n")
                    input("Press Enter to continue...")
                    clear()
                    return()
                else:
                    clear()
                    for ID in intpluginID:
                        mod = modsoff_list[ID-1]
                        base = os.path.splitext(mod)[0]
                        os.rename(mod, base + '.dll')
                        print(modsoff_list[ID-1], "- Plugin enabled")
                    print(" ")
                    input("Press Enter to continue...")
                    clear()
                    return()
            except:
                clear()
                print (" ")
                print('Wrong input. Please enter a comma-separated numbers or "all"!\n')
                input("Press Enter to continue...")
                clear()
                return()

# -------------------------------------------------------------
# Disable plugin
def disableplugin():
    modson_list=listenable(Valheim_plugins_dir)
    if len(modson_list)==0:
            clear()
            print (" ")
            print("No plugins to disable\n")
            input("Press Enter to continue...")
            clear()
    else:
        pluginID = input('Enter your choice: ').split(",")
        if ''.join(pluginID) == "all":
            clear()
            print (" ")
            for offID in range (len(modson_list)):
                mod = modson_list[offID-1]
                base = os.path.splitext(mod)[0]
                os.rename(mod, base + '.disable')
                print(modson_list[offID-1], "- Plugin disabled")
            print(" ")
            input("Press Enter to continue...")
            clear()
            return()
        else:            
            try:
                intpluginID = [int(pluginID) for pluginID in pluginID]
                if ((max(intpluginID)) > len(modson_list)):
                    clear()
                    print (" ")
                    print('Wrong input. Please enter "all" to enable all plugins, or a comma-separated numbers from 1 to',(len(modson_list)),"\n")
                    input("Press Enter to continue...")
                    clear()
                    return()
                elif((min(intpluginID)) == 0):
                    clear()
                    print (" ")
                    print('Wrong input. Please enter "all" to enable all plugins, or a comma-separated numbers from 1 to',(len(modson_list)),"\n")
                    input("Press Enter to continue...")
                    clear()
                    return()
                else:
                    clear()
                    for ID in intpluginID:
                        mod = modson_list[ID-1]
                        base = os.path.splitext(mod)[0]
                        os.rename(mod, base + '.disable')
                        print(modson_list[ID-1], "- Plugin disabled")
                    print(" ")
                    input("Press Enter to continue...")
                    clear()
                    return()
            except:
                clear()
                print (" ")
                print('Wrong input. Please enter a comma-separated numbers or "all"!\n')
                input("Press Enter to continue...")
                clear()
                return()

# -------------------------------------------------------------
# Menu
menu_options = {
    1: 'List plugins',
    2: 'Enable plugins',
    3: 'Disable plugins',
    4: 'Exit',
}

def print_menu():
    clear()
    print (" ")
    print ("Valheim plugins folder location:", Valheim_plugins_dir)
    print(" ")
    for key in menu_options.keys():
        print (key,'--', menu_options[key] )

def option1():
    clear()
    if ValheimLocation() == False:
        pass
    else:
        clear()
        print (" ")
        print ("Valheim plugins folder location:", Valheim_plugins_dir)
        print(" ")
        listenable(Valheim_plugins_dir)
        print(" ")
        listdisable(Valheim_plugins_dir)
        print(" ")
        input("Press Enter to continue...")
        clear()

def option2():
    clear()
    if ValheimLocation() == False:
        pass
    else:
        clear()
        print (" ")
        print ("Valheim plugins folder location:", Valheim_plugins_dir)
        print("")
        enableplugin()

def option3():
    clear()
    if ValheimLocation() == False:
        pass
    else:
        clear()
        print (" ")
        print ("Valheim plugins folder location:", Valheim_plugins_dir)
        print("")
        disableplugin()

Valheim_plugins_dir = ValheimLocation()
if __name__=='__main__':
    while(True):
        print("")
        print_menu()
        print("")
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        if option == 1:
           option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            clear()
            print('Thanks!')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')
block = input()
