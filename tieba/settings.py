# -*- coding: utf-8 -*-

BOT_NAME = 'tieba'

SPIDER_MODULES = ['tieba.spiders']
NEWSPIDER_MODULE = 'tieba.spiders'

DEPTH_PRIORITY = 1 #1表示广度优先 0表示深度优先

#使用先进先出FIFO（要在 Scrapy 中实现广度优先搜索（BFS），需要将调度器配置为使用先进先出（FIFO）队列。）
SCHEDULER = 'scrapy.core.scheduler.Scheduler'
SCHEDULER_DISK_QUEUE = 'scrapy.squeues.PickleFifoDiskQueue'
SCHEDULER_MEMORY_QUEUE = 'scrapy.squeues.FifoMemoryQueue'


#AUTO_THROTTLE_ENABLED = True #根据目标网站的负载动态调整爬虫速度
DOWNLOAD_TIMEOUT = 5
RETRY_TIMES = 50
# Obey robots.txt rules
ROBOTSTXT_OBEY = False
#DOWNLOAD_DELAY = 1
#RANDOMIZE_DOWNLOAD_DELAY = True
#CONCURRENT_REQUESTS_PER_IP = 5
#CONCURRENT_REQUESTS = 10  # 最大并发数
#CONCURRENT_REQUESTS_PER_DOMAIN=10
# Configure item pipelines

# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html

ITEM_PIPELINES = {
    'tieba.pipelines.TiebaPipeline': 500,
}

#LOG_LEVEL = 'ERROR'
LOG_LEVEL = 'WARNING'
#LOG_LEVEL = 'INFO'

COMMANDS_MODULE = 'tieba.commands'

COOKIES_ENABLED = False

DOWNLOADER_MIDDLEWARES = {
    'tieba.middlewares.ProxyMiddleware': 100,
    'tieba.middlewares.TiebaSpiderMiddleware': 543,
}
