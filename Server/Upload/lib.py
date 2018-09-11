def unique(fileName):  # fileName: 传入的文件名
    return fileName  # return 绝对唯一的文件名


def fileName2key(fileName):  # fileName: 绝对唯一的文件名
    key = fileName
    return key  # 8位密钥，前四位为日期，后四位随机
