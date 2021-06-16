import scrapy,re

from ..items  import WorkPediyItem


class PediySpider(scrapy.Spider):
    name = 'pediy'
    # allowed_domains = ['https://bbs.pediy.com/new-tid.htm']
    start_urls = []
    # 分页
    for i in range(1,41):
        # 确定url
        base_url = 'https://bbs.pediy.com/new-digest-{}.htm'.format(i)
        # 将分页的链接传入至start_urls中
        start_urls.append(base_url)
        pass


    def parse(self,response):
        '''
        提取分页中的所有链接
        :param response:
        :return:
        '''
        # 请求页面中每一个帖子的详情链接
        bbs_urls = response.xpath('//tr[@class="thread "]/td/div[@class="subject"]/a[position()<2]/@href').extract()
        # print(bbs_urls)
        for post_url in bbs_urls:
            # 发送请求
            yield scrapy.Request(url= "https://bbs.pediy.com/"+post_url, callback= self.parse_detail, encoding= 'utf-8')
            # print('https://bbs.pediy.com/'+bbs_url)
            pass
        pass

    def parse_detail(self, response):
        # 文章标题
        # print(response.text)
        post_title = response.xpath('//*[@class="break-all m-0"]/span/text()').extract_first().strip()
        # print(post_title)
        # 文章作者
        post_author = response.xpath('//div[@class="col pr-0"]/div[1]/span/a/text()').extract_first()
        # print(post_author)
        # 查看人数
        post_view = response.xpath('//span[@class="text-grey ml-3 hidden-md-down"]/text()').extract_first()
        # print(post_view)
        # 最后更新时间
        lastest_time = response.xpath('//span[@class="date text-grey ml-1"]/text()').extract_first()
        # print(lastest_time)
        # 文章内容

        post_content = response.xpath('string(//div[@class="message break-all"])').extract_first().strip()
        print(post_content)

        # post_images = response.xpath('//div[@class="message break-all"])//img/@src').extract()
        # print(post_images)
        # 文章链接
        post_url = response.url
        # print(post_url)
        # 使用字典保存数据
        item = WorkPediyItem()
        item['post_title'] = post_title
        item['post_author'] = post_author
        item['post_url'] = post_url
        item['post_content'] = post_content
        item['post_view'] = post_view
        item['lastest_time'] = lastest_time
        print(item)
        # print(response)
        yield item
        pass
