from urllib.request import urlopen
from course_finder import *
from general import *

class spider:
    project_name = ''
    base_url = ''
    queue_file = ''
    crawled_file = ''
    courses_file = ''
    queue = set()
    crawled = set()
    courses = set()
    keyword = ''

    def __init__(self, project_name, base_url, keyword):
        spider.project_name = project_name
        spider.base_url = base_url
        spider.queue_file = spider.project_name + '/queue.txt'
        spider.crawled_file = spider.project_name + '/crawled.txt'
        spider.courses_file = spider.project_name + '/courses.txt'
        spider.keyword = keyword
        self.boot()
        self.crawl_page('First spider', spider.base_url, spider.keyword)

    @staticmethod
    def boot():
        create_project_dir(spider.project_name)
        create_data_files(spider.project_name, spider.base_url)
        spider.queue = file_to_set(spider.queue_file)
        spider.crawled = file_to_set(spider.crawled_file)
        spider.courses = file_to_set(spider.courses_file)

    @staticmethod
    def crawl_page(thread_name, page_url, keyword):
        if page_url not in spider.crawled:
            print(thread_name + ' is now crawling ' + page_url)
            print('Queue ' + str(len(spider.queue)) + ' | Crawled ' + str(len(spider.crawled)))
            print('Already found ' + str(len(spider.courses)) + ' courses')
            links, courses = spider.gather_links_and_courses(page_url, keyword)
            spider.add_links_to_queue(links)
            print('Finish adding links to queue!')
            spider.queue.remove(page_url)
            spider.crawled.add(page_url)
            spider.add_courses(courses)
            print('Finish adding courses')
            spider.update_files()

    @staticmethod
    def add_courses(courses):
        print('In this page, there is ' + str(len(courses)) + ' courses to add.')
        if courses:
            for course in courses:
                spider.courses.add(course)

    @staticmethod
    def add_links_to_queue(links):
        #print('there are ' + str(len(links)) + ' links to add')
        for link in links:
            if link not in spider.crawled:
                spider.queue.add(link)

    @staticmethod
    def gather_links_and_courses(page_url, keyword):
        html_string = ''
        try:
            response = urlopen(page_url)
            print("response.getheader('Content-Type') is " + response.getheader('Content-Type'))
            if 'text/html' in response.getheader('Content-Type'):
                print('We start encoding and decoding the html')
                html_bytes = response.read()
                html_string = html_bytes.decode('utf-8')
            print('The html_string works fine: ', (html_string != ''))
            finder_link = open_new_link()
            finder_course = CourseFinder(keyword)
            finder_link.feed(html_string)
            finder_course.feed(html_string)
        except:
            print('Error! We cannot add links or courses!')
            return set(), set()
        print("We gathered " + str(len(finder_link.links())) + ' links')
        print('We gathered ' + str(len(finder_course.courses())) + ' courses')
        return finder_link.links(), finder_course.courses()

    @staticmethod
    def update_files():
        set_to_file(spider.queue, spider.queue_file)
        set_to_file(spider.crawled, spider.crawled_file)
        set_to_file(spider.courses, spider.courses_file)

