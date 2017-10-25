import threading
from queue import Queue
from spider import spider
from general import *

PROJECT_NAME = 'get_courses'
HOMEPAGE = "http://classes.berkeley.edu/search/class/?f[0]=im_field_subject_area%3A483"
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
COURSES_FILE = PROJECT_NAME + '/courses.txt'
NUMBER_OF_THREADS = 8
KEYWORD = 'web crawler'
queue = Queue()
spider(PROJECT_NAME, HOMEPAGE, KEYWORD)

def crawl():
    queue_set = file_to_set(QUEUE_FILE)
    if len(queue_set) > 0:
        print(str(len(queue_set)) + ' links are queuing')
        create_jobs()
    else:
        print('Bravo! We have finished crawling!')

def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()

def create_spiders():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()

def work():
    while True:
        url = queue.get()
        spider.crawl_page(threading.current_thread().name, url, KEYWORD)
        queue.task_done()

create_spiders()
crawl()