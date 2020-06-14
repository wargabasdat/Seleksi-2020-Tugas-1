## US Hospital

![acmh](/screenshot/ACMH.jpg)
US Hospital: ACMH <br/>
source: http://www.cvexcel.org/AccreditedFacilitiesdetails.aspx?cid=f843fdaa-5592-405a-a569-71788cd564a9


### Table of Contents

This README.md contains the following:

- [Description](#description)
- [Specification](#specification)
- [How to use](#how-to-use)
- [JSON Structure](#json-structure)
- [Screenshot](#screenshot)
- [Reference](#reference)
- [Author](#author)


## Description

In US, hospitals have their grade every 6 months. The grade determined by scores in 5 aspects: Infections, Problem with Surgery, Practices to Prevent Error, Safety Problems, and Doctor, Nurse & Hospital Staff. This is a project to scrap grade information from US Hospital published in www.hospitalsafetygrade.org using Pyhton 3.   


## Specification

We will need the following library to run the code in this project:

- ##### TQDM
```
pip install tqdm
```
Scraping takes a lot of time. In order to know whether our code is running or our computer has crashed, we will use TQDM. TQDM will show progress bar for a loop in our code, so we will know how far the loop has run.
- ##### BeautifulSoup
```
pip install beautifulsoup4
```
There are some tools in Python to help the user when scraping webiste. In this project, we will use Beautifulsoup because it is user friendly and easy to understand.
- ##### Urllib
```
pip install urllib3
```
We will use urllib library to grab the HTML of webistes.
- ##### Time
In this project, we will grab HTML from many websites. In order to not crashing the server, we will put our program to sleep in each loop using Sleep() from Time library. Time library is standard library in Python so it is already installed along with Python.
- ##### JSON
Scraped data will be stored in JSON format. To dump the data into json, we will use JSON library. JSON is also standard library in Python so it is already insalled along with Python.
- ##### Threading
Scraping takes a lot of time. In order to reduce the time taken in scraping, we can implement multithreading in our code. To implement multithreading, we need Threading library. Threading is also standard library in Python so it is already installed along with Python.
- ##### Jupyter Notebook
```
pip install notebook
```
The codes are in .ipynb. We can use Jupyter Notebook to open and run this code.


## How to Use

Before we get started, make sure you have a stable internet connection to prevent error when running the code. <br/> <br/>

1. Clone this repository to your local directory. 
```
git clone https://github.com/KevinCahyadiGiri/USHospital.git
```
2. Open Jupyter Notebook and open Hospital.ipynb
Open Jupyter Notebook by open your terminal in your local directory and type: `jupyter notebook`
3. Run the code on Jupyter Notebok


## JSON Structure

The scraped data will be saved in JSON. Below are the example of JSON structure used in this project.  

<pre>
{
    "rs1": {
        "Name": "ACMH Hospital",
        "Address": "One Nolte Drive Kittanning, PA",
        "Grade Spring 2020": "c",
        "Grade Fall 2019": "c",
        "Grade Spring 2019": "c",
        "Grade Fall 2018": "c",
        "Grade Spring 2018": "c",
        "Grade Fall 2017": "c",
        "Grade Spring 2017": "c",
        "Infection MRSA": -1.0,
        "Infection C Diff": 0.218,
        "Infection in Blood": 0.0,
        "Infection in Urinary Tract": 0.0,
        "Infection after Colon Surgery": -1.0,
        "Problem with Surgery Object Left in Patient Body": 0.0,
        "Problem with Surgery Wound Open": 0.94,
        "Problem with Surgery Complications": -1.0,
        "Problem with Surgery Collapsed Lung": 0.26,
        "Problem with Surgery Breathing Problem": 5.83,
        "Problem with Surgery Blood Clot": 3.23,
        "Problem with Surgery Accidental Cuts": 1.23,
        "Practices to Prevent Errors Order Medications through Computer": 45.0,
        "Practices to Prevent Errors Safe Medication Administration": 45.0,
        "Practices to Prevent Errors Handwashing": -2.0,
        "Practices to Prevent Errors Communication about Medicine": 76.0,
        "Practices to Prevent Errors Communication about Discharge": 89.0,
        "Practices to Prevent Errors Staff Work Together": -2.0,
        "Safety Problems Bed Sores": 0.74,
        "Safety Problems Patient Fals and Injuries": 1.067,
        "Safety Problems Air on Gas Bubble in Blood": 0.0,
        "Safety Problems Track and Reduce Risks": -2.0,
        "Doctor Nurse Staff Leadership": -2.0,
        "Doctor Nurse Staff Qualified Nurses": -2.0,
        "Doctor Nurse Staff Trained Doctors for ICU Patients": 5.0,
        "Doctor Nurse Staff Communication with Doctors": 91.0,
        "Doctor Nurse Staff Communication with Nurses": 89.0,
        "Doctor Nurse Staff Responsiveness of Hospital Staff": 85.0
    }
}
</pre>


## Screenshot

- ##### Normalization 
![normalization](/screenshot/normalization.png)

- ##### Saving to JSON
![saving-to-json](/screenshot/saving-to-json.png)

- ##### TQDM show progress bar
![scrapping-tqdm](/screenshot/scrapping-tqdm.png)


## Reference

For dependency installation, we can look the detail here.
- https://pypi.org/

For tutorial using BeautifulSoup.
- https://medium.com/@raiyanquaium/how-to-web-scrape-using-beautiful-soup-in-python-without-running-into-http-error-403-554875e5abed
- https://www.youtube.com/watch?v=XQgXKtPSzUI

For the Scraped Webpage, the list of all US hospitals can be found here
- https://www.hospitalsafetygrade.org/all-hospitals


## Author

Nyoman Kevin Cahyadig Giri

Information System and Technology (18218001)


