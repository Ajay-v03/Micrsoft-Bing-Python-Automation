Hey!
Welcome to _**Microsoft Bing Search Bar**_  Project.

Project name: MS Bing Search result data fetcher.

Objective: Python Bot need to fetch 10 pages search data and store in a JSON with valid keys,values.

Dependencies: It's a platform independent project. Python should be installed in Machine.

Project details:

MsBingTest.py >> This is test crawler file which extracts the data of 10 pages search bar results from web and store output as JSON file.

MsBingMain.py >> This Python Bot take a name entry as a input from shared csv file and give output as a json.
As we have test this code, we have achieved only 3 processes work parallely.
Here 3 Browser windows have open paralel threads and generate output for three entries in same time.

MsBingWithDB.py >> This Bot have also perform the above. But here we store generated json in MongoDB. The testing have been done in local DB.

TestResultDemo.json >> Here we have generated json files by Python Bots for reference. Kindly go through it.

TestResultDemo2.json >> As mentioned above same generated file for different name netry, have attached for your reference.

us_name.csv >> A csv file that have combination of name entries. Bot need to be fetch data of these shared name entities.

requirement.txt >> Project all dependencies have float in this file. Run this before run Python Bot.

Note: As it's a Demo Project but we can design a better one where Ip Switches automatically like Tor Browser, PhantomJs etc.
SOme of the time bot have captured by websites and they hav blocked ip. So we are unable to extaract data from these websites like Amazon, flipkart, and e-commerce etc.
