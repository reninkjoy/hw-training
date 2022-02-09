import pandas as pd
import re
import json
error_log=[]
path=input("Enter the path of the csv separated semicolon\n")
source=input("Enter the Value of Source Field\n")
country=input("Enter the Country_Code Field\n")
imageu=input("Enter the Format of Image_url split with(|)\n")
df=pd.read_csv(path,keep_default_na=False,sep=";")
error_log.append({"Number of line without header":len(df)})
for i in range(len(df)):
    if df["product_id"][i]:
        df["product_id"][i]==df["catalog_id"][i]
        continue
    else:
        error_log.append({'error': 'product_id not equal to catalog_id', 'line_number': i + 2,"key":df["catalog_id"][i]})
for i in range(len(df)):
    if df["product_name"][i]:
        df["catalog_name"][i]==df["product_name"][i]
        continue
    else:
        error_log.append({'error': 'product_name not equal to catalog_name', 'line_number': i + 2,"key":df["catalog_name"][i]})
for i in range(len(df)):
    if df["source"][i]==source:
        continue
    else:
        error_log.append({'error': 'source not equal to amazon', 'line_number': i + 2,"key":df["source"][i]})
img="https?:\/\/.*\.(?:"+imageu+")"
image=re.compile(img)
for i in range(len(df)):
    if re.fullmatch(image, df["image_url"][i]):
        continue
    else:
        error_log.append({'error': 'not having jpg', 'line_number': i + 2,"key":df["image_url"][i]})
date=re.compile(r"\d*-\d*-\d* \d*:\d*:\d*")
for i in range(len(df)):
    if re.fullmatch(date, df["scraped_date"][i]):
        continue
    else:
        error_log.append({'error': 'scraped_date format change', 'line_number': i + 2,"key":df["scraped_date"][i]})
ch=re.compile("{.*?}")
for i in range(len(df)):
    if re.fullmatch(ch,df["category_hierarchy"][i]):
            continue
    elif df["category_hierarchy"][i]=="N/A":
        continue
    else:
        error_log.append({'error': 'category_hierarchy another value', 'line_number': i + 2, "key": df["category_hierarchy"][i]})

for i in range(len(df)):
    try:
        price=float(df["product_price"][i])
    except:
        if df["product_price"][i] == "N/A":
            continue
        else:
            error_log.append({'error': 'product_price another value', 'line_number': i + 2, "key": df["product_price"][i]})

for i in range(len(df)):
    if re.fullmatch(date, df["arrival_date"][i]):
        continue
    elif df["arrival_date"][i] =="N/A":
        continue
    else:
        error_log.append({'error': ' arrival_date another value', 'line_number': i + 2,"key":df["arrival_date"][i]})

for i in range(len(df)):
    try:
        price=float(df["shipping_charges"][i])
    except:
        error_log.append({'error': 'shipping_charges another value', 'line_number': i + 2, "key": df["shipping_charges"][i]})
for i in range(len(df)):
    if str(df["is_sold_out"][i])=="True":
        continue
    elif str(df["is_sold_out"][i])=="False":
        continue
    else:
        error_log.append({'error': 'is_sold_out another value', 'line_number': i + 2, "key":str(df["is_sold_out"][i])})
dis=re.compile("\d*?%")
for i in range(len(df)):
    if re.fullmatch(dis,df["discount"][i]):
        continue
    elif df["discount"][i]=="N/A":
        continue
    else:
        error_log.append({'error': 'discount another value', 'line_number': i + 2, "key": df["discount"][i]})
for i in range(len(df)):
    try:
        price=float(df["mrp"][i])
    except:
        if df["mrp"][i] == "N/A":
            continue
        else:
            error_log.append({'error': 'mrp another value', 'line_number': i + 2, "key": df["mrp"][i]})
for i in range(len(df)):
    if df["page_url"][i]=="N/A":
        continue
    else:
        error_log.append({'error': 'page_url another value', 'line_number': i + 2, "key": df["page_url"][i]})
for i in range(len(df)):
    if df["product_url"][i]:
        continue
    else:
        error_log.append({'error': 'product_url not have value', 'line_number': i + 2, "key": df["product_url"][i]})
for i in range(len(df)):
    try:
        price=int(df["number_of_ratings"][i])
    except:
        error_log.append({'error': 'number_of_ratings another value', 'line_number': i + 2, "key": df["number_of_ratings"][i]})
for i in range(len(df)):
    try:
        price=float(df["avg_rating"][i])
    except:
        error_log.append({'error': 'avg_rating another value', 'line_number': i + 2, "key": df["avg_rating"][i]})
for i in range(len(df)):
    if df["position"][i]:
        continue
    else:
        error_log.append({'error': 'position not have value', 'line_number': i + 2, "key": df["position"][i]})
for i in range(len(df)):
    if df["country_code"][i]==country:
        continue
    else:
        error_log.append({'error': 'country_code equal to IN', 'line_number': i + 2,"key":df["source"][i]})
for i in range(len(df)):
    if re.fullmatch(ch,df["others"][i]):
        continue
    else:
        error_log.append({'error': 'others has datatype value', 'line_number': i + 2, "key": df["others"][i]})


val=json.dumps(error_log)
with open("outfile.json","w")as f:
    f.write(json.dumps(json.loads(val),indent=4))
