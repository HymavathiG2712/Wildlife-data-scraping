#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# search for the keyword
#ask user to input the word
# make a list of all websites in a list
#give common name and terminology for all the websites
#make for 5 websites


# In[1]:


import requests
from bs4 import BeautifulSoup

search_word="ivory"
# specify the Etsy search URL
url = f"https://www.etsy.com/search?q={search_word}&ref=search_bar"

# send a request to the URL and get the page content
response = requests.get(url)
content = response.content

# create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(content, "html.parser")

# find all the listings on the page
listings = soup.find_all("div", {"class": "v2-listing-card"})

# loop through each listing and extract the title, price, and URL
for listing in listings:
    # get the title and URL
    title = listing.find("h3", {"class": "v2-listing-card__title"}).text.strip()
    
    url_elem = listing.find("a", {"class": "listing-link"})
    if url_elem:
        url = url_elem.get("href")
    else:
        url = "N/A"
    # get the price, if available
    if listing.find("span", {"class": "currency-value"}):
        price = listing.find("span", {"class": "currency-value"}).text
    else:
        price = "N/A"
    
    
    image=listing.find('img')
    if image is not None:
        image=image.get('src') 
        
    # print the title, price, and URL
    print(title)
    print(price)
    print(url)
    print(f'image: {image}')
    print("--------------------")




# In[1]:


def my_python_function(search_word):

    import requests
    from bs4 import BeautifulSoup

    # URL to scrape
    url = 'https://www.chairish.com/search?q={search_word}'
    # Send a GET request to the URL and store the response
    response = requests.get(url)
    # Create a BeautifulSoup object from the response content
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find all the product containers on the page
    products = soup.find_all('div', {'class': 'grid-product-menu-wrapper js-grid-product-menu-wrapper'})
    #s-item__wrapper clearfix
    # Loop through each product container and extract the title, price and URL
    for product in products:
        # Extract the title, price and URL of each product, handling cases where they are not present
        titles = product.find('h3', {'class': 'product-title'}).text
        price = product.find('span', {'class': 'product-price-value'})
        if price is not None:
            price = price.text.strip()

        url = product.find('a', {'class': 'product-link'})
        if url is not None:
            url = url.get('href')

        image=product.find('img')
        if image is not None:
            image=image.get('src') 

        # Print the title, price and URL of each product
        print(f'Title:{titles}')
        print(f'Price: {price}')
        print(f'URL: {url}')
        print(f'image: {image}', "\n")
        
my_python_function("ivory")


# In[5]:


import requests
from bs4 import BeautifulSoup

# URL to scrape
url = 'https://www.chairish.com/search?q={search_word}'
# Send a GET request to the URL and store the response
response = requests.get(url)
# Create a BeautifulSoup object from the response content
soup = BeautifulSoup(response.content, 'html.parser')
# Find all the product containers on the page
products = soup.find_all('div', {'class': 'grid-product-menu-wrapper js-grid-product-menu-wrapper'})
#s-item__wrapper clearfix
# Loop through each product container and extract the title, price and URL
for product in products:
    # Extract the title, price and URL of each product, handling cases where they are not present
    titles = product.find('h3', {'class': 'product-title'}).text
    price = product.find('span', {'class': 'product-price-value'})
    if price is not None:
        price = price.text.strip()

    url = product.find('a', {'class': 'product-link'})
    if url is not None:
        url = url.get('href')

    image=product.find('img')
    if image is not None:
        image=image.get('src') 

    # Print the title, price and URL of each product
    print(f'Title:{titles}')
    print(f'Price: {price}')
    print(f'URL: {url}')
    print(f'image: {image}', "\n")


# In[15]:


import requests
from bs4 import BeautifulSoup 

def my_python_function(search_word):

    # URL to scrape
    url = 'https://www.ebay.com/sch/i.html?_nkw={search_word}'
    # Send a GET request to the URL and store the response
    response = requests.get(url)
    # Create a BeautifulSoup object from the response content
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find all the product containers on the page
    products = soup.find_all('div', {'class': 's-item__wrapper clearfix'})
    #s-item__wrapper clearfix
    # Loop through each product container and extract the title, price and URL
    for product in products:
        # Extract the title, price and URL of each product, handling cases where they are not present
        titles = product.find('div', {'class': 's-item__title'})
        for title in titles:
            title = titles.find('span').text

        price = product.find('span', {'class': 's-item__price'})
        if price is not None:
            price = price.text.strip()

        url = product.find('a', {'class': 's-item__link'})
        if url is not None:
            url = url.get('href')

        image=product.find('img')
        if image is not None:
            image=image.get('src') 

        # Print the title, price and URL of each product
        print(f'Title: {title}')
        print(f'Price: {price}')
        print(f'URL: {url}')
        print(f'image: {image}')

my_python_function("ivory")


# In[11]:


import requests
from bs4 import BeautifulSoup

search_word='ivory'
sdate='2023-04-20'
edate='2023-04-30'
# URL to scrape
url = f'https://www.auctionzip.com/search-results?query={search_word}&startDate={sdate}&endDate={edate}'
# Send a GET request to the URL and store the response
response = requests.get(url)
# Create a BeautifulSoup object from the response content
soup = BeautifulSoup(response.content, 'html.parser')
# Find all the product containers on the page
products = soup.find_all('div', {'class': 'col-6 col-md-4 col-lg-3 mt-3 mb-5 lotListItem'})
#s-item__wrapper clearfix
# Loop through each product container and extract the title, price and URL
for product in products:
    # Extract the title, price and URL of each product, handling cases where they are not present
    titles = product.find('h2', {'class': 'lot-title mt-2 text-clamp-2'})
    for title in titles:
        title = titles.find('span').text

    price = product.find('span', {'class': 'bold'})
    if price is not None:
        price = price.text.strip()

    
    url = product.find('a', {'class': 'link linkToLot text-clamp-2'})
    if url is not None:
        url = "https://www.auctionzip.com" + url.get('href')


    i=product.find('div',{'class': 'thumb'})
    image=product.find('img')
    if image is not None:
        image=image.get('data-src') 
    

    # Print the title, price and URL of each product
    print(f'Title: {title}')
    print(f'Price: {price}')
    print(f'URL: {url}')
    print(f'image: {image}')
    


# In[13]:


import requests
from bs4 import BeautifulSoup

search_word='ivory'
# URL to scrape
url = f'https://www.ebid.net/us/perl/main.cgi?go=1&mo=search&category=&type=keyword&words={search_word}&categoryid='
# Send a GET request to the URL and store the response
response = requests.get(url)
# Create a BeautifulSoup object from the response content
soup = BeautifulSoup(response.content, 'html.parser')
# Find all the product containers on the page
products = soup.find_all('li', {'class': 'showroomcell'})

#s-item__wrapper clearfix
# Loop through each product container and extract the title, price, URL and image


# In[16]:


import requests
from bs4 import BeautifulSoup

search_word='ivory'

# URL to scrape
url = f'https://www.trademe.co.nz/a/search?search_string={search_word}'

# Send a GET request to the URL and store the response
response = requests.get(url)

# Create a BeautifulSoup object from the response content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the product containers on the page
# products = soup.find('div', {'class': 'tm-search__two-col-grid l-container'})

titles=[]
images=[]
prices=[]
urls=[]
# Find the URL of the product
for url in soup.find_all('a', {'class': 'tm-marketplace-search-card__detail-section tm-marketplace-search-card__detail-section--link'}):
    url = 'https://www.trademe.co.nz/a/' + url['href']
    urls.append(url)
         
for title in soup.find_all("div", class_="tm-marketplace-search-card__title"):
    titles.append(title.text.strip())

for image in soup.find_all('img', {'class': 'marketplace-summary-image-lazy-loader__thumbnail contain ng-star-inserted'}):
    images.append(image['src'])
    
for price in soup.find_all('div', {'class': 'tm-marketplace-search-card__price ng-star-inserted'}):
    prices.append(price.text.strip())

for i in range(len(images)):
    print([titles[i],
           images[i], 
           prices[i], 
           urls[i]])


# In[7]:


import requests
from bs4 import BeautifulSoup

search_word='ivory'
# URL to scrape
url = f'https://www.canadianlisted.com/{search_word}/listing'
# Send a GET request to the URL and store the response
response = requests.get(url)
# Create a BeautifulSoup object from the response content
soup = BeautifulSoup(response.content, 'html.parser')
# Find all the product containers on the page
products = soup.find_all('div', {'class': 'itemclbox'})

for product in products:
    # Extract the title, price, URL and image of each product, handling cases where they are not present
  
  
    title = product.find('div',{'class' :'salecladtop'})
    if title is not None:
        title = title.text.strip()
    else:
        title = "N/A"
        
    price = product.find('span', {'class': 'bold'})
    if price is not None:
        price = price.text.strip()

    url = product.find('a')
    if url is not None:
        url = url.get('href')
    else:
        url = "N/A"
    
    image=product.find('img') 
    if image is not None:
        image="https:"+image.get('src') 
    else:
        image = "N/A"
        

    # Print the title, price, URL and image of each product
    print(f'Title: {title}')
    print(f'URL: {url}')
    print(f'Image: {image}')


# In[19]:


import requests
from bs4 import BeautifulSoup


url = 'https://www.ukclassifieds.co.uk/search/q,ivory'
response = requests.get(url)

# parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# find all the items displayed on the page
products = soup.find_all('div', class_='simple-wrap')

for product in products:
    
    title = product.find('a',{'class' :'title'})
    if title is not None:
        title = title.text.strip()
    else:
        title = "N/A"
        
    price = product.find('div', {'class': 'price isGrid isDetail'})
    if price is not None:
        price = price.text.strip()
    
    url = product.find('a', {'class': 'img'})
    if url is not None:
        url = url.get('href')

    image=product.find('img')
    if image is not None:
        image=image.get('src') 
    # Print the title, price, URL and image of each product
    print(f'Title: {title}')
    print(f'Price: {price}')
    print(f'URL: {url}')
    print(f'Image: {image}')


# In[ ]:


#for some URLs you cannot search by giving search word


# In[ ]:


search_word = input("Enter your value: ")

url = f"https://www.etsy.com/search?q={search_word}&ref=search_bar"

# send a request to the URL and get the page content
response = requests.get(url)
content = response.content

# create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(content, "html.parser")

# find all the listings on the page
listings = soup.find_all("div", {"class": "v2-listing-card"})

# loop through each listing and extract the title, price, and URL
for listing in listings:
    # get the title and URL
    title = listing.find("h3", {"class": "v2-listing-card__title"}).text.strip()
    
    url_elem = listing.find("a", {"class": "listing-link"})
    if url_elem:
        url = url_elem.get("href")
    else:
        url = "N/A"
    # get the price, if available
    if listing.find("span", {"class": "currency-value"}):
        price = listing.find("span", {"class": "currency-value"}).text
    else:
        price = "N/A"
    
    
    image=listing.find('img')
    if image is not None:
        image=image.get('src') 
        
    # print the title, price, and URL
    print(title)
    print(price)
    print(url)
    print(f'image: {image}')
    print("--------------------")

    
    
import requests
from bs4 import BeautifulSoup

search_word='ivory'
# URL to scrape
url = f'https://www.canadianlisted.com/{search_word}/listing'
# Send a GET request to the URL and store the response
response = requests.get(url)
# Create a BeautifulSoup object from the response content
soup = BeautifulSoup(response.content, 'html.parser')
# Find all the product containers on the page
products = soup.find_all('div', {'class': 'itemclbox'})

for product in products:
    # Extract the title, price, URL and image of each product, handling cases where they are not present
  
  
    title = product.find('div',{'class' :'salecladtop'})
    if title is not None:
        title = title.text.strip()
    else:
        title = "N/A"
        
    price = product.find('span', {'class': 'bold'})
    if price is not None:
        price = price.text.strip()

    url = product.find('a')
    if url is not None:
        url = url.get('href')
    else:
        url = "N/A"
    
    image=product.find('img') 
    if image is not None:
        image="https:"+image.get('src') 
    else:
        image = "N/A"
        

    # Print the title, price, URL and image of each product
    print(f'Title: {title}')
    print(f'URL: {url}')
    print(f'Image: {image}')


# URL to scrape
url = f'https://www.chairish.com/search?q={search_word}'
# Send a GET request to the URL and store the response
response = requests.get(url)
# Create a BeautifulSoup object from the response content
soup = BeautifulSoup(response.content, 'html.parser')
# Find all the product containers on the page
products = soup.find_all('div', {'class': 'grid-product-menu-wrapper js-grid-product-menu-wrapper'})
#s-item__wrapper clearfix
# Loop through each product container and extract the title, price and URL
for product in products:
    # Extract the title, price and URL of each product, handling cases where they are not present
    titles = product.find('h3', {'class': 'product-title'}).text
    price = product.find('span', {'class': 'product-price-value'})
    if price is not None:
        price = price.text.strip()

    url = product.find('a', {'class': 'product-link'})
    if url is not None:
        url = url.get('href')
    
    image=product.find('img')
    if image is not None:
        image=image.get('src') 

    # Print the title, price and URL of each product
    print(f'Title:{titles}')
    print(f'Price: {price}')
    print(f'URL: {url}')
    print(f'image: {image}', "\n")

    
    

# URL to scrape
url = f'https://www.ebay.com/sch/i.html?_nkw={search_word}'
# Send a GET request to the URL and store the response
response = requests.get(url)
# Create a BeautifulSoup object from the response content
soup = BeautifulSoup(response.content, 'html.parser')
# Find all the product containers on the page
products = soup.find_all('div', {'class': 's-item__wrapper clearfix'})
#s-item__wrapper clearfix
# Loop through each product container and extract the title, price and URL
for product in products:
    # Extract the title, price and URL of each product, handling cases where they are not present
    titles = product.find('div', {'class': 's-item__title'})
    for title in titles:
        title = titles.find('span').text

    price = product.find('span', {'class': 's-item__price'})
    if price is not None:
        price = price.text.strip()

    url = product.find('a', {'class': 's-item__link'})
    if url is not None:
        url = url.get('href')
    
    image=product.find('img')
    if image is not None:
        image=image.get('src') 

    # Print the title, price and URL of each product
    print(f'Title: {title}')
    print(f'Price: {price}')
    print(f'URL: {url}')
    print(f'image: {image}')

# URL to scrape
url = f'https://www.trademe.co.nz/a/search?search_string={search_word}'

# Send a GET request to the URL and store the response
response = requests.get(url)

# Create a BeautifulSoup object from the response content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the product containers on the page
# products = soup.find('div', {'class': 'tm-search__two-col-grid l-container'})

titles=[]
images=[]
prices=[]
urls=[]
# Find the URL of the product
for url in soup.find_all('a', {'class': 'tm-marketplace-search-card__detail-section tm-marketplace-search-card__detail-section--link'}):
    url = 'https://www.trademe.co.nz/a/' + url['href']
    urls.append(url)
         
for title in soup.find_all("div", class_="tm-marketplace-search-card__title"):
    titles.append(title.text.strip())

for image in soup.find_all('img', {'class': 'marketplace-summary-image-lazy-loader__thumbnail contain ng-star-inserted'}):
    images.append(image['src'])
    
for price in soup.find_all('div', {'class': 'tm-marketplace-search-card__price ng-star-inserted'}):
    prices.append(price.text.strip())

for i in range(len(images)):
    print([titles[i],
           images[i], 
           prices[i], 
           urls[i]])


# In[3]:


import requests
from bs4 import BeautifulSoup

search_word='ivory'
url = f'https://www.gumtree.com.au/s-antiques-art-collectables/{search_word}/k0c18297r10?categoryRedirected=true'
response = requests.get(url)

# parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# find all the items displayed on the page
products = soup.find_all('div', {'class': 'user-ad-collection-new-design__wrapper--row'})

for product in products:
    url = product.find('a')
    if url is not None:
        url = "https://www.gumtree.com.au/"+url.get('href')
    
    image=product.find('img')
    if image is not None:
        image=image.get('data-src') 
    
    title = product.find('span',{'class' :'user-ad-row-new-design__title-span'})
    if title is not None:
        title = title.text.strip()
    else:
        title = "N/A"
    
    price = product.find('span', {'class': 'user-ad-price-new-design__price'})
    if price is not None:
        price = price.text.strip()

    print(f'Title: {title}')
    print(f'Price: {price}')
    print(f'URL: {url}')
    print(f'Image: {image}')


# In[ ]:


import requests
from bs4 import BeautifulSoup

search_word='ivory'
# URL to scrape
url = f'https://www.preloved.co.uk/search?keyword={search_word}'
# Send a GET request to the URL and store the response
response = requests.get(url)
# Create a BeautifulSoup object from the response content
soup = BeautifulSoup(response.content, 'html.parser')
# Find all the product containers on the page
products = soup.find_all('li', {'class': 'search-result'})

for product in products:
    title = product.find('h2')
    if title is not None:
        title = title.text.strip()
    else:
        title = "N/A"
        
    price = product.find('span', {'class': 'search-result__meta bold t-color--2-2 u-capitalize is-price'})
    if price is not None:
        price = price.text.strip()
        
    url = product.find('a')
    if url is not None:
        url = url.get('href')
    else:
        url = "N/A"
        
    image=product.find('img') 
    if image is not None:
        image=image.get('data-src') 
    else:
        image = "N/A"
        
    print(f'URL: {url}')
    print(f'Title: {title}')
    print(f'Price: {price}')
    print(f'Image: {image}')


# In[ ]:


import requests
from bs4 import BeautifulSoup

search_word='ivory'
# URL to scrape
url = f'https://www.thetaxidermystore.com/catalogsearch/result/?cat=0&q={search_word}'
# Send a GET request to the URL and store the response
response = requests.get(url)
# Create a BeautifulSoup object from the response content
soup = BeautifulSoup(response.content, 'html.parser')
# Find all the product containers on the page
products = soup.find_all('div', {'class': 'item first'})

for product in products:
    title = product.find('h2')
    if title is not None:
        title = title.text.strip()
    else:
        title = "N/A"
    
    url = product.find('a')
    if url is not None:
        url = url.get('href')
    else:
        url = "N/A"
        
    price = product.find('span', {'class': 'price'})
    if price is not None:
        price = price.text.strip()
    
    image=product.find('img') 
    if image is not None:
        image=image.get('src') 
    else:
        image = "N/A"
    
        
    print(f'URL: {url}')
    print(f'Title: {title}')
    print(f'Price: {price}')
    print(f'Image: {image}')


# In[17]:


import requests
from bs4 import BeautifulSoup

search_word='ivory'
# URL to scrape
url = f'https://picclick.com/?q={search_word}'
# Send a GET request to the URL and store the response
response = requests.get(url)
# Create a BeautifulSoup object from the response content
soup = BeautifulSoup(response.content, 'html.parser')
# Find all the product containers on the page
products = soup.find_all('li', {'class':'amazon'})


for product in products:
    
    title = product.find('h3')
    if title is not None:
        title = title.text.strip()
    else:
        title = "N/A"
        
    url = product.find('a')
    if url is not None:
        url = url.get('href')
    else:
        url = "N/A"
        
    price = product.find('div', {'class': 'price'})
    if price is not None:
        price = price.text.strip()
        
    image=product.find('img') 
    if image is not None:
        image=image.get('src') 
    else:
        image = "N/A"
        
        
    print(f'Title: {title}')
    print(f'URL: {url}')
    print(f'Price: {price}')
    
    print(f'Image: {image}')


# In[21]:


import requests
from bs4 import BeautifulSoup

search_word='ivory'
# URL to scrape
url = f'https://www.1stdibs.com/search/?q={search_word}'
# Send a GET request to the URL and store the response
response = requests.get(url)
# Create a BeautifulSoup object from the response content
soup = BeautifulSoup(response.content, 'html.parser')
# Find all the product containers on the page
products = soup.find_all('div', {'class':'_10b2665f _b88c87ca _6dba19f'})


for product in products:
    
    title = product.find('div',{'class':'_16da7886'})
    if title is not None:
        title = title.text.strip()
    else:
        title = "N/A"
        
    url = product.find('a',{'class':'_9e04a611 _9f85bf45 _f7a3e2b1'})
    if url is not None:
        url = "https://www.1stdibs.com/"+ url.get('href')
    else:
        url = "N/A"
        
    price = product.find('div', {'class': '_60451376'})
    if price is not None:
        price = price.text()
        
    image=product.find('img') 
    if image is not None:
        image=image.get('src') 
    else:
        image = "N/A"
        
        
    print(f'Title: {title}')
    print(f'URL: {url}')
    print(f'Price: {price}')
    print(f'Image: {image}')


# In[5]:


import requests
from bs4 import BeautifulSoup

search_word='ivory'
# URL to scrape
url = f'https://www.boneroom.com/apps/search?q={search_word}'
# Send a GET request to the URL and store the response
response = requests.get(url)
# Create a BeautifulSoup object from the response content
soup = BeautifulSoup(response.content, 'html.parser')
# Find all the product containers on the page
products = soup.find_all('li', {'id':'wsite-search-product-result-section'})

for product in products:
    
    title = product.find('span',{'class':'wsite-search-product-name'})
    if title is not None:
        title = title.text.strip()
    else:
        title = "N/A"
    
    url = product.find('a')
    if url is not None:
        url = "https://www.boneroom.com"+url.get('href')
    else:
        url = "N/A"
    
    price = product.find('span', {'class': 'wsite-search-product-price'})
    if price is not None:
        price = price.text.strip()
    else:
        price = "N/A"
    
    image=product.find('a',{'class':'cloud-zoom'}) 
    if image is not None:
        image=image.get('href') 
    else:
        image = "N/A"
    
    print(f'Title: {title}')
    print(f'URL: {url}')
    print(f'Price: {price}')
    print(f'Image: {image}')


# In[2]:


import requests
from bs4 import BeautifulSoup

search_word='tusk'
# URL to scrape
url = 
f'https://www.trocadero.com/directory/search.php?keyword={search_word}&archinsearch=yes&click_to_search_now.x=0&click_to_search_now.y=0&category=ALL+ITEMS&period=No+Selection&order=Most+Recent&item=&numitem=15&listtype=thumb'

# Send a GET request to the URL and store the response
response = requests.get(url)
# Create a BeautifulSoup object from the response content
soup = BeautifulSoup(response.content, 'html.parser')
# Find all the product containers on the page
products = soup.find_all('div', {'class':'item-cell'})

for product in products:
    
    title = product.find('span',{'class':'item-pict-dealer'})
    if title is not None:
        title = title.text.strip()
    else:
        title = "N/A"
    
    url = product.find('a')
    if url is not None:
        url = url.get('href')
    else:
        url = "N/A"
    
    price = product.find('span', {'class': 'item-pict-price'})
    if price is not None:
        price = price.text.strip()
    else:
        price = "N/A"
    
    image=product.find('img') 
    if image is not None:
        image=image.get('src') 
    else:
        image = "N/A"
    
    print(f'Title: {title}')
    print(f'URL: {url}')
    print(f'Price: {price}')
    print(f'Image: {image}')


# In[ ]:


import requests
from bs4 import BeautifulSoup

search_word='tusk'
# URL to scrape
url = f'https://chichesterinc.com/?ss360Query={search_word}'
# Send a GET request to the URL and store the response
response = requests.get(url)
# Create a BeautifulSoup object from the response content
soup = BeautifulSoup(response.content, 'html.parser')
# Find all the product containers on the page
products = soup.find_all('div',{'class':'ss360-suggests'})

for product in products:
    
    title = product.find('a')
    if title is not None:
        title = title.text.strip()
    else:
        title = "N/A"
    
    url = product.find('a',{'class':'ss360-result-link'})
    if url is not None:
        url = url.get('href')
    else:
        url = "N/A"
    
    image=product.find('img') 
    if image is not None:
        image=image.get('src') 
    else:
        image = "N/A"
    
    print(f'Title: {title}')
    print(f'URL: {url}')
    print(f'Image: {image}')


# In[ ]:


import requests
from bs4 import BeautifulSoup

search_word='tusk'
# URL to scrape
url = f'http://www.rubylane.com/search?q={search_word}&sb=1'
# Send a GET request to the URL and store the response
response = requests.get(url)
# Create a BeautifulSoup object from the response content
soup = BeautifulSoup(response.content, 'html.parser')
# Find all the product containers on the page
products = soup.find_all('div',{'class':'gallery itemlisting hover-container'})

for product in products:
    
    title = product.find('div',{'class':'itemlisting-title'})
    if title is not None:
        title = title.text.strip()
    else:
        title = "N/A"
    
    url = product.find('a')
    if url is not None:
        url = "http://www.rubylane.com"+ url.get('href')
    else:
        url = "N/A"
        
    price = product.find('span')
    if price is not None:
        price = price.text.strip()
    else:
        price = "N/A"
    
    image=product.find('img') 
    if image is not None:
        image=image.get('src') 
    else:
        image = "N/A"
    
    print(f'Title: {title}')
    print(f'URL: {url}')
    print(f'Price: {price}')
    print(f'Image: {image}')


# In[8]:


import requests
from bs4 import BeautifulSoup


search_word='ivory'
# URL to scrape
url = f'https://www.usedcalgary.com/all?q={search_word}'
# Send a GET request to the URL and store the response
response = requests.get(url)
# Create a BeautifulSoup object from the response content
soup = BeautifulSoup(response.content, 'html.parser')
# Find all the product containers on the page
products = soup.find_all('div',{'class':'row used-item bg-light-grey'})

for product in products:
    
    title = product.find('a',{'class':'ad-list-item-link col h6 text-regular'})
    if title is not None:
        title = title.text.strip()
    else:
        title = "N/A"
    
    url = product.find('a')
    if url is not None:
        url = "https://www.usedcalgary.com"+ url.get('href')
    else:
        url = "N/A"

    
    image=product.find('img',{'class':'rounded'}) 
    if image is not None:
        image=image.get('src') 
    else:
        image = "N/A"
    
    print(f'Title: {title}')
    print(f'URL: {url}')
    print(f'Image: {image}')


# In[9]:


import requests
from bs4 import BeautifulSoup

search_word='ivory'
# URL to scrape
stoneforgestudios
    
    print(f'Title: {title}')
    print(f'URL: {url}')
    print(f'Price: {price}')
    print(f'Image: {image}')
    print("\n")


# In[13]:


import requests
from bs4 import BeautifulSoup

search_word='ivory'
# URL to scrape
url = f'https://stoneforgestudios.com/search?q={search_word}'
# Send a GET request to the URL and store the response
response = requests.get(url)
# Create a BeautifulSoup object from the response content
soup = BeautifulSoup(response.content, 'html.parser')
# Find all the product containers on the page
products = soup.find_all('div',{'data-aos':'row-of-'})

for product in products:
    
    title = product.find('div',{'class':'grid-product__title grid-product__title--body'})
    if title is not None:
        title = title.text.strip()
    else:
        title = "N/A"
    
    url = product.find('a',{'class': "grid-product__link"})
    if url is not None:
        url = "https://stoneforgestudios.com"+url.get('href')
    else:
        url = "N/A"
        
    price = product.find('div',{'class':'grid-product__price'})
    if price is not None:
        price = price.text.strip()
    else:
        price = "N/A"
    
    image=product.find('div',{'class':'grid-product__secondary-image small--hide lazyloaded'}) 
    if image is not None:
        image=image.get('src') 
    else:
        image = "N/A"
    
    print(f'Title: {title}')
    print(f'URL: {url}')
    print(f'Price: {price}')
    print(f'Image: {image}')
    print("\n")


# In[ ]:





# In[ ]:





# In[14]:


import requests
from bs4 import BeautifulSoup

search_word='tea'
# URL to scrape
url = f'https://jwteacompany.com/search?q={search_word}'
# Send a GET request to the URL and store the response
response = requests.get(url)
# Create a BeautifulSoup object from the response content
soup = BeautifulSoup(response.content, 'html.parser')
# Find all the product containers on the page
products = soup.find_all('li',{'class':'list-view-item'})

for product in products:
    
    title = product.find('span',{'class':'visually-hidden'})
    if title is not None:
        title = title.text.strip()
    else:
        title = "N/A"
    
    url = product.find('a',{'class': "full-width-link"})
    if url is not None:
        url = "https://jwteacompany.com"+url.get('href')
    else:
        url = "N/A"
        
    price = product.find('div',{'class':'grid-product__price'})
    if price is not None:
        price = price.text.strip()
    else:
        price = "N/A"
    
    image=product.find('img') 
    if image is not None:
        image="https:"+image.get('src') 
    else:
        image = "N/A"
    
    print(f'Title: {title}')
    print(f'URL: {url}')
    print(f'Price: {price}')
    print(f'Image: {image}')
    print("\n")


# In[18]:


import requests
from bs4 import BeautifulSoup

search_word='ivory'
# URL to scrape
url = f'https://www.alibaba.com/trade/search?tab=all&searchText={search_word}'
# Send a GET request to the URL and store the response
response = requests.get(url)
# Create a BeautifulSoup object from the response content
soup = BeautifulSoup(response.content, 'html.parser')
# Find all the product containers on the page
products = soup.find_all('div',{'class':'list-no-v2-outter J-offer-wrapper traffic-product-card'})

for product in products:
    
    title = product.find('p',{'class':'elements-title-normal__content large'})
    if title is not None:
        title =  title.text.strip()
    else:
        title = "N/A"
    
    url = product.find('a',{'class': "list-no-v2-left__img-container"})
    if url is not None:
        url = "https://www." + url.get('href')
    else:
        url = "N/A"
        
    price = product.find('span',{'class':'elements-offer-price-normal__price'})
    if price is not None:
        price = price.text.strip()
    else:
        price = "N/A"
    
    image=product.find('img') 
    if image is not None:
        image="https:"+ image.get('src') 
    else:
        image = "N/A"
    
    print(f'Title: {title}')
    print(f'URL: {url}')
    print(f'Price: {price}')
    print(f'Image: {image}')
    print("\n")


# In[19]:


import requests
from bs4 import BeautifulSoup

search_word='tusk'
# URL to scrape
url = f'https://www.weaverleathersupply.com/search?type=product&options%5Bprefix%5D=last&options%5Bunavailable_products%5D=show&q={search_word}'
# Send a GET request to the URL and store the response
response = requests.get(url)
# Create a BeautifulSoup object from the response content
soup = BeautifulSoup(response.content, 'html.parser')
# Find all the product containers on the page
products = soup.find_all('div',{'class':'product-list product-list--collection'})

for product in products:
    
    title = product.find('a',{'class':'product-item__title text--strong link'})
    if title is not None:
        title =  title.text.strip()
    else:
        title = "N/A"
    
    url = product.find('a',{'class': "product-item__image-wrapper product-item__image-wrapper--with-secondary"})
    if url is not None:
        url = "https://www." + url.get('href')
    else:
        url = "N/A"
        
    price = product.find('span',{'class':'price'})
    if price is not None:
        price = price.text.strip()
    else:
        price = "N/A"
    
    image=product.find('img',{'class':'product-item__primary-image image--fade-in lazyautosizes lazyloaded'}) 
    if image is not None:
        image="https:"+ image.get('srcset') 
    else:
        image = "N/A"
    
    print(f'Title: {title}')
    print(f'URL: {url}')
    print(f'Price: {price}')
    print(f'Image: {image}')
    print("\n")


# In[20]:


import requests
from bs4 import BeautifulSoup

search_word='tusk'
# URL to scrape
url = f'https://www.aliexpress.com/w/wholesale-tusk.html?catId=0&initiative_id=SB_20230323050154&SearchText={search_word}&spm=a2g0o.productlist.1000002.0'
# Send a GET request to the URL and store the response
response = requests.get(url)
# Create a BeautifulSoup object from the response content
soup = BeautifulSoup(response.content, 'html.parser')
# Find all the product containers on the page
products = soup.find_all('a',{'class':'manhattan--container--1lP57Ag cards--gallery--2o6yJVt'})

for product in products:
    
    title = product.find('a',{'class':'manhattan--container--1lP57Ag cards--gallery--2o6yJVt'})
    if title is not None:
        title =  title.text.strip()
    else:
        title = "N/A"
    
    url = product.find('a',{'class': "manhattan--container--1lP57Ag cards--gallery--2o6yJVt"})
    if url is not None:
        url = "https:" + url.get('href')
    else:
        url = "N/A"
        
    price = product.find('div',{'class':'manhattan--price-sale--1CCSZfK'})
    if price is not None:
        price = price.text.strip()
    else:
        price = "N/A"
    
    image=product.find('img',{'class':'manhattan--img--36QXbtQ product-img'}) 
    if image is not None:
        image="https:"+ image.get('src') 
    else:
        image = "N/A"
    
    print(f'Title: {title}')
    print(f'URL: {url}')
    print(f'Price: {price}')
    print(f'Image: {image}')
    print("\n")


# In[ ]:


import requests
from bs4 import BeautifulSoup

search_word='tusk'
# URL to scrape
url = f'https://www.lowtideislanddesign.com/search?q={search_word}&options%5Bprefix%5D=last'
# Send a GET request to the URL and store the response
response = requests.get(url)
# Create a BeautifulSoup object from the response content
soup = BeautifulSoup(response.content, 'html.parser')
# Find all the product containers on the page
products = soup.find_all('ul',{'class':'grid product-grid  grid--2-col-tablet-down grid--4-col-desktop'})

for product in products:
    
    title = product.find('a',{'class':'full-unstyled-link'})
    if title is not None:
        title =  title.text.strip()
    else:
        title = "N/A"
    
    url = product.find('a',{'class': "full-unstyled-link"})
    if url is not None:
        url = "https:" + url.get('href')
    else:
        url = "N/A"
        
    price = product.find('span',{'class':'price-item price-item--regular'})
    if price is not None:
        price = price.text.strip()
    else:
        price = "N/A"
    
    image=product.find('img',{'class':'manhattan--img--36QXbtQ product-img'}) 
    if image is not None:
        image="https:"+ image.get('src') 
    else:
        image = "N/A"
    
    print(f'Title: {title}')
    print(f'URL: {url}')
    print(f'Price: {price}')
    print(f'Image: {image}')
    print("\n")


# In[ ]:


import requests
from bs4 import BeautifulSoup

search_word='ivory'
# URL to scrape
url = f'https://www.allegorygallery.com/search?type=product&q={search_word}'
# Send a GET request to the URL and store the response
response = requests.get(url)
# Create a BeautifulSoup object from the response content
soup = BeautifulSoup(response.content, 'html.parser')
# Find all the product containers on the page
products = soup.find_all('div',{'class':'grid-item search-result large--one-fifth medium--one-third small--one-half'})

for product in products:
    
    title = product.find('p')
    if title is not None:
        title =  title.text.strip()
    else:
        title = "N/A"
    
    url = product.find('a',{'class': "product-grid-item"})
    if url is not None:
        url = "https:" + url.get('href')
    else:
        url = "N/A"
        
    price = product.find('div',{'class':'product-item--price'})
    if price is not None:
        price = price.text.strip()
    else:
        price = "N/A"
    
    image=product.find('img',{'class':'no-js lazyautosizes lazyloaded'}) 
    if image is not None:
        image="https:"+ image.get('srcset') 
    else:
        image = "N/A"
    
    print(f'Title: {title}')
    print(f'URL: {url}')
    print(f'Price: {price}')
    print(f'Image: {image}')
    print("\n")


# In[ ]:


import requests
from bs4 import BeautifulSoup

search_word='ivory'
# URL to scrape
url = f'https://www.opalauctions.com/search?oa.auctions%5Bquery%5D={search_word}'
# Send a GET request to the URL and store the response
response = requests.get(url)
# Create a BeautifulSoup object from the response content
soup = BeautifulSoup(response.content, 'html.parser')
# Find all the product containers on the page
products = soup.find_all('li',{'class':'ais-Hits-item'})

for product in products:
    
    title = product.find('a',{'class':'flex-grow-0 flex-shrink-0 text-sm text-left text-[#1c87c3] visited:text-purple-800 hover:underline'})
    if title is not None:
        title =  title.text.strip()
    else:
        title = "N/A"
    
    url = product.find('a',{'class': "flex-grow-0 flex-shrink-0 text-sm text-left text-[#1c87c3] visited:text-purple-800 hover:underline"})
    if url is not None:
        url = "https:" + url.get('href')
    else:
        url = "N/A"
        
    price = product.find('div',{'class':'product-item--price'})
    if price is not None:
        price = price.text.strip()
    else:
        price = "N/A"
    
    image=product.find('img',{'class':'w-full h-full object-cover'}) 
    if image is not None:
        image="https:"+ image.get('src') 
    else:
        image = "N/A"
    
    print(f'Title: {title}')
    print(f'URL: {url}')
    print(f'Price: {price}')
    print(f'Image: {image}')
    print("\n")


# In[20]:


import requests
from bs4 import BeautifulSoup

search_word='ivory'
# URL to scrape
url = f'https://www.safariworkstaxidermysales.com/search?type=product&q={search_word}'
# Send a GET request to the URL and store the response
response = requests.get(url)
# Create a BeautifulSoup object from the response content
soup = BeautifulSoup(response.content, 'html.parser')
# Find all the product containers on the page
products = soup.find_all('div',{'itemprop':'itemListElement'})

for product in products:
    
    title = product.find('span',{'class':'title'})
    if title is not None:
        title =  title.text.strip()
    else:
        title = "N/A"
    
    url = product.find('a')
    if url is not None:
        url = url.get('href')
    else:
        url = "N/A"
        
    price = product.find('meta',{'itemprop':'price'})
    if price is not None:
        price = price.text.strip()
    else:
        price = "N/A"
    
    image=product.find('img') 
    if image is not None:
        image="https:"+ image.get('src') 
    else:
        image = "N/A"
    
    print(f'Title: {title}')
    print(f'URL: {url}')
    print(f'Price: {price}')
    print(f'Image: {image}')
    print("\n")


# In[21]:


import requests
from bs4 import BeautifulSoup

search_word='ivory'
# URL to scrape
url = f'https://clintorms.com/search?type=product&q={search_word}'
# Send a GET request to the URL and store the response
response = requests.get(url)
# Create a BeautifulSoup object from the response content
soup = BeautifulSoup(response.content, 'html.parser')
# Find all the product containers on the page
products = soup.find_all('div',{'data-initial-width':'one-third'})

for product in products:
    
    title = product.find('span',{'class':'thumbnail__title'})
    if title is not None:
        title =  title.text.strip()
    else:
        title = "N/A"
    
    url = product.find('a')
    if url is not None:
        url = "https://clintorms.com/" + url.get('href')
    else:
        url = "N/A"
        
    price = product.find('span',{'class':'money'})
    if price is not None:
        price = price.text.strip()
    else:
        price = "N/A"
    
    image=product.find('img') 
    if image is not None:
        image="https:"+ image.get('data-src') 
    else:
        image = "N/A"
    
    print(f'Title: {title}')
    print(f'URL: {url}')
    print(f'Price: {price}')
    print(f'Image: {image}')
    print("\n")


# In[ ]:


import requests
from bs4 import BeautifulSoup

search_word='ivory'
# URL to scrape
url = f'https://www.overland.com/filter?qr={search_word}'
# Send a GET request to the URL and store the response
response = requests.get(url)
# Create a BeautifulSoup object from the response content
soup = BeautifulSoup(response.content, 'html.parser')
# Find all the product containers on the page
products = soup.find_all('div',{'class':'col-6 col-md-4 col-xxl-3 product-item'})

for product in products:
    
    title = product.find('div',{'class':'product-name'})
    if title is not None:
        title =  title.text.strip()
    else:
        title = "N/A"
    
    url = product.find('a',{'class':'product-link'})
    if url is not None:
        url = url.get('href')
    else:
        url = "N/A"
        
    price = product.find('div',{'class':'priceNum'})
    if price is not None:
        price = price.text.strip()
    else:
        price = "N/A"
    
    image=product.find('img',{'class':'main-image'}) 
    if image is not None:
        image="https:"+ image.get('src') 
    else:
        image = "N/A"
    
    print(f'Title: {title}')
    print(f'URL: {url}')
    print(f'Price: {price}')
    print(f'Image: {image}')


# In[1]:


import requests
from bs4 import BeautifulSoup

search_word = input("Enter your value: ")

url = f"https://www.etsy.com/search?q={search_word}&ref=search_bar"

# send a request to the URL and get the page content
response = requests.get(url)
# content = response.content

# create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# find all the listings on the page
listings = soup.find_all("div", {"class": "v2-listing-card"})

# loop through each listing and extract the title, price, and URL
for listing in listings:
    # get the title and URL
    title = listing.find("h3", {"class": "v2-listing-card__title"}).text.strip()
    
    url_elem = listing.find("a", {"class": "listing-link"})
    if url_elem:
        url = url_elem.get("href")
    else:
        url = "N/A"
    # get the price, if available
    if listing.find("span", {"class": "currency-value"}):
        price = listing.find("span", {"class": "currency-value"}).text
    else:
        price = "N/A"
    
    
    image=listing.find('img')
    if image is not None:
        image=image.get('src') 
        
    # print the title, price, and URL
    print(title)
    print(price)
    print(url)
    print(f'image: {image}')
    print("--------------------")

    
    
import requests
from bs4 import BeautifulSoup

search_word='ivory'
# URL to scrape
url = f'https://www.canadianlisted.com/{search_word}/listing'
# Send a GET request to the URL and store the response
response = requests.get(url)
# Create a BeautifulSoup object from the response content
soup = BeautifulSoup(response.content, 'html.parser')
# Find all the product containers on the page
products = soup.find_all('div', {'class': 'itemclbox'})

for product in products:
    # Extract the title, price, URL and image of each product, handling cases where they are not present
  
  
    title = product.find('div',{'class' :'salecladtop'})
    if title is not None:
        title = title.text.strip()
    else:
        title = "N/A"
        
    price = product.find('span', {'class': 'bold'})
    if price is not None:
        price = price.text.strip()

    url = product.find('a')
    if url is not None:
        url = url.get('href')
    else:
        url = "N/A"
    
    image=product.find('img') 
    if image is not None:
        image="https:"+image.get('src') 
    else:
        image = "N/A"
        

    # Print the title, price, URL and image of each product
    print(f'Title: {title}')
    print(f'URL: {url}')
    print(f'Image: {image}')


# URL to scrape
url = f'https://www.chairish.com/search?q={search_word}'
# Send a GET request to the URL and store the response
response = requests.get(url)
# Create a BeautifulSoup object from the response content
soup = BeautifulSoup(response.content, 'html.parser')
# Find all the product containers on the page
products = soup.find_all('div', {'class': 'grid-product-menu-wrapper js-grid-product-menu-wrapper'})
#s-item__wrapper clearfix
# Loop through each product container and extract the title, price and URL
for product in products:
    # Extract the title, price and URL of each product, handling cases where they are not present
    titles = product.find('h3', {'class': 'product-title'}).text
    price = product.find('span', {'class': 'product-price-value'})
    if price is not None:
        price = price.text.strip()

    url = product.find('a', {'class': 'product-link'})
    if url is not None:
        url = url.get('href')
    
    image=product.find('img')
    if image is not None:
        image=image.get('src') 

    # Print the title, price and URL of each product
    print(f'Title:{titles}')
    print(f'Price: {price}')
    print(f'URL: {url}')
    print(f'image: {image}', "\n")

    
    

# URL to scrape
url = f'https://www.ebay.com/sch/i.html?_nkw={search_word}'
# Send a GET request to the URL and store the response
response = requests.get(url)
# Create a BeautifulSoup object from the response content
soup = BeautifulSoup(response.content, 'html.parser')
# Find all the product containers on the page
products = soup.find_all('div', {'class': 's-item__wrapper clearfix'})
#s-item__wrapper clearfix
# Loop through each product container and extract the title, price and URL
for product in products:
    # Extract the title, price and URL of each product, handling cases where they are not present
    titles = product.find('div', {'class': 's-item__title'})
    for title in titles:
        title = titles.find('span').text

    price = product.find('span', {'class': 's-item__price'})
    if price is not None:
        price = price.text.strip()

    url = product.find('a', {'class': 's-item__link'})
    if url is not None:
        url = url.get('href')
    
    image=product.find('img')
    if image is not None:
        image=image.get('src') 

    # Print the title, price and URL of each product
    print(f'Title: {title}')
    print(f'Price: {price}')
    print(f'URL: {url}')
    print(f'image: {image}')



import requests
from bs4 import BeautifulSoup

search_word='ivory'
url = f'https://www.gumtree.com.au/s-antiques-art-collectables/{search_word}/k0c18297r10?categoryRedirected=true'
response = requests.get(url)

# parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# find all the items displayed on the page
products = soup.find_all('div', {'class': 'user-ad-collection-new-design__wrapper--row'})

for product in products:
    url = product.find('a')
    if url is not None:
        url = "https://www.gumtree.com.au/"+url.get('href')
    
    image=product.find('img')
    if image is not None:
        image=image.get('data-src') 
    
    title = product.find('span',{'class' :'user-ad-row-new-design__title-span'})
    if title is not None:
        title = title.text.strip()
    else:
        title = "N/A"
    
    price = product.find('span', {'class': 'user-ad-price-new-design__price'})
    if price is not None:
        price = price.text.strip()

    print(f'Title: {title}')
    print(f'Price: {price}')
    print(f'URL: {url}')
    print(f'Image: {image}')
    
import requests
from bs4 import BeautifulSoup

search_word='ivory'
# URL to scrape
url = f'https://www.preloved.co.uk/search?keyword={search_word}'
# Send a GET request to the URL and store the response
response = requests.get(url)
# Create a BeautifulSoup object from the response content
soup = BeautifulSoup(response.content, 'html.parser')
# Find all the product containers on the page
products = soup.find_all('li', {'class': 'search-result'})

for product in products:
    title = product.find('h2')
    if title is not None:
        title = title.text.strip()
    else:
        title = "N/A"
        
    price = product.find('span', {'class': 'search-result__meta bold t-color--2-2 u-capitalize is-price'})
    if price is not None:
        price = price.text.strip()
        
    url = product.find('a')
    if url is not None:
        url = url.get('href')
    else:
        url = "N/A"
        
    image=product.find('img') 
    if image is not None:
        image=image.get('data-src') 
    else:
        image = "N/A"
        
    print(f'URL: {url}')
    print(f'Title: {title}')
    print(f'Price: {price}')
    print(f'Image: {image}')
    

import requests
from bs4 import BeautifulSoup

search_word='ivory'
# URL to scrape
url = f'https://www.thetaxidermystore.com/catalogsearch/result/?cat=0&q={search_word}'
# Send a GET request to the URL and store the response
response = requests.get(url)
# Create a BeautifulSoup object from the response content
soup = BeautifulSoup(response.content, 'html.parser')
# Find all the product containers on the page
products = soup.find_all('div', {'class': 'item first'})

for product in products:
    title = product.find('h2')
    if title is not None:
        title = title.text.strip()
    else:
        title = "N/A"
    
    url = product.find('a')
    if url is not None:
        url = url.get('href')
    else:
        url = "N/A"
        
    price = product.find('span', {'class': 'price'})
    if price is not None:
        price = price.text.strip()
    
    image=product.find('img') 
    if image is not None:
        image=image.get('src') 
    else:
        image = "N/A"
    
        
    print(f'URL: {url}')
    print(f'Title: {title}')
    print(f'Price: {price}')
    print(f'Image: {image}')


import requests
from bs4 import BeautifulSoup

search_word='ivory'
# URL to scrape
url = f'https://picclick.com/?q={search_word}'
# Send a GET request to the URL and store the response
response = requests.get(url)
# Create a BeautifulSoup object from the response content
soup = BeautifulSoup(response.content, 'html.parser')
# Find all the product containers on the page
products = soup.find_all('li', {'class':'amazon'})


for product in products:
    
    title = product.find('h3')
    if title is not None:
        title = title.text.strip()
    else:
        title = "N/A"
        
    url = product.find('a')
    if url is not None:
        url = url.get('href')
    else:
        url = "N/A"
        
    price = product.find('div', {'class': 'price'})
    if price is not None:
        price = price.text.strip()
        
    image=product.find('img') 
    if image is not None:
        image=image.get('src') 
    else:
        image = "N/A"
        
        
    print(f'Title: {title}')
    print(f'URL: {url}')
    print(f'Price: {price}')
    
    print(f'Image: {image}')
    
import requests
from bs4 import BeautifulSoup

search_word='ivory'
# URL to scrape
url = f'https://www.1stdibs.com/search/?q={search_word}'
# Send a GET request to the URL and store the response
response = requests.get(url)
# Create a BeautifulSoup object from the response content
soup = BeautifulSoup(response.content, 'html.parser')
# Find all the product containers on the page
products = soup.find_all('div', {'class':'_10b2665f _b88c87ca _6dba19f'})


for product in products:
    
    title = product.find('div',{'class':'_16da7886'})
    if title is not None:
        title = title.text.strip()
    else:
        title = "N/A"
        
    url = product.find('a',{'class':'_9e04a611 _9f85bf45 _f7a3e2b1'})
    if url is not None:
        url = "https://www.1stdibs.com/"+ url.get('href')
    else:
        url = "N/A"
        
    price = product.find('div', {'class': '_60451376'})
    if price is not None:
        price = price.text()
        
    image=product.find('img') 
    if image is not None:
        image=image.get('src') 
    else:
        image = "N/A"
        
        
    print(f'Title: {title}')
    print(f'URL: {url}')
    print(f'Price: {price}')
    print(f'Image: {image}')
    
import requests
from bs4 import BeautifulSoup

search_word='tusk'
# URL to scrape
url = f'https://www.boneroom.com/apps/search?q={search_word}'
# Send a GET request to the URL and store the response
response = requests.get(url)
# Create a BeautifulSoup object from the response content
soup = BeautifulSoup(response.content, 'html.parser')
# Find all the product containers on the page
products = soup.find_all('li', {'id':'wsite-search-product-result-section'})

for product in products:
    
    title = product.find('span',{'class':'wsite-search-product-name'})
    if title is not None:
        title = title.text.strip()
    else:
        title = "N/A"
    
    url = product.find('a')
    if url is not None:
        url = "https://www.boneroom.com"+url.get('href')
    else:
        url = "N/A"
    
    price = product.find('span', {'class': 'wsite-search-product-price'})
    if price is not None:
        price = price.text.strip()
    else:
        price = "N/A"
    
    image=product.find('a',{'class':'cloud-zoom'}) 
    if image is not None:
        image=image.get('href') 
    else:
        image = "N/A"
    
    print(f'Title: {title}')
    print(f'URL: {url}')
    print(f'Price: {price}')
    print(f'Image: {image}')
    
    
# URL to scrape
url = f'https://www.trademe.co.nz/a/search?search_string={search_word}'

# Send a GET request to the URL and store the response
response = requests.get(url)

# Create a BeautifulSoup object from the response content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the product containers on the page
# products = soup.find('div', {'class': 'tm-search__two-col-grid l-container'})

titles=[]
images=[]
prices=[]
urls=[]
# Find the URL of the product
for url in soup.find_all('a', {'class': 'tm-marketplace-search-card__detail-section tm-marketplace-search-card__detail-section--link'}):
    url = 'https://www.trademe.co.nz/a/' + url['href']
    urls.append(url)
         
for title in soup.find_all("div", class_="tm-marketplace-search-card__title"):
    titles.append(title.text.strip())

for image in soup.find_all('img', {'class': 'marketplace-summary-image-lazy-loader__thumbnail contain ng-star-inserted'}):
    images.append(image['src'])
    
for price in soup.find_all('div', {'class': 'tm-marketplace-search-card__price ng-star-inserted'}):
    prices.append(price.text.strip())

for i in range(len(images)):
    print([titles[i],
           images[i], 
           prices[i], 
           urls[i]])
    


# In[ ]:




