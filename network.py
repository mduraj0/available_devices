import socket


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

