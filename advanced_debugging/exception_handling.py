# 异常处理调试示例
try:
    result = 10 / 0
except Exception as e:
    print(f'错误信息: {e}')