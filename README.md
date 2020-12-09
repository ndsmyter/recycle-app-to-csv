# Recycle! app data to CSV

In Belgium the Recycle! app is used to show when you have to put your garbage outside for collection.
As I only use this app for the calendar, I created a script that will export the information from the site and put it in a CSV file that can be imported in Google Calendar.
So I don't need to have the app installed locally all year long.

# Download the JSON

* Open the site https://recycleapp.be/
* Open the Developer Console in your browser
* Enter your address
* Press the "Help me Recycle!" button on the site
* Click on "Recycling calendar" at the top
* You can then find a request to https://recycleapp.be/api/app/v1/collections in the Network tab of your Developer Console
* Copy that request to cURL (or something else)
* Tweak the "fromDate" and "untilDate" query parameters to your preference
* Set the "size" query parameter to the max value of "200"
* Execute the modified request

The result is a JSON that you contains the information for that time period on the selected address.
As an example I have entered the request for the address "Kouter 1, 9000 Ghent" for 2021.
The cURL request can be found in curl2021.txt and the JSON result can be found in json2021.txt.

# Parse the JSON

Parsing the JSON is as easy as calling the Python script.
The script itself is very easy, and should generate the CSV file "calendar2021.csv".

# Notice

It also possible to chain the cURL request and the JSON parsing in Python, but as I also had some other plans with the JSON, I've split this into 2 separate steps.
