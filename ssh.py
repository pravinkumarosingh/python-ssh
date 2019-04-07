      
      
print("                              _____                      ");
print("      \          /  |     |  |          |                ");
print("       \        / . |  ___|  |          |____   __    _  ");
print("        \  /\  /  | | |   |  |     \  / |    | |__| |/   ");
print("         \/  \/   | | |___|  |_____ \/  |____| |__  |    ");
print("                                    /                    ");
print("                                   /                     ");

import subprocess

ip=input("ip address>")
username=input("username>")


subprocess.call("ssh " +username+"@"+ip,shell=True)
