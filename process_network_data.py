import pandas as pd 
import networkx as nx
import json

def links_data_to_dot_file(infile="./network_data_raw/Max_Network_Data_Clean_Links.csv", outfile='./network.dot'):
	'''Read in the network links data and write the network structure to a dot file''' 

	G = nx.DiGraph()
	links = pd.read_csv(infile)

	for _, link in links.iterrows():

		G.add_edge(link['Parent_First_Last'].decode('utf-8'), link['Child_First_Last'].decode('utf-8'))

	nx.write_dot(G, outfile)

def node_metadata_to_file(infile="./network_data_raw/Max_Network_Data_Clean_People.csv", outfile='./node_data.json'):
	'''Read in the node metadata and write relevant pieces to a JSON'''

	nodes = pd.read_csv(infile)
	kv = {}

	for _, node in nodes[['First_Last', 'Website']].iterrows(): 

		# Just adding their website for now if it exists 
		if not pd.isnull(node['Website']): 
			kv[node['First_Last']] = {'site': node['Website']}

	with open(outfile, "w") as f:
		json.dump(kv, f, indent=4, separators=(',', ': '))


if __name__ == "__main__": 


	# Convert the links data into a dot file and write it here
	links_data_to_dot_file()

	# Convert the node metadata to a JSON and store it here
	node_metadata_to_file()