*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Login Command

*** Test Cases ***
Register With Valid Username And Password
    Create User  minni  kisu4567
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Create User  kalle  kallestin4
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Create User  ei  e1onnistu
    Output Should Contain  Username must be at least 3 characters long and contain only characters a-z

Register With Valid Username And Too Short Password
    Create User  minni  k1su
    Output Should Contain  Password must be at least 8 characters long and can not contain only characters a-z

Register With Valid Username And Long Enough Password Containing Only Letters
    Create User  minni  kisukisukisu
    Output Should Contain  Password must be at least 8 characters long and can not contain only characters a-z

*** Keywords ***
Create User And Input Login Command
    Create User  kalle  kalle123
    Input Login Command