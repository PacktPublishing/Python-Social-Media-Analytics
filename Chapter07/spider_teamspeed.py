# -*- coding: utf-8 -*-

from pymongo import MongoClient
from bs4 import BeautifulSoup
import datetime
import logging
import scrapy
import json
import time
import sys
import re


class ForumTeamSpeedSpider(scrapy.Spider):
    name = "forum_teamspeed"
    allowed_domains = ['teamspeed.com']

    def __init__(self):
        self.client = MongoClient('127.0.0.1', 27017)
        self.mongo_db = self.client['teamspeed'].forum_teamspeed

    def get_info(self,msg, subject, subject_url, url):
        """ Parse a post and add it to the db.

        Args:
            msg: the html of a post
            subject: the name of the subject
            subject_url: the subject scrapped's url
            url: the scraped url
        """
        #post
        regex = re.compile('.*message.*')
        post = msg.find('div',id=regex).text.strip()

        #username
        try:
            username = msg.find('a', class_ = 'bigusername').text.strip()
        except Exception as e:
            logging.warning('Username not found on page {}'.format(url))
            return

        #date
        try:
            date = msg.find_all('div', class_ = 'normal')[1].text.strip()
        except Exception as e:
            logging.debug('Date not found on page {}'.format(url))
            date = None

        item = { 'forum': 'forum_teamspeed', 'subject': subject.strip(), \
                 'post': post, 'username': username, 'date': date, 'subject_url': subject_url.strip() }


        self.mongo_db.insert_one(item)


    def parse_posts(self,res, meta):
        """ Parse the html page and add posts to db.

        Args:
            res: response
            meta: other info for the post

        Returns:
            None
        """
        soup = BeautifulSoup(res.text, 'html.parser')
        messages = self.get_messages(soup)
        infos = self.foreach(lambda x: self.get_info(x, meta['subject'], meta['subject_url'], res.url), messages)

    def foreach(self,fn, args):
        """ Foreach function as map without return.

        Args:
            fn: function
            args: an iterable
        """
        for x in args:
            fn(x)

    def get_messages(self,soup):
        """ Find messages on the page.

        Args:
            soup: the html page

        Returns:
            The posts tr
        """
        msgs = soup.select('div[id=posts]')

        return msgs

    def start_requests(self):
        """ Start function for crawling """
        urls = ['https://teamspeed.com/forums/']
        for url in urls:
            yield scrapy.Request(url = url, callback = self.get_categories)

    def get_posts(self, res):
        """ Crawl over the posts.

        Args:
            self: self
            res: the before scrapy req

        Returns:
            Request of the subject crawler
        """
        domain = 'https://teamspeed.com/forums/'

        next_links = []

        try:
            nb_pages = int(res.xpath('//div[@class="pagenav"]/table//tr/td[@class="vbmenu_control"]/text()').extract()[0].split("of")[1].strip().replace(",",""))
        url_parts = res.url.split('/')
            new_url = "https://" + url_parts[2] + "/" + url_parts[3] + "/" + url_parts[4] + ".html"
            for i in range(0,nb_pages):
                next_links.append(new_url + str(i) + '.html')
        except:
            nb_pages = 1


        self.parse_posts(res, res.meta)

        for next_link in next_links:
            logging.debug('next_link_post {}'.format(next_link))
            yield scrapy.Request(next_link, callback = self.get_posts, dont_filter = False, meta = {'domain': domain})


    def get_subject(self, res):
        """ Crawl over the subjects.

        Args:
            self: self
            res: response

        Returns:
            Request
        """

        nb_pages = int(res.xpath('//div[@class="pagenav"]/table/tr/td[@class="vbmenu_control"]/text()').extract()[0].split("of")[1].strip().replace(",",""))
        next_links = []
        url_parts = res.url.split('/')
        new_url = "https://" + url_parts[2] + "/" + url_parts[3] + "/" + url_parts[4] + "/index"
        for i in range(0,nb_pages):
            next_links.append(new_url + str(i) + '.html')

        domain = 'https://teamspeed.com/forums/'
        urls = [(path.extract(), subject.extract()) for path, subject in zip(res.xpath('//tbody[contains(@id,"threadbit")]/tr/td[3]/div[1]/a/@href'), res.xpath('//tbody[contains(@id,"threadbit")]/tr/td[3]/div[1]/a/text()'))]

        for url in urls:
            yield scrapy.Request(url = url[0], callback=self.get_posts, dont_filter = False, meta = {'subject': url[1], 'subject_url': url[0],'rec': True, 'dont_redirect': True})
        for next_link in next_links:
            yield scrapy.Request(next_link, callback = self.get_subject, dont_filter = False, meta = {'domain': domain})


    def get_categories(self, res):
        """ Crawl over the categories.

        Args:
            self: self
            res: response

        Returns:
            Request
        """
        domain = 'https://teamspeed.com/forums/'
        urls = {(path.extract(), cat.extract()) for path, cat in zip(res.xpath('//tbody[contains(@id,"forumbit")]/tr/td[2]/div/a/@href'), res.xpath('//tbody[contains(@id,"forumbit")]/tr/td[2]/div/a/strong/text()'))}
        for url in urls:
            yield scrapy.Request(url = url[0], callback = self.get_subject, meta = {'rec': True, 'cat': url[1], 'dont_redirect': True})
