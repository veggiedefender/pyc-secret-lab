from cryptography.fernet import Fernet
from secrets import SECRET_KEY

encrypted_blob = (
    b'gAAAAABeuwxiJNGdLdoALoKWiiBNBZgqnI5vJbsN_hlT5O32pCHG4AF_nrYyjw40hIqJjc36m'
    b'M1WPy30VcvawBrXcV44iGjC-pSLhcLqSjMgr1GSoAZUKl8Tnm9wAr_a5dDarCE8LnafLLbQ43'
    b'pRQWQWAyXXVSdopPfpGv3abIXbLyYL_696VK0TcvbYZQmj62hVgLI-gZr_NWXZjWCANGefIbr'
    b'SmK-b5t7LnoHSliR0K6oouSdz1kfDhoKPd2XgwZocrzMiAgaMjj_mmX8tG--RLA_80mWIiA=='
)

f = Fernet(SECRET_KEY)
print(f.decrypt(encrypted_blob).decode("utf-8"))
