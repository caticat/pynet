# -*- coding: utf-8 -*-

"const define"

# 长度
MSG_DATA_LEN = 32 // 8 # 协议数据长度(协议号+数据)
MSG_PROTOCOL_LEN = 32 // 8 # 协议号长度
MSG_MAX_LEN = 65535 # 协议最大长度

# 起始位置
MSG_LEN_POS = 0
MSG_PROTOCOL_POS = MSG_LEN_POS + MSG_DATA_LEN
MSG_DATA_POS = MSG_PROTOCOL_POS + MSG_PROTOCOL_LEN

# PTL SIGNAL
PTL_EXIT = -1 # 退出信号

# 杂项
PORT_NO_DEFAULT = 10000 # 初始默认端口号
LISTEN_WAIT_NO_MAX = 5 # 最大等待连接数
