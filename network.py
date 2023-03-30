import socket
import sys
import subprocess


def extract_ip_addr():
    st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        st.connect(('1.1.1.1', 1))
        local_ip, _ = st.getsockname()
    except Exception:
        local_ip = '127.0.0.1'
    finally:
        st.close()
    return local_ip


def convert_mask(mask):
    return sum(bin(int(octet)).count('1') for octet in mask.split('.'))


def is_reachable(ip_addr):
    arg = '-c'
    if sys.platform.startswith('win'):
        arg = '-n'

    output = subprocess.run(['ping', arg, '1', ip_addr], capture_output=True)
    return 'unreachable' not in str(output.stdout)


def is_reachable_with_ports(ip_addr):
    global answer
    for port in range(21, 9000):
        socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = socket_obj.connect_ex((ip_addr, port))
        if result == 0:
            answer = True
        else:
            answer = False
            socket_obj.close()

    return answer
