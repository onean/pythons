import os,shutil
import time

def process_article(path):
    add_header(path)
    if os.path.isfile(path):
        file = open(path, 'r', encoding='utf-8')
        content = file.read()
        content = add_more(content)
        content = upload_img(content)
        file = open(path, 'w+', encoding='utf-8')
        file.write(content)
    pass

def add_header(path):
    if os.path.exists(path):
        createtime = os.path.getctime(path)
        name = os.path.basename(path)
        name = name.split('.')[0]
        categories = []
        tags = []

        file = open(path, 'r', encoding='utf-8')
        content = file.read()
        file.close()
        head = ''
        head = '---\n' + head
        if len(tags) > 0:
            head = 'tags: ' + str(tags) + '\n' + head
        if len(categories) > 0:
            head = 'categories: ' + str(categories) + '\n' + head
        head = 'date: ' + time.strftime('%Y-%m-%d',time.gmtime(createtime)) + '\n' + head
        head = 'title: ' + name + '\n' + head
        head = '---\n' + head
        content = head + content
        file = open(path, 'w+', encoding='utf-8')
        file.write(content)
        # file.write(content)
        file.close()
    else:
        print('the path is error')

#判断行数超过20行或字数超过300字
def add_more(content):
    return  content
def upload_img(content):
    return content

#提取标签
def extract_tag(content):
    pass
#提取分类
def extract_categories(content):
    pass
def move_to_blog(path):
    shutil.copy(filePath,'/Users/ay/Desktop/Project/Blog/onean.github.io/source/_posts/')

def distribute():
    os.system('cd /Users/ay/Desktop/Project/Blog/onean.github.io/ ; hexo clean ; hexo g ; hexo d')
    pass


filePath = input('输入路径：')

add_header(filePath)
move_to_blog(filePath)
distribute()