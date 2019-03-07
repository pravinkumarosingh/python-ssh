import subprocess

ip=input("ip address>")
username=input("username>")


subprocess.call("ssh " +username+"@"+ip,shell=True)
