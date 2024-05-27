import matplotlib.colors as cl
def get_cmap(c_list):
    cmap = cl.LinearSegmentedColormap.from_list("",c_list)
    return cmap

def Diana_cmap(name='bloom'):
    x={
    'Diana':[0,1/3,2/3,1],
    'Bloom':[0,0.2,0.5,0.75,1],
    'Normal':[0,1/3,0.5,1],
    'Donkey':[0,0.35,0.5,0.75,1]}[name]
    colors={
    'Diana':['f9f8f8','fcd1de','E799B0','fe77a0'],
    'Bloom':['ba875d','dfb795','fcf8fd','cbc1fa','6761a6'],
    'Normal':['dc5a5b','ee9e85','ffe5cc','d0a07c'],
    'Donkey':['bf7b4e','dfb68d',
              'fec589','f3ebbb','fdfbf7']}[name]
    c_list=[]
    for index,i in enumerate(x):
        c_list.append([i,'#'+colors[index]])
    return get_cmap(c_list)