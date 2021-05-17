# PC wiki

## What is PC Wiki?
    PC wiki is a webapp that allows for users to learn about the process of building their own PC. This concept is woefully
    underdocumented on the internet so this app hopes to resolve that issue. PC wiki assesses understanding through a simple
    quiz which uses multiple choice and a single word question. By assessing this way the relativly simple concept can be
    reinforced ensuring that the person learns and understands how to build a PC.

## How does PC Wiki Work?
    PC wiki is a series of HTML templates controlled through a flask backend and linked to a REST api. The templates use jinja
    to load and ensure that the webpage can store data, run efficiently and only show information to those who should see it. Stlying
    and front end functionality is provided throuhg both bootstrap 5 integration and jquerey 3.6.0. There are also custom parts found in 
    pc-wiki.css and pcBuild.js. User information is stored in the User table which stores user ID, account creation time and hased passwords for
    security. It supports more information but that is currently not used because there is no need for the app to store any personal user info.
    The quiz uses hardcoded questions so must be adjusted manually by chaning the source code of the pages. All question answers and answers 
    given by uses are stored in the Attempts table of the database which to determine if a user answeredcorrectly in the quiz is compared to 
    the quiz table which stores the correct answers for the questions. By performing all assesment grading in the backend there is no way for 
    the user to know which the correct answer is without actually thinking about the question. Logs about site usage are stored in the log table
    and can displayed in the admin exclusive stats page.

## What do the Tests do?
    These two test files perform two different types of tests. The unittest file tests the main data model of the site and ensures that all database
    function and site control fuctions will work properly as without those being ensured to work there is no way that the site frontend could work.
    SystemTest is a set of selenium tests that check all user actions, it checks that error messages display properly to users, checks the functionality 
    of login, logout, attempted duplicate accounts, quiz functionality and results displaying.

## Known Issues
    The UTC to local date conversion does not work in firefox due to no support for the timezone in the javascript library


## Setup
    Requires Python
    install requirements from requirements.txt

    flask run

## Testing
    requires the terminal to be selected on the CITS3403_WEBDEV folder
    pyton -m tests.unittest 

    To perform the systemtest
    first start the webserver
    while the webserver is running use the geckowebdriver on windows
    then run
        python -m tests.systemtest










## Setup

flask db init
flask db migrate
flask db upgrade

## Testing

python test.py
flask shell

## Planned contents

CPU

    Connected though main socket

    Depends on manufacturer and model

GPU

    Connects through a PCI-E connection

    Commonly uses PCI-E 3.0 but modern cards are now supporting 4.0

RAM

    Operates in DDR (Double Data Rate)

    To use this mode installed in pairs

    Speed and max size are determined by the CPU and motherboard

Storage Drive

    Connected through SATA, or M.2

    Can be SSD or HDD.

Fan/Liquid Cooling

    Necessary for ensuring a computer continued operation

PSU

    Bringer of power to the system

    Power Efficiency

Case

    I/O

    USB

    Ethernet

    Power/ Reset buttons

    Audio jacks

Peripherals

    Keyboard

    Switches

    Mouse

    DPI

    Monitor

    Resolution

    Contrast Ratio

    Refresh rate

    Response time

    Webcam

    Megapixels

    Speakers/Headset/Earphone

    Speaker range

    Mic

Global

Navigation bar

    Home

    Lessons

    Assessments

Login info

Dark Mode

Planned Pages

1. Home Page

2. Lessons Page

3. Assessments Page

    ```
    HTML Form

    Marking done on server-side
    ```

4. Login page

    ```
    Login and signup
    ```

5. Administrative page

    ```
    Administrative information (not visible to non admin users)

    Secure access
    ```

6. Review page

# Table Models

![Entity Relationship Diagrams](./ERD.png)
