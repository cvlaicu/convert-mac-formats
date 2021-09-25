# convert-mac-formats
This script converts a list of MAC addresses written in a format to another MAC address format. 

Scenario: we once received a list of MAC addresses which were written in the hypen-hexadecimal notation. We had our list of MAC addresses which were written in the period-separated hexadecimal notation. Due to the fact that they were not using the same format, we could not use Excel to easily compare them. 

This script can convert a list of MAC addresses from a specified format to any of the two formats. For colon- and hypen- hexadecimal notation, Excel's "Find & Replace" works great. However, when you have a list of period-separated MACs, then you start running into some troubles. 

How it works:
You need to feed the list of MACs in a .CSV file called "macs". Then, when you run the script, you have to specify the format in which the MACs currently are. Finally, you specify the format you want them to be converted into. 
