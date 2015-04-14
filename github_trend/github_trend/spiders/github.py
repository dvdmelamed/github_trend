# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from github_trend.items import GithubTrendItem
import re

class GithubSpider(scrapy.Spider):
    name = "github"
    allowed_domains = ["github.com"]
    start_urls = (
        'http://www.github.com/trending',
    )

    def parse(self, response):
        sel = Selector(response)

        items = []
        item_nodes = response.xpath('//li[contains(@class, "repo-list-item")]')
        for item_node in item_nodes:
        	repo = GithubTrendItem()
        	repo['repo_name'] = item_node.xpath('.//h3[contains(@class, "repo-list-name")]/a/@href').extract()[0]
        	repo_description = item_node.xpath('.//p[contains(@class, "repo-list-description")]/text()').extract()
        	if repo_description:
        		repo['repo_description'] = repo_description[0].lstrip().rstrip()
        	
        	meta = item_node.xpath('.//p[contains(@class, "repo-list-meta")]').extract()
        	if meta:
        		num_stars = re.findall('\d+', meta[0])
        		if num_stars:
        			repo['num_stars'] = num_stars[0]
        	items.append(repo) 

        return items
