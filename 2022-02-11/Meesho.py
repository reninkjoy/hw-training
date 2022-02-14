import pandas as pd
import re
import json
error_log = []

def instr_procat(df):
    for i in range(len(df)):
        if df["product_id"][i] != df["catalog_id"][i]:
            continue
        else:
            error_log.append({'error': 'product_id not equal to catalog_id', 'line_number': i + 2, "key": f"{df['catalog_id'][i],df['product_id'][i]}"})
    for i in range(len(df)):
        if df["catalog_name"][i] != df["product_name"][i]:
            continue
        else:
            error_log.append({'error': 'product_name not equal to catalog_name', 'line_number': i + 2,"key":f"{df['catalog_name'][i],df['product_name'][i]}"})

def amazon_procat(df):
    for i in range(len(df)):
        if df["product_id"][i]:
            df["product_id"][i]==df["catalog_id"][i]
            continue
        else:
            error_log.append({'error': 'product_id not equal to catalog_id', 'line_number': i + 2,"key": f"{df['catalog_id'][i],df['product_id'][i]}"})
    for i in range(len(df)):
        if df["product_name"][i]:
            df["catalog_name"][i]==df["product_name"][i]
            continue
        else:
            error_log.append({'error': 'product_name not equal to catalog_name', 'line_number': i + 2,"key":f"{df['catalog_name'][i],df['product_name'][i]}"})

def all_source(source,df):
    for i in range(len(df)):
        if df["source"][i]==source:
            continue
        else:
            error_log.append({'error': 'source not equal to amazon', 'line_number': i + 2,"key":df["source"][i]})

def img(imageu,df):
    image=re.compile("https?:\/\/.*\.(?:"+imageu+")")
    for i in range(len(df)):
        if re.fullmatch(image, df["image_url"][i]):
            continue
        else:
            error_log.append({'error': f'not having {imageu} ', 'line_number': i + 2,"key":df["image_url"][i]})

def scrapdate(df):
    date=re.compile(r"\d*-\d*-\d* \d*:\d*:\d*")
    for i in range(len(df)):
        if re.fullmatch(date, df["scraped_date"][i]):
            continue
        else:
            error_log.append({'error': 'scraped_date format change', 'line_number': i + 2,"key":df["scraped_date"][i]})

def category_hierarchy(df):
    ch=re.compile("{.*?}")
    for i in range(len(df)):
        if re.fullmatch(ch,df["category_hierarchy"][i]):
            continue
        elif df["category_hierarchy"][i]=="N/A":
            continue
        else:
            error_log.append({'error': 'category_hierarchy another value', 'line_number': i + 2, "key": df["category_hierarchy"][i]})

def product_price(df):
    price=re.compile("\d*.\d*")
    for i in range(len(df)):
        try:
            if re.fullmatch(price,df["product_price"][i]):
                continue
        except:
            if df["product_price"][i] == "N/A":
                continue
            else:
                error_log.append({'error': 'product_price another value', 'line_number': i + 2, "key": df["product_price"][i]})

def arrival_date(df):
    date = re.compile(r"\d*-\d*-\d* \d*:\d*:\d*")
    for i in range(len(df)):
        if re.fullmatch(date, df["arrival_date"][i]):
            continue
        elif df["arrival_date"][i] =="N/A":
            continue
        else:
            error_log.append({'error': ' arrival_date another value', 'line_number': i + 2,"key":df["arrival_date"][i]})

def flip_shipping_charges(df):
    price=re.compile("\d*")
    for i in range(len(df)):
        if re.fullmatch(price,df["shipping_charges"][i]):
            continue
        else:
            error_log.append(
                {'error': 'shipping_charges another value', 'line_number': i + 2, "key": df["shipping_charges"][i]})

def shipping_charges(df):
    price=re.compile("\d*.\d*")
    for i in range(len(df)):
        if re.fullmatch(price, df["shipping_charges"][i]):
            continue
        else:
            error_log.append({'error': 'shipping_charges another value', 'line_number': i + 2, "key": df["shipping_charges"][i]})

def is_sold_out(df):
    for i in range(len(df)):
        if df["is_sold_out"][i]=="true":
            continue
        elif df["is_sold_out"][i]=="false":
            continue
        else:
            error_log.append({'error': 'is_sold_out another value', 'line_number': i + 2, "key":df["is_sold_out"][i]})

def discount(df):
    dis=re.compile("\d*?%")
    for i in range(len(df)):
        if re.fullmatch(dis,df["discount"][i]):
            continue
        elif df["discount"][i]=="N/A":
            continue
        else:
            error_log.append({'error': 'discount another value', 'line_number': i + 2, "key": df["discount"][i]})

def mrp(df):
    price=re.compile("\d*.\d*")
    for i in range(len(df)):
        try:
            if re.fullmatch(price,df["mrp"][i]):
                continue
        except:
            if df["mrp"][i] == "N/A":
                continue
            else:
                    error_log.append({'error': 'mrp another value', 'line_number': i + 2, "key": df["mrp"][i]})

def page_url(df):
    for i in range(len(df)):
        if df["page_url"][i]=='':
            continue
        else:
            error_log.append({'error': 'page_url another value', 'line_number': i + 2, "key": df["page_url"][i]})

def product_url(df):
    for i in range(len(df)):
        if df["product_url"][i]!='':
            continue
        else:
            error_log.append({'error': 'product_url not have value', 'line_number': i + 2, "key": df["product_url"][i]})

def number_of_ratings(df):
    price=re.compile("\d*")
    for i in range(len(df)):
        try:
            if re.fullmatch(price,df["number_of_ratings"][i]):
                continue
        except:
            error_log.append({'error': 'number_of_ratings another value', 'line_number': i + 2, "key": df["number_of_ratings"][i]})

def avg_rating(df):
    price=re.compile("\d*.\d*")
    for i in range(len(df)):
        if re.fullmatch(price, df["avg_rating"][i]):
            continue
        else:
            error_log.append({'error': 'avg_rating another value', 'line_number': i + 2, "key": df["avg_rating"][i]})

def position(df):
    for i in range(len(df)):
        if df["position"][i]=='':
            error_log.append({'error': 'position not have value', 'line_number': i + 2, "key": df["position"][i]})
        else:
            continue

def country_code(df,country):
    for i in range(len(df)):
        if df["country_code"][i]==country:
            continue
        else:
            error_log.append({'error': 'country_code equal to IN', 'line_number': i + 2,"key":df["country_code"][i]})

def others(df):
    ch = re.compile("{.*?}")
    for i in range(len(df)):
        if re.fullmatch(ch,df["others"][i]):
            res=json.loads(df["others"][i])
            if "null" in res.values():
                error_log.append({'error': 'others has null value', 'line_number': i + 2, "key": df["others"][i]})#prime
            elif "None" in res.values():
                error_log.append({'error': 'others has none value', 'line_number': i + 2, "key": df["others"][i]})
            try:
                if res["Prime"]=="1":
                    continue
                elif res["Prime"]=="0":
                    continue
                else:
                    error_log.append({'error': 'others Prime has another value', 'line_number': i + 2, "key":res['Prime']})
            except:
                a=0
        else:
            error_log.append({'error': 'others has datatype value', 'line_number': i + 2, "key": df["others"][i]})

def create(filename):
    val=json.dumps(error_log)
    with open(filename+"_test.json","w")as f:
        f.write(json.dumps(json.loads(val),indent=4))
    print("File is created")

def NA(df,field):
    for i in range(len(df)):
        if df[field][i] == "N/A":
            continue
        else:
                error_log.append({'error':f"{field}has another values","line_number": i+2, "key": df[field][i]})

def zerofield(df,field):
    for i in range(len(df)):
        if df[field][i]=="0":
            continue
        else:
            error_log.append({'error': f"{field} not Zero", "line_number": i + 2, "key": df[field][i]})

def detect(df,field):
    for i in range(len(df)):
        if "\\n" in str(df[field][i]):
            error_log.append({'error': f"{field} has (/n)", "line_number": i + 2, "key": df[field][i]})
        elif "\\t" in str(df[field][i]):
            error_log.append({'error': f"{field} has (/t)", "line_number": i + 2, "key": df[field][i]})
        elif "\\r" in str(df[field][i]):
            error_log.append({'error': f"{field} has (/r)", "line_number": i + 2, "key": df[field][i]})
        # elif "<" in str(df[field][i]):
        #     error_log.append({'error': f"{field} has (tags)", "line_number": i + 2, "key": df[field][i]})

def empty_values(df,field):
    for i in range(len(df)):
        if df[field][i]=='':
            error_log.append({'error': f"{field} has Empty values", "line_number": i + 2, "key": df[field][i]})

def amazon(df,imageu):
    for i in range(len(df.columns)):
        detect(df,str(df.columns[i]))
        empty_values(df,str(df.columns[i]))
    amazon_procat(df)
    all_source("amazon",df)
    scrapdate(df)
    img(imageu,df)
    category_hierarchy(df)
    product_price(df)
    arrival_date(df)
    shipping_charges(df)
    is_sold_out(df)
    discount(df)
    mrp(df)
    NA(df,"page_url")
    product_url(df)
    number_of_ratings(df)
    avg_rating(df)
    position(df)
    country_code(df,"IN")
    others(df)

def flipkart(df,imageu):
    for i in range(len(df.columns)):
        detect(df,str(df.columns[i]))
        empty_values(df, str(df.columns[i]))
    amazon_procat(df)
    all_source("flipkart",df)
    scrapdate(df)
    img(imageu,df)
    category_hierarchy(df)
    product_price(df)
    NA(df,'arrival_date')
    flip_shipping_charges(df)
    is_sold_out(df)
    discount(df)
    mrp(df)
    NA(df,'page_url')
    product_url(df)
    number_of_ratings(df)
    avg_rating(df)
    position(df)
    country_code(df,"IN")
    others(df)

def myntra(df,imageu):
    for i in range(len(df.columns)):
        detect(df,str(df.columns[i]))
        empty_values(df, str(df.columns[i]))
    amazon_procat(df)
    all_source("myntra",df)
    scrapdate(df)
    img(imageu,df)
    category_hierarchy(df)
    product_price(df)
    arrival_date(df)
    shipping_charges(df)
    is_sold_out(df)
    discount(df)
    mrp(df)
    NA(df,'page_url')
    product_url(df)
    number_of_ratings(df)
    avg_rating(df)
    position(df)
    country_code(df,"IN")
    others(df)

def instagram(df,imageu):
    for i in range(len(df.columns)):
        detect(df,str(df.columns[i]))
        empty_values(df, str(df.columns[i]))
    instr_procat(df)
    all_source("instagram",df)
    scrapdate(df)
    country_code(df,"IN")
    img(imageu,df)
    NA(df,'category_hierarchy')
    NA(df,"product_price")
    zerofield(df,"shipping_charges")
    arrival_date(df)
    NA(df,"is_sold_out")
    NA(df,"discount")
    NA(df,"mrp")
    page_url(df)
    product_url(df)
    number_of_ratings(df)
    zerofield(df, "avg_rating")
    NA(df,"position")
    country_code(df,"IN")
    others(df)

def snapdeal(df,imageu):
    for i in range(len(df.columns)):
        detect(df,str(df.columns[i]))
        empty_values(df, str(df.columns[i]))
    amazon_procat(df)
    all_source( "snapdeal",df)
    NA(df,"arrival_date")
    NA(df,"page_url")
    country_code(df,"IN")
    others(df)
    scrapdate(df)
    zerofield(df,"shipping_charges")

def firstcry(df,imageu):
    for i in range(len(df.columns)):
        detect(df,str(df.columns[i]))
        empty_values(df, str(df.columns[i]))
    amazon_procat(df)
    all_source("firstcry",df)
    scrapdate(df)
    img(imageu,df)
    category_hierarchy(df)
    product_price(df)
    NA(df,"arrival_date")
    flip_shipping_charges(df)
    is_sold_out(df)
    discount(df)
    mrp(df)
    NA(df,"page_url")
    product_url(df)
    number_of_ratings(df)
    avg_rating(df)
    position(df)
    country_code(df,"IN")
    others(df)

def order(key,field):
    a=0
    for i in range(len(field)):
        if key[i] == field[i]:
            continue
        else:
            a=1
            error_log.append({"Order spelling lowercase are not equal ": key[i]})
    return a

if __name__ == "__main__":
    mode = input("Enter the amazon, flipkart, myntra, instagram, snapdeal, firstcry\n")
    path = input("Enter the path of the csv separated semicolon\n")

    imageu = input("Enter the Format of Image_url split with(|)\n")
    df = pd.read_csv(path, keep_default_na=False, sep=";",dtype=str,na_filter=False)
    error_log.append({"Number of line without header": len(df)})
    field = ["product_id", "catalog_name", "catalog_id", "source", "scraped_date", "product_name", "image_url",
             "category_hierarchy", "product_price", "arrival_date", "shipping_charges", "is_sold_out", "discount",
             "mrp", "page_url", "product_url", "number_of_ratings", "avg_rating", "position", "country_code",
             "others"]
    if mode=="amazon":
        a=order(df.columns,field)
        if a == 0:
            amazon(df,imageu)

    elif mode=="flipkart":
        a = order(df.columns, field)
        if a == 0:
            flipkart(df,imageu)

    elif mode=="myntra":
        a = order(df.columns, field)
        if a == 0:
            myntra(df,imageu)

    elif mode=="instagram":
        a = order(df.columns, field)
        if a == 0:
            instagram(df,imageu)
    elif mode=="snapdeal":
        a = order(df.columns, field)
        if a == 0:
            snapdeal(df,imageu)

    elif mode=="firstcry":
        a = order(df.columns, field)
        if a == 0:
            firstcry(df,imageu)

    else:
        print("Error wrong mode")
    create(mode)

