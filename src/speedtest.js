const puppeteer = require('puppeteer');

// Scrape from speedtest.com
class speedPage {
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
            waitUntil: 'networkidle2',
          });

        await this.page.setViewport({
            width: 1300,
            height: 5000,
          });
      
    }

    // Parse data from webpage
    async parseResult(type){
        console.log(`Scraping ${type} speed`)
        const elements = this.elements;

        let extractor = await this.page.evaluate((elements, type) => {
            let nameNode;
            let speedNode;
            let infoArray = [];
            
            if (type == 'broadband'){
                nameNode = document.querySelectorAll(elements.nameBroadband);
                speedNode = document.querySelectorAll(elements.broadband);
            }
            else {
                nameNode = document.querySelectorAll(elements.nameMobile);
                speedNode = document.querySelectorAll(elements.mobile);
            }

            // Save data to country object
            for (let i = 0; i < nameNode.length; i++){
                let country = null;
                country = {
                    name: nameNode[i].innerText.trim(),
                    broadband_speed: speedNode[i].innerText,
                    url: nameNode[i].href
                }
                infoArray.push(country);
            }

            return infoArray;
        }, elements, type);

        // Return parse result
        return extractor;
    }

    // Selectors from the webpage
    getSelector(){
        const elements = {
            nameBroadband: `#column-fixed a`,
            broadband: `#column-fixed .results .speed`,
            nameMobile: `#column-mobile a`,
            mobile: `#column-mobile .results .speed`
        }
        return elements;
    }

}

// Export to index.js
module.exports = speedPage;