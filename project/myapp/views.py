from django.shortcuts import render

# Create your views here.

# def display_results(request):
#     result = "Hello, Django!"
#     return render(request, 'results.html', {'result': result})

import requests
from bs4 import BeautifulSoup

def search_results(request):
    if request.method == 'POST':
        search_word = request.POST['search_word']
        source = request.POST['source']
        results = []

        if source == "etsy":
            url = f"https://www.etsy.com/search?q={search_word}&ref=search_bar"
            response = requests.get(url)
            content = response.content
            soup = BeautifulSoup(content, "html.parser")
            listings = soup.find_all("div", {"class": "v2-listing-card"})

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

                results.append({
                    "title": title,
                    "price": price,
                    "url": url,
                    "image": image
                })

        elif source == "canadianlisted":
            url = f'https://www.canadianlisted.com/{search_word}/listing'
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
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
            
                results.append({
                    "title": title,
                    "price": price,
                    "url": url,
                    "image": image
                })
                
        elif source=="auctionzip":
            
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
                    
                results.append({
                "title": title,
                "price": price,
                "url": url,
                "image": image
                })
        elif source=="picclick":
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
            
                results.append({
                "title": title,
                "price": price,
                "url": url,
                "image": image
                })
                   
        elif source=="UKClassifieds":
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
                    
                results.append({
                "title": title,
                "price": price,
                "url": url,
                "image": image
                })

        elif source=="taxidermystore":
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
                    
                results.append({
                "title": title,
                "price": price,
                "url": url,
                "image": image
                })
                
        elif source=="1stdibs":
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
                
                results.append({
                "title": title,
                "price": price,
                "url": url,
                "image": image
                })

        elif source=="boneroom":
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
                
                results.append({
                "title": title,
                "price": price,
                "url": url,
                "image": image
                })
                
        elif source=="trocadero":
            url = f'https://www.trocadero.com/directory/search.php?keyword={search_word}&archinsearch=yes&click_to_search_now.x=0&click_to_search_now.y=0&category=ALL+ITEMS&period=No+Selection&order=Most+Recent&item=&numitem=15&listtype=thumb'            
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

                results.append({
                        "title": title,
                        "price": price,
                        "url": url,
                        "image": image
                        })   
        
        elif source=="rubylane":
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

                results.append({
                    "title": title,
                    "price": price,
                    "url": url,
                    "image": image
                    })

                
                
        elif source=="gumtree":
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
                results.append({
                    "title": title,
                    "price": price,
                    "url": url,
                    "image": image
                    })
                
                    
        elif source=="usedcalgary":
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
                    
                results.append({
                    "title": title,
                    "price": None,
                    "url": url,
                    "image": image
                    })

        elif source=="ecrater":
            url = f'https://www.ecrater.com/filter.php?keywords={search_word}'
            # Send a GET request to the URL and store the response
            response = requests.get(url)
            # Create a BeautifulSoup object from the response content
            soup = BeautifulSoup(response.content, 'html.parser')
            # Find all the product containers on the page
            products = soup.find_all('li',{'class':'product-item'})

            for product in products:

                title = product.find('h2')
                if title is not None:
                    title = title.text.strip()
                else:
                    title = "N/A"

                url = product.find('a')
                if url is not None:
                    url = "https://www.ecrater.com"+ url.get('href')
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
                
                results.append({
                    "title": title,
                    "price": price,
                    "url": url,
                    "image": image
                    })
                
        elif source=="stoneforgestudios":
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
                results.append({
                    "title": title,
                    "price": price,
                    "url": url,
                    "image": image
                    })
                
        elif source=="jwteacompany":
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
                
                results.append({
                    "title": title,
                    "price": price,
                    "url": url,
                    "image": image
                    })
                
        elif source=="ebay":
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


                    
                results.append({
                    "title": title,
                    "price": price,
                    "url": url,
                    "image": image
                    })
                    
        elif source=="chairish":
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
            
                results.append({
                    "title": titles,
                    "price": price,
                    "url": url,
                    "image": image
                    })
                
        elif source=="weaverleathersupply":
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
                results.append({
                    "title": title,
                    "price": price,
                    "url": url,
                    "image": image
                    })
                
        elif source=="aliexpress":   
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
                    
                results.append({
                    "title": title,
                    "price": price,
                    "url": url,
                    "image": image
                    })
        elif source=="allegorygallery":
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
                
                results.append({
                    "title": title,
                    "price": price,
                    "url": url,
                    "image": image
                    })  
                
        elif source=="safariworkstaxidermysales":
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
                    
                results.append({
                    "title": title,
                    "price": price,
                    "url": url,
                    "image": image
                    })
                
        elif source=="clintorms":
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
                
                results.append({
                    "title": title,
                    "price": price,
                    "url": url,
                    "image": image
                    })

        return render(request, 'results.html', {'results': results})

    return render(request, 'search.html')
