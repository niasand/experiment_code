# coding=utf-8
import os
import logbook
from logbook import Logger, TimedRotatingFileHandler
from logbook.more import ColorizedStderrHandler
import datetime


def log_type(record, handler):
    log = "[{date}] [{level}] [{filename}] [{func_name}] [{lineno}] {msg}".format(
        date=datetime.datetime.now().strftime("%Y:%m:%d-%H:%M:%S"),
        level=record.level_name,
        filename=os.path.split(record.filename)[-1],
        func_name=record.func_name,
        lineno=record.lineno,
        msg=record.message
    )
    return log


# 日志存放路径
LOG_DIR = os.path.expanduser("~/")
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)
# 日志打印到屏幕
log_std = ColorizedStderrHandler(bubble=True)
log_std.formatter = log_type
# 日志打印到文件
log_file = TimedRotatingFileHandler(
    os.path.join(
        LOG_DIR,
        '%s.log' %
        'log'),
    date_format='%Y-%m-%d',
    bubble=True,
    encoding='utf-8')
log_file.formatter = log_type

# 脚本日志
log = Logger("script_log")


def init_logger():
    logbook.set_datetime_format("local")
    log.handlers = []
    log.handlers.append(log_file)
    log.handlers.append(log_std)


# 实例化，默认调用
logger = init_logger()
