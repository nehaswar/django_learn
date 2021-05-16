from django.shortcuts import render
import requests
import json
from petrol.models import Petroleum_data

def home(request):
    template_name = "index.html"
    content = {"name": "Petrol data"}
    response = requests.get("https://raw.githubusercontent.com/younginnovations/internship-challenges/master/programming/petroleum-report/data.json")
    petrol_response = response.json()
    
   
    for data in petrol_response:

        petrol_data, created = Petroleum_data.objects.get_or_create(year=data["year"], petroleum_product=data["petroleum_product"], sale =data["sale"], country =data["country"])
        # print(created)
        if created:
            petrol_data.save()
   
    countries = Petroleum_data.objects.values("country","petroleum_product").distinct()
    years = Petroleum_data.objects.values("year").distinct()
    products = Petroleum_data.objects.values("petroleum_product").distinct()
    

    
    question_1=[]
    for e in countries:
        data = Petroleum_data.objects.all().filter(country= e["country"]).filter(petroleum_product = e["petroleum_product"])
        
        sol_1 =[ ]
        for x in data:
            
            if x.sale !=0:
                sol_1.append(x)

       
        total_sales = 0
        for s in sol_1:
            total_sales = total_sales + s.sale
           
        question_1.append({"country":e["country"],"petroleum_product":e["petroleum_product"], "total_sales":total_sales})
    question_2 =[]
    for e in products:
        print(len(years))
        for count, value in enumerate(years, start=0):
            print(count)
            print(len(years))
            if(count== len(years)-1):
                break
        
            else:
                print('sss')
                # print(count+1)
                b= years[count+1]
                y = Petroleum_data.objects.all().filter(year__lte=value["year"],year__gte=b["year"]).filter(petroleum_product = e["petroleum_product"])
                t=0
                for sales_data in y:
                    t = t+ sales_data.sale
                
                question_2.append({"year1":b["year"], "year2": value["year"],"petroleum_product":e["petroleum_product"],"sales":t/2 })

    question_3=[]
    for f in products:
        least_sale = {}
        sale_each= []
        for e in years:
            year_data = Petroleum_data.objects.all().filter(year = e["year"]).filter(petroleum_product = f["petroleum_product"])
            sol_2 =0
            for x in year_data:
                sol_2 = sol_2 + x.sale
            if sol_2 != 0:
                sale_each.append({"year":e["year"],"total":sol_2})
                
        
        for s in sale_each:
            if(len(least_sale)==0):
                least_sale = {"year":s["year"],"total":s["total"]}
                
            elif(least_sale["total"]>s["total"]):
                least_sale = {"year":s["year"],"total":s["total"]}
        question_3.append({"year":least_sale["year"], "petroleum_product": f["petroleum_product"],"least_sale":least_sale["total"]})
    
    return render(request, template_name, {"question1": question_1,"question_2":question_2,"question_3":question_3})



    