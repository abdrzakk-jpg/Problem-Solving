from loguru import logger

logger.add("logs/debug.log", rotation="500 KB", backtrace=True, diagnose=True)

def divide(x, y):
    return x / y

@logger.catch
def main():
    logger.info("بدينا الخدمة 💪")
    result = divide(10, 0)
    logger.success(f"النتيجة: {result}")

main()