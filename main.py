def deleteOld():
        with open('correos.txt', 'w', encoding='utf-8'):
            pass
def save2File(msg):
    with open('correos.txt', 'a', encoding='utf-8') as archivo:
            archivo.write(msg+ '\n')

if __name__ == "__main__":
    deleteOld()
    tour = input("Insert tour name: ")
    divs = int(input("Insert number of involved divisions: "))
    dueDate = input("Insert due date for reply: ")
    for i in range(divs):
        div = input(f"Insert code for the {i+1} region: ")
        title = f'{tour} - Request for Relevant Information from {div} division'
        save2File(title)
        emails = f'{div.lower()}-atcops@ivao.aero {div.lower()}-flightops@ivao.aero w-hq@ivao.aero'
        save2File(emails)
        airports = f''
        numArpt = 1
        airport = input(f"Insert the {numArpt} airport code: ")
        prevAirport = ""
        while airport != "ZZZZ":
            if numArpt == 1:
                prevAirport = airport
                numArpt+=1              
            else:
                airports = airports+'\u2022'+prevAirport+f'-{airport}\n'
                prevAirport = airport
                numArpt+=1
            airport = input(f"Insert the {numArpt} airport code: ")
        message = f"""Dear {div},
I hope this message finds you well. The {tour} is set to pass through your specific IVAO Division, and we kindly request the following information to ensure a smooth journey for our participants:\n
        
The route(s) passing through your division is (are):\n
{airports}
1. Recommended or Mandatory Route: We are seeking your recommendations for the best route departing from your division, considering air traffic control procedures, airspace restrictions, recommended alternates for the arrivals in your division, and any other information so that we can share it with our pilots in the Leg Description. If there is any mandatory route for that exact leg. (If necessary, clarify the ACFT CAT for their better understanding).

2. Aeronautical Charts and Resources: Please provide links to aeronautical charts, NOTAMs, and any other relevant information that would aid our flight planning and navigation, such as freeware sceneries to be downloaded before the flight.

Please use REPLY TO ALL email back to us until {dueDate} so we can get everything ready.

Your guidance will contribute to the success of our tour. We look forward to your prompt response. If you have any questions, please don't hesitate to contact us.
        """
        save2File(message)