# Ethereum Block data scrape

[![N|Solid](https://miro.medium.com/max/1200/1*YJNS0JVl7RsVDTmORGZ6xA.png)](https://scrapy.org/)

This script written in python with the help of scrapy framework help's us to scrape Ethereum Block data. Every Minute or may be less than that, a new block is added to ethereum network. So they are millions of blocks in the network.

 
###### I have uploaded the data having nearly 4.3M+ Ethereum Block data. The link to dataset is [here](https://www.kaggle.com/muhammedabdulazeem/ethereum-block-data) 


## Installation

It requires [Scrapy](https://scrapy.org/) v1+ to run.

Install the dependencies and devDependencies and start the server.

```sh
pip install scrapy
```

Then clone this repo and 

```sh
cd Ethereum-Block-data
scrapy crawl eth
```

and if you want to save this record into csv then run the below command

```sh
scrapy crawl eth -o results.csv
```

or

```sh
scrapy crawl eth -o results.json
```

**WARNING:** Please beware while you are running. This script may take hours to scrape the data because it has millions of records. Uncomment the code written in ethereum/spiders/eth.py before running the script.