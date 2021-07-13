import datetime
import os

# 添加导包路径
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print('BASE_DIR项目的根目录的位置:',BASE_DIR)  # 项目的根目录的位置
print('sys.path是python的搜索模块的路径集，是一个list',sys.path)  # sys.path是python的搜索模块的路径集，是一个list
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
print('被插入后的目录',sys.path)  # 被插入的目录

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7s_d!+(4)&&_$3d3kg8f&k^68+2owee5+!_czx!-myzc1%39=u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    #"yxm.apps.users.apps.UsersConfig",
    'users.apps.UsersConfig', #用户模块
    'verifications.apps.VerificationsConfig',#验证模块
    'corsheaders',#CORS跨域白名单
    'xadmin',#xadminv
    'crispy_forms',#django-crispy-forms 是对django form在html页面呈现方式进行管理的一个第三方插件。
    'feedback.apps.FeedbackConfig',#用户反馈
    'oauth.apps.OauthConfig',  # 第三方登录
    'area.apps.AreaConfig',  # 省市区
    'goods.apps.GoodsConfig',  # 商品
    'qiniustorage', # 七牛云存储
    'ckeditor',  # 富文本编辑器
    'ckeditor_uploader',  # 富文本编辑器上传图片模块
    'contents.apps.ContentsConfig',  # 商品
    'django_crontab',  # 定时任务
    'haystack',#通过使用haystack来调用Elasticsearch搜索引擎
    'orders', #订单
    'payment', #支付



]



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'yxm.urls'
AUTH_USER_MODEL="users.User"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'yxm.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'yxm_db',
        "HOST": '127.0.0.1',
        "PORT": "3306",
        "USER": "yxm_db",
        "PASSWORD": "ZwTK7Kt6Tz5cF6k3"
    }
}
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/0",
        "OPTIONS": {"CLIENT_CLASS": "django_redis.client.DefaultClient", }},
    "session": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {"CLIENT_CLASS": "django_redis.client.DefaultClient", }
    },
    "verify_codes": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "cart": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/4",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
}


SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "session"

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

# STATIC_URL = '/static/'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,  # 是否禁用已经存在的日志器
    'formatters': {  # 日志信息显示的格式
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(lineno)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(module)s %(lineno)d %(message)s'
        },
    },
    'filters': {  # 对日志进行过滤
        'require_debug_true': {  # django在debug模式下才输出日志
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {  # 日志处理方法
        'console': {  # 向终端中输出日志
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {  # 向文件中输出日志
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(os.path.dirname(BASE_DIR), "logs/yxm.log"),  # 日志文件的位置
            'maxBytes': 300 * 1024 * 1024,  # kb*Kb=M，300M
            'backupCount': 10,  # 最多个300M文件
            'formatter': 'verbose'
        },
    },
    'loggers': {  # 日志器
        'django': {  # 定义了一个名为django的日志器
            'handlers': ['console', 'file'],  # 可以同时向终端与文件中输出日志
            'propagate': True,  # 是否继续传递日志信息
            'level': 'INFO',  # 日志器接收的最低日志级别
        },

    }
}

REST_FRAMEWORK = {
    # 异常处理
    'EXCEPTION_HANDLER': 'yxm.utils.exceptions.exception_handler',
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #     'rest_framework.authentication.SessionAuthentication',#session认证
    #     'rest_framework.authentication.BasicAuthentication',#基本认证
    # ),
    'DEFAULT_RENDERER_CLASSES': (  # 默认响应渲染类
        'rest_framework.renderers.JSONRenderer',  # json渲染器
        'rest_framework.renderers.BrowsableAPIRenderer',  # 浏览API渲染器
    ),
    #JWT以及认证
    'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
            'rest_framework.authentication.SessionAuthentication',
            'rest_framework.authentication.BasicAuthentication',
        ),
    #限流
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.ScopedRateThrottle',
    ),
    'DEFAULT_THROTTLE_RATES': {
        'contacts': '1000/day',
        'uploads': '20/day'
    },

    # 分页
    'DEFAULT_PAGINATION_CLASS':'yxm.utils.pages.MyGageSet'



}

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),
    'jwt_response_payload_handler':'user.utils.jwt_response_payload_handler'
}

# CORS  白名单
CORS_ORIGIN_WHITELIST = (
    'http://127.0.0.1',
    'http://localhost',
    'http://demo.myuxi.wang',
    'http://mm.yxmm.com',
    'http://api.myuxi.wang',



)
CORS_ALLOW_CREDENTIALS = True  # 允许携带cookie
#告知django使用我们自定义的后端
AUTHENTICATION_BACKENDS = [
    'users.utils.UsernameMobileAuthBackend',
]
#QQ登录
QQ_CLIENT_ID = '101792382' # 应用ID
QQ_REDIRECT_URI = 'http://demo.myuxi.wang/oauth_callback.html' # 回调网址
QQ_STATE = '/wap/member/member.html' # 会员中心 next
QQ_CLIENT_SECRET = '09a0d1903eb475f6c9e7181048a8e7b0' # 应用秘钥

# Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'hyzcreate@qq.com'
EMAIL_HOST_PASSWORD = 'qtdbtkjqhfmqdjjf'
EMAIL_FROM = '余惜网<hyzcreate@qq.com>'

# DRF扩展
REST_FRAMEWORK_EXTENSIONS = {
    # 缓存时间
    'DEFAULT_CACHE_RESPONSE_TIMEOUT': 60 * 60 *24,
    # 缓存存储
    'DEFAULT_USE_CACHE': 'default',
}

# 静态文件配置
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# 七牛存储
QINIU_ACCESS_KEY = 'y2xgNLjhOOa14IHXk28o8h_qENYxfXA1AaVNA3jD'
QINIU_SECRET_KEY = '_nx2oPnouefn-CfkuYIyFBdN7N2fgNgzetBWOphF'
QINIU_BUCKET_NAME = 'yxmall'
QINIU_BUCKET_DOMAIN = 's.myuxi.wang' #解析的域名
QINIU_SECURE_URL = False    #使用http


PREFIX_URL = 'http://'# 前缀协议是否用https

MEDIA_URL = PREFIX_URL + QINIU_BUCKET_DOMAIN + '/media/'

# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_ROOT = 'media'

STATIC_URL = QINIU_BUCKET_DOMAIN + '/static/' #改为起牛云访问
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = "static" # 静态文件收集

DEFAULT_FILE_STORAGE = 'qiniustorage.backends.QiniuMediaStorage'
STATICFILES_STORAGE = 'qiniustorage.backends.QiniuStaticStorage'



# 富文本编辑器ckeditor配置
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',  # 工具条功能
        'height': 300,  # 编辑器高度
        # 'width': 300,  # 编辑器宽
    },
}
CKEDITOR_UPLOAD_PATH = ''  # 上传图片保存路径，使用了七牛云，所以此处设为''

GENERATED_STATIC_HTML_FILES_DIR = os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), 'web')
print(os.path.dirname(BASE_DIR)) #该文件的文件目录
print(GENERATED_STATIC_HTML_FILES_DIR)

# 定时任务
CRONJOBS = [
    # 每5分钟执行一次生成主页静态文件
    ('*/5 * * * *', 'contents.crons.generate_static_index_html', '>> /home/sixstar/Desktop/yxm/yxm/logs/crontab.log')
]
#>:指向写入文件
#>>:追加

# 解决crontab中文问题
CRONTAB_COMMAND_PREFIX = 'LANG_ALL=zh_cn.UTF-8'

# Haystack
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://192.168.190.135:9200/',  # 此处为elasticsearch运行的服务器ip地址不是127那个，端口号固定为9200
        'INDEX_NAME': 'yxmall',  # 指定elasticsearch建立的索引库的名称
    },
}
# 当添加、修改、删除数据时，自动生成索引
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'


# 支付宝
ALIPAY_APPID = "2021000117666841"

ALIPAY_DEBUG = True

ALIPAY_URL = "https://openapi.alipaydev.com/gateway.do" # 沙箱模式的支付网关
# ALIPAY_URL = "https://openapi.alipay.com/gateway.do" # 线上模式的支付网关

ALIPAY_RETURN_URL = "http://127.0.0.1/pay_success.html" # 支付回调 支付成功后支付宝跳转到此页面



