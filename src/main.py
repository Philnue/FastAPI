from os import system
import os
from typing import ItemsView
from fastapi import FastAPI
import businesslogic as dbConnection
import json

api = FastAPI()
con = dbConnection.BusinesssLogic()

@api.get("/")
async def root():
    #return {"message": "Hello World"}
    return "Hey na du"

@api.get("/loadpersonbyid/{item_id}")
async def read_item(item_id):
    #return {"item_id": item_id}
    
    return con.get_item_by_id(item_id)

@api.get("/loadallpersons/")
async def get_all_items():
    #return liste.keys
       
    values = con.get_all_entries()

    #t = json.dumps(values)

    return values

@api.get("/addperson/{vorname},{nachname}")
async def create_item(vorname, nachname):
    
    return con.insert_into(vorname, nachname)
