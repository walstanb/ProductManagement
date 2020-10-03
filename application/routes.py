from application import app,db
from flask import render_template, flash, redirect, request, jsonify
from application.forms import *
from application.models import *
from datetime import datetime
import time

app.jinja_env.filters['zip'] = zip

@app.route("/",methods=['GET','POST'])
@app.route("/ProductMovement",methods=['GET','POST'])
def productmovement():
    movement_list=[x for x in db.ProductMovement.find()]
    product_list=[x for x in db.Product.find()]
    location_list=[x for x in db.Location.find()]
    form=ProductMovementForm()
    result=request.form.to_dict()
    if len(result)!=0:
        if(result['action']=="new"):
            if((result['from_location']=='' and result['to_location']=='') or int(result['qty'])<=0):
                return redirect("/ProductMovement")
            if len(movement_list)==0:
                result['movement_id']="MID0001"
            else:
                result['movement_id']="MID"+str(int(movement_list[-1]['movement_id'][3:])+1).zfill(4)
            result['timestamp']=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            del result['action']
            db.ProductMovement.insert(result)
            return redirect("/")
        if(result['action']=="delete"):
            db.ProductMovement.remove({"movement_id": result["x-id"]})
            return redirect("/ProductMovement")
        if(result['action']=="update"):
            prev_id=result['x-id']
            del result['action']
            del result['x-id']
            db.ProductMovement.update_one({ "movement_id" : prev_id},{ "$set": result });
            return redirect("/ProductMovement")
        #print(result.product_id)
    return render_template('ProductMovement.html',form=form,movement_list=movement_list,location_list=location_list,product_list=product_list)


@app.route("/Location",methods=['GET','POST'])
def location():
    location_list=[x for x in db.Location.find()]
    form=LocationForm()
    result=request.form.to_dict()
    if len(result)!=0:
        if(result['action']=="new"):
            del result['action']
            db.Location.insert(result)
            return redirect("/Location")
        if(result['action']=="delete"):
            db.Location.remove({"location_id": result["x-id"]})
            return redirect("/Location")
        if(result['action']=="update"):
            prev_id=result['x-id']
            del result['action']
            del result['x-id']
            db.Location.update_one({ "location_id" : prev_id},{ "$set": result });
            return redirect("/Location")
        #print(result.location_id)
    return render_template('Location.html',form=form,location_list=location_list)

@app.route("/Product",methods=['GET','POST'])
def product():
    product_list=[x for x in db.Product.find()]
    form=ProductForm()
    result=request.form.to_dict()
    if len(result)!=0:
        if(result['action']=="new"):
            del result['action']
            db.Product.insert(result)
            return redirect("/Product")
        if(result['action']=="delete"):
            db.Product.remove({"product_id": result["x-id"]})
            return redirect("/Product")
        if(result['action']=="update"):
            prev_id=result['x-id']
            del result['action']
            del result['x-id']
            db.Product.update_one({ "product_id" : prev_id},{ "$set": result });
            return redirect("/Product")
        #print(result.product_id)
    return render_template('Product.html',form=form,product_list=product_list)


@app.route("/BalanceReport",methods=['GET','POST'])
def balancereport():
    grand={}
    movement_list=[x for x in db.ProductMovement.find()]
    location_list=[x for x in db.Location.find()]

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
    return render_template('BalanceReport.html',grand=grand,location_list=location_list)

'''
@app.route("/",methods=['GET','POST'])
def moveproduct():
    product_list=[x for x in db.Product.find()]
    loaction_list=[x for x in db.Location.find()]
    movement_list=[x for x in db.ProductMovement.find()]

    form=ProductMovementForm()
    result=request.form.to_dict()
    if len(result)!=0:
        if len(movement_list)==0:
            result['movement_id']="MID0001"
        else:
            result['movement_id']="MID"+str(int(movement_list[-1]['movement_id'][3:])+1).zfill(4)
        result['timestamp']=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(result)
        del result['action']
        db.ProductMovement.insert(result)
        return redirect("/")
    return render_template("MoveProduct.html",form=form,location_list=loaction_list,product_list=product_list)

    grand={}
    for x in movement_list:
        if(len(x['from_location'])==0 and len(x['to_location'])!=0):
            if(x['product_id'] in grand[x['from_location']].keys()):
                grand[x['from_location']][x['product_id']]=int(grand[x['from_location']][x['product_id']])+int(x['qty'])
            else:
                grand[x['from_location']][x['product_id']]=int(x['qty'])
        elif(len(x['from_location'])!=0 and len(x['to_location'])==0):
            if(x['product_id'] in grand[x['to_location']].keys()):
                if(int(x['qty'])<=int(grand[x['to_location']][x['product_id']])):
                    grand[x['to_location']][x['product_id']]=int(grand[x['to_location']][x['product_id']])-int(x['qty'])
                else:
                    raise Exception('Invalid Operation: You Cannot Remove More than stored amount')
        elif(len(x['from_location'])==0 and len(x['to_location'])==0):
            raise  Exception('Invalid Operation')
        elif(len(x['from_location'])!=0 and len(x['to_location'])!=0):
            if((x['product_id'] in grand[x['from_location']].keys()) and int(x['qty'])<=int(grand[x['to_location']][x['product_id']])):
                grand[x['to_location']][x['product_id']]=int(grand[x['to_location']][x['product_id']])-int(x['qty'])
                grand[x['from_location']][x['product_id']]=int(grand[x['from_location']][x['product_id']])+int(x['qty'])
            else:
                raise Exception('Invalid Operation: You Cannot Remove More than stored amount')
    print(grand)'''