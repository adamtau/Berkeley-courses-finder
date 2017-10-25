import os


def create_project_dir(directory):
    """each website I crawled has a new directory"""

    if not os.path.exists(directory):
        print('Creating new directory ' + directory)
        os.makedirs(directory)
    else:
        print('The directory already exists.')


def create_data_files(project_name, base_url):
    """create queue and crawled files"""
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    courses = project_name + '/courses.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)

    if not os.path.isfile(crawled):
        write_file(crawled, '')

    if not os.path.isfile(courses):
        write_file(courses, '')


def write_file(path, data):
    """write a new file. Create a new file"""
    with open(path, 'w') as f:
        f.write(data)


def append_to_file(path, data):
    """add data onto an existing file"""
    with open(path, 'a') as file:
        file.write(data + '\n')


def delete_file_contents(path):
    """delete all the contents in a file"""
    open(path, 'w').close()


def file_to_set(file):
    """read a file and convert all data into a set. So, we can use set, a faster way, to store data"""
    set_of_data = set()
    with open(file, 'rt') as f:
        for line in f:
            set_of_data.add(line.replace('\n', ''))
    return set_of_data


def set_to_file(set_of_data, file):
    """Store all data in a set into a file, so that we can store data safely even we shut down the computer"""
    with open(file, 'w') as f:
        for l in sorted(set_of_data):
            try:
                f.write(l + '\n')
            except:
                pass






