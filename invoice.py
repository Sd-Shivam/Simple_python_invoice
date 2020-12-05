
from datetime import date
from datetime import datetime
today = date.today()
date=today.strftime("%b-%d-%Y")
now = datetime.now()
time = now.strftime("%H:%M:%S")


logo='''
██████╗ ██╗  ██╗ █████╗ ██████╗  █████╗ ████████╗███╗   ███╗ ██████╗ ██████╗ ██╗██╗     ███████╗███████╗
██╔══██╗██║  ██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝████╗ ████║██╔═══██╗██╔══██╗██║██║     ██╔════╝██╔════╝
██████╔╝███████║███████║██████╔╝███████║   ██║   ██╔████╔██║██║   ██║██████╔╝██║██║     █████╗  ███████╗
██╔══██╗██╔══██║██╔══██║██╔══██╗██╔══██║   ██║   ██║╚██╔╝██║██║   ██║██╔══██╗██║██║     ██╔══╝  ╚════██║
██████╔╝██║  ██║██║  ██║██║  ██║██║  ██║   ██║   ██║ ╚═╝ ██║╚██████╔╝██████╔╝██║███████╗███████╗███████║
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚═╝ ╚═════╝ ╚═════╝ ╚═╝╚══════╝╚══════╝╚══════╝
                                                         website:- www.bharatphonix.com
'''
print(logo)
print("Hello Sir, Welcome to bharatMobile invoice program"+"\n")
clear_prd=open("log\\product.ss",'w')
clear_prd.write(" ")
clear_prd.close()
id1=open("log\\invoice.id",'r')
invoiceid=id1.read()
id1.close()
id2=open("log\\invoice.id",'w')
id3=int(invoiceid) + 1
id2.write(str(id3))
id2.close()
Customer_id=invoiceid
Customer_name=input("Please type Customer Name:-")
Customer_contact=str(input("Please Type Customer Contact Mobile Number:-"))
Customer_addr=input("Please Type Customer Address:-")
Customer_mode=input("Please Mode of payment done by customer:-")
customer_detail_html='''
 <main>
  <div class="row">
    <div class="col-sm-6"><strong>Date & Time:</strong> '''+str(date)+ "   " + str(time) +'''</div>
    <div class="col-sm-6 text-sm-right"> <strong>Invoice No:</strong>#00'''+str(invoiceid)+'''</div>
  </div>
  <hr>
  <div class="row">
    <div class="col-sm-6 text-sm-right order-sm-1"> <strong>Pay To:</strong>
      <address>
      BharatMobile Store<br/>
      near state bank<br/>
      274203, Hata , Kushinager<br/>
      help@bharatphonix.com
      </address>
    </div>
    <div class="col-sm-6 order-sm-0"> <strong>Invoiced To:</strong>
      <address>
      '''+str(Customer_name)+'''<br /> +91-
     '''+str(Customer_contact)+'''<br />
      '''+str(Customer_addr)+'''<br />
     <div class=""> <strong>Payment Mode:</strong> '''+str(Customer_mode)+'''</div>
      </address>
    </div>
  </div> 
   <div class="card">
    <div class="card-body px-2" style="padding-top: 0px; padding-bottom: 0px;">
      <div class="table-responsive">
        <table class="table">
          <tbody>
          <tr>
            <th class="col-3 border-0"  style="padding-left: 11px;padding-top: 16px;"><strong>Products</strong></th>
            <th class="col-4 border-0" style="padding-left: 11px;padding-top: 16px;"><strong>Description</strong></th>
            <th class="col-2 text-center border-0" style="padding-left: 11px;padding-top: 16px;"><strong>Rate</strong></th>
            <th class="col-1 text-center border-0" style="padding-left: 11px;padding-top: 16px;"><strong>Quantity</strong></th>
            <th class="col-2 text-right border-0" style="padding-left: 11px;padding-top: 16px;"><strong>Amount</strong></th>
          </tr>
'''



Customer_order=int(input("Please Type The number of items:-"))
products_record=" "
t_amount=0
i=1
while(i<=Customer_order):
  prod_name=input("Please type the "+ str(i) +" product Name:-")
  prod_des=input("Please type the "+ str(i) +" product description:-")
  prod_rate=int(input("Please type the "+ str(i) +" product Rate:-"))
  prod_quantity=int(input("Please type the "+ str(i) +" product Quantity:-"))
  prod_total=prod_rate*prod_quantity
  t_amount=t_amount+int(prod_total)
  products_record=str(products_record)+str("{"+str(prod_name)+","+str(prod_des)+","+str(prod_rate)+","+str(prod_quantity)+","+str(prod_total)+"}")
  html_tr_code=''' <tr>
            <td>'''+str(prod_name)+'''</td>
            <td class="text-1">'''+str(prod_des)+'''</td>
            <td class="text-center">'''+str(prod_rate)+'''</td>
            <td class="text-center">'''+str(prod_quantity)+'''</td>
            <td class="text-right">'''+str(prod_total)+'''</td>
          </tr>
          '''
  log_products=open("log\\product.ss",'a',encoding="utf-8")
  log_products.write(str(html_tr_code))
  log_products.close()
  i=i+1


total_html='''<tr>
              <td colspan="4" class="bg-light-2 text-right"><strong>Sub Total:</strong></td>
              <td class="bg-light-2 text-right">'''+str(u"\u20B9")+str(t_amount)+'''</td>
            </tr>
            <tr>
              <td colspan="4" class="bg-light-2 text-right"><strong>Tax:</strong></td>
              <td class="bg-light-2 text-right">'''+str(u"\u20B9")+'''00.00</td>
            </tr>
            <tr>
              <td colspan="4" class="bg-light-2 text-right"><strong>Total:</strong></td>
              <td class="bg-light-2 text-right">'''+str(u"\u20B9")+str(t_amount)+'''</td>
            </tr>
    '''

def html(data):
    f=open('print_invoice.html','w',encoding="utf-8")
    body=open('log\\body.ss','r')
    b1=str(body.read())
    footer=open('log\\footer.ss','r')
    f1=str(footer.read())
    tr_data=open("log\\product.ss",'r')
    main_contant=tr_data.read()
    code_html=(b1 + data + main_contant+ total_html + f1)
    f.write(code_html)
    f.close()
    body.close()
    footer.close()
    os.system('start print_invoice.html')

def record(id,name,mobile,address,mode,products,total):
  record_file=open("log\\invoice_record.txt",'a')
  record=str("[ #"+str(id)+","+str(name)+","+str(mobile)+","+str(address)+","+str(mode)+","+str(products)+", Total Paid="+str(total)+']')
  record_file.write(record)
  record_file.close()


html(customer_detail_html)
record(Customer_id,Customer_name,Customer_contact,Customer_addr,Customer_mode,products_record,t_amount)
