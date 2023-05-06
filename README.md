# Skinport Assistant

This code will assist you in making the best deal for CSGO skins. It outputs the best item according to your preferences in a clear format. This micro-project wouldn't exist if not my dear fried A.Z.❤️

## Requirements
To use this code, you will need to install the following modules on your computer:
1. `requests` module
2. `json` module
3. `matplotlib` module

The installation process may differ depending on your operating system. If you are unfamiliar with how to install a module, simply search the internet for "how to install python *module name* on *your operating system name*". After completing these minor installations, you should be all set to use the code.

## Usage
You will first be prompted to enter the following parameters:
1. `acceptable_volume` - the number of times an item was traded during your specified `acceptable_timing` parameter. Alternatively, you can leave this parameter blank to search for the best deal on the marketplace during a given time period.
2. `acceptable_timing` - a period of time (24h, 7d, 30d, 90d) during which you would like to search for items. Your `acceptable_volume` parameter will play a crucial role in sorting all items that were traded during this time period.
3. `acceptable_min_price` - the minimum price you are comfortable with paying for an item.
4. `acceptable_max_price` - the maximum amount of money you are willing to pay for a particular item.
5. `acceptable_display_items` - the number of items you would like to see in a single page of the report generated by this program.

After entering these parameters, you will receive a stylish report with links to items that fit your preferences and are currently being traded on the marketplace. You will then be asked if you want to make another analysis in case you are unsure about the parameters you just entered.

## Additional notes
This code includes a visual representation of market analysis results, but I deemed it unnecessary during development. If you know a little coding, you can uncomment line №149 to turn on the `visual_module()` and get a graph that uses the `matplotlib` framework.

If this code proves helpful to someone, I may add additional functions such as a static settings feature, where you would input your preferences once and then use them whenever you like, without compromising flexibility.
