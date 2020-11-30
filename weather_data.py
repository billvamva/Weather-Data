import csv
import codecs
import urllib.request
import sys

''' OUTDATED METHOD found online TO INSERT INFORMATION IN COMMAND: TO BE EDITTED
# This is the core of our weather query URL
BaseURL = 'http://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/weatherdata/'

if len(sys.argv) < 4:
    print('')
    print('Usage: FetchWeather Location Date API_KEY')
    print()
    print('  Location: Please provide a location for the weatch search.')
    print('    (Make sure to use quotes if the name contains spaces.)')
    print('  Date: Please specify a date in the format YYYY-MM-DD to look up weather for a specific date.')
    print('    Or use the FORECAST to look up the current weather forcast.')
    print('  API_KEY: Please specify your Visual Crossing Weather API Key')
    print('    If you don\'t already have an API Key, get one at www.visualcrossing.com/weather-api.')
    print()
    print('Example: FetchWeather \"Herndon, VA\" 2006-04-12 KEY_123')
    print('Example: FetchWeather \"Beverly Hills, CA\" FORECAST KEY_123')
    print()
    sys.exit()

print('')
print(' - Requesting weather for: ', sys.argv[1])

DateParam = sys.argv[2].upper()

# Set up the location parameter for our query
QueryLocation = '&location=' + urllib.parse.quote(sys.argv[1])

# Set up the key parameter for our query
QueryKey = '&key=' + sys.argv[3]

# Set up the specific parameters based on the type of query
if DateParam == 'FORECAST':
    print(' - Fetching forecast data')
    QueryTypeParams = 'forecast?&aggregateHours=24&unitGroup=us&shortColumnNames=false'
else:
    print(' - Fetching history for date: ', DateParam)

    # History requests require a date.  We use the same date for start and end since we only want to query a single date in this example
    QueryDate = '&startDateTime=' + DateParam + 'T00:00:00&endDateTime=' + sys.argv[2] + 'T00:00:00'
    QueryTypeParams = 'history?&aggregateHours=24&unitGroup=us&dayStartTime=0:0:00&dayEndTime=0:0:00' + QueryDate


# Build the entire query
URL = BaseURL + QueryTypeParams + QueryLocation + QueryKey

print(' - Running query URL: ', URL)
print()
'''

URL = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/weatherdata/forecast?aggregateHours=24&combinationMethod=aggregate&contentType=csv&unitGroup=metric&locationMode=single&key=52LWX62A83VVMS5RGJ8RNGAGF&dataElements=default&locations=herndon'
# Parse the results as CSV
EncodedData = urllib.request.urlopen(URL)
Data = csv.reader(codecs.iterdecode(EncodedData, 'utf-8'))

rowIndex = 0

# First Row is the header,
# First Column is the Location, Second Row is the Date
for row in Data:
    if rowIndex == 0:
        header = row
    else:
        print('Weather in ', row[0].upper(), ' on ', row[1])

        colIndex = 0
        for col in row:
            if colIndex >= 2:
                print('   ', header[colIndex], ' = ', row[colIndex])
            colIndex += 1
    rowIndex += 1

# No rows returned: Error in connection
if rowIndex == 0:
    print('Error connecting to the weather server.')

# One row returned: Error from server
if rowIndex == 1:
    print('Error: ', header)

print()