import hashlib


# MD5并不是太安全,改进准备采用SHA-256

def md5_encrypt(data):
    md5 = hashlib.md5()
    md5.update(data.encode('utf-8'))
    return md5.hexdigest()


if __name__ == '__main__':
    # 测试
    data = "Hello World"
    encrypt_data = md5_encrypt(data)
    print(f"encrypt_data:{encrypt_data}")
