#OLD
from pwn import remote

with remote('localhost', 9841) as r:
    r.recvuntil(b' > ')
    r.sendline(b'sggsg')
    print(r.recvline().decode().strip())