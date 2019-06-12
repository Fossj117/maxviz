## Max Bazerman Viz.js Advisee Network Visualization

This repository has all the code and data for Max Bazerman's advisee network visualization. Documentation: 

* `README.md`: this file!
* `index.html`: the code that builds the visualization 
* `network_data_raw`: folder that contains raw `CSV` / `XLSX` data for the visualization 
  * `Max_Network_Data_Clean.xlsx`: original excel doc from Max 
  * `Max_Network_Data_Clean_Links.csv`: one row for each link in the network (parent advised child)
  * `Max_Network_Data_Clean_People.csv`: one row for each person in the network (with full metadata) **\[Deprecated but saved for posterity\]**
  * `Max_Network_Data_Clean_People_Final.csv`: live version of people spreadsheet, including website results from googling
* `process_network_data.py`: python script that converts raw network data to a form consumable by `index.html`
* `generate_clean_people_csv.py`: python script that googles `name` + ` academic` and stores first result. 
