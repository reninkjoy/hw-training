import pandas as pd
import re
import json
import os
error_log = []
info=[]

def create(filename,paths):
    final={"info":info,"error":error_log}
    final = json.dumps(final)
    filename=filename.split('.')[0]
    with open(paths+"_test.json","w")as f:
        f.write(json.dumps(json.loads(final), indent=4))

    print(f"File is created to {filename}_test.json")

def order(key,field,file):
    flag=0
    for i in range(len(field)):
        if key[i].strip() == field[i].strip():
            continue
        else:
            flag=1
            error_log.append({f"{file} Order spelling lowercase are not equal ": key[i]})
    return flag
def empty(df):
    empty=[]
    for field in df.columns:
        a=df[df[field] == ''].index
        if len(a)==len(df[field]):
            empty.append(field)
    return empty

def csv_write(filename,field,file):
    df = pd.read_csv(filename, keep_default_na=False, sep=",", dtype=str, na_filter=False)
    a=order(df.columns, field,file)
    emptys = empty(df)
    if a == 0:
        info.append({f"{file}":"ok","data count":len(df),"Empty fields":emptys})
    else:
        info.append({f"{file}":"fail"})

def audi(folder):
    towing_hitches_field=['URL','Website','Date & Time','Part number','Catalogue_price','Net_price','Stock','Brand','Input Category','Input Brand','Input Model','Model Selected','Engine','Input_Keyword','kit','Articulation','13 pins vs 7 pins','Description']
    floormats_field=['URL','Website','Date & Time','Part number','Catalogue_price','Net_price','Stock','Brand','Input Category','Input Brand','Input Model','Model Selected','Engine','Input_Keyword','Universel vs Specific','Position','Material','Description']
    bike_carriers_field=['URL','Website','Date & Time','Part number','Catalogue_price','Net_price','Stock','Brand','Input Category','Input Brand','Input Model','Model Selected','Engine','Input_Keyword','# bikes','Load Capacity','Extensible','Foldable','Description']
    crossbar_field=['URL','Website','Date & Time','Part number','Catalogue_price','Net_price','Stock','Brand','Input Category','Input Brand','Input Model','Model Selected','Engine','Input Roof_type','Input_Keyword','Universel vs Specific','With Lock','Load Capacity','Aerodynamic','Description']
    trunkliners_filed=['URL','Website','Date & Time','Part number','Catalogue_price','Net_price','Stock','Brand','Input Category','Input Brand','Input Model','Model Selected','Engine','Input_Keyword','Universel vs Specific','Format','Material','Description']
    skiboxes_field=['URL','Website','Date & Time','Part number','Catalogue_price','Net_price','Stock','Brand','Input Category','Input Brand','Input Model','Model Selected','Engine','Input_Keyword','Volume','Color','2-Sides Opening','Fixation Type','Description']
    csv=os.listdir(folder)
    for file in csv:
        print(file)
        if "towing_hitches" in file:
            csv_write(folder+"/"+file,towing_hitches_field,file)
        if "floormats" in file:
            csv_write(folder+"/"+file,floormats_field,file)
        if "bike_carriers" in file:
            csv_write(folder+"/"+file,bike_carriers_field,file)
        if "crossbar" in file:
            csv_write(folder+"/"+file,crossbar_field,file)
        if "trunkliners" in file:
            csv_write(folder+"/" + file,trunkliners_filed, file)
        if "skiboxes" in file:
            csv_write(folder+"/"+file,skiboxes_field,file)

def skoda(folder):
    towing_hitches_field=['URL','Website','Date & Time','Part number','Catalogue_price','Net_price','Stock','Brand','Input Category','Input Brand','Input Model','Model Selected','Engine','Input_Keyword','kit','Articulation','13 pins vs 7 pins','Description']
    floormats_field=['URL','Website','Date & Time','Part number','Catalogue_price','Net_price','Stock','Brand','Input Category','Input Brand','Input Model','Model Selected','Engine','Input_Keyword','Universel vs Specific','Position','Material','Description']
    bike_carriers_field=['URL','Website','Date & Time','Part number','Catalogue_price','Net_price','Stock','Brand','Input Category','Input Brand','Input Model','Model Selected','Engine','Input_Keyword','# bikes','Load Capacity','Extensible','Foldable','Description']
    crossbar_field=['URL','Website','Date & Time','Part number','Catalogue_price','Net_price','Stock','Brand','Input Category','Input Brand','Input Model','Model Selected','Engine','Input Roof_type','Input_Keyword','Universel vs Specific','With Lock','Load Capacity','Aerodynamic','Description']
    trunkliners_filed=['URL','Website','Date & Time','Part number','Catalogue_price','Net_price','Stock','Brand','Input Category','Input Brand','Input Model','Model Selected','Engine','Input_Keyword','Universel vs Specific','Format','Material','Description']
    skiboxes_field=['URL','Website','Date & Time','Part number','Catalogue_price','Net_price','Stock','Brand','Input Category','Input Brand','Input Model','Model Selected','Engine','Input_Keyword','Volume','Color','2-Sides Opening','Fixation Type','Description']
    csv=os.listdir(folder)
    for file in csv:
        print(file)
        if "towing_hitches" in file:
            csv_write(folder+"/"+file,towing_hitches_field,file)
        if "floormats" in file:
            csv_write(folder+"/"+file,floormats_field,file)
        if "bike_carriers" in file:
            csv_write(folder+"/"+file,bike_carriers_field,file)
        if "crossbar" in file:
            csv_write(folder+"/"+file,crossbar_field,file)
        if "trunkliners" in file:
            csv_write(folder + "/" + file,trunkliners_filed, file)
        if "skiboxes" in file:
            csv_write(folder+"/"+file,skiboxes_field,file)

def seat(folder):
    towing_hitches_field=['URL','Website','Date & Time','Part number','Catalogue_price','Net_price','Stock','Brand','Input Category','Input Brand','Input Model','Model Selected','Engine','Input_Keyword','kit','Articulation','13 pins vs 7 pins','Description']
    floormats_field=['URL','Website','Date & Time','Part number','Catalogue_price','Net_price','Stock','Brand','Input Category','Input Brand','Input Model','Model Selected','Engine','Input_Keyword','Universel vs Specific','Position','Material','Description']
    bike_carriers_field=['URL','Website','Date & Time','Part number','Catalogue_price','Net_price','Stock','Brand','Input Category','Input Brand','Input Model','Model Selected','Engine','Input_Keyword','# bikes','Load Capacity','Extensible','Foldable','Description']
    crossbar_field=['URL','Website','Date & Time','Part number','Catalogue_price','Net_price','Stock','Brand','Input Category','Input Brand','Input Model','Model Selected','Engine','Input Roof_type','Input_Keyword','Universel vs Specific','With Lock','Load Capacity','Aerodynamic','Description']
    trunkliners_filed=['URL','Website','Date & Time','Part number','Catalogue_price','Net_price','Stock','Brand','Input Category','Input Brand','Input Model','Model Selected','Engine','Input_Keyword','Universel vs Specific','Format','Material','Description']
    skiboxes_field=['URL','Website','Date & Time','Part number','Catalogue_price','Net_price','Stock','Brand','Input Category','Input Brand','Input Model','Model Selected','Engine','Input_Keyword','Volume','Color','2-Sides Opening','Fixation Type','Description']
    csv=os.listdir(folder)
    for file in csv:
        print(file)
        if "towing_hitches" in file:
            csv_write(folder+"/"+file,towing_hitches_field,file)
        if "floormats" in file:
            csv_write(folder+"/"+file,floormats_field,file)
        if "bike_carriers" in file:
            csv_write(folder+"/"+file,bike_carriers_field,file)
        if "crossbar" in file:
            csv_write(folder+"/"+file,crossbar_field,file)
        if "trunkliners" in file:
            csv_write(folder + "/" + file,trunkliners_filed, file)
        if "skiboxes" in file:
            csv_write(folder+"/"+file,skiboxes_field,file)

def volkswagen(folder):
    towing_hitches_field=['URL','Website','Date & Time','Part number','Catalogue_price','Net_price','Stock','Brand','Input Category','Input Brand','Input Model','Model Selected','Engine','Input_Keyword','kit','Articulation','13 pins vs 7 pins','Description']
    floormats_field=['URL','Website','Date & Time','Part number','Catalogue_price','Net_price','Stock','Brand','Input Category','Input Brand','Input Model','Model Selected','Engine','Input_Keyword','Universel vs Specific','Position','Material','Description']
    bike_carriers_field=['URL','Website','Date & Time','Part number','Catalogue_price','Net_price','Stock','Brand','Input Category','Input Brand','Input Model','Model Selected','Engine','Input_Keyword','# bikes','Load Capacity','Extensible','Foldable','Description']
    crossbar_field=['URL','Website','Date & Time','Part number','Catalogue_price','Net_price','Stock','Brand','Input Category','Input Brand','Input Model','Model Selected','Engine','Input Roof_type','Input_Keyword','Universel vs Specific','With Lock','Load Capacity','Aerodynamic','Description']
    trunkliners_filed=['URL','Website','Date & Time','Part number','Catalogue_price','Net_price','Stock','Brand','Input Category','Input Brand','Input Model','Model Selected','Engine','Input_Keyword','Universel vs Specific','Format','Material','Description']
    skiboxes_field=['URL','Website','Date & Time','Part number','Catalogue_price','Net_price','Stock','Brand','Input Category','Input Brand','Input Model','Model Selected','Engine','Input_Keyword','Volume','Color','2-Sides Opening','Fixation Type','Description']
    csv=os.listdir(folder)
    for file in csv:
        print(file)
        if "towing_hitches" in file:
            csv_write(folder+"/"+file,towing_hitches_field,file)
        if "floormats" in file:
            csv_write(folder+"/"+file,floormats_field,file)
        if "bike_carriers" in file:
            csv_write(folder+"/"+file,bike_carriers_field,file)
        if "crossbar" in file:
            csv_write(folder+"/"+file,crossbar_field,file)
        if "trunkliners" in file:
            csv_write(folder + "/" + file,trunkliners_filed, file)
        if "skiboxes" in file:
            csv_write(folder+"/"+file,skiboxes_field,file)

def autoonderdelen24(folder):
    towing_hitches_field=['URL','Website','Date & Time','Part number','Catalogue price','Net price','Stock','Brand','Input Category','Input Brand','Input Model','Model Selected','Engine','Input Keyword','kit','Articulation','13 pins vs 7 pins','Description']
    floormats_field=['URL','Website','Date & Time','Part number','Catalogue price','Net price','Stock','Brand','Input Category','Input Brand','Input Model','Model Selected','Engine','Input Keyword','Universel vs Specific','Position','Material','Description']
    bike_carriers_field=['URL','Website','Date & Time','Part number','Catalogue price','Net price','Stock','Brand','Input Category','Input Brand','Input Model','Model Selected','Engine','Input Keyword','# bikes','Load Capacity','Extensible','Foldable','Description']
    crossbar_field=['URL','Website','Date & Time','Part number','Catalogue price','Net price','Stock','Brand','Input Category','Input Brand','Input Model','Input Year/Type(model selected)','Engine','Input Roof_type','Input Keyword','Universel vs Specific','With Lock','Load Capacity','Aerodynamic','Description']
    trunkliners_filed=['URL','Website','Date & Time','Part number','Catalogue price','Net price','Stock','Brand','Input Category','Input Brand','Input Model','Model Selected','Engine','Input Keyword','Universel vs Specific','Format','Material','Description']
    skiboxes_field=['URL','Website','Date & Time','Part number','Catalogue price','Net price','Stock','Brand','Input Category','Input Brand','Input Model','Input Year/Type(model selected)','Engine','Input Keyword','Volume','Color','2-Sides Opening','Fixation Type','Description']
    csv=os.listdir(folder)
    for file in csv:
        print(file)
        if "towing_hitches" in file:
            csv_write(folder+"/"+file,towing_hitches_field,file)
        if "floormats" in file:
            csv_write(folder+"/"+file,floormats_field,file)
        if "bike_carriers" in file:
            csv_write(folder+"/"+file,bike_carriers_field,file)
        if "crossbar" in file:
            csv_write(folder+"/"+file,crossbar_field,file)
        if "trunkliners" in file:
            csv_write(folder + "/" + file,trunkliners_filed, file)
        if "skiboxes" in file:
            csv_write(folder+"/"+file,skiboxes_field,file)

def rameder(folder):
    towing_hitches_field=['URL','Website','Date & Time','Part number','Catalogue price','Net price','Stock','Brand','Input Category','Input Brand','Input Model','Model Selected','Engine','Input Keyword','kit','Articulation','13 pins vs 7 pins','Description']
    floormats_field=['URL','Website','Date & Time','Part number','Catalogue price','Net price','Stock','Brand','Input Category','Input Brand','Input Model','Model Selected','Engine','Input Keyword','Universel vs Specific','Position','Material','Description']
    bike_carriers_field=['URL','Website','Date & Time','Part number','Catalogue price','Net price','Stock','Brand','Input Category','Input Brand','Input Model','Model Selected','Engine','Input Keyword','# bikes','Load Capacity','Extensible','Foldable','Description']
    crossbar_field=['URL','Website','Date & Time','Part number','Catalogue price','Net price','Stock','Brand','Input Category','Input Brand','Input Model','Input Year/Type(model selected)','Engine','Input Roof_type','Input Keyword','Universel vs Specific','With Lock','Load Capacity','Aerodynamic','Description']
    trunkliners_filed=['URL','Website','Date & Time','Part number','Catalogue price','Net price','Stock','Brand','Input Category','Input Brand','Input Model','Model Selected','Engine','Input Keyword','Universel vs Specific','Format','Material','Description']
    csv=os.listdir(folder)
    for file in csv:
        print(file)
        if "towing_hitches" in file:
            csv_write(folder+"/"+file,towing_hitches_field,file)
        if "floormats" in file:
            csv_write(folder+"/"+file,floormats_field,file)
        if "bike_carriers" in file:
            csv_write(folder+"/"+file,bike_carriers_field,file)
        if "crossbar" in file:
            csv_write(folder+"/"+file,crossbar_field,file)
        if "trunkliners" in file:
            csv_write(folder + "/" + file,trunkliners_filed, file)

def dakkofferstore(folder):
    crossbar_field=['URL','Website','Date & Time','Part number','Catalogue price','Net price','Stock','Brand','Input Category','Input Brand','Input Model','Input Year/Type(model selected)','Engine','Input Roof_type','Input Keyword','Universel vs Specific','With Lock','Load Capacity','Aerodynamic','Description']
    csv=os.listdir(folder)
    for file in csv:
        print(file)
        if "crossbar" in file:
            csv_write(folder+"/"+file,crossbar_field,file)

def bol(folder):
    towing_hitches_field=['URL','Website','Date & Time','Part number','Catalogue price','Net price','Stock','Brand','Input Category','Input Brand','Input Model','Model Selected','Engine','Input Keyword','kit','Articulation','13 pins vs 7 pins','Description']
    floormats_field=['URL','Website','Date & Time','Part number','Catalogue price','Net price','Stock','Brand','Input Category','Input Brand','Input Model','Model Selected','Engine','Input Keyword','Universel vs Specific','Position','Material','Description']
    bike_carriers_field=['URL','Website','Date & Time','Part number','Catalogue price','Net price','Stock','Brand','Input Category','Input Brand','Input Model','Model Selected','Engine','Input Keyword','# bikes','Load Capacity','Extensible','Foldable','Description']
    crossbar_field=['URL','Website','Date & Time','Part number','Catalogue price','Net price','Stock','Brand','Input Category','Input Brand','Input Model','Input Year/Type(model selected)','Engine','Input Roof_type','Input Keyword','Universel vs Specific','With Lock','Load Capacity','Aerodynamic','Description']
    trunkliners_filed=['URL','Website','Date & Time','Part number','Catalogue price','Net price','Stock','Brand','Input Category','Input Brand','Input Model','Model Selected','Engine','Input Keyword','Universel vs Specific','Format','Material','Description']
    skiboxes_field=['URL','Website','Date & Time','Part number','Catalogue price','Net price','Stock','Brand','Input Category','Input Brand','Input Model','Input Year/Type(model selected)','Engine','Input Keyword','Volume','Color','2-Sides Opening','Fixation Type','Description']
    csv=os.listdir(folder)
    for file in csv:
        print(file)
        if "towing_hitches" in file:
            csv_write(folder+"/"+file,towing_hitches_field,file)
        if "floormats" in file:
            csv_write(folder+"/"+file,floormats_field,file)
        if "bike_carriers" in file:
            csv_write(folder+"/"+file,bike_carriers_field,file)
        if "crossbar" in file:
            csv_write(folder+"/"+file,crossbar_field,file)
        if "trunkliners" in file:
            csv_write(folder + "/" + file,trunkliners_filed, file)
        if "skiboxes" in file:
            csv_write(folder+"/"+file,skiboxes_field,file)

def auto5(folder):
    towing_hitches_field=['URL','Website','Date & Time','Part number','Catalogue price','Net price','Stock','Brand','Input Category','Input Brand','Input Model',' Model Selected','Engine','Input Keyword','kit','Articulation ','13 pins vs 7 pins','Description']
    floormats_field=['URL','Website','Date & Time','Part number','Catalogue price','Net price','Stock','Brand','Input Category','Input Brand','Input Model',' Model Selected','Engine','Input Keyword','Universel vs Specific','Position','Material','Description']
    bike_carriers_field=['URL','Website','Date & Time','Part number','Catalogue price','Net price','Stock','Brand','Input Category','Input Brand','Input Model',' Model Selected','Engine','Input Keyword','# bikes',' Load Capacity','Extensible','Foldable','Description']
    crossbar_field=['URL','Website','Date & Time','Part number','Catalogue price','Net price','Stock','Brand','Input Category','Input Brand','Input Model',' Model Selected','Engine','Input Roof_type','Input Keyword','Universel vs Specific','With Lock','Load Capacity','Aerodynamic','Description']
    trunkliners_filed=['URL','Website','Date & Time','Part number','Catalogue price','Net price','Stock','Brand','Input Category','Input Brand','Input Model',' Model Selected','Engine','Input Keyword','Universel vs Specific','Format','Material','Description']
    skiboxes_field=['URL','Website','Date & Time','Part number','Catalogue price','Net price','Stock','Brand','Input Category','Input Brand','Input Model',' Model Selected','Engine','Input Keyword','Volume','Color','2-Sides Opening','Fixation Type','Description']
    csv=os.listdir(folder)
    for file in csv:
        print(file)
        if "towing_hitches" in file:
            csv_write(folder+"/"+file,towing_hitches_field,file)
        if "floormats" in file:
            csv_write(folder+"/"+file,floormats_field,file)
        if "bike_carriers" in file:
            csv_write(folder+"/"+file,bike_carriers_field,file)
        if "crossbar" in file:
            csv_write(folder+"/"+file,crossbar_field,file)
        if "trunkliners" in file:
            csv_write(folder + "/" + file,trunkliners_filed, file)
        if "skiboxes" in file:
            csv_write(folder+"/"+file,skiboxes_field,file)

if __name__ == "__main__":
    paths=input("Enter the path folder\n")
    dir=paths.split("/")[-1]

    if dir in 'audi':
        audi(paths)
    elif dir in 'skoda':
        skoda(paths)
    elif dir in 'seat':
        seat(paths)
    elif dir in 'volkswagen':
        volkswagen(paths)
    elif dir in 'auto5be':
        auto5(paths)
    elif dir in 'bol':
        bol(paths)
    elif dir in 'dakkofferstore':
        dakkofferstore(paths)
    elif dir in 'rameder':
        rameder(paths)
    elif dir in 'autoonderdelen24be':
        autoonderdelen24(paths)
    else:
        print("folder name error(audi, skoda, seat, volkswagen, auto5be, bol, dakkofferstore, rameder, autoonderdelen24be)")
        print('check the path')

    create(dir,paths)