# Scrapy settings for zakupki project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "zakupki"

SPIDER_MODULES = ["zakupki.spiders"]
NEWSPIDER_MODULE = "zakupki.spiders"





# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 16

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 5
RANDOMIZE_DOWNLOAD_DELAY = True
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 1
#CONCURRENT_REQUESTS_PER_IP = 16



# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False





#A dict containing the downloader middlewares enabled by default in Scrapy. 
# Low orders are closer to the engine, high orders are closer to the downloader. 
# You should never modify this setting in your project, 
# modify DOWNLOADER_MIDDLEWARES instead
DOWNLOADER_MIDDLEWARES_BASE_to_see = {
    "scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware": 100,
    "scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware": 300,
    "scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware": 350,
    "scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware": 400,
    "scrapy.downloadermiddlewares.useragent.UserAgentMiddleware": 500,
    "scrapy.downloadermiddlewares.retry.RetryMiddleware": 550,
    "scrapy.downloadermiddlewares.ajaxcrawl.AjaxCrawlMiddleware": 560,
    "scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware": 580,
    "scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware": 590,
    "scrapy.downloadermiddlewares.redirect.RedirectMiddleware": 600,
    "scrapy.downloadermiddlewares.cookies.CookiesMiddleware": 700,
    "scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware": 750,
    "scrapy.downloadermiddlewares.stats.DownloaderStats": 850,
    "scrapy.downloadermiddlewares.httpcache.HttpCacheMiddleware": 900,
}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   "zakupki.middlewares.ZakupkiDownloaderMiddleware": 543,
}

"-----------------CookiesMiddleware------------------"
# scrapy.downloadermiddlewares.cookies.CookiesMiddleware
# Disable cookies (enabled by default)
# Default: True. 
COOKIES_ENABLED = True
# Default: False. log all cookies sent in requests (i.e. Cookie header) 
# and all cookies received in responses (i.e. Set-Cookie header).
COOKIES_DEBUG = True

"-----------------DefaultHeadersMiddleware------------"
# scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware
#default headers
# {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
# }
# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}

"-------------DownloadTimeoutMiddleware---------------"
# scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware
# Default: 180 
# The amount of time (in secs) that the downloader will wait before timing out.
DOWNLOAD_TIMEOUT = 180


"-------------HttpAuthMiddleware---------------------"
# scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False


"-----------------HttpCacheMiddleware----------------"
# scrapy.downloadermiddlewares.httpcache.HttpCacheMiddleware
# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# Default: False
HTTPCACHE_ENABLED = True
# Default: 0 Expiration time for cached requests, in seconds.
# Cached requests older than this time will be re-downloaded. 
# If zero, cached requests will never expire.
HTTPCACHE_EXPIRATION_SECS = 0
# Default: 'httpcache'
HTTPCACHE_DIR = "httpcache"
# Default: [] Don’t cache response with these HTTP codes.
HTTPCACHE_IGNORE_HTTP_CODES = []
# If enabled, requests not found in the cache will be ignored instead of downloaded.
# Default: False
HTTPCACHE_IGNORE_MISSING = False
# Don’t cache responses with these URI schemes. Default: ['file']
HTTPCACHE_IGNORE_SCHEMES = ['file']
# Default:
HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"
# Default. The database module to use in the DBM storage backend. 
# This setting is specific to the DBM backend.
HTTPCACHE_DBM_MODULE = 'dbm'
# The class which implements the cache policy. Default
HTTPCACHE_POLICY = 'scrapy.extensions.httpcache.DummyPolicy'
# If enabled, will compress all cached data with gzip. 
# This setting is specific to the Filesystem backend.
# Default: False
HTTPCACHE_GZIP  = False
# If enabled, will cache pages unconditionally. 
# Default: False
HTTPCACHE_ALWAYS_STORE = False
# List of Cache-Control directives in responses to be ignored.
# Default: []
HTTPCACHE_IGNORE_RESPONSE_CACHE_CONTROLS = []

"-----------------HttpCompressionMiddleware--------------"
# scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware
# Whether the Compression middleware will be enabled.
# This middleware allows compressed (gzip, deflate) traffic 
# to be sent/received from web sites.
# This middleware also supports decoding brotli-compressed 
# as well as zstd-compressed responses, provided that 
# brotli or zstandard is installed, respectively.
# Default: True
COMPRESSION_ENABLED = True

"-----------------HttpProxyMiddleware--------------"
# scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware
# Default: True
HTTPPROXY_ENABLED = True
# Default: "latin-1"
HTTPPROXY_AUTH_ENCODING = "latin-1"
# 

"-----------------RedirectMiddleware--------------"
# scrapy.downloadermiddlewares.redirect.RedirectMiddleware
# This middleware handles redirection of requests based on response status.
# Default: True
REDIRECT_ENABLED = True
# Default: 20
REDIRECT_MAX_TIMES = 20

"-----------------MetaRefreshMiddleware--------------"
# scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware
# This middleware handles redirection of requests based on meta-refresh html tag.
# Default: True
METAREFRESH_ENABLED = True
# Default: []
METAREFRESH_IGNORE_TAGS = []
# Default: 100
METAREFRESH_MAXDELAY = 100

"-----------------RetryMiddleware--------------"
# scrapy.downloadermiddlewares.retry.RetryMiddleware
# A middleware to retry failed requests that are potentially 
# caused by temporary problems such as a connection timeout 
# or HTTP 500 error.
# Default: True
RETRY_ENABLED = True
# Default: 2
RETRY_TIMES = 2
# Default: [500, 502, 503, 504, 522, 524, 408, 429]
RETRY_HTTP_CODES = [500, 502, 503, 504, 522, 524, 408, 429]
# Default: all
RETRY_EXCEPTIONS = [
    'twisted.internet.defer.TimeoutError',
    'twisted.internet.error.TimeoutError',
    'twisted.internet.error.DNSLookupError',
    'twisted.internet.error.ConnectionRefusedError',
    'twisted.internet.error.ConnectionDone',
    'twisted.internet.error.ConnectError',
    'twisted.internet.error.ConnectionLost',
    'twisted.internet.error.TCPTimedOutError',
    'twisted.web.client.ResponseFailed',
    IOError,
    'scrapy.core.downloader.handlers.http11.TunnelError',
]
# Adjust retry request priority relative to original request:
# a positive priority adjust means higher priority.
# a negative priority adjust (default) means lower priority.
# Default: -1
RETRY_PRIORITY_ADJUST = -1
# 

"-----------------RobotsTxtMiddleware--------------"
# scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware
# This middleware filters out requests forbidden by the robots.txt exclusion standard.
# Obey robots.txt rules
ROBOTSTXT_OBEY = True


"-----------------DownloaderStats--------------"
# scrapy.downloadermiddlewares.stats.DownloaderStats
# Middleware that stores stats of all requests, responses 
# and exceptions that pass through it.
# Default: True
DOWNLOADER_STATS = True

"-----------------UserAgentMiddleware--------------"
# scrapy.downloadermiddlewares.useragent.UserAgentMiddleware
# Middleware that allows spiders to override the default user agent.
# Default
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "zakupki (+http://www.yourdomain.com)"
USER_AGENT =    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",

USER_AGENTS_WIN = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
]
USER_AGENTS_LIN = [
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.2 Chrome/87.0.4280.141 Mobile Safari/537.36",
]
USER_AGENTS_MAC = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]

"-----------------AjaxCrawlMiddleware--------------"
# scrapy.downloadermiddlewares.ajaxcrawl.AjaxCrawlMiddleware
# Middleware that finds ‘AJAX crawlable’ page variants based on meta-fragment html tag.
# Default: False
AJAXCRAWL_ENABLED = False

"================ Spider Middleware ==================="
# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# Default: {}
SPIDER_MIDDLEWARES = {
   "zakupki.middlewares.ZakupkiSpiderMiddleware": 543,
}

SPIDER_MIDDLEWARES_BASE_for_see = {
    "scrapy.spidermiddlewares.httperror.HttpErrorMiddleware": 50,
    "scrapy.spidermiddlewares.offsite.OffsiteMiddleware": 500,
    "scrapy.spidermiddlewares.referer.RefererMiddleware": 700,
    "scrapy.spidermiddlewares.urllength.UrlLengthMiddleware": 800,
    "scrapy.spidermiddlewares.depth.DepthMiddleware": 900,
}

"-----------------DepthMiddleware--------------"
scrapy.spidermiddlewares.depth.DepthMiddlewar


# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "zakupki.pipelines.ZakupkiPipeline": 300,
#}

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
