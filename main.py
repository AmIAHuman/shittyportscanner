import socket
import _thread

def check(ip, p):
  print(p)
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  result = s.connect_ex((target, port))
  s.close()
  if(result == 0):
  	print("Port found at " + str(target) + ":" + str(port))
    

target = input("> ")

for port in range(1, 65536):
  _thread.start_new_thread(check, (target, port))
