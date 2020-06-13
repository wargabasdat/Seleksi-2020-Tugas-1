// Import modules
const internetPage = require('./internetstats');
const speedPage = require('./speedtest')
const puppeteer = require('puppeteer');
const fs = require("fs");

// FUnctions to get resulst from other module
const getInternetResult = async (page, region, link) => {
    await page.init(link);
    return page.parseResult(region);
};

const getSpeedResult = async (page, type, link) => {
    await page.init(link);
    return page.parseResult(type);
};

(async () => {
    const browser = await puppeteer.launch({
        headless: true,
        ignoreHTTPSErrors: true});

    console.log('Scraping from 2 websites...');

    // Scrape from internetworldstats.com
    const asia = new internetPage(browser);
    const america = new internetPage(browser);
    const africa = new internetPage(browser);
    const europe = new internetPage(browser);
    const eunion = new internetPage(browser);
    const mideast = new internetPage(browser);
    const oceania = new internetPage(browser);

    // 5 different web pages
    const asiaResult = getInternetResult(asia, 'Asia', 'https://www.internetworldstats.com/stats3.htm#asia');
    const americaResult = getInternetResult(america, 'America', 'https://www.internetworldstats.com/stats2.htm#americas');
    const africaResult = getInternetResult(africa, 'Africa', 'https://www.internetworldstats.com/stats1.htm');
    const europeResult = getInternetResult(europe, 'Europe', 'https://www.internetworldstats.com/stats4.htm#europe');
    const eunionResult = getInternetResult(eunion, 'European Union', 'https://www.internetworldstats.com/stats9.htm');
    const mideastResult = getInternetResult(mideast, 'Middle East', 'https://www.internetworldstats.com/stats5.htm#me');
    const oceaniaResult = getInternetResult(oceania, 'Oceania', 'https://www.internetworldstats.com/stats6.htm');
    
    let internetData = [];
    await Promise.all([asiaResult, americaResult, africaResult, europeResult, eunionResult, mideastResult, oceaniaResult]).then((values) => {
        internetData = [].concat.apply([], values);
    })

    // Scrape from speedtest.com
    const broadband = new speedPage(browser);
    const mobile = new speedPage(browser);

    // Get mobile and broadband speed from every country available
    const broadbandRes = getSpeedResult(broadband, 'broadband', 'https://www.speedtest.net/global-index');
    const mobileRes = getSpeedResult(mobile, 'mobile', 'https://www.speedtest.net/global-index');

    // Wait until all process have done asynchronously
    await Promise.all([broadbandRes, mobileRes]).then((values) => {

        // Merged mobile and brodband speed based on country name
        let speedData = values[0].map((el) => {
            const idx = values[1].map(el2 => el2.name).indexOf(el.name);
            if (idx != -1) {
                el.broadband_speed = parseFloat(el.broadband_speed);
                el.mobile_speed = parseFloat(values[1][idx].broadband_speed)
            } else{
                el.mobile_speed = null;
            }
            return el;
        })

        // Merged data internet stats (internetworldstats.com) and internet speed data (speedtest.com)
        // Data cleaning removes countries that do not have internet speed data
        let finalData = internetData.filter((el3) => {
            const idx2 = speedData.map(el4 => el4.name).indexOf(el3.name);
            if (idx2 != -1){

                // Parsing some string data type to integer or float
                delete speedData[idx2].name;
                el3.penetration = parseFloat(el3.penetration.replace(' %', ''));
                el3.usersInRegion = parseFloat(el3.usersInRegion.replace(' %', ''));
                el3.population = parseInt(el3.population.replace(/,/g,''));
                el3.internetUsers = parseInt(el3.internetUsers.replace(/,/g,''));
                el3.facebookSubs = parseInt(el3.facebookSubs.replace(/,/g,''));
                el3.speed_data = speedData[idx2];
                return el3;
            }
        });

        // Write Array of Object to .json file
        fs.writeFile(`${__dirname}/../data/data.json`, JSON.stringify(finalData, null, 3), 'utf8' ,function(err) {
            if (err) throw err;
            console.log("Saved!");
            browser.close();
        });
    })
    
})();


