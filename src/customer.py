# Creating a script to input customer information
# Importing modules for stamoing dates duriong initial profile creation
import datetime
# Variables for names,address, phone, occupation and create a serial number from julian date for profile and demographics
# We define the initial client account as one block
def clientAccount():
    clientFirstName = input('First Name: ')
    clientLastName  = input('Last Name: ')
    clientPhone = input('Phone Number: ')
    clientAddressStreet = input ('Street: ')
    clientAddressUnit = input ('Unit/Apt: ')
    clientCity = input('City: ')
    clientAddressState = input ('State: ')
    clientAddressZipCode = input ('Zip Code: ')
    clientOccupation = input('Occupation: ')

# For existing accounts we would like to reference information by a key an value system
# We now create a dictionary to input that information


