var1="""SET progman TO $'''c:\\windows\\system32\\$notepad.exe'''
System.RunApplication.RunApplication ApplicationPath: progman WindowStyle: System.ProcessWindowStyle.Maximized ProcessId=> AppProcessId
WAIT 5
"""
var2="MouseAndKeyboard.MoveMouse X: $0 Y: $1 RelativeTo: MouseAndKeyboard.PositionRelativeTo.ActiveWindow MovementStyle: MouseAndKeyboard.MovementStyle.Instant"
var4="WAIT 1"
xy=[]
print("\033c\033[40;37m\n give me windows program to run like 'paint' ? ")
a=input()
print("\033[40;37m\n give me x y vars separete by ','  enter to exit? ")

while 1:
    b=input().strip()
    if b=="":
        break
    else:
        xy=xy + [b]
var1=var1.replace("$notepad.exe",a)
print("\n"+"-"*80 +"\n")
print(var1)
for l in xy:
     d=l.split(",")
     x=d[0].strip()
     y=d[1].strip()
     var3=var2.replace("$0",x)
     var3=var3.replace("$1",y)
     print(var3)
     print(var4)