import os

ROOT_PATH = os.path.abspath(os.path.dirname(__file__))

#Directories
LAYOUT_DIR = os.path.join(ROOT_PATH, 'layout')
CONTENT_DIR = os.path.join(ROOT_PATH, 'content')
MEDIA_DIR = os.path.join(ROOT_PATH, 'media')
DEPLOY_DIR = os.path.join(ROOT_PATH, 'deploy')
TMP_DIR = os.path.join(ROOT_PATH, 'deploy_tmp')

BACKUPS_DIR = os.path.join(ROOT_PATH, 'backups')
BACKUP = False

SITE_ROOT = ""
SITE_WWW_URL = "http://cloudpanic.com"
SITE_NAME = "Cloudpanic : Technologies to master. Crap to ignore."
SITE_AUTHOR = "tipiirai (Tero Piirainen)"

#Url Configuration
GENERATE_ABSOLUTE_FS_URLS = False

# Clean urls causes Hyde to generate urls without extensions. Examples:
# http://example.com/section/page.html becomes
# http://example.com/section/page/, and the listing for that section becomes
# http://example.com/section/
# The built-in CherryPy webserver is capable of serving pages with clean urls
# without any additional configuration, but Apache will need to use Mod_Rewrite
# to map the clean urls to the actual html files.  The HtaccessGenerator site
# post processor is capable of automatically generating the necessary
# RewriteRules for use with Apache.
GENERATE_CLEAN_URLS = False

# A list of filenames (without extensions) that will be considered listing
# pages for their enclosing folders.
# LISTING_PAGE_NAMES = ['index']
LISTING_PAGE_NAMES = ['listing']

# Determines whether or not to append a trailing slash to generated urls when
# clean urls are enabled.
APPEND_SLASH = False
 	

CONTEXT = {
	'analytics'	: "UA-19863497-1", # Google Analytics id
	'keywords' 	: "IT trends, technology trends, computing trends, cloud trends, cloud technologies, sap sucks"
}


# {folder : extension : (processors)}
# The processors are run in the given order and are chained.
# Only a lone * is supported as an indicator for folders. Path 
# should be specified. No wildcard card support yet.
 
# Starting under the media folder. For example, if you have media/css under 
# your site root,you should specify just css. If you have media/css/ie you 
# should specify css/ie for the folder name. css/* is not supported (yet).

# Extensions do not support wildcards.
MEDIA_PROCESSORS = {
    '*':{
        '.css':('hydeengine.media_processors.TemplateProcessor',
                'hydeengine.media_processors.YUICompressor',),
                
        '.less':('hydeengine.media_processors.TemplateProcessor',
                'hydeengine.media_processors.LessCSS',
                'hydeengine.media_processors.YUICompressor',),
        '.js':(
                'hydeengine.media_processors.TemplateProcessor',
                'hydeengine.media_processors.YUICompressor',)
    } 
}

CONTENT_PROCESSORS = {
    'prerendered/': {
        '*.*' : ('hydeengine.content_processors.PassthroughProcessor',)
	 }
}

SITE_POST_PROCESSORS = {
    # 'media/js': {
    #        'hydeengine.site_post_processors.FolderFlattener' : {
    #                'remove_processed_folders': True,
    #                'pattern':"*.js"
    #        }
    #    }
}

FILTER = { 
    'exclude': (".*","*~")
}        


#Processor Configuration 

# 
#  Set this to the output of `which growlnotify`. If `which`  returns emtpy,
#  install growlnotify from the Extras package that comes with the Growl disk image.
# 
#
GROWL = None

# path for YUICompressor, or None if you don't
# want to compress JS/CSS. Project homepage:
# http://developer.yahoo.com/yui/compressor/
# YUI_COMPRESSOR = "./lib/yuicompressor-2.4.2.jar"
YUI_COMPRESSOR = None 

# path for Closure Compiler, or None if you don't
# want to compress JS/CSS. Project homepage:
# http://closure-compiler.googlecode.com/
#CLOSURE_COMPILER = "./lib/compiler.jar"
CLOSURE_COMPRILER = None 

# path for HSS, which is a preprocessor for CSS-like files (*.hss)
# project page at http://ncannasse.fr/projects/hss
#HSS_PATH = "./lib/hss-1.0-osx"
HSS_PATH = None # if you don't want to use HSS

#Django settings

TEMPLATE_DIRS = (LAYOUT_DIR, CONTENT_DIR, TMP_DIR, MEDIA_DIR)

INSTALLED_APPS = (
    'hydeengine',
    'django.contrib.webdesign',
)
