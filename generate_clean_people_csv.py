import os 
import pandas as pd 
from google import search
from urlparse import urlsplit

if __name__ == '__main__': 

	people = pd.read_csv('./network_data_raw/Max_Network_Data_Clean_People.csv')
	people = people[['First_Last', 'Website']]

	googled_websites = pd.Series(index = people.index)
	website_is_same = pd.Series(index = people.index)

	for ix, person in people.iterrows():

		curr_site = person['Website']
		googled_site = search(person["First_Last"] + " academic", num = 1).next()

		googled_websites[ix] = googled_site

		if not pd.isnull(curr_site): 
			website_is_same[ix] = (urlsplit(curr_site).netloc == urlsplit(googled_site).netloc)
		else: 
			website_is_same[ix] = True

		print "{} {} {}".format(person["First_Last"], curr_site, googled_site)

	# Add to original DF 
	people['googled_sites'] = googled_websites
	people['website_is_same'] = website_is_same

	people.to_csv('./network_data_raw/Max_Network_Data_Clean_People_Processed.csv')




