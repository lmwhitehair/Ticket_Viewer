# Ticket_Viewer
Console application that connects to Zendesk's Ticket api and pulls individual ticket details 

# Important
In order to use this application you must have a Zendesk account, if you don't already have one, you can start a free trial at: https://www.zendesk.com/register

# Instructions
Before running Ticket_Viewer.py, you must first set up some environment variables. Paste the following commands into your terminal (input your credentials in the quotes)(exclude the quotes)

  export Zendesk_password='your personal password'
  
  export Zendesk_username='your personal email'
  
  export Zendesk_url='your url' ~ this should point to the tickets api and at the end of the url be sure to put ?page[size]=25
  
  
  
To delete the environment variables after using the application, use the following command
  unset 'variable name'
  
You can run this Python script directly from your terminal/console or from a text editor.

# Dependencies
  -> Python3
  
  -> requests (library)
	
  -> dotenv (library)
  
  -> os (library)
  
  -> configparser (library)
  
  -> requests.auth - HTTPBasicAuth (library)
  
  -> unittest (library)
  
  -> assertpy (library)
  
# Other information
I used Python for this project because I am attempting to get more experience with the language

I chose to create a console application because I wanted most of my time working on this project to be focused on correctly implementing the necessary features of a
Ticket Viewer application rather than spending time working on a UI. As a UI is not necessary due to little user input. A simple command line interface is sufficient enough. 
