import pandas as pd
import re
import json
error_log = []
def instr_procat(df):
    for i in range(len(df)):
        if df["product_id"][i]:
            df["product_id"][i] != df["catalog_id"][i]
            continue
        else:
            error_log.append(
                {'error': 'product_id not equal to catalog_id', 'line_number': i + 2, "key": f"{df['catalog_id'][i],df['product_id'][i]}"})
    for i in range(len(df)):
        if df["product_name"][i]:
            df["catalog_name"][i] != df["product_name"][i]
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
        if df["page_url"][i]=="N/A":
            continue
        else:
            error_log.append({'error': 'page_url another value', 'line_number': i + 2, "key": df["page_url"][i]})

def product_url(df):
    for i in range(len(df)):
        if df["product_url"][i]!=None:
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
            elif res['Prime']:
                if res["Prime"]=="1":
                    continue
                elif res["Prime"]=="0":
                    continue
                else:
                    error_log.append({'error': 'others Prime has another value', 'line_number': i + 2, "key":res['Prime']})

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

def instzerofield(df,field):
    for i in range(len(df)):
        if df[field][i]==0:
            continue
        else:
            error_log.append({'error': f"{field}not Zero", "line_number": i + 2, "key": df[field][i]})

def replace(df,field):
    for i in range(len(df)):
        if (str(df[field][i]).find("\n"))!=-1:
            continue
        elif (str(df[field][i]).find("\t"))!=-1:
            continue
        elif (str(df[field][i]).find("\r"))!=-1:
            continue
        elif (str(df[field][i]).find(re.search("<.*?>",df[field][i]))) != -1:
            continue
        else:
            error_log.append({'error': f"{field}has (/t,/r,/n)", "line_number": i + 2, "key": df[field][i]})

def amazon(df,country,imageu):
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
    page_url(df)
    product_url(df)
    number_of_ratings(df)
    avg_rating(df)
    position(df)
    country_code(df,country)
    others(df)


def flipkart(df,country,imageu):
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
    country_code(df,country)
    others(df)


def myntra(df,country,imageu):
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
    page_url(df)
    product_url(df)
    number_of_ratings(df)
    avg_rating(df)
    position(df)
    country_code(df,country)
    others(df)


def instragram(df,country,imageu):
    instr_procat(df)
    all_source(df,"instragram")
    country_code(df,country)
    for i in range(len(df.columns)):
        replace(df,df.columns[i])
    others(df)
    scrapdate(df)
    instzerofield(df,"shipping_charges")
    instzerofield(df, "avg_rating")
    NA(df,'category_hierarchy')
    NA(df,"product_price")
    NA(df,"is_sold_out")
    NA(df,"discount")
    NA(df,"mrp")
    NA(df,"position")

def snapdeal(df, country, imageu):
    return

def firstcry(df, country, imageu):
    return

if __name__ == "__main__":
    mode = input("Enter the amazon,flipkart,myntra,instragram,snapdeal,firstcry\n")
    path = input("Enter the path of the csv separated semicolon\n")
    country = input("Enter the Country_Code Field\n")
    imageu = input("Enter the Format of Image_url split with(|)\n")
    df = pd.read_csv(path, keep_default_na=False, sep=";",dtype=str)
    error_log.append({"Number of line without header": len(df)})
    if mode=="amazon":
        amazon(df,country,imageu)
    elif mode=="flipkart":
        flipkart(df,country,imageu)
    elif mode=="myntra":
        myntra(df,country,imageu)
    elif mode=="instragram":
        instragram(df,country,imageu)
    elif mode=="snapdeal":
        snapdeal(df,country,imageu)
    elif mode=="firstcry":
        firstcry(df,country,imageu)
    else:
        print("Error wrong mode")
    create(mode)
