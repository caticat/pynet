# -*- coding: utf-8 -*-

"const define"

# 长度
MSG_PROTOCOL_LEN = 32 # 协议号长度
MSG_MAX_LEN = 65535 # 协议最大长度

# 起始位置
MSG_PROTOCOL_POS = 0
MSG_DATA_POS = MSG_PROTOCOL_LEN

# PTL SIGNAL
PTL_EXIT = -1 # 退出信号

# 杂项
PORT_NO_DEFAULT = 10000 # 初始默认端口号
PORT_NO_MAX = 65535 # 最大可用端口号
