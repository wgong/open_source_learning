# coding: utf-8
"""
purpose: this utility converts xml doc exported by Draw.io to json used by Learning Anything mindmap
created_by: weng
created_on: 2017-07-13
"""

try:
    from lxml import etree as etree
except ImportError:
    import xml.etree.ElementTree as etree
    
import collections
import re

la_node_data = {} # store all node data
la_nodes = []     # 
la_subnodes = []  # leaf node

def construct_trees_by_TingYu(edges):
    """
    Given a list of edges [child, parent], return trees. 
    see http://xahlee.info/perl-python/python_construct_tree_from_edge.html
    """
    trees = collections.defaultdict(dict)

    for child, parent in edges:
        trees[parent][child] = trees[child]

    # Find roots
    children, parents = zip(*edges)
    roots = set(parents).difference(children)

    return {root: trees[root] for root in roots}

def strip_font(line):
    matchObj = re.match( r'<font(.*)>(.*)</font>', line, re.M|re.I)
    if matchObj and matchObj.group(2):
        return matchObj.group(2)
    else:
        return line

def walk_sort(node):
    for k in node.keys():
        item = node[k]
        #print(k,item, len(item))
        if not len(item):
            la_subnodes.append(k)
        else:
            la_nodes.append(k)
            walk_sort(item)

"""
import uuid
# make a random UUID
token4 = str(uuid.uuid4())
# make a UUID based on the host ID and current time
token1 = str(uuid.uuid1())
token1, token4
"""

def convert_drawio2la_json(file_in, map_name):

    edges = []     # used to construct tree

    # parse Draw.io exported XML doc
    drawio_tree = etree.parse(file_in)

    # parse mxCells node
    mxCells = drawio_tree.findall('//mxCell[@vertex="1"]')

    for e in mxCells:
        if 'id' in e.keys():
            #print(e.attrib['id'])
            xy = e.find('./mxGeometry')
            la_node_data[int(e.attrib['id'])] = {
                 'id': e.attrib['id'],
                 'text': strip_font(e.attrib['value']),
                 'url': '',
                 'fx': xy.attrib['x'], 
                 'fy': xy.attrib['y']
            }

    # parse UserObject node
    usrObjs = drawio_tree.findall('//UserObject') 

    for e in usrObjs:
        #c = e.find('mxCell')
        #print(e.attrib['id'], e.attrib['label'], e.attrib['link'])
        xy = e.find('./mxCell/mxGeometry')
        la_node_data[int(e.attrib['id'])] = {
                  'id': e.attrib['id'],
                  'text': strip_font(e.attrib['label']),
                  'url': e.attrib['link'],
                  'fx': xy.attrib['x'],
                  'fy': xy.attrib['y']        
                 }
        

    # parse edges: mxCell[@source]
    edges_el = drawio_tree.findall('//mxCell[@source]')

    for g in edges_el:
        edg_att = g.attrib
        if edg_att['edge'] == "1":
            #print(edg_att['source'], edg_att['target'], edg_att['id'], edg_att['parent'])
            edges.append([int(edg_att['target']),int(edg_att['source'])])


    edgeDict = {e[0] : e[1] for e in edges}

    # build tree
    t2 = construct_trees_by_TingYu(edges)
    # walk tree and sort out la_nodes/la_subnodes
    walk_sort(t2)

    #import json  
    #print(json.dumps(t2, indent=3))
    
    # generate JSON
    nodes_str = ""
    for n,k in enumerate(la_nodes):
        if n: nodes_str += ','
        nodes_str += "{'text': '%s', 'url': '%s', 'fx': '%s', 'fy': '%s'}" % (
             la_node_data[k]['text'], la_node_data[k]['url'], la_node_data[k]['fx'], la_node_data[k]['fy'])

    subnodes_str = ""
    for n,k in enumerate(la_subnodes):
        if n: subnodes_str += ','
        subnodes_str += "{'text': '%s', 'url': '%s', 'fx': '%s', 'fy': '%s', 'parent': '%s'}" % (
            la_node_data[k]['text'], la_node_data[k]['url'], la_node_data[k]['fx'], la_node_data[k]['fy'], 
            la_node_data[edgeDict[k]]['text'])

    conn_str = ""
    n = -1
    for k in edgeDict.keys():
        if not k in la_subnodes:
            n += 1
            if n: conn_str += ','
            conn_str += "{'source': '%s', 'target': '%s'}" % (
                la_node_data[edgeDict[k]]['text'], la_node_data[k]['text'])

    return "{'title': '%s', 'nodes': [%s], 'subnodes': [%s], 'connections': [%s]}" % (
            map_name, nodes_str, subnodes_str, conn_str)

if __name__ == '__main__':
    import sys, os.path
    
    file_in=''
    map_name='learn anything'

    if len(sys.argv) <= 1:
        print('Usage: python convert_drawio2la_json <drawio.xml> [<map-name>]')
        exit(-1)
    if len(sys.argv) > 1:
        file_in = sys.argv[1]
    if len(sys.argv) > 2:
        map_name = sys.argv[2]

    if not os.path.exists(file_in):
        print('File ', file_in, ' not found' )
        exit(-2)
    
    file_name, file_ext = os.path.splitext(file_in)
    file_out = file_name + ".json"
    
    fo = open(file_out,'w')
    fo.write(convert_drawio2la_json(file_in, map_name))
    fo.close()
    exit(0)