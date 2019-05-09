# TSP_web_scraping_and_visualization_in_map

This repository provides a solution for travelling salesman problem (TSP) which takes original city names in form of an excel sheet. The current program takes the cities from India only and shows the resulting optimal travelling path on a map.

The program used ```selenium``` based web-automation to find the distance among cities from the website <https://www.distancecalculator.net/>. To plot the result on India map the latitude and longitude values of the cities are required. The latitude and longitude values are acquired using the ```MapQuest API```. 

### Prerequisite Installation

- pip install numpy

- pip install pandas

- pip install selenium

- pip install bs4

- pip install tsp

- pip install tqdm

- pip install matplotlib

- pip install mapq

- install **chromedriver** which can be downloaded from <http://chromedriver.chromium.org/>

  - [Installing ChromeDriver on macOS - Chris Kenst](https://www.kenst.com/2015/03/installing-chromedriver-on-mac-osx/) 

    ```
    ==> Satisfying dependencies
    ==> Downloading https://chromedriver.storage.googleapis.com/74.0.3729.6/chromedr
    ######################################################################## 100.0%
    ==> Verifying SHA-256 checksum for Cask 'chromedriver'.
    ==> Installing Cask chromedriver
    ==> Linking Binary 'chromedriver' to '/usr/local/bin/chromedriver'.
    
    ```

    

    
