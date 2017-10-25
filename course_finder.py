from html.parser import HTMLParser
from urllib.parse import urljoin


class CourseFinder(HTMLParser):
    def __init__(self, keyword):
        super().__init__()
        self.course = set()
        self.keyword = keyword

    def handle_starttag(self, tag, attrs):
        true = True
        false = False
        if tag == 'div':
            for (attribute, value) in attrs:
                if attribute == 'data-course':
                    print('Successfully open data-course!')
                    dic = eval(value)
                    description = dic['description']
                    title = dic['title']
                    if self.keyword.casefold() in description.casefold() or \
                            self.keyword.casefold() in title.casefold():
                        print('We find a course!')
                        current_course = dic['displayName']
                        self.course.add(current_course)

    def courses(self):
        return self.course

    def error(self, message):
        pass


class open_new_link(HTMLParser):
    def __init__(self):
        super().__init__()
        self.link = set()
        self.special = 'http://classes.berkeley.edu'
        print('successfully create class open_new_link')

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'title' and 'Go to page ' in value:
                    #print('attribute title, value go to page exists')
                    for (att, v) in attrs:
                        if att == 'href':
                            if 'amp;' in v:
                                v = v.replace('amp;', '')
                            url = urljoin(self.special, v)
                            print('final url we decided to add to self.link is ' + url)
                            self.link.add(url)
                            break
                    break

    def links(self):
        return self.link

    def error(self, message):
        pass

#testing = open_new_link('http://classes.berkeley.edu/search/class/?f[0]=im_field_subject_area%3A483', )