
### Get this product for $5

<i>Packt is having its biggest sale of the year. Get this eBook or any other book, video, or course that you like just for $5 each</i>


<b><p align='center'>[Buy now](https://packt.link/9781787121485)</p></b>


<b><p align='center'>[Buy similar titles for just $5](https://subscription.packtpub.com/search)</p></b>


# Python Social Media Analytics
This is the code repository for [Python Social Media Analytics](https://www.packtpub.com/big-data-and-business-intelligence/python-social-media-analytics?utm_source=github&utm_medium=repository&utm_campaign=9781787121485), published by [Packt](https://www.packtpub.com/?utm_source=github). It contains all the supporting project files necessary to work through the book from start to finish.
## About the Book
Social Media platforms such as Facebook, Twitter, Forums, Pinterest, and YouTube have become part of everyday life in a big way. However, these complex and noisy data streams pose a potent challenge to everyone when it comes to harnessing them properly and benefiting from them. This book will introduce you to the concept of social media analytics, and how you can leverage its capabilities to empower your business.


Right from acquiring data from various social networking sources such as Twitter, Facebook, YouTube, Pinterest, and social forums, you will see how to clean data and make it ready for analytical operations using various Python APIs. This book explains how to structure the clean data obtained and store in MongoDB using PyMongo. You will also perform web scraping and visualize data using Scrappy and Beautifulsoup. 


Finally, you will be introduced to different techniques to perform analytics at scale for your social data on the cloud, using Python and Spark. By the end of this book, you will be able to utilize the power of Python to gain valuable insights from social media data and use them to enhance your business processes.

## Instructions and Navigation
All of the code is organized into folders. Each folder starts with a number followed by the application name. For example, Chapter02.



The code will look like the following:
```
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import requests\n",
    "\n",
    "results = []\n",
    "q = \"created:>2017-01-01\"\n",
    "\n",
    "def search_repo_paging(q):\n",
    "    params = {'q' : q, 'sort' : 'forks', 'order': 'desc', 'per_page' : 100}\n",
    "    url = 'https://api.github.com/search/repositories'\n",
    "\n",
    "    while True:\n",
    "\n",
    "        res = requests.get(url, params = params)\n",
    "        result = res.json()\n",
    "        results.extend(result['items'])\n",
    "        params = {}\n",
    "\n",
    "        try:\n",
    "            url = res.links['next']['url']\n",
    "        except:\n",
    "            break"
   ]
  },
```



## Related Products
* [Learning Social Media Analytics with R](https://www.packtpub.com/big-data-and-business-intelligence/learning-social-media-analytics-r?utm_source=github&utm_medium=repository&utm_campaign=9781787127524)

* [Mastering Social Media Mining with Python](https://www.packtpub.com/big-data-and-business-intelligence/mastering-social-media-mining-python?utm_source=github&utm_medium=repository&utm_campaign=9781783552016)

* [Mastering Social Media Mining with R](https://www.packtpub.com/big-data-and-business-intelligence/mastering-social-media-mining-r?utm_source=github&utm_medium=repository&utm_campaign=9781784396312)
### Download a free PDF

 <i>If you have already purchased a print or Kindle version of this book, you can get a DRM-free PDF version at no cost.<br>Simply click on the link to claim your free PDF.</i>
<p align="center"> <a href="https://packt.link/free-ebook/9781787121485">https://packt.link/free-ebook/9781787121485 </a> </p>