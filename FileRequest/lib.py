import random
import string
import shutil
import os


def strRand():
    buf = string.ascii_letters + string.digits
    return ''.join(random.choice(buf) for _ in range(20))


def key2fileName(key):
    return key


def getFile(key):
    filename = key2fileName(key)
    sep = os.path.sep
    if not os.path.exists('usr%suploads%s%s' % (sep, sep, filename)):
        return -1
    dst = '%s.%s' % (strRand(), filename.split('.')[-1])
    shutil.copyfile('usr%suploads%s%s' % (sep, sep, filename), 'usr%sdownloads%s%s' % (sep, sep, dst))
    return dst