import pymongo

conn = pymongo.MongoClient("mongodb+srv://sbuzzdbuser:rTZqgmtHXhpISrR7@cluster0.60uwm.gcp.mongodb.net/ProductManagement?retryWrites=true&w=majority")
db = conn["ProductManagement"]

movement_list=[x for x in db.ProductMovement.find()]
location_list=[x for x in db.Location.find()]
grand={}
'''
for x in movement_list:
    if(x['from_location']=='' and x['to_location']!=''):
        if(x['product_id'] in grand[x['from_location']].keys()):
            grand[x['from_location']][x['product_id']]=int(grand[x['from_location']][x['product_id']])+int(x['qty'])
        else:
            grand[x['from_location']][x['product_id']]=int(x['qty'])
    elif(x['from_location']!='' and x['to_location']==''):
        if(x['product_id'] in grand[x['to_location']].keys()):
            if(int(x['qty'])<=int(grand[x['to_location']][x['product_id']])):
                grand[x['to_location']][x['product_id']]=int(grand[x['to_location']][x['product_id']])-int(x['qty'])
            else:
                raise Exception('Invalid Operation: You Cannot Remove More than stored amount')
    elif(x['from_location']=='' and x['to_location']==''):
        raise  Exception('Invalid Operation')
    elif(x['from_location']!='' and x['to_location']!=''):
        if((x['product_id'] in grand[x['from_location']].keys()) and int(x['qty'])<=int(grand[x['to_location']][x['product_id']])):
            grand[x['to_location']][x['product_id']]=int(grand[x['to_location']][x['product_id']])-int(x['qty'])
            grand[x['from_location']][x['product_id']]=int(grand[x['from_location']][x['product_id']])+int(x['qty'])
        else:
            raise Exception('Invalid Operation: You Cannot Remove More than stored amount')
print(grand)
'''
for x in location_list:
    grand[x['location_id']]={}

for x in movement_list:
    froml=x['from_location']
    tol=x['to_location']
    qty=x["qty"]
    product_id=x['product_id']

    if(froml=='' and tol!=''):
        if(product_id in grand[tol].keys()):
            grand[tol][product_id]=int(grand[tol][product_id])+int(qty)
        else:
            grand[tol][product_id]=int(qty)
    elif(froml!='' and tol==''):
        if(product_id in grand[froml].keys()):
            grand[froml][product_id]=int(grand[froml][product_id])-int(qty)
    elif(froml!='' and tol!=''):
        if(product_id in grand[tol].keys()):
            grand[tol][product_id]=int(grand[tol][product_id])+int(qty)
            grand[froml][product_id]=int(grand[froml][product_id])-int(qty)
        else:
            grand[tol][product_id]=int(qty)
            grand[froml][product_id]=int(grand[froml][product_id])-int(qty)
print(grand)