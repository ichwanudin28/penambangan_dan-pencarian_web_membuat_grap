import requests
from bs4 import BeautifulSoup
import networkx as nx
import matplotlib.pyplot as plt

def getLinks(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    news_links = soup.find_all('a',{'class':'mod-judul-post'}, href=True)
    for link in news_links:
        listUrl.append(link['href'])
        node.append(link['href'])
        
    n_depth = 3
    swap_depth = 0
    swap_list = 0
    while swap_depth < n_depth :
        listUrl.append("depth")
        next_depth = False
        while next_depth == False:
            if listUrl[swap_list] == "depth" :
                swap_list+=1
                next_depth = True
                swap_depth+=1
                break
            try :
                urls = listUrl[swap_list]
                reqs = requests.get(urls)
                soups = BeautifulSoup(reqs.text, 'html.parser')
                news_linkss = soups.find_all('a',{'class':'vrp-thumb-link'}, href=True)
                for link in news_linkss:
                    listUrl.append(link['href'])
                
                    if link['href'] not in node :
                        node.append(link['href'])
                    value = (str(node.index(urls)),str(node.index(link['href'])))
                    edge.append(value)
                    
            except :
                pass
            swap_list+=1
        swap_depth+=1
        
if __name__== "__main__":
    listUrl = []
    node = []
    edge = []
 
    
    links = getLinks("http://lintasperistiwa.com/")
    #print(listUrl)
    G=nx.DiGraph()
    pages = []
    for i in range(0,len(node)):
        pages.append(str(i))
        
    G.add_nodes_from(pages)
    G.add_edges_from(edge)
    
    print(edge)
    print(type(edge))
    #print(type(edge[0]))
    #membuat graf
    image = nx.draw_circular(G,node_color='blue', with_labels = True)
    plt.savefig("grap.png", format="PNG")
    #mancari nilai pagerank
    PR = nx.pagerank(G)
    print(PR)
    value = max(PR, key=PR.get)
    print("node : " + max(PR,key=PR.get))
    print("link : " + node[int(value)])
    nx.draw(G)
    plt.show()
    print(node)
    

 
