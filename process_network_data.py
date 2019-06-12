import pandas as pd 
import networkx as nx
import json
import os

def build_graph_from_links_data(infile = "./network_data_raw/Max_Network_Data_Clean_Links.csv"):
	'''
	Read from file and return NetworkX graph object
	'''

	G = nx.DiGraph()
	links = pd.read_csv(infile)

	for _, link in links.iterrows():

		G.add_edge(link['Parent_First_Last'].decode('utf-8'), link['Child_First_Last'].decode('utf-8'))

	return G


def links_data_to_dot_file(infile="./network_data_raw/Max_Network_Data_Clean_Links.csv", outfile='./network.dot'):
	'''
	Read in the network links data and write the network structure to a dot file
	''' 

	G = build_graph_from_links_data(infile)

	nx.write_dot(G, 'raw_network.dot')

	with open('raw_network.dot', "r") as f:
		with open(outfile, 'w') as out: 

			for ix, line in enumerate(f): 
				if ix == 0: 
					out.write("var DOTstring = '"+line.strip())
				else: 
					out.write(line.strip())
			out.write("'")

	os.remove('raw_network.dot')


def node_metadata_to_file(infile="./network_data_raw/Max_Network_Data_Clean_People_Final.csv", outfile='./node_data.json'):
	'''
	Read in the node metadata and write relevant pieces to a JSON. 
	This also does the graph processing to find the steps for each node 
	'''

	# Build and initialize things
	nodes = pd.read_csv(infile)
	G = build_graph_from_links_data() # default reads the links
	kv = {}

	# Add websites to node metadata
	for _, node in nodes[['First_Last', 'Website']].iterrows(): 

		node_key = node['First_Last']

		# Compute distance from Max as an integer and store it
		kv[node_key] = {'steps': nx.shortest_path_length(G, source='Max Bazerman', target = node_key.decode('utf8'))}

		# Add website if it exists 
		if not pd.isnull(node['Website']): 
			kv[node_key]['site'] = node['Website']

	# Write to file with some hacks to later load with JS
	with open(outfile, "w") as f:
		f.write("var node_data = '")
		json.dump(kv, f)
		f.write("'")


if __name__ == "__main__": 


	# Convert the links data into a dot file and write it here
	links_data_to_dot_file()

	# Convert the node metadata to a JSON and store it here
	node_metadata_to_file()