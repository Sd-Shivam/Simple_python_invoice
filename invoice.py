import os
from datetime import date
from datetime import datetime
#Main variables start
Invoice_id=' '
Invoice_type='Invoice'
Date_Time=' '
Customer_Name=' '
Customer_PhoneNo=' '
Customer_Address=' '
Customer_GSTNo=' '
Pay_Mode=' '
Products_names=[]
Products_descriptions=[]
Products_rate=[]
Products_quantity=[]
product_each_total=[]
Sub_Total='00'
Discount='00'
Tax='00'
Net_Total='00'
#Main variables end
#html variable section start
header=' '
Products_html=' ' 
Footer=' '
#html variable section end

# all main functions section start
def clear():
    os.system('cls')
    logo='''
            ______________________________________________________________________________
                ____                                  _   _                                
                /   )    /                            /  /|          /     ,   /           
            ---/__ /----/__----__---)__----__--_/_---/| /-|----__---/__-------/----__---__-
              /    )   /   ) /   ) /   ) /   ) /    / |/  |  /   ) /   ) /   /   /___) (_ `
            _/____/___/___/_(___(_/_____(___(_(_ __/__/___|_(___/_(___/_/___/___(___ _(__)_                                                                              
           '''
    print(logo)

def id_generate():
    log1=open('log\\invoice.id','r')
    global Invoice_id
    Invoice_id =log1.read()
    log1.close()
    log2=open('log\\invoice.id','w')
    log2.write(str(int(Invoice_id) + int(1)))
    log2.close()

def datetime_genegrate():
    today = date.today()
    date1=today.strftime("%b-%d-%Y")
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    global Date_Time
    Date_Time=str(str(date1)+' '+str(time))

def Customer_data_inputs():
    global Invoice_type
    global Customer_Name
    global Customer_PhoneNo
    global Customer_Address
    global Customer_GSTNo
    global Tax
    clear()
    print('[1] --> Normal Invoice ')
    print('[2] --> GST Invoice ')
    answer=input('[-] Please Choose one option -->')
    Customer_Name=input('[-] Enter the Customer name --> ')
    Customer_PhoneNo=str('+91-')+str(input('[-] Enter the Customer PhoneNo. --> '))
    Customer_Address=input('[-] Enter the Customer Address --> ')
    if int(answer)== 2 :
        Invoice_type='GST-Invoice'
        Customer_GSTNo=input('[-] Enter the Customer GSTNo --> ')
        Tax=input('[-] Enter the CGST/SGST tax rate(rcommended-18% ) --> ')

def html_variable_control():
    global header
    global Footer
    gst_header=''' <head>
        <meta charset="utf-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="https://img.icons8.com/ios/344/s-symbol.png" rel="icon" />
        <title>BharatMobile invoice</title>
        <meta name="author" content="Shivam">
        <!-- Web Fonts
        ======================= -->
        <link rel='stylesheet' href='https://fonts.googleapis.com/css?family=Poppins:100,200,300,400,500,600,700,800,900' type='text/css'>
        <!-- Stylesheet
        ======================= -->
        <link rel="stylesheet" type="text/css" href=" vendor/bootstrap/css/bootstrap.min.css"/>
        <link rel="stylesheet" type="text/css" href=" vendor/font-awesome/css/all.min.css"/>
        <link rel="stylesheet" type="text/css" href=" css/stylesheet.css"/>
        </head>
        <body>
        <div class="container-fluid invoice-container">
        <!-- Header -->
        <div>
            <img id="head" src="./css/bk.jpg" style="width: 100%;margin-left: -3px;" title="BharatMobile" alt="BharatMobile" />

        </div>
        <header>
        <div class="row align-items-center">
        <div class="col-sm-7 text-center text-sm-left mb-3 mb-sm-0">
        <img id="logo" src="./css/b-logo.png" title="BharatMobile" alt="BharatMobile" />
        </div>
        <div class="col-sm-5 text-center text-sm-right">
        <h4 class="text-7 mb-0"> '''+str(Invoice_type)+''' </h4>
        </div>
        </div>
        <hr>
        </header>
         <main>
        <div class="row">
            <div class="col-sm-6"><strong>Date & Time:</strong> '''+str(Date_Time)+'''</div>
            <div class="col-sm-6 text-sm-right"> <strong>Invoice No:</strong>#00'''+str(Invoice_id)+'''</div>
        </div>
        <hr>
        <div class="row">
            <div class="col-sm-6 text-sm-right order-sm-1"> <strong>Pay To:</strong>
            <address>
            BharatMobile Store<br/>
            near state bank<br/>
            274203, Hata , Kushinager<br/>
            help@bharatphonix.com
            <div class=""> <strong>GST No:</strong> <i> 09FZLPS0388N1ZA</i></div>
            </address>
            </div>
            <div class="col-sm-6 order-sm-0"> <strong>Invoiced To:</strong>
            <address>
            '''+str(Customer_Name)+'''<br />
            '''+str(Customer_PhoneNo)+'''<br />
            '''+str(Customer_Address)+'''<br />
            <div class=""> <strong>Payment Mode:</strong> '''+str(Pay_Mode)+'''</div>
            <div class=""> <strong>GST-No:</strong> '''+str(Customer_GSTNo)+'''</div>
            </address>
            </div>
        </div> 
        <div class="card" style="margin-bottom: -31px;">
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
                </tr>'''
    Normal_header=''' <head>
        <meta charset="utf-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="https://img.icons8.com/ios/344/s-symbol.png" rel="icon" />
        <title>BharatMobile invoice</title>
        <meta name="author" content="Shivam">
        <!-- Web Fonts
        ======================= -->
        <link rel='stylesheet' href='https://fonts.googleapis.com/css?family=Poppins:100,200,300,400,500,600,700,800,900' type='text/css'>
        <!-- Stylesheet
        ======================= -->
        <link rel="stylesheet" type="text/css" href=" vendor/bootstrap/css/bootstrap.min.css"/>
        <link rel="stylesheet" type="text/css" href=" vendor/font-awesome/css/all.min.css"/>
        <link rel="stylesheet" type="text/css" href=" css/stylesheet.css"/>
        </head>
        <body>
        <div class="container-fluid invoice-container">
        <!-- Header -->
        <div>
            <img id="head" src="./css/bk.jpg" style="width: 100%;margin-left: -3px;" title="BharatMobile" alt="BharatMobile" />

        </div>
        <header>
        <div class="row align-items-center">
        <div class="col-sm-7 text-center text-sm-left mb-3 mb-sm-0">
        <img id="logo" src="./css/b-logo.png" title="BharatMobile" alt="BharatMobile" />
        </div>
        <div class="col-sm-5 text-center text-sm-right">
        <h4 class="text-7 mb-0"> '''+str(Invoice_type)+''' </h4>
        </div>
        </div>
        <hr>
        </header>
         <main>
        <div class="row">
            <div class="col-sm-6"><strong>Date & Time:</strong> '''+str(Date_Time)+'''</div>
            <div class="col-sm-6 text-sm-right"> <strong>Invoice No:</strong>#00'''+str(Invoice_id)+'''</div>
        </div>
        <hr>
        <div class="row">
            <div class="col-sm-6 text-sm-right order-sm-1"> <strong>Pay To:</strong>
            <address>
            BharatMobile Store<br/>
            near state bank<br/>
            274203, Hata , Kushinager<br/>
            help@bharatphonix.com
            <div class=""> <strong>GST No:</strong> <i> 09FZLPS0388N1ZA</i></div>
            </address>
            </div>
            <div class="col-sm-6 order-sm-0"> <strong>Invoiced To:</strong>
            <address>
            '''+str(Customer_Name)+'''<br />
            '''+str(Customer_PhoneNo)+'''<br />
            '''+str(Customer_Address)+'''<br />
            <div class=""> <strong>Payment Mode:</strong> '''+str(Pay_Mode)+'''</div>
            </address>
            </div>
        </div> 
        <div class="card" style="margin-bottom: -31px;">
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
                </tr>'''
    gst_Footer='''
                <tr>
              <td colspan="4" class="bg-light-2 text-right"><strong>Sub Total:</strong></td>
              <td class="bg-light-2 text-right">'''+str(u"\u20B9")+str(Sub_Total)+'''</td>
            </tr>
            <tr>
              <td colspan="4" class="bg-light-2 text-right"><strong>CGST/SGST:</strong></td>
              <td class="bg-light-2 text-right">'''+str(u"\u20B9")+str(Tax)+'''</td>
            </tr>
            <tr>
              <td colspan="4" class="bg-light-2 text-right"><strong>Total:</strong></td>
              <td class="bg-light-2 text-right">'''+str(u"\u20B9")+str(Net_Total)+'''</td>
            </tr>
                </tbody>
                </table>
            </div>
            </div>
        </div>
        </main>
        <footer class="text-center mt-4">
            
            <div style="font-size: 11px;">
            <br><strong style="margin-right: 496px;"><span> Our store services :-</span></strong> 
            <ol>
                <li style="margin-right: 407px;">All Type of phones Repairing service.</li>
                <li style="margin-right: 331px;">Touch glass and display Pesting Machine service.</li>
                <li style="margin-right: 98px;">All Modle SmartPhone, keypad phone , Assessories & Repairing tools Availables to our store..</li>
            </ol>
            </div>
                <p class="text-1"><strong>  THANK YOU COME AGAIN </strong>   
            </p><div class="btn-group btn-group-sm d-print-none"> <a href="javascript:window.print()" class="btn btn-light border text-black-50 shadow-none"><i class="fa fa-print"></i> Print</a> <a href="" class="btn btn-light border text-black-50 shadow-none"><i class="fa fa-download"></i> Download</a> </div>
        </footer>

        </div>

        <!-- footer -->
        <div id="foot">
        <img src="./css/ft.jpg" style="width: 100%;" alt="footer">
        </div>
        </html>'''
    Normal_Footer='''
                <tr>
              <td colspan="4" class="bg-light-2 text-right"><strong>Sub Total:</strong></td>
              <td class="bg-light-2 text-right">'''+str(u"\u20B9")+str(Sub_Total)+'''</td>
            </tr>
            <tr>
              <td colspan="4" class="bg-light-2 text-right"><strong>Discount:</strong></td>
              <td class="bg-light-2 text-right">'''+str(u"\u20B9")+str(Discount)+'''</td>
            </tr>
            <tr>
              <td colspan="4" class="bg-light-2 text-right"><strong>Total:</strong></td>
              <td class="bg-light-2 text-right">'''+str(u"\u20B9")+str(Net_Total)+'''</td>
            </tr>
                </tbody>
                </table>
            </div>
            </div>
        </div>
        </main>
        <footer class="text-center mt-4">
            
            <div style="font-size: 11px;">
            <br><strong style="margin-right: 496px;"><span> Our store services :-</span></strong> 
            <ol>
                <li style="margin-right: 407px;">All Type of phones Repairing service.</li>
                <li style="margin-right: 331px;">Touch glass and display Pesting Machine service.</li>
                <li style="margin-right: 98px;">All Modle SmartPhone, keypad phone , Assessories & Repairing tools Availables to our store..</li>
            </ol>
            </div>
                <p class="text-1"><strong>  THANK YOU COME AGAIN </strong>   
            </p><div class="btn-group btn-group-sm d-print-none"> <a href="javascript:window.print()" class="btn btn-light border text-black-50 shadow-none"><i class="fa fa-print"></i> Print</a> <a href="" class="btn btn-light border text-black-50 shadow-none"><i class="fa fa-download"></i> Download</a> </div>
        </footer>

        </div>

        <!-- footer -->
        <div id="foot">
        <img src="./css/ft.jpg" style="width: 100%;" alt="footer">
        </div>
        </html>'''
    if str(Invoice_type) == 'GST-Invoice':
        header=gst_header
        Footer=gst_Footer
    else:
        Footer=Normal_Footer
        header=Normal_header

def products_input():
    no=input('[-] Enter the Total no of products :')
    i=1
    print('[*] Example :(with single / between only as shown )')
    print('    ---> Name/Description/Rate/Quantity')
    while i<=int(no):
        prod_name,prod_des,prod_rate,prod_quantity=input('[-] Enter '+ str(i)+' Product details -->').split('/')
        total_rate=int(int(prod_rate)*int(prod_quantity))
        html=''' <tr><td>'''+str(prod_name)+'''</td><td class="text-1">'''+str(prod_des)+'''</td><td class="text-center">'''+str(prod_rate)+'''</td><td class="text-center">'''+str(prod_quantity)+'''</td><td class="text-right">'''+str(total_rate)+'''</td></tr>'''
        global Products_html
        global Sub_Total
        global Products_names
        global Products_descriptions
        global Products_rate
        global Products_quantity
        global product_each_total 
        Sub_Total=int(Sub_Total)+int(total_rate)
        Products_html=str(Products_html)+str(html)
        Products_names.append(prod_name)
        Products_descriptions.append(prod_des)
        Products_rate.append(prod_rate)
        Products_quantity.append(prod_quantity)
        product_each_total.append(total_rate)
        i=i+1
  
def total_calculation():
    global Sub_Total
    global Discount
    global Tax
    global Net_Total
    global Products_names
    global Products_quantity
    global Products_rate
    global product_each_total
    i=0
    index=int(len(Products_names))
    Sub_Total=int(00)
    while i<index:
        i=int(i)
        quant=Products_quantity[i]
        rate=Products_rate[i]
        each_total=int(quant)*int(rate)
        product_each_total[i]=int(each_total)
        Sub_Total=int(Sub_Total)+int(each_total)
        i=i+1
    if int(Discount)!=0:
        Net_Total2=int(Sub_Total)-int(Discount)
        Net_Total=Net_Total2
    else:
        Net_Total=int(Sub_Total)
    if int(Tax)!=0:
        tax_cal=int(Sub_Total)*int(Tax)/100
        Net_Total3=int(Sub_Total)+int(tax_cal)
        Net_Total=Net_Total3
    else:
        Net_Total=int(Sub_Total) 

def invoice_print():
    invoice_html_file=open('log\\last_invoice.html','w',encoding="utf-8")
    total_html=str(header)+str(Products_html)+str(Footer)
    invoice_html_file.write(total_html)
    invoice_html_file.close()
    os.system('start log\last_invoice.html')
    
def store_data():
    database_file=open('log\\Database.shiva','a',encoding="utf-8")
    data=str(str(Invoice_id)+'!@'+str(Invoice_type)+'!@'+str(Date_Time)+'!@'+str(Customer_Name)+'!@'+str(Customer_PhoneNo)+'!@'+str(Customer_Address)+'!@'+str(Customer_GSTNo)+'!@'+str(Pay_Mode)+'!@'+str(Products_html)+'!@'+str(Sub_Total)+'!@'+str(Discount)+'!@'+str(Tax)+'!@'+str(Net_Total)+'->')
    database_file.write(data)
    database_file.close()

def final_review():
    global Customer_Name
    global Products_html
    global Customer_PhoneNo
    global Customer_Address
    global Customer_GSTNo
    global Discount
    global Pay_Mode
    global Tax
    clear()
    total_calculation()
    print('\n\n\t[>-<]Final Review Point[>-<]')
    print('[*] Invoice_Id-->'+str(Invoice_id)+'\t\t[*] Date_time-->'+str(Date_Time))
    print('[1] Name-->'+str(Customer_Name)+'\t\t[2] Phone_No-->'+str(Customer_PhoneNo))
    print('[3] Address -->'+str(Customer_Address)+'\t\t[4] GSTNo-->'+str(Customer_GSTNo))
    print('[5] Discount-->'+str(Discount)+'\t\t[6] Tax -->'+str(Tax))
    i=0
    lens=len(Products_names)
    print('--------------------------------------------------------------------')
    print('Name Description Rate Quantity Total')
    print('--------------------------------------------------------------------')
    while i<lens:
        i=int(i)
        print(str(Products_names[i])+'\t'+str(Products_descriptions[i])+'\t'+str(Products_rate[i])+'\t'+str(Products_quantity[i])+'\t'+str(product_each_total[i]))
        i=i+1
    print('--------------------------------------------------------------------')
    print('[*] Sub Total Amount is '+str(Sub_Total) )
    print('[*] Net Total Amount is '+str(Net_Total) )
    print('--------------------------------------------------------------------')
    print('[1-6] To change edit customer details pressnumber.')
    print('[A] To Add new product.')
    print('[P] To change edit any product Name.')
    print('[D] To change edit any product description.')
    print('[R] To change edit any product Rate.')
    print('[Q] To change edit any product Quantity.')
    print('[S] To Print invoice and exit .')
    answer=input('[-] Please choose the option --> ')
    try:
        if int(answer)==int(1):
            new_Customer_Name=input('[-] Enter the new name --> ')
            Customer_Name=new_Customer_Name
        elif int(answer)== 2:
            new_Customer_PhoneNo=str('+91-')+str(input('[-] Enter the Customer PhoneNo. --> '))
            Customer_PhoneNo=new_Customer_PhoneNo
        elif int(answer)== 3:
            new_Customer_Address=input('[-] Enter the Customer Address --> ')
            Customer_Address=new_Customer_Address
        elif int(answer)== 4:
            new_Customer_GSTNo=input('[-] Enter the Customer GSTNo --> ')
            Customer_GSTNo=new_Customer_GSTNo
        elif int(answer)== 5:
            Discount=input('[-] Enter the discount value(ruppes) --> ')
        elif int(answer)== 6:
            Tax=input('[-] Enter the CGST/SGST tax rate(rcommended-18% ) --> ')
        
    except:
        answer=answer.capitalize()
        if str(answer)== 'P':
            ans=int(input('[-] Enter the product number -->'))
            index=ans-1
            print('[*] you are going to change name '+str(Products_names[index]))
            new_name=input('[-] Enter the new name --> ')
            Products_html=Products_html.replace(str(Products_names[index]),str(new_name))
            Products_names[index]=str(new_name)
        elif str(answer)== 'D':
            ans=int(input('[-] Enter the product number -->'))
            index=ans-1
            print('[*] you are going to change name '+str(Products_descriptions[index]))
            new_desc=input('[-] Enter the new des --> ')
            Products_html=Products_html.replace(str(Products_descriptions[index]),str(new_desc))
            Products_descriptions[index]=str(new_desc)
        elif str(answer)== 'R':
            ans=int(input('[-] Enter the product number -->'))
            index=ans-1
            print('[*] you are going to change rate '+str(Products_rate[index]))
            new_rate=input('[-] Enter the new rate --> ')
            Products_html=Products_html.replace(str(Products_rate[index]),str(new_rate))
            Products_rate[index]=str(new_rate)
        elif str(answer)== 'Q':
            ans=int(input('[-] Enter the product number -->'))
            index=ans-1
            print('[*] you are going to change quantity '+str(Products_quantity[index]))
            new_quantity=input('[-] Enter the new quantity --> ')
            Products_html=Products_html.replace(str(Products_quantity[index]),str(new_quantity))
            Products_quantity[index]=str(new_quantity)
        elif str(answer)=='A':
            products_input()
        elif str(answer)== 'S':
            clear()
            print('[1] Cash\t[2]PhonePe')
            print('[3] Card\t[4]GooglePay')
            anspay=int(input('[-] Choose the mode of payment ---> '))
            if anspay==1:
                Pay_Mode='Cash'
            if anspay==2:
                Pay_Mode='PhonePe'
            if anspay==3:
                Pay_Mode='Card'
            if anspay==4:
                Pay_Mode='GooglePay'
            total_calculation()
            html_variable_control()
            invoice_print()
            store_data()
            exit()
    total_calculation()
    clear()
    final_review()

def reopen_invoice():
    clear()
    # main variables section start
    Invoice_id=' '
    Invoice_type='Invoice'
    Date_Time=' '
    Customer_Name=' '
    Customer_PhoneNo=' '
    Customer_Address=' '
    Customer_GSTNo=' '
    Pay_Mode=' '
    Products_html=' '
    Sub_Total='00'
    Discount='00'
    Tax='00'
    Net_Total='00'
    header=' '
    Footer=' '
    # main variables section end
    invoice_id_e=str(input('[-] Enter the invoice_Id (Example- #0021 as 21) ---> '))
    database_file=open('log\\Database.shiva','r')
    data=database_file.read()
    lines=data.split('->')
    for items in lines:
        s=items.split('!@')
        ids=str(s[0])
        if ids==str(invoice_id_e):
            Invoice_id=s[0]
            Invoice_type=s[1]
            Date_Time=s[2]
            Customer_Name=s[3]
            Customer_PhoneNo=s[4]
            Customer_Address=s[5]
            Customer_GSTNo=s[6]
            Pay_Mode=s[7]
            Products_html=s[8]
            Sub_Total=s[9]
            Discount=s[10]
            Tax=s[11]
            Net_Total=s[12]
    gst_header=''' <head>
        <meta charset="utf-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="https://img.icons8.com/ios/344/s-symbol.png" rel="icon" />
        <title>BharatMobile invoice</title>
        <meta name="author" content="Shivam">
        <!-- Web Fonts
        ======================= -->
        <link rel='stylesheet' href='https://fonts.googleapis.com/css?family=Poppins:100,200,300,400,500,600,700,800,900' type='text/css'>
        <!-- Stylesheet
        ======================= -->
        <link rel="stylesheet" type="text/css" href=" vendor/bootstrap/css/bootstrap.min.css"/>
        <link rel="stylesheet" type="text/css" href=" vendor/font-awesome/css/all.min.css"/>
        <link rel="stylesheet" type="text/css" href=" css/stylesheet.css"/>
        </head>
        <body>
        <div class="container-fluid invoice-container">
        <!-- Header -->
        <div>
            <img id="head" src="./css/bk.jpg" style="width: 100%;margin-left: -3px;" title="BharatMobile" alt="BharatMobile" />

        </div>
        <header>
        <div class="row align-items-center">
        <div class="col-sm-7 text-center text-sm-left mb-3 mb-sm-0">
        <img id="logo" src="./css/b-logo.png" title="BharatMobile" alt="BharatMobile" />
        </div>
        <div class="col-sm-5 text-center text-sm-right">
        <h4 class="text-7 mb-0"> '''+str(Invoice_type)+''' </h4>
        </div>
        </div>
        <hr>
        </header>
        <main>
        <div class="row">
            <div class="col-sm-6"><strong>Date & Time:</strong> '''+str(Date_Time)+'''</div>
            <div class="col-sm-6 text-sm-right"> <strong>Invoice No:</strong>#00'''+str(Invoice_id)+'''</div>
        </div>
        <hr>
        <div class="row">
            <div class="col-sm-6 text-sm-right order-sm-1"> <strong>Pay To:</strong>
            <address>
            BharatMobile Store<br/>
            near state bank<br/>
            274203, Hata , Kushinager<br/>
            help@bharatphonix.com
            <div class=""> <strong>GST No:</strong> <i> 09FZLPS0388N1ZA</i></div>
            </address>
            </div>
            <div class="col-sm-6 order-sm-0"> <strong>Invoiced To:</strong>
            <address>
            '''+str(Customer_Name)+'''<br />
            '''+str(Customer_PhoneNo)+'''<br />
            '''+str(Customer_Address)+'''<br />
            <div class=""> <strong>Payment Mode:</strong> '''+str(Pay_Mode)+'''</div>
            <div class=""> <strong>GST-No:</strong> '''+str(Customer_GSTNo)+'''</div>
            </address>
            </div>
        </div> 
        <div class="card" style="margin-bottom: -31px;">
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
                </tr>'''
    Normal_header=''' <head>
        <meta charset="utf-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="https://img.icons8.com/ios/344/s-symbol.png" rel="icon" />
        <title>BharatMobile invoice</title>
        <meta name="author" content="Shivam">
        <!-- Web Fonts
        ======================= -->
        <link rel='stylesheet' href='https://fonts.googleapis.com/css?family=Poppins:100,200,300,400,500,600,700,800,900' type='text/css'>
        <!-- Stylesheet
        ======================= -->
        <link rel="stylesheet" type="text/css" href=" vendor/bootstrap/css/bootstrap.min.css"/>
        <link rel="stylesheet" type="text/css" href=" vendor/font-awesome/css/all.min.css"/>
        <link rel="stylesheet" type="text/css" href=" css/stylesheet.css"/>
        </head>
        <body>
        <div class="container-fluid invoice-container">
        <!-- Header -->
        <div>
            <img id="head" src="./css/bk.jpg" style="width: 100%;margin-left: -3px;" title="BharatMobile" alt="BharatMobile" />

        </div>
        <header>
        <div class="row align-items-center">
        <div class="col-sm-7 text-center text-sm-left mb-3 mb-sm-0">
        <img id="logo" src="./css/b-logo.png" title="BharatMobile" alt="BharatMobile" />
        </div>
        <div class="col-sm-5 text-center text-sm-right">
        <h4 class="text-7 mb-0"> '''+str(Invoice_type)+''' </h4>
        </div>
        </div>
        <hr>
        </header>
        <main>
        <div class="row">
            <div class="col-sm-6"><strong>Date & Time:</strong> '''+str(Date_Time)+'''</div>
            <div class="col-sm-6 text-sm-right"> <strong>Invoice No:</strong>#00'''+str(Invoice_id)+'''</div>
        </div>
        <hr>
        <div class="row">
            <div class="col-sm-6 text-sm-right order-sm-1"> <strong>Pay To:</strong>
            <address>
            BharatMobile Store<br/>
            near state bank<br/>
            274203, Hata , Kushinager<br/>
            help@bharatphonix.com
            <div class=""> <strong>GST No:</strong> <i> 09FZLPS0388N1ZA</i></div>
            </address>
            </div>
            <div class="col-sm-6 order-sm-0"> <strong>Invoiced To:</strong>
            <address>
            '''+str(Customer_Name)+'''<br />
            '''+str(Customer_PhoneNo)+'''<br />
            '''+str(Customer_Address)+'''<br />
            <div class=""> <strong>Payment Mode:</strong> '''+str(Pay_Mode)+'''</div>
            </address>
            </div>
        </div> 
        <div class="card" style="margin-bottom: -31px;">
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
                </tr>'''
    gst_Footer='''
                <tr>
            <td colspan="4" class="bg-light-2 text-right"><strong>Sub Total:</strong></td>
            <td class="bg-light-2 text-right">'''+str(u"\u20B9")+str(Sub_Total)+'''</td>
            </tr>
            <tr>
            <td colspan="4" class="bg-light-2 text-right"><strong>CGST/SGST:</strong></td>
            <td class="bg-light-2 text-right">'''+str(u"\u20B9")+str(Tax)+'''</td>
            </tr>
            <tr>
            <td colspan="4" class="bg-light-2 text-right"><strong>Total:</strong></td>
            <td class="bg-light-2 text-right">'''+str(u"\u20B9")+str(Net_Total)+'''</td>
            </tr>
                </tbody>
                </table>
            </div>
            </div>
        </div>
        </main>
        <footer class="text-center mt-4">
            
            <div style="font-size: 11px;">
            <br><strong style="margin-right: 496px;"><span> Our store services :-</span></strong> 
            <ol>
                <li style="margin-right: 407px;">All Type of phones Repairing service.</li>
                <li style="margin-right: 331px;">Touch glass and display Pesting Machine service.</li>
                <li style="margin-right: 98px;">All Modle SmartPhone, keypad phone , Assessories & Repairing tools Availables to our store..</li>
            </ol>
            </div>
                <p class="text-1"><strong>  THANK YOU COME AGAIN </strong>   
            </p><div class="btn-group btn-group-sm d-print-none"> <a href="javascript:window.print()" class="btn btn-light border text-black-50 shadow-none"><i class="fa fa-print"></i> Print</a> <a href="" class="btn btn-light border text-black-50 shadow-none"><i class="fa fa-download"></i> Download</a> </div>
        </footer>

        </div>

        <!-- footer -->
        <div id="foot">
        <img src="./css/ft.jpg" style="width: 100%;" alt="footer">
        </div>
        </html>'''
    Normal_Footer='''
                <tr>
            <td colspan="4" class="bg-light-2 text-right"><strong>Sub Total:</strong></td>
            <td class="bg-light-2 text-right">'''+str(u"\u20B9")+str(Sub_Total)+'''</td>
            </tr>
            <tr>
            <td colspan="4" class="bg-light-2 text-right"><strong>Discount:</strong></td>
            <td class="bg-light-2 text-right">'''+str(u"\u20B9")+str(Discount)+'''</td>
            </tr>
            <tr>
            <td colspan="4" class="bg-light-2 text-right"><strong>Total:</strong></td>
            <td class="bg-light-2 text-right">'''+str(u"\u20B9")+str(Net_Total)+'''</td>
            </tr>
                </tbody>
                </table>
            </div>
            </div>
        </div>
        </main>
        <footer class="text-center mt-4">
            
            <div style="font-size: 11px;">
            <br><strong style="margin-right: 496px;"><span> Our store services :-</span></strong> 
            <ol>
                <li style="margin-right: 407px;">All Type of phones Repairing service.</li>
                <li style="margin-right: 331px;">Touch glass and display Pesting Machine service.</li>
                <li style="margin-right: 98px;">All Modle SmartPhone, keypad phone , Assessories & Repairing tools Availables to our store..</li>
            </ol>
            </div>
                <p class="text-1"><strong>  THANK YOU COME AGAIN </strong>   
            </p><div class="btn-group btn-group-sm d-print-none"> <a href="javascript:window.print()" class="btn btn-light border text-black-50 shadow-none"><i class="fa fa-print"></i> Print</a> <a href="" class="btn btn-light border text-black-50 shadow-none"><i class="fa fa-download"></i> Download</a> </div>
        </footer>

        </div>

        <!-- footer -->
        <div id="foot">
        <img src="./css/ft.jpg" style="width: 100%;" alt="footer">
        </div>
        </html>'''
    if str(Invoice_type) == 'GST-Invoice':
        header=gst_header
        Footer=gst_Footer
    else:
        Footer=Normal_Footer
        header=Normal_header
    invoice_html_file=open('log\\last_invoice.html','w',encoding="utf-8")
    total_html=str(header)+str(Products_html)+str(Footer)
    invoice_html_file.write(total_html)
    invoice_html_file.close()
    os.system('start log\last_invoice.html')
    exit()

def start_manager():
    clear()
    os.system('title BharatMobiles')
    print('[1] Create a New Invoice ')
    print('[2] Open Invoice from Database ')
    print('[9] Close ')
    ans=str(input('[-] Please Choose one option ---> '))
    if ans==str(2):
        reopen_invoice()
    elif ans==str(1):
        id_generate()
        datetime_genegrate()
        Customer_data_inputs()
        products_input()
        final_review()
    elif ans==str(9):
        exit()
    else:
        print('[!] Alert option not found , Restarting program......')
        os.system('sleep(5)')
        start_manager()    

# all main functions sction end

start_manager()