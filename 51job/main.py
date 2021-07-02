import time,threading,requests

from lxml import etree
from selenium import webdriver
from queue import Queue

class Job(threading.Thread):
    def __init__(self,url, q_page, name):
        self.base_url = base_url
        super().__init__()
        self.url = url
        self.q_page = q_page
        self.name = name

    def get_content_for_webdriver(self,url):
        '''
        请求页面，获取响应
        :param url:
        :return:
        '''
        # print(url)
        # 请求页面
        drive.get(url)
        # 返回页面源代码
        html_str = drive.page_source
        return etree.HTML(html_str)
        pass
    def get_content(self,url):
        '''
        请求子链接正文
        :param url:
        :return:
        '''
        # 请求头部信息
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
        }
        response = requests.get(url,headers = headers)
        # 使用gbk解码
        response.encoding = "gbk"
        return etree.HTML(response.text)

    def parse_page(self,tree):
        '''
        解析页面数据
        :param tree:
        :return:
        '''
        #获取职位链接
        time.sleep(2)
        job_urls = tree.xpath('//div[@class="j_joblist"]/div[@class="e"]/a/@href')
        # print(job_urls)
        drive.close()
        # print(job_urls)
        for job in job_urls:
            # 遍历请求子链接
            detail_urls = self.get_content(job)
            for data in detail_urls:
                # 职位名称
                job_name = data.xpath('//h1/@title')
                # print(job_name)
                company = data.xpath('//div[@class="cn"]/p[@class="cname"]/a[1]/text()')
                # print(company)
                company_url = data.xpath('//div[@class="cn"]/p[@class="cname"]/a[1]/@href')
                # print(company_url)
                salary = data.xpath('//div[@class="cn"]/strong/text()')
                # print(salary)
                work_location = data.xpath('//div[@class="bmsg inbox"]/p/text()')
                job_info = data.xpath('//div[@class="cn"]/p[2]/text()')
                # print(job_info)
                # print(work_location)

                item = {}

                item["job_name"] = job_name
                item["company"] = company
                item["company_url"] = company_url
                item["salary"] = salary
                item["work_location"] = work_location
                item["job_info"] = job_info
                print(item)

                pass
        pass


    def main(self):
        base_url = r"https://search.51job.com/list/000000,000000,0000,00,9,99,Python,2,%s.html?\
                                lang=c&postchannel=0000&workyear=99\
                                &cotype=99&degreefrom=99&jobterm=99&\
                                companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
        # 遍历50页数据
        # for i in range(1,20):
        tree_page = self.get_content_for_webdriver(base_url % i)
        # 提取数据
        self.parse_page(tree_page)

            pass
        pass
    def run(self):
        '''
        开启多线程
        :return:
        '''
        while True:
            if self
if __name__ == '__main__':
    drive = webdriver.Chrome()
    base_url = r"https://search.51job.com/list/000000,000000,0000,00,9,99,Python,2,%s.html?\
                        lang=c&postchannel=0000&workyear=99\
                        &cotype=99&degreefrom=99&jobterm=99&\
                        companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
    # 创建任务队列
    q_page = Queue()
    # 初始化任务队列
    # 页数控制
    for i in range(1, 2):
        # print(base_url)
        # 入队操作
        q_page.put(i)
    # 创建list，长度就是线程数量
    crawl_list = ['a','b','c','d']
    # 循环遍历线程数量，开启多线程
    for crawl in  crawl_list:
        t = Job(base_url,q_page,crawl)
        t.start()
    # Job().main()
