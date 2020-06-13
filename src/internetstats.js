const puppeteer = require('puppeteer');

// Scrape from internetworldstats.com
class internetPage {
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
    async parseResult(region){
        const elements = this.elements;
        console.log(`Scraping ${region}`)

        let extractor = await this.page.evaluate((elements, region) => {
            window.scrollBy(0, window.innerHeight);
            let infoArray = [];
            let rowArrList = null; 
            const idx = {};

            // Parse based on region
            if (region == 'Asia' || region == 'America' || region == 'Africa' || region == 'Middle East' || region == 'Oceania'){
                idx.internetUsers = 3;
                idx.penetration = 4;
                idx.usersInRegion = 5;
                idx.facebookSubs = 6;
                if (region == 'Asia' || region == 'Middle East') {
                    idx.from = 2;
                    rowArrList =  Array.from(document.querySelectorAll(elements.rowAsiaMidEastSelector));
                    idx.to = rowArrList.length - 3;
                    if (region == 'Middle East') idx.to = rowArrList.length - 4;
                }
                else if (region == 'America'){
                    idx.from = 3;
                    rowArrList =  Array.from(document.querySelectorAll(elements.rowAmericaEuropeSelector));
                    idx.to = rowArrList.length - 2;
                }
                else if (region == 'Africa') {
                    idx.from = 2;
                    rowArrList =  Array.from(document.querySelectorAll(elements.rowAfricaSelector));
                    idx.to = rowArrList.length - 4;
                }
                else if (region == 'Oceania'){
                    idx.from = 2;
                    rowArrList =  Array.from(document.querySelectorAll(elements.rowOceaniaSelector));
                    idx.to = rowArrList.length - 2;
                }
            }
            else if (region == 'Europe' || region == 'European Union'){
                idx.internetUsers = 2;
                idx.penetration = 3;
                idx.usersInRegion = 4;
                idx.facebookSubs = 5;

                if (region == 'Europe') {
                    idx.from = 2;
                    rowArrList =  Array.from(document.querySelectorAll(elements.rowAmericaEuropeSelector));
                    idx.to = rowArrList.length - 2;
                }
                else if (region == 'European Union'){
                    idx.from = 6;
                    rowArrList =  Array.from(document.querySelectorAll(elements.rowEUSelector));
                    idx.to = rowArrList.length - 3;
                }
            }

            // Cleaning data and string matching from 2 different websites
            replaceName = (str) => {
                let res = str.replace('(SAR)', '');
                res = res.replace('*', '');
                res = res.replace('Afganistan', 'Afghanistan');
                res = res.replace('Korea, South','South Korea');
                res = res.replace('Kyrgystan','Kyrgyzstan');
                res = res.replace('Macao','Macau');
                res = res.replace('Republic of the Union of ','');
                res = res.replace('&','and');
                res = res.replace('Bahamas','The Bahamas');
                res = res.replace('St. Kitts & Nevis','Saint Kitts and Nevis');
                res = res.replace('St. Vincent & Grenadines','Saint Vincent and the Grenadines');
                res = res.replace('Gambia','The Gambia');
                res = res.replace('Bosnia-Herzegovina','Bosnia and Herzegovina');
                res = res.replace(' (State of)','');
                res = res.replace('Papau','Papua');
                return res;
            };

            // Save data to country object
            for (let i = idx.from; i < idx.to; i++){
                let name = replaceName(rowArrList[i].cells[0].innerText);
                let country = {
                    name, region,
                    population: rowArrList[i].cells[1].innerText,
                    internet_users: rowArrList[i].cells[idx.internetUsers].innerText,
                    penetration: rowArrList[i].cells[idx.penetration].innerText,
                    users_region: rowArrList[i].cells[idx.usersInRegion].innerText,
                    facebook_subs: rowArrList[i].cells[idx.facebookSubs].innerText,
                }
                infoArray.push(country);
            }

            return infoArray;
        }, elements, region);
        
        // Return parse result
        return extractor;
    }

    // Seelctors from the webpage
    getSelector(){
        const elements = {
            rowAsiaMidEastSelector: `td td tr`,
            rowAmericaEuropeSelector: `p+ table tr`,
            rowAfricaSelector: `p+ table table tr`,
            rowEUSelector: `table:nth-child(2) tr`,
            rowOceaniaSelector: `center center tr`,
        }
        return elements;
    }
}

// Export to index.js
module.exports = internetPage;