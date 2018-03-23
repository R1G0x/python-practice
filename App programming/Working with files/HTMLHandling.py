#HTML is a markup language for describing web documents or web pages.
#HTML documents are described by HTML tags. Each HTML tag describes different document content.
#For understanding parsing of HTML pages, let consider the sample url "http://xkcd.com". This url
#display comics about math and other languages.
#The displayed comics keep changing with respect to time.

#Read the contents of sample url using "urllib" module.
#Parse the contents of the web page to view the "Title" and "Caption" of displayed comic.
#Download the displayed comic to the current directory as comic.png 
import urllib.request
from lxml import etree

def readUrl(url):
  urlfile = urllib.request.urlopen(url)
  if urlfile.getcode() == 200:
    contents = urlfile.read()
    return contents
    
def downloadImage(url, ImageFileName=None):
  url = 'http:'+url
  contents = readUrl(url)
  
  if ImageFileName is None:
    ImageFileName = 'Sample.png'
    
  with open(ImageFileName, 'wb') as img:
    img.write(contents)
    
def get_title(con):
  if con:
    tree = etree.HTML(con)
    title = tree.xpath("//div[@id='ctitle']/text()")
    return title
    
def get_caption(con):
  if con:
    tree = etree.HTML(con)
    caption = tree.xpath("//div[@id='comic']/img/@title")
    return caption

def get_comic(con, comic_name=None):
  if con:
    tree = etree.HTML(con)
    comic_url = tree.xpath("//div[@id='comic']/img/@src")[0]
    downloadImage(comic_url, comic_name)
    
if __name__ == '__main__':
  url = "http://xkcd.com"
  html = readUrl(url)
  
  #Obtains title of the shown comic
  t = get_title(html)
  for e in t:
    print("Title: ", e)
  
  #Obtains caption of shown comic
  caption = get_caption(html)
  for c in caption:
    print("Caption: ", c)
  
  #Download's the comic image to current folder
  get_comic(html, 'Comic.png')