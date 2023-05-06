"""
Yevgeny Zamyatin, who is known for his dystopian novel "We", which was published in 1924 and inspired later works such as 
George Orwell's "1984". The name "Zamyatin" has a cool and mysterious feel to it, which could be fitting for an analytic assistant that 
provides insights on market trends and behaviors. 
"""
import requests
import json
import base64
import matplotlib.pyplot as plt

#Acceptable values prompted from user.
acceptable_volume = 1 
acceptable_timing = None 
acceptable_max_price = None 
acceptable_min_price = None
acceptable_display_items = 15
change_settings_state = False

#Promp user for input.
def ask_for_input(acceptable_volume, acceptable_timing, acceptable_min_price, acceptable_display_items, acceptable_max_price):
    """Ask user to input: volume of trades per period, period, maximum price, minimum price of an item."""
    state_of_input = False 
    while state_of_input != True:
        try:
            acceptable_volume = input('What is your aceptable trade volume number? Or just hit Enter. ')
            acceptable_timing = input('What would be the prefered timing: 24h, 7, 30 or 90 days? ')
            acceptable_max_price = float(input('What price MAXIMUM is preferable to you? '))
            acceptable_min_price = float(input('What price MINIMUM is prefarable to you? '))
            acceptable_display_items = input('How many items would you like to display? ')
            return(acceptable_volume, acceptable_max_price, acceptable_min_price, acceptable_display_items, acceptable_timing)
            state_of_input = True 
        except ValueError:
            print('\nThere seem to be wrong value. Did you typed a letter in number field?')
            print("Let's try one more time.\n")

#Request making module.
def make_request():
    """Make .GET request to skinport API."""
    url = 'https://api.skinport.com/v1/sales/history'
    params = {'app_id': '730'}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        print('\n---SKINPORT RESPONSE: OK ---\n')
        data = response.json()

        with open('sales_history.json', 'w') as sh:
            json.dump(data, sh, indent=4)
        print('\n---JSON FILE COMPILED SUCCESSFULY---\n')
    else:
        print('Failed to compile JSON file...')

#Sync with user preferances on timing.
def timing_sync(acc_tim):
    """Translate user input to values that match json's file."""
    acc_tim = str(acc_tim)
    if acc_tim == '24h':
        acc_tim = 'last_24_hours'
    if acc_tim == '7':
        acc_tim = 'last_7_days'
    if acc_tim == '30':
        acc_tim = 'last_30_days'
    if acc_tim == '90':
        acc_tim= 'last_90_days'
    return(acc_tim)

#Compiling a dictionary according to user preferances.
def compile_dictionary(acc_vol, acc_max_pr, acc_min_pr, acc_display_items, market_timing):
    """Build a dictionary of sorted by volume items in the X number of days."""
    with open('sales_history.json', 'r') as sh:
        lots = json.load(sh)
        acceptable_lots  = {}
        market_timing = timing_sync(market_timing)
        lot_number = 0
        
        #Looping through skinport database.
        for lot in lots:
            lot_item_name = lot['market_hash_name']
            lot_volume = lot[market_timing]['volume']
            
            #In X number of days, compile a dictionary Name-Volume-Price,
            # that fits price range and volume of minimum 1 trades per X days.
            if lot_volume >= 1 and int(lot[market_timing]['avg']) <= float(acc_max_pr) and int(lot[market_timing]['avg']) >= float(acc_min_pr):
                acceptable_lots.update({lot_number: {'name': lot_item_name,
                                                        'volume': lot_volume, 
                                                        'avg': lot[market_timing]['avg'],
                                                        'item_page': lot['item_page']
                                                        }})
            lot_number += 1 
            

        #Sorting acceptable_lots by the most traded(volume) number.
        sorted_lots = dict(sorted(acceptable_lots.items(), key=lambda x: x[1]['volume'], reverse=True))
        sorted_lots_limited = dict(list(sorted_lots.items())[:int(acc_display_items)])

        #Looping through sorted_lots to form a dict: Name of an item and its price.
        name_and_price = {}
        for key, value in sorted_lots.items():
            name_and_price[key] = value['avg'] 

        #Limiting name_and_price dict to make it viewable in matplotlib.
        name_and_price_limited = dict(list(name_and_price.items())[:int(acc_display_items)])

        #Simple output of description of each item in name_and_price_limited.
        print('🔫👀 Here is what I found fitting your preferances: ')
        for item in sorted_lots_limited:
            print(f"\t{sorted_lots_limited[item]['name']}")
            print(f"\t\tWhich was traded: {sorted_lots_limited[item]['volume']} times in {market_timing}.")
            print(f"\t\t💰Price: {sorted_lots_limited[item]['avg']} EUR.")
            print(f"\t\t🌐Link to that item: {sorted_lots_limited[item]['item_page']}")

        return(name_and_price_limited.keys(), name_and_price_limited.values())
        


#Visual accomodations.
def visual_module():
    """Build matplotlib scatter graph according to compile_dictionary() output."""
    #compile_dictionary_set_up_var = ask_for_input(acceptable_volume, acceptable_max_price, acceptable_min_price, acceptable_timing)
    #data = compile_dictionary(*compile_dictionary_set_up_var)
    #point_numbers = range(len(data[0]))
    c_num = len(data[0])

    #Styling the scatter graphic.
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(15, 8))

    #Compiling scatter graphic.
    ax.scatter(data[0], data[1], c=range(c_num), cmap=plt.cm.cool, edgecolors='none', s=45)

    #Labeling of the scatter graphic.
    ax.set_title('Zamyatin_Neumann_0.3.0 Market analysis results. This version is in beta test.')
    ax.set_xlabel('Name of the fitting items on sale', fontsize=14)
    ax.set_ylabel(f"Average price in EUR", fontsize=14)

    #Additional appearance tweeks.
    plt.subplots_adjust(top=0.9,bottom=0.3,left=0.05,right=0.95,hspace=0.2,wspace=0.2)
    plt.xticks(rotation=45)

    plt.show()

def launch():
    """Launch Market assistant."""
    print('Welcome to Market assistent built by - @kadynsky on twitter.')
    print('\tZamyatin_Neumann_0.3.0 Market analysis. This version is in beta test.\n')

    make_request()
    run_state = True
    while run_state:
        #visual_module()

        #In case visual_module() is OFF. Turn following two lines ON.
        compile_dictionary_set_up_var = ask_for_input(acceptable_volume, acceptable_max_price, acceptable_min_price, acceptable_display_items, acceptable_timing)
        data = compile_dictionary(*compile_dictionary_set_up_var)

        state_related_answer = input('Would you like to make another analysis on same data? y/n ')
        if state_related_answer == 'y':
            continue
        else:
            print('Thanks for using our services!')
            break

#Launching.
launch()
