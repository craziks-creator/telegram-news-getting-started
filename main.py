import hashlib
import json
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from telegram_news.template import InfoExtractor, NewsPostman, InfoExtractorJSON, NewsPostmanJSON
from telegram_news.utils import xml_to_json
bot_token = os.getenv("TOKEN")
channel = os.getenv("CHANNEL")
channel2 = os.getenv("CHANNEL2")
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
db = Session(bind=engine.connect())

def ssc_id_policy(link):
        return hashlib.md5(link.encode("utf-8")).hexdigest()

#-------------------------channel 2----------------------------------#

url2 = "https://sscnr.nic.in/newlook/site/Whatsnew.html"
#url7 = "https://sscnr.nic.in/newlook/site/application_status.html"
#url6 = "https://sscnr.nic.in/newlook/site/admit_card.html"
tag2 = "Nrnews"
table_name2 = "Nrnews"

# Info extractor to process data format
ie1 = InfoExtractor()

# Select elements by CSS-based selector
ie1.set_list_selector('div.inner_page > ul > li') #id_ul_li
ie1.set_title_selector('h4')  #id
ie1.set_paragraph_selector('div.inner_page > ul > li a')
ie1.set_time_selector('span')
ie1.set_source_selector('span.sourceTemplate')
ie1.max_post_length = 2000

# News postman to manage sending affair
np1 = NewsPostman(listURLs=[url2, ], sendList=[channel,channel2, ], db=db, tag=tag2)
np1.set_bot_token(bot_token)
np1.set_extractor(ie1)
np1.set_table_name(table_name2)
np1.set_max_list_length(10)
np1.set_max_table_rows(25 * 3, False)
np1.poll()

#-------------------------channel 3----------------------------------#

url3 = "https://ssc.nic.in/Portal/AnswerKey"
tag3 = "answerkey"
table_name3 = "anskey"

# Info extractor to process data format
ie1 = InfoExtractor()

# Select elements by CSS-based selector
ie1.set_list_selector('div.frmatCertificates > ul > li') #id_ul_li
ie1.set_title_selector('h2')  #id
ie1.set_paragraph_selector('div.frmatCertificates > ul > li a')
ie1.set_time_selector('span')
ie1.set_source_selector('span.sourceTemplate')
ie1.max_post_length = 2000

# News postman to manage sending affair
np1 = NewsPostman(listURLs=[url3, ], sendList=[channel,channel2, ], db=db, tag=tag3)
np1.set_bot_token(bot_token)
np1.set_extractor(ie1)
np1.set_table_name(table_name3)
ie1.set_id_policy(ssc_id_policy)
np1.set_max_list_length(15)
np1.set_max_table_rows(25 * 3, False)
np1.poll()
"""
#-------------------------channel 4----------------------------------#

url4 = "https://ssc.nic.in/MarksStatus/MarksStatusIndex"
tag4 = "sscscore"
table_name4 = "scorecard"

# Info extractor to process data format
ie1 = InfoExtractor()

# Select elements by CSS-based selector
ie1.set_list_selector('select#ddlExam > option') #id_ul_li
ie1.set_title_selector('h1')  #id
ie1.set_paragraph_selector('select#ddlExam > option')
ie1.set_time_selector('span')
ie1.set_id_policy(ssc_id_policy)
ie1.set_source_selector('span.sourceTemplate')
ie1.max_post_length = 2000

# News postman to manage sending affair
np1 = NewsPostman(listURLs=[url4, ], sendList=[channel,channel2 ], db=db, tag=tag4)
np1.set_bot_token(bot_token)
np1.set_extractor(ie1)
np1.set_table_name(table_name4)
ie1.set_id_policy(ssc_id_policy)
np1.set_max_list_length(10)
np1.set_max_table_rows(25 * 3, False)
np1.poll()

#-------------------------channel 5----------------------------------#

url5 = "https://ssc.nic.in/Portal/Results"
tag5 = "cporesult"
table_name5 = "cpo"

# Info extractor to process data format
ie1 = InfoExtractor()

# Select elements by CSS-based selector
ie1.set_list_selector('div#noticeschsl.tab-content>tbody') #id_ul_li
ie1.set_title_selector('div#noticeschsl.tab-content>tbody>tr>td:nth-child(4)>a')  #id
ie1.set_paragraph_selector('div#noticeschsl.tab-content>tbody>tr>td:nth-child(4)>a')
ie1.set_time_selector('span')
ie1.set_source_selector('span.sourceTemplate')
ie1.max_post_length = 2000

# News postman to manage sending affair
np1 = NewsPostman(listURLs=[url5, ], sendList=[channel,channel2, ], db=db, tag=tag5)
np1.set_bot_token(bot_token)
np1.set_extractor(ie1)
np1.set_table_name(table_name5)
np1.set_max_list_length(10)
np1.set_max_table_rows(25 * 3, False)
np1.poll()
"""
#-------------------------channel 6----------------------------------#

url6 = "https://sscnr.nic.in/newlook/site/admit_card.html"
tag6 = "sscadmit"
table_name6 = "admit"

# Info extractor to process data format
ie1 = InfoExtractor()

# Select elements by CSS-based selector
ie1.set_list_selector('div.inner_page > ul ') #id_ul_li
ie1.set_title_selector('div.inner_page > ul > li ')  #id
ie1.set_paragraph_selector('div.inner_page > ul > li ')
ie1.set_time_selector('')
ie1.set_source_selector('span.sourceTemplate')
ie1.max_post_length = 2000
ie1.set_id_policy(ssc_id_policy)

# News postman to manage sending affair
np1 = NewsPostman(listURLs=[url6, ], sendList=[channel,channel2, ], db=db, tag=tag6)
np1.set_bot_token(bot_token)
np1.set_extractor(ie1)
np1.set_table_name(table_name6)
np1.set_max_list_length(10)
np1.set_max_table_rows(25 * 3, False)
np1.poll()

#-------------------------channel 7----------------------------------#

url7 = "https://sscnr.nic.in/newlook/site/application_status.html"
tag7 = "sscnrstatus"
table_name7 = "sscnrstatus"

# Info extractor to process data format
ie1 = InfoExtractor()

# Select elements by CSS-based selector
ie1.set_list_selector('div.inner_page > ul ') #id_ul_li
ie1.set_title_selector('div.inner_page > ul > li ')  #id
ie1.set_paragraph_selector('div.inner_page > ul > li ')
ie1.set_time_selector('')
ie1.set_source_selector('span.sourceTemplate')
ie1.max_post_length = 2000
ie1.set_id_policy(ssc_id_policy)

# News postman to manage sending affair
np1 = NewsPostman(listURLs=[url7, ], sendList=[channel,channel2, ], db=db, tag=tag7)
np1.set_bot_token(bot_token)
np1.set_extractor(ie1)
np1.set_table_name(table_name7)
np1.set_max_list_length(15)
np1.set_max_table_rows(25 * 3, False)
np1.poll()
#-------------------------channel 1----------------------------------#

url1 = "https://ssc.nic.in/Portal/LatestNews"
tag1 = "ssc"
table_name1 = "sscnews"

# Info extractor to process data format
ie1 = InfoExtractor()

# Select elements by CSS-based selector
ie1.set_list_selector('#forScrollNews > ul > li') #id_ul_li
ie1.set_title_selector('h3')  #id
ie1.set_paragraph_selector('a')
ie1.set_time_selector('span')
ie1.set_source_selector('span.sourceTemplate')
ie1.max_post_length = 2000

# News postman to manage sending affair
np1 = NewsPostman(listURLs=[url1, ], sendList=[channel,channel2, ], db=db, tag=tag1)
np1.set_bot_token(bot_token)
np1.set_extractor(ie1)
np1.set_table_name(table_name1)
np1.set_max_list_length(15)
np1.set_max_table_rows(25 * 3, False)
np1.poll()

#-------------------------channel 2----------------------------------#
"""
url2 = "https://createfeed.fivefilters.org/extract.php?url=https%3A%2F%2Fssc.nic.in%2FPortal%2FLatestNews&max=5&order=document&guid=0"
tag2 = "Sscrss"
table_name2 = "sscrss"

ie2 = InfoExtractorJSON()

# Pre-process the XML string, convert to JSON string
def list_pre_process(text):
    text = json.loads(xml_to_json(text))
    return json.dumps(text)
ie2.set_list_pre_process_policy(list_pre_process)

# Route by key list
ie2.set_list_router(['rss', 'channel', 'item'])
ie2.set_link_router(['link'])
ie2.set_title_router(['title'])
ie2.set_paragraphs_router(['description'])
ie2.set_time_router(['pubDate'])
ie2.set_source_router(['author'])
ie2.set_image_router(['media:thumbnail', '@url'])

# Customize ID for news item
def id_policy(link):
    return hashlib.md5(link.encode("utf-8")).hexdigest()
ie2.set_id_policy(id_policy)

np2 = NewsPostmanJSON(listURLs=[url2, ], sendList=[channel, ], db=db, tag=tag2)
np2.set_extractor(ie2)
np2.set_table_name(table_name2)
np2.set_max_list_length(50)
np2.set_max_table_rows(50 * 3, False)
np2.poll()
"""
