"""
Use this script to list process and service information
Require:
pip install wmi
"""


import wmi

conn = wmi.WMI()

print ("------------------ List WMI Classes: --------------------")
for class_name in conn.classes:
    if 'Process' in class_name:
        print(class_name)

# Even if you know the name of the WMI class, you will still require the exact name 
# of the property these classes offer and methods that can perform specific operations
# wmi.WMI().Win32_Process.methods.keys()

print ("------------------ Win32_Process Properties and Methods: --------------------")
properties = wmi.WMI().Win32_Process.methods.keys()
print(properties)


print ("------------------ Win32_Process Objects: --------------------")
for process in conn.Win32_Process():
     print("ID: {0}\nHandleCount: {1}\nProcessName: {2}\n".format(process.ProcessId, process.HandleCount, process.Name))


print ("------------------ Win32_Process running services:  --------------------")
for s in conn.Win32_Service(StartMode="Auto", State="Running"):
    print(s.State, s.StartMode, s.Name, s.DisplayName)

print ("------------------ Win32_Process Stopped services:  --------------------")
for s in conn.Win32_Service(StartMode="Auto", State="Stopped"):
    if 'Update' in s.Name:
        result = s.StartService()
        if result == 0:
            print("Successfully started service:", s.Name)



