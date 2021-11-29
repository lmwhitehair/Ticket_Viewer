
import requests
import os
from requests.auth import HTTPBasicAuth

'''
@author Logan Whitehair
This is a simple python script that fetches tickets that are in Zendesk's api
Any valid url and login credentials will work  
'''


EMAIL = os.getenv('Zendesk_username')
PASSWORD = os.getenv('Zendesk_password')


"""
This method prints all tickets within the ticket api of given url

prints: 25 tickets and prompts user if they want to see next page of tickets
Initially displays ticket id and subject of ticket
"""


def get_tickets():
    api_endpoint = os.getenv('Zendesk_url')
    auth = HTTPBasicAuth(EMAIL, PASSWORD)
    response = requests.get(api_endpoint, auth=auth)

    if(response.status_code != 200):  # if api is unreachable
        print("Something went wrong")
        print(response.status_code)
    else:
        while api_endpoint:  # after all necessary tickets are displayed, api_endpoint will be set to None and the loop will stop
            tickets = response.json()
            for i in tickets['tickets']:  # interating and printing 25 tickets
                print("Id: ", end='')
                print(i['id'], end='')
                print("   Subject: ", end='')
                print(i['subject'])
                print()
            # if there is another page of tickets, prompt user
            if(tickets['meta']['has_more'] == True): # my attempt at pagination
                userInput = input(
                    "Do you want to see the next page of tickets? (y or n) ")
                if(userInput == "y"):
                    api_endpoint = tickets['links']['next']
                    response = requests.get(api_endpoint, auth=auth)
                else:
                    api_endpoint = None
            else:
                api_endpoint = None


"""
    @param the id number of the ticket that the user wants to view
    this method is called whenever the user inputs '2' meaning that they want to 
    view specific details of a ticket 

    prints: user id, requester id, current status(open, closed, pending), time that 
    it was created, and the type of ticket that it is
"""


def get_specific_ticket(id):
    api_endpoint = os.getenv('Zendesk_url')
    auth = HTTPBasicAuth(EMAIL, PASSWORD)
    response = requests.get(api_endpoint, auth=auth)

    if(id == "exit"):  # if user wants to exit after entering '2', exit
        return
    if(response.status_code != 200):  # if api is unavailable
        print("Something went wrong")
        print(response.status_code)
    else:
        tickets = response.json()
        id = int(id)

        for i in tickets['tickets']:  # printing specific details of given ticket
            if(i['id'] == id):
                print("\n--user--")
                print(i['requester_id'])
                print("\n--status--")
                print(i['status'])
                print("\n--created at--")
                print(i['created_at'])
                print("\n--type--")
                print(i['type'])
                return

    print("Ticket Viewer could not find a ticket with the subject of " +
          id + " press '2' to retry.")  # if id entered is unrecognizable


'''
    main method
'''


def main():
    print("------------Ticket Viewer------------")
    print("Type 'help' to view commands or 'exit' to exit the viewer")
    userInput = input()
    while(userInput != "exit"):
        if(userInput == "help"):
            userInput = input(
                "*What do you want to view? \n *Press '1' to view all tickets \n *Press '2' to view a ticket \n *Type 'exit' to exit the viewer\n")
        elif(userInput == "1"):
            get_tickets()
            userInput = input()
        elif(userInput == "2"):
            userInput = input(
                "Type the id of the ticket that you want to view: \n")
            get_specific_ticket(userInput)
            userInput = input()
        else:
            print("Ticket Viewer did not recognize your command, please try again.")
            userInput = input()

    print("\nTicket Viewer says: Goodbye")


if __name__ == '__main__':
    main()
