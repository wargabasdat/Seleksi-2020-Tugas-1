const puppeteer = require('puppeteer');

// Scrape from speedtest.com
class wikiPage {
    constructor(browser){
        this.elements = null;
        this.browser = browser;
        this.page = null;
    }
    
    // Get data from page
    async init(url) {
        this.elements = await this.getSelector();
        this.page = await this.browser.newPage();

        // Wait until page fully loaded
        await this.page.goto(url, {
            waitUntil: 'networkidle0',
          });

        await this.page.setViewport({
            width: 1300,
            height: 5000,
          });
      
    }

    // Parse data from webpage
    async parseResult(){
        console.log(`Scraping GNI (nominal) per capita speed`)
        const elements = this.elements;

        let extractor = await this.page.evaluate((elements) => {
            let nameNode;
            let gniNode;
            let infoArray = [];
            
            nameNode = document.querySelectorAll(elements.nameCountry);
            gniNode = document.querySelectorAll(elements.GNICountry);

            replaceName= (str) => {
              let res = str.replace('Myanmar', 'Republic of the Union of Myanmar')
              res = res.replace('Bahamas', 'The Bahamas')
              res = res.replace('Republic of the Congo', 'Congo')
              res = res.replace('Gambia', 'The Gambia')
              return res
            }  

            // Save data to country object
            for (let i = 0; i < gniNode.length; i++){
                let country = null;
                let j = 0;
                (i >= 8) ? j = i+2 : j =1
                
                let name = replaceName(nameNode[j].innerText);
                let GNI = gniNode[i].textContent.replace(',','')
                country = {
                    name, GNI
                }
                infoArray.push(country);
            }
      

            return infoArray;
        }, elements);

        // Return parse result
        return extractor;
    }

    // Selectors from the webpage
    getSelector(){
        const elements = {
            nameCountry: `#content-collapsible-block-1 .wikitable td a`,
            GNICountry: `td:nth-child(3)`
        }
        return elements;
    }
}

// Export to index.js
module.exports = wikiPage;