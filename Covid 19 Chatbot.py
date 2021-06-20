import random
greet=input()
def greeting(greet):
    if greet=="hii" or greet=="hi" or greet=="Hii" or greet=="HII" or greet=="Hi" or greet=="HI":
        return("Namasthe\nThis is Covid-19 chatbot for Andhra Pradesh to  create awareness on corona and help you and your family stay safe.\nI will help you to find about the info of :-\n1.Vaccination hospitals \n2.Availability of Oxygen beds\n3.Precautions to fight against coronavirus\n4.Syptoms of coronavirus\n5.Vaccines")    
    elif greet=="hello" or greet=="Hello" or greet=="HELLO" or greet=="HEllo":
        return("Namasthe\nThis is Covid-19 chatbot for Andhra Pradesh to  create awareness on corona and help you and your family stay safe.\nI will help you to find about the info of:-\n1.Vaccination hospitals \n2.Availability of Oxygen beds\n3.Precautions to fight against coronavirus\n4.Syptoms of coronavirus\n5.Vaccines")    
    elif greet=="Namasthe" or greet=="namasthe" or greet=="NAMASTHE":
        return("Namasthe\nThis is Covid-19 chatbot for Andhra Pradesh to  create awareness on corona and help you and your family stay safe.\nI will help you to find about the info of:-\n1.Vaccination hospitals \n2.Availability of Oxygen beds\n3.Precautions to fight against coronavirus\n4.Syptoms of coronavirus\n5.Vaccines")    
print(greeting(greet))
select=input()
def vaccine_locator(select):
    if select=="1":
        print("Please select the district:-\n1.Anantapur\n2.Chittor\n3.East Godavari\n4.Guntur\n5.Kadapa\n6.Krishna\n7.Kurnool\n8.Nellore\n9.Prakasham\n10.Srikakulam\n11.Vishakhapatnam\n12.Vizianagaram\n13.West Godavari\n***Type Menu to go to the menu page or say Thank you to quit from the bot***")       
        num=input()
        if num=="1":
            print('''These are the vaccination hospitals in Ananthapur:-
1.Hospital Name: Pavani Multi Speciality Hospital  2.Hospital Name: Sainath Hospital  3.Hospital Name: Teja Nursing Home   4.Hospital Name: Nephroplus
  Category : Private                                 Category : Private                 Category : Private                   Category : Public
  Type : Paid                                        Type : Paid                        Type : Paid                          Type : Free         
  Address: D.No. 12-3-195,                           Address: 1-616-2B,                 Address:17-4-3/2, R.P.G.T.ROAD,      Address:Govt.General Hospital,
  5th Cross,Sai Nagar,Anantapur                      R.S.ROAD,KADIRI                    Hindupur Muncipality,                Anantapur
                                                                                        Hindupur, Anantapur
  Contact: 085542 45333                              Contact: 084942 23496              Contact:  085562 25411               Contact: NA
  ***For more information,please refer this link "https://pmjay.gov.in/sites/default/files/2021-02/PMJAY_empanelled_hospitals_0.pdf"***

***Type "Menu" to go to the home page or say "Thank you" to quit from the bot***''')
            q=input()
            if q=="Menu":
                print(greeting("hii"))
                wish=input()
                for i in range(1):
                    return(vaccine_locator(wish))
            elif q=='Thank you':
                print("You are always welcome")      
        elif num=="2":
            print('''These are the vaccination hospitals in Chittor:-
1.Hospital Name:Russh Hospitals Pvt Ltd  2.Hospital Name:Sri Priya Nursing Home   3.Hospital Name:NEPHROPLUS    4.Hospital Name:Apollo Hospitals Enterprises 
  Category : Private                       Category : Private                       Category : Public             Category : Private
  Type : Paid                              Type : Paid                              Type : Free                   Type : Paid 
  Address:10-14-576/6 1ST STREET R & R     Address:A.P Vajravelu Chetty Street,     Address:GOVT.GENRAL HOSPITAL  Address:ARAGONDA,THAVANAMPALLI (M),CHITTOOR
  COLONY, TIRUPATHI                        Kuppam- 517425, Chittoor                 ALIPIRI Road,Tirupathi 
  Contact:  0877 222 7340                  Contact: 085702 55136                    Contact: 0877 222 2867        Contact:  085732 83221
  ***For more information,please refer this link "https://pmjay.gov.in/sites/default/files/2021-02/PMJAY_empanelled_hospitals_0.pdf"***

***Type "Menu" to go to the home page or say "Thank you" to quit from the bot***''')
            q=input()
            if q=="Menu":
                print(greeting("hii"))
                wish=input()
                for i in range(1):
                    return(vaccine_locator(wish))
            elif q=='Thank you':
                print("You are always welcome")
        elif num=="3":
            print('''These are the vaccination hospitals in East Godavari:-
1.Hospital Name:Royal Hospital   2.Hospital Name:Siddhartha Hospital   3.Hospital Name:KIMS   4.Hospital Name:NEPHROPLUS
  Category : Private               Category : Private                    Category : Private     Category : Public
  Type : Paid                      Type : Paid                           Type : Paid            Type : Free
  Address:20-23-4,Aryapuram,       Address:34-1-20, TEMPLE STREET,       Address:KATARIGARDENS, Address:GOVERNMENT GENRAL HOSPITAL,GGH ROAD,                      
  Behind Nagadevi Theatre,         KAKINADA                              SEELAM NUKARAJU COMPLEX        RRROAD,KAKINADA
  Rajahmundry                                                            ROAD,RAJAHMUNDRY
  Contact: 094907 41382            Contact:0883 244 4800                 Contact:0883 247 7779  Contact:NA
  ***For more information,please refer this link "https://pmjay.gov.in/sites/default/files/2021-02/PMJAY_empanelled_hospitals_0.pdf"***

***Type "Menu" to go to the home page or say "Thank you" to quit from the bot***''')
            q=input()
            if q=="Menu":
                print(greeting("hii"))
                wish=input()
                for i in range(1):
                    return(vaccine_locator(wish))
            elif q=='Thank you':
                print("You are always welcome")
        elif num=="4":
            print('''These are the vaccination hospitals in Guntur:-
1.Hospital Name:FARZANA HOSPITALS  2.Hospital Name:Manipal Health Enterprises  3.Hospital Name:Yerras Super Speciality Hospital 4.Hospital Name:NEPHROPLUS 
  Category : Private                 Category : Private                          Category : Private                               Category : Public
  Type : Paid                        Type : Paid                                 Type : Paid                                      Type : Free
  Address:16-3-12/3,NIMMATHOTA,      Address:Near Varadhi,Tadepalli,Guntur       Address:12-23-3,KOTHAPET GUNTUR                  Address:WARD NO 116,
  NARSARAOPET,Guntur                                                                                                              RAILWAY STATION ROAD, SAMBAS
                                                                                                                                  -IVAPET,GUNTUR
  Contact:NA                         Contact: 0866 246 9700                      Contact: 0863 222 3181                           Contact:NA
  ***For more information,please refer this link "https://pmjay.gov.in/sites/default/files/2021-02/PMJAY_empanelled_hospitals_0.pdf"***

***Type "Menu" to go to the home page or say "Thank you" to quit from the bot***''')
            q=input()
            if q=="Menu":
                print(greeting("hii"))
                wish=input()
                for i in range(1):
                    return(vaccine_locator(wish))
            elif q=='Thank you':
                print("You are always welcome")
        elif num=="5":
            print('''These are the vaccination hospitals in Kadapa:-
1.Hospital Name:Himalaya Multi Speciality   2.Hospital Name:NANDIKA HOSPITAL  3.Hospital Name:Sree Mohan Hospitals   4.Hospital Name:TEJA HOSPITAL
  Category : Private                          Category : Private                Category : Private                     Category : Private
  Type : Paid                                 Type : Paid                       Type : Paid                            Type : Paid
  Address:d.no1-81/1, teja enclave, RS Road,  Address:4-14-44-8                 Address:42/347-23-2                    Address:4/596
          yerramujkkapally,kadapa
  Contact: 085622 56100                       Contact:NA                        Contact:085622 46171                   Contact:NA
  ***For more information,please refer this link "https://pmjay.gov.in/sites/default/files/2021-02/PMJAY_empanelled_hospitals_0.pdf"***

***Type "Menu" to go to the home page or say "Thank you" to quit from the bot***''')
            q=input()
            if q=="Menu":
                print(greeting("hii"))
                wish=input()
                for i in range(1):
                    return(vaccine_locator(wish))
            elif q=='Thank you':
                print("You are always welcome")
        elif num=="6":
            print('''These are the vaccination hospitals in Krishna:-
1.Hospital Name:SENTINI HOSPITALS PRIVATE LIMITED  2.Hospital Name:SUNRISE HOSPITALS  3.Hospital Name:NEPHROPLUS  4.Hospital Name:MARTHA HEALTH CARE SERVICE 
  Category : Private                                 Category : Private                 Category : Public           Category : Private
  Type : Paid                                        Type : Paid                        Type : Free                 Type : Paid
  Address:DR NO:54-15-5,B&C BESIDE VINAYAK THEATER   Address:33-25-35                   Address:MEDICINE BLOCK,     Address:16-99-3,ASHOK NAGAR,TIRUVURU
          RING ROAD VIJAYAWADA                                                          1ST FLORR, NH 16 SERVICE
                                                                                        ROAD,NEAR MEDICAL COLLEGE,
                                                                                        BESIDE NTR HEALTH UNIVERSITY,
                                                                                        GUNADALA, VIJAYAWADA
  Contact: 0866 667 7869                             Contact: 0866 243 4646             Contact: 0866 245 2244       Contact:NA
  ***For more information,please refer this link "https://pmjay.gov.in/sites/default/files/2021-02/PMJAY_empanelled_hospitals_0.pdf"***

***Type "Menu" to go to the home page or say "Thank you" to quit from the bot***''')
            q=input()
            if q=="Menu":
                print(greeting("hii"))
                wish=input()
                for i in range(1):
                    return(vaccine_locator(wish))
            elif q=='Thank you':
                print("You are always welcome")
        elif num=="7":
            print('''These are the vaccination hospitals in Kurnool:-
1.Hospital Name:Shantiram Medical College  2.Hospital Name:NEPHROPLUS  3.Hospital Name:VISWABHARATHI HOSPITAL 4.Hospital Name:SANJEEVANI HEALTH CARE
  Category : Private                         Category : Public           Category :Private                      Category : Private
  Type : Paid                                Type : Free                 Type : Paid                            Type : Paid
  Address:NH-18,NandyalKurnool               Address:SUPER SPECIALITY    Address:50-760-A-4, GAYATHRI ESTATE    Address:201/2A2,MAMIDALAPADU,KURNOOL  
                                             BLOCK,1ST FLOOR, BUDHWARPET         , KURNOOL
                                             ROAD, KURNOOL
  Contact:NA                                 Contact:085182 55422         Contact: 085182 29966                 Contact: 085182 26463
  ***For more information,please refer this link "https://pmjay.gov.in/sites/default/files/2021-02/PMJAY_empanelled_hospitals_0.pdf"***

***Type "Menu" to go to the home page or say "Thank you" to quit from the bot***''')
            q=input()
            if q=="Menu":
                print(greeting("hii"))
                wish=input()
                for i in range(1):
                    return(vaccine_locator(wish))
            elif q=='Thank you':
                print("You are always welcome")
        elif num=="8":
            print('''These are the vaccination hospitals in Nellore:-
1.Hospital Name:KIMS Bollineni hospitals   2.Hospital Name:NEPHROPLUS  3.Hospital Name:TRINITY HOSPITAL   4.Hospital Name:LOTUS HOSPITAL
  Category : Private                         Category : Public           Category :Private                  Category : Private
  Type : Paid                                Type : Free                 Type : Paid                        Type : Paid
  Address:DARGAMITTA,NELLORE                 Address:ACR medicalcollege, Address:1-151,SRI RAM NAGAR,       Address:16-02-1951
                                                     Nellore                     NAIDUPET 
  Contact:0861 231 5835                      Contact:NA                  Contact: 086232 47333              Contact:0861 230 4289
***For more information,please refer this link "https://pmjay.gov.in/sites/default/files/2021-02/PMJAY_empanelled_hospitals_0.pdf"***

***Type "Menu" to go to the home page or say "Thank you" to quit from the bot***''')
            q=input()
            if q=="Menu":
                print(greeting("hii"))
                wish=input()
                for i in range(1):
                    return(vaccine_locator(wish))
            elif q=='Thank you':
                print("You are always welcome")
        elif num=="9":
            print('''These are the vaccination hospitals in Prakasham:-
1.Hospital Name:PRAKASAM SUPER SPECIALITY HOSPITAL  2.Hospital Name:KAKUMANI HOSPITAL  3.Hospital Name:NEPHROPLUS  4.Hospital Name:SURAKSHA HOSPITAL
  Category : Private                                  Category : Private                 Category :Public            Category : Private
  Type : Paid                                         Type : Paid                        Type : Free                 Type : Paid
  Address:37-169/49                                   Address:37-1-5-17                  Address:Rims,Bhagyanagar,   Address:62-2-58
                                                                                                 Ongole,5th lane
  Contact: 077998 66666                               Contact: 085922 22022              Contact:NA                  Contact:088860 92129
  ***For more information,please refer this link "https://pmjay.gov.in/sites/default/files/2021-02/PMJAY_empanelled_hospitals_0.pdf"***

***Type "Menu" to go to the home page or say "Thank you" to quit from the bot***''')
            q=input()
            if q=="Menu":
                print(greeting("hii"))
                wish=input()
                for i in range(1):
                    return(vaccine_locator(wish))
            elif q=='Thank you':
                print("You are always welcome")
        elif num=="10":
            print('''These are the vaccination hospitals in Srikakulam:-
1.Hospital Name:KIMS SAI SESHDRI HOSPITAL  2.Hospital Name:Sindhura Hospitals   3.Hospital Name:NEPHROPLUS  4.Hospital Name:AMRUTHA HOSPITAL
  Category : Private                         Category : Private                   Category :Public            Category : Private
  Type : Paid                                Type : Paid                          Type : Free                 Type : Paid
  Address:137                                Address:NEW BRIDGE ROAD, DAY & NIGHT Address:RIMS,BALAGA,        Address:6-615
                                                     JUNCTION, SRIKAKULAM                 SRIKAKAULAM
  Contact:089422 71116                       Contact:089422 28455                 Contact:NA                  Contact:NA
  ***For more information,please refer this link "https://pmjay.gov.in/sites/default/files/2021-02/PMJAY_empanelled_hospitals_0.pdf"***

***Type "Menu" to go to the home page or say "Thank you" to quit from the bot***''')
            q=input()
            if q=="Menu":
                print(greeting("hii"))
                wish=input()
                for i in range(1):
                    return(vaccine_locator(wish))
            elif q=='Thank you':
                print("You are always welcome")
        elif num=="11":
            print('''These are the vaccination hospitals in Visakhapatnam:-
1.Hospital Name:Care Hospital    2.Hospital Name:Apollo Hospitals Enterprises Ltd  3.Hospital Name:Annapoorna Hopsital   4.Hospital Name:Padmaja Hospital
  Category : Private               Category : Private                                Category :Private                     Category : Private
  Type : Paid                      Type : Paid                                       Type : Paid                           Type : Paid
  Address:MAIN ROAD, VIZAG         Address:SIRIPURAM MAIN ROAD,VIZAG                 Address:47-9-32, 3rd Lane,            Address:OLD GAJUWAKA JUNCTION, 
                                                                                             Dwarakanagar,VISAKHAPATNAM            VISAKHAPATNAM
  Contact:0891 616 5656            Contact: 089127 27272                             Contact:080085 44666                  Contact:089125 15648
  ***For more information,please refer this link "https://pmjay.gov.in/sites/default/files/2021-02/PMJAY_empanelled_hospitals_0.pdf"***

***Type "Menu" to go to the home page or say "Thank you" to quit from the bot***''')
            q=input()
            if q=="Menu":
                print(greeting("hii"))
                wish=input()
                for i in range(1):
                   return(vaccine_locator(wish))
            elif q=='Thank you':
                print("You are always welcome")
        elif num=="12":
            print('''These are the vaccination hospitals in Vizianagaram:-
1.Hospital Name:GAYATRI HOSPITALS  2.Hospital Name:MARUTHI HOSPITAL   3.Hospital Name:NEPHROPLUS   4.Hospital Name:srinivasanursing home
  Category : Private                 Category : Private                 Category :Public             Category : Private
  Type : Paid                        Type : Paid                        Type : Free                  Type : Paid
  Address:25-10-18, DASANNAPETA ROAD Address:22-87                      Address:VIZIANAGARAM         Address:Main Road Gajapathinagaram
  Contact: 094405 22847              Contact:NA                         Contact:NA                   Contact:089222 26367
  ***For more information,please refer this link "https://pmjay.gov.in/sites/default/files/2021-02/PMJAY_empanelled_hospitals_0.pdf"***

***Type "Menu" to go to the home page or say "Thank you" to quit from the bot***''')
            q=input()
            if q=="Menu":
                print(greeting("hii"))
                wish=input()
                for i in range(1):
                    return(vaccine_locator(wish))
            elif q=='Thank you':
                print("You are always welcome")
        elif num=="13":
            print('''These are the vaccination hospitals in West Godavari:-
1.Hospital Name:VIJAYA HOSPITALS  2.Hospital Name:VADLAMUDI HOSPITALS  3.Hospital Name:NEPHROPLUS   4.Hospital Name:SRI SAI SPURTHI HOSPITALS
  Category : Private                 Category : Private                 Category :Public             Category : Private
  Type : Paid                        Type : Paid                        Type : Free                  Type : Paid
  Address:23A-6-63/2                 Address:1-11-146                   Address:ELURU                Address:9-190
  Contact: 088122 30500              Contact:NA                         Contact: 088122 30401        Contact: 094418 86142
  ***For more information,please refer this link "https://pmjay.gov.in/sites/default/files/2021-02/PMJAY_empanelled_hospitals_0.pdf"***

***Type "Menu" to go to the home page or say "Thank you" to quit from the bot***''')
            q=input()
            if q=="Menu":
                print(greeting("hii"))
                wish=input()
                for i in range(1):
                    return(vaccine_locator(wish))
            elif q=='Thank you':
                print("You are always welcome")
        else: 
            if num=="Menu":
                print(greeting("hii"))
                wish=input()
                for i in range(1):
                    return(vaccine_locator(wish))
            elif num=="Thank you":
                print("You are always welcome")
    elif select=="2":
        print("Please select the district:-\n1.Anantapur\n2.Chittor\n3.East Godavari\n4.Guntur\n5.Kadapa\n6.Krishna\n7.Kurnool\n8.Nellore\n9.Prakasham\n10.Srikakulam\n11.Vishakhapatnam\n12.Vizianagaram\n13.West Godavari\n***Type Menu to go to the menu page or say Thank you to quit from the bot***")
        char=input()
        if char=="1":
            print('''These are the oxygen beds availibility hospitals in Anantapur:-
1.Hospital Name:Harshitha Multispeciality Hospital  2.Hospital Name:Saveera Hospital   3.Hospital Name:AH, Kadiri  4.Hospital Name:Tadipatri Covid Hospital
  Arogyasri status: Private                           Arogyasri status:Partially         Arogyasri status:Government Arogyasri status: Government
  Available Oxygen beds: 13                           Available Oxygen beds:16           Available Oxygen beds:31    Available Oxygen beds:426
  Address:#6-3-984, 1st Cross Rd, Maruthi Nagar,      Address:1348, Opp Sakshi Office    Address:Main Rd, Revenue    Address:Government Hospital Road,
          Anantapur                                           Srinagar Colony Extension,         Colony, Kadiri              near Arvind Colony, Anantapur
                                                              NH 44, Anantapur
  Contact: 085542 43422                               Contact:  099663 12345             Contact:08494223595         Contact:9493667671
  ***For Furthur updates,please refer this link "http://dashboard.covid19.ap.gov.in/ims/hospbed_reports/"***


***Type "Menu" to go to the home page or say "Thank you" to quit from the bot***''')
            q=input()
            if q=="Menu":
                print(greeting("hii"))
                wish=input()
                for i in range(1):
                    return(vaccine_locator(wish))
            elif q=='Thank you':
                print("You are always welcome")
        elif char=="2":
            print('''These are the oxygen beds availibility hospitals in Chittor:-
1.Hospital Name:Madhuri Remdey Hospital  2.Hospital Name:Lotus Hospital   3.Hospital Name:SRI MARUTH SPECIALITY HOSPITAL 4.Hospital Name:SVRRGG Hospital
  Arogyasri status: Private                Arogyasri status:Partially       Arogyasri status:Arogyasri                     Arogyasri status: Government
  Available Oxygen beds: 30	           Available Oxygen beds: 15        Available Oxygen beds: 40                      Available Oxygen beds: 252	
  Address:Besides Federal Bank,            Address:Chittor                  Address: Abbanna Colony, Srinivasa Nagar,      Address:Alipiri Rd, Alipiri Gate,
  Isckon Temple Road, near Anna Rao                                                  Korlagunta, Tirupati                  Sri Padmavati Mahila Visvavidyalaya
  Circle, Tirupati                                                                                                         -m,Tirupati
  Contact: 0877 223 0004                   Contact:8772252962               Contact: 087905 29777                          Contact: 0877 222 2867
  ***For Furthur updates,please refer this link "http://dashboard.covid19.ap.gov.in/ims/hospbed_reports/"***


***Type "Menu" to go to the home page or say "Thank you" to quit from the bot***''')
            q=input()
            if q=="Menu":
                print(greeting("hii"))
                wish=input()
                for i in range(1):
                    return(vaccine_locator(wish))
            elif q=='Thank you':
                print("You are always welcome")
        elif char=="3":
            print('''These are the oxygen beds availability hospitals in East Godavari:-
1.Hospital Name:TEAM HOSPITAL  2.Hospital Name:GSL MEDICAL COLLEGE  3.Hospital Name:KIMS AMALAPURAM  4.Hospital Name:District Hospital Rajahmundry	
  Arogyasri status: Private      Arogyasri status:Arogyasri           Arogyasri status:Arogyasri       Arogyasri status: Government
  Available Oxygen beds: 19      Available Oxygen beds: 165           Available Oxygen beds: 82        Available Oxygen beds: 175		
  Address:behind Ashram Public   Address: NH16, Lakshmi Puram,        Address: Chaitanya Health City,  Address:Police Quarters, Padmavathi Nagar, 
  school, Nagamalli Thota,                Rajahmundry                           NH216, Amalapuram              Rajahmundry
  Kakinada
  Contact:08842356002            Contact:7815858263                   Contact:08856239999              Contact:08832951177
  ***For Furthur updates,please refer this link "http://dashboard.covid19.ap.gov.in/ims/hospbed_reports/"***


***Type "Menu" to go to the home page or say "Thank you" to quit from the bot***''')
            q=input()
            if q=="Menu":
                print(greeting("hii"))
                wish=input()
                for i in range(1):
                    return(vaccine_locator(wish))
            elif q=='Thank you':
                print("You are always welcome")
        elif char=="4":
            print('''These are the oxygen beds availability hospitals in Guntur:-
1.Hospital Name:Aditya Multi Specialty Hospital  2.Hospital Name:Amaravathi Hospital  3.Hospital Name:NRI Hospital,GUNTUR  4.Hospital Name:GGH,GUNTUR
  Arogyasri status: Private                        Arogyasri status:Partially           Arogyasri status:Arogyasri           Arogyasri status: Government
  Available Oxygen beds: 73                        Available Oxygen beds: 33            Available Oxygen beds: 179           Available Oxygen beds: 100		
  Address:13-4-64, 4th Ln, Gunturvari Thota,       Address:Old Club Rd, Gunturvari      Address: Mangalagiri Road,           Address:Sambasiva Pet, Guntur 
          Kothapeta, Guntur                                Thota, Kothapeta, Guntur              Chinakakani, Guntur
  Contact:9182184495                               Contact:08632256699                  Contact:08645-230139                 Contact:9494520370	
  ***For Furthur updates,please refer this link "http://dashboard.covid19.ap.gov.in/ims/hospbed_reports/"***


***Type "Menu" to go to the home page or say "Thank you" to quit from the bot***''')
            q=input()
            if q=="Menu":
                print(greeting("hii"))
                wish=input()
                for i in range(1):
                    return(vaccine_locator(wish))
            elif q=='Thank you':
                print("You are always welcome")
        elif char=="5":
            print('''These are the oxygen beds availability hospitals in Kadapa:-
1.Hospital Name:KVR MULTI SPECIALITY HOSPITAL  2.Hospital Name:Komma Hospital Kadapa  3.Hospital Name:DH Proddutur  4.Hospital Name:GGH Kadapa(Y.S.R.)	
  Arogyasri status: Partially                    Arogyasri status::Arogyasri            Arogyasri status:Government   Arogyasri status: Government
  Available Oxygen beds: 17                      Available Oxygen beds: 21              Available Oxygen beds: 45     Available Oxygen beds: 168		
  Address:Beside Superbazar Road,Gandhi Road,    Address:Door No 1/100, 1/101, George   Address: Dastagiripet 2,      Address:Puttampalli, Andhra Pradesh
          PRODDATUR                              Reddy Street, Yerramukkapalli, Kadapa  Nadimpalli, Proddatur
  Contact:7207155004                             Contact:8886620606                     Contact:08564245255           Contact:08562299901
  ***For Furthur updates,please refer this link "http://dashboard.covid19.ap.gov.in/ims/hospbed_reports/"***


***Type "Menu" to go to the home page or say "Thank you" to quit from the bot***''')
            q=input()
            if q=="Menu":
                print(greeting("hii"))
                wish=input()
                for i in range(1):
                    return(vaccine_locator(wish))
            elif q=='Thank you':
                print("You are always welcome")
        elif char=="6":
            print('''These are the oxygen beds availability hospitals in Krishna:-
1.Hospital Name:Andhra Hospitals Pvt Ltd    2.Hospital Name:Pinnamaneni Hospital  3.Hospital Name:Heart Care Centre  4.Hospital Name:GGH,Vijayawada
  Arogyasri status: Private                   Arogyasri status:Partially            Arogyasri status:Arogyasri         Arogyasri status: Government
  Available Oxygen beds: 21                   Available Oxygen beds: 100            Available Oxygen beds: 19          Available Oxygen beds: 125		
  Address:ZP High School, Moulangar Masjid    Address:Chinna Avutapalli,            Address:Mogalrajapuram,            Address:NH 16 Service Rd, Beside NTR 
  Rd Opp,Bhavanipuram,Gollapudi,Vijayawada            Peda Avutapalli               Christurajupuram, Vijayawada       Health University, Gunadala, Vijayawada
  Contact:0866-2415757                        Contact:08676257223                   Contact:0866-2438588               Contact:08662457789
  ***For Furthur updates,please refer this link "http://dashboard.covid19.ap.gov.in/ims/hospbed_reports/"***


***Type "Menu" to go to the home page or say "Thank you" to quit from the bot***''')
            q=input()
            if q=="Menu":
                print(greeting("hii"))
                wish=input()
                for i in range(1):
                    return(vaccine_locator(wish))
            elif q=='Thank you':
                print("You are always welcome")
        elif char=="7":
            print('''These are the oxygen beds availability hospitals in Kurnool:-
1.Hospital Name:SJ HOSPITAL  2.Hospital Name:Ameelio Hospitals   3.Hospital Name:Vishwabharathi Medical Hospital  4.Hospital Name:Area Hospital
  Arogyasri status: Private    Arogyasri status:Partially          Arogyasri status:Partially                       Arogyasri status: Government
  Available Oxygen beds: 22    Available Oxygen beds: 62           Available Oxygen beds: 59                        Available Oxygen beds: 54	
  Address:Kurnool              Address:Guru Raghavendra Nagar,     Address:Plot No. 113, Shop No. 3, P.K.R.         Address:Old Town, Adoni
                                        Kurnool                    Complex, Ulchala - Kurnool Rd, Kurnool
  Contact:08518220444          Contact:7207082844	           Contact:9059978128                               Contact:08512295796
  ***For Furthur updates,please refer this link "http://dashboard.covid19.ap.gov.in/ims/hospbed_reports/"***


***Type "Menu" to go to the home page or say "Thank you" to quit from the bot***''')
            q=input()
            if q=="Menu":
                print(greeting("hii"))
                wish=input()
                for i in range(1):
                    return(vaccine_locator(wish))
            elif q=='Thank you':
                print("You are always welcome")
        elif char=="8":
            print('''These are the oxygen beds availability hospitals in Nellore:-
1.Hospital Name:Anasuya Instute of Medical Science 2.Hospital Name:NARAYANA MEDICAL HOSPITAL  3.Hospital Name:Govt General Hospital  4.Hospital Name:CHC Allur
  Arogyasri status: Partially                        Arogyasri status:Arogyasri                 Arogyasri status:Government            Arogyasri status: Government
  Available Oxygen beds: 32                          Available Oxygen beds: 90                  Available Oxygen beds: 475             Available Oxygen beds: 22	
  Address: Pogathota, Nellore                        Address:Chintareddy Palem, Nellore         Address:GNT Rd, Dargamitta, Nellore    Address:Nellore
  Contact:9492272514                                 Contact:08612350554                        Contact:08612330026                    Contact:08622-295580
  ***For Furthur updates,please refer this link "http://dashboard.covid19.ap.gov.in/ims/hospbed_reports/"***


***Type "Menu" to go to the home page or say "Thank you" to quit from the bot***''')
            q=input()
            if q=="Menu":
                print(greeting("hii"))
                wish=input()
                for i in range(1):
                    return(vaccine_locator(wish))
            elif q=='Thank you':
                print("You are always welcome")
        elif char=="9":
            print('''Theses are the oxygen beds availability hospitals in Prakasham:-
1.Hospital Name:ZACHARAIAH HOSPITAL   2.Hospital Name:Sri Kamakshi Care Hospital  3.Hospital Name:GGH              4.Hospital Name:Area Hospital
  Arogyasri status: Private             Arogyasri status:Arogyasri                  Arogyasri status:Government      Arogyasri status: Government
  Available Oxygen beds: 20             Available Oxygen beds: 12	            Available Oxygen beds: 217       Available Oxygen beds: 64	
  Address:D.No: 35-3-72, Zachariah      Address: Wood Nagar Colony, Chirala         Address: Gopal Nagar 5th Ln,     Address:Perala, Chirala 
          Nagar, Ongole                                                                      Bhagyanagar, Ongole
  Contact:9966838306                    Contact:9000808198                          Contact:08592233270              Contact:08594237000
  ***For Furthur updates,please refer this link "http://dashboard.covid19.ap.gov.in/ims/hospbed_reports/"***


***Type "Menu" to go to the home page or say "Thank you" to quit from the bot***''')
            q=input()
            if q=="Menu":
                print(greeting("hii"))
                wish=input()
                for i in range(1):
                    return(vaccine_locator(wish))
            elif q=='Thank you':
                print("You are always welcome")
        elif char=="10":
            print('''These are the oxygen beds availability hospitals in Srikakulam:-
1.Hospital Name:GMR VARALAKSHMI CARE HOSPITAL  2.Hospital Name:Sindhura       3.Hospital Name:GEMS HOSPITAL  4.Hospital Name:RIMS HOSPITAL
  Arogyasri status: Private                      Arogyasri status:Partially     Arogyasri status:Arogyasri     Arogyasri status: Government
  Available Oxygen beds: 24                      Available Oxygen beds: 9       Available Oxygen beds: 447     Available Oxygen beds: 144		
  Address:Hospital Rd, GMR Nagar, Near Andhra    Address:NEW BRIDGE ROAD,,      Address:Gems Medical College   Address:Hudco Colony, Balaga, Srikakulam
  Bank GMR Nagar, Srikakulam District, Razam             Srikakulam             Road, Aditya Educational Soci
                                                                                -ety Srikakulam, Ragolu  
  Contact:9959325181	                           Contact:08942-228455           Contact:8331029565             Contact:08942279214
  ***For Furthur updates,please refer this link "http://dashboard.covid19.ap.gov.in/ims/hospbed_reports/"***


***Type "Menu" to go to the home page or say "Thank you" to quit from the bot***''')
            q=input()
            if q=="Menu":
                print(greeting("hii"))
                wish=input()
                for i in range(1):
                    return(vaccine_locator(wish))
            elif q=='Thank you':
                print("You are always welcome")
        elif char=="11":
            print('''These are the oxygen beds availability hospitals in Visakhapatnam:-
1.Hospital Name:Apollo hospital   2.Hospital Name:Pradhama Multi Speciality Hospital  3.Hospital Name:VIMS          4.Hospital Name:Govt Hospital
  Arogyasri status: Private         Arogyasri status:Partially                          Arogyasri status:Arogyasri    Arogyasri status: Government
  Available Oxygen beds: 84         Available Oxygen beds: 145                          Available Oxygen beds: 127    Available Oxygen beds: 200     		
  Address: Health City, Arilova,    Address:1-1-83, NH16, beside Petrol Bunk,           Address:Visakhapatnam         Address: Chinna Waltair, Pedda Waltair,
            Chinagadila                     Sector- 6, Venkojipalem, Visakhapatnam                                              Visakhapatnam
  Contact:0891-2867777              Contact:7331151828	                                Contact:08912738758           Contact:9392307880	
  ***For Furthur updates,please refer this link "http://dashboard.covid19.ap.gov.in/ims/hospbed_reports/"***


***Type "Menu" to go to the home page or say "Thank you" to quit from the bot***''')
            q=input()
            if q=="Menu":
                print(greeting("hii"))
                wish=input()
                for i in range(1):
                    return(vaccine_locator(wish))
            elif q=='Thank you':
                print("You are always welcome")
        elif char=="12":
            print('''These are the oxygen beds availability hospitals in Vizianagaram:-
1.Hospital Name:MIMS           2.Hospital Name:P.G.Star Hospital   3.Hospital Name:DISTRICT HOSPITAL   4.Hospital Name:AREA HOSPITAL
  Arogyasri status: Partially    Arogyasri status:Partially          Arogyasri status:Government         Arogyasri status: Government
  Available Oxygen beds: 110     Available Oxygen beds: 20           Available Oxygen beds: 58	         Available Oxygen beds: 17     		
  Address:31-15, near MDO Office Address:Tankbund Rd, State Bank     Address:Cantonment, Phase 4,        Address:Vizianagaram
          , Nellimarla           Main Branch Area, Santha Pet,       Vizianagaram Cantonment 
                                 Vizianagaram
  Contact:08922 244666           Contact:08922-223444                Contact:9492951256                  Contact:08963222098
  ***For Furthur updates,please refer this link "http://dashboard.covid19.ap.gov.in/ims/hospbed_reports/"***


***Type "Menu" to go to the home page or say "Thank you" to quit from the bot***''')
            q=input()
            if q=="Menu":
                print(greeting("hii"))
                wish=input()
                for i in range(1):
                    return(vaccine_locator(wish))
            elif q=='Thank you':
                print("You are always welcome")
        elif char=="13":
            print('''These are the oxygen beds availability hospitals in West Godavari:-
1.Hospital Name:New Life Hospital  2.Hospital Name:Ashram       3.Hospital Name:Murali Krishna Multi Speciality Hospital  4.Hospital Name:DISTRICT HOSPITAL
  Arogyasri status: Private          Arogyasri status:Partially   Arogyasri status:Arogyasri                                Arogyasri status: Government
  Available Oxygen beds: 16          Available Oxygen beds: 151	  Available Oxygen beds: 5                                  Available Oxygen beds: 81    		
  Address:Venkatarayapuram, Tanuku   Address:NH 5, Asram Road     Address:opp. Fire Station, Narasimharao Pet, Eluru        Address:Islampet, Eluru
  Contact:08814-220055	             Contact:08812288288          Contact:08812 239877                                      Contact:8466015130
  ***For Furthur updates,please refer this link "http://dashboard.covid19.ap.gov.in/ims/hospbed_reports/"***


***Type "Menu" to go to the home page or say "Thank you" to quit from the bot***''')
            q=input()
            if q=="Menu":
                print(greeting("hii"))
                wish=input()
                for i in range(1):
                    return(vaccine_locator(wish))
            elif q=='Thank you':
                print("You are always welcome")
        else: 
            if char=="Menu":
                print(greeting("hii"))
                wish=input()
                for i in range(1):
                    return(vaccine_locator(wish))
            elif char=="Thank you":
                print("You are always welcome")
    elif select=="3":
        print('''Follow below precautions to keep yourself and your loved ones safe from covid-19:-

---> Wear a mask: Wear a well-fitting three-layer mask, especially when you can’t physically distance,or\nif you’re indoors. Clean your hands before putting on and taking off a mask.)

--->Keep your distance: Stay at least 1 metre away from others, even if they don’t appear to be sick,since\n people can have the virus without having symptoms.

--->Follow local guidance: Check to see what national, regional and local authorities are advising so you have\n the most relevant information for where you are.

--->Avoid crowded places, poorly ventilated, indoor locations and avoid prolonged contact\n with others. Spend more time outdoors than indoors.

--->Ventilation is important: Open windows when indoors to increase the amount of outdoor air.

--->Avoid touching surfaces, especially in public settings or health facilities, in case people infected \nwith COVID-19 have touched them. Clean surfaces regularly with standard disinfectants.

--->Frequently clean your hands with soap and water, or an alcohol-based hand rub.\nIf you can, carry alcohol-based rub with you and use it often.

--->Cover your coughs and sneezes with a bent elbow or tissue, throwing used tissues \ninto a closed bin right away. Then wash your hands or use an alcohol-based hand rub.

--->Get vaccinated: When it’s your turn, get vaccinated. Follow local guidance and recommendations about vaccination.


***Type "Menu" to go to the home page or say "Thank you" to quit from the bot***''')
        q=input()
        if q=="Menu":
            print(greeting("hii"))
            wish=input()
            for i in range(1):
                return(vaccine_locator(wish))
        elif q=='Thank you':
            print("You are always welcome")
    elif select=="4":
        print('''Symptoms  of corona virus:-
--|--Most common symptoms:
--->fever

--->dry cough

--->tiredness

--|--Less common symptoms:
--->aches and pains

--->sore throat

--->diarrhoea

--->conjunctivitis

--->headache

--->loss of taste or smell

--->a rash on skin, or discolouration of fingers or toes

--|--Serious symptoms:
--->difficulty breathing or shortness of breath

--->chest pain or pressure

--->loss of speech or movement

***Seek immediate medical attention if you have serious symptoms. Always call before visiting your doctor or health facility.

***On average it takes 5–6 days from when someone is infected with the virus for symptoms to show, however it can take up to 14 days.

***People with mild symptoms who are otherwise healthy should manage their symptoms at home


***Type "Menu" to go to the home page or say "Thank you" to quit from the bot***''')
        q=input()
        if q=="Menu":
            print(greeting("hii"))
            wish=input()
            for i in range(1):
                return(vaccine_locator(wish))
        elif q=='Thank you':
            print("You are always welcome")
    elif select=="5":
            print('''Present there are mainly three types of vaccines running in India:-
1.Covaxin:-
           Covaxin is a COVID-19 vaccine developed by Bharat Biotech, an Indian biotechnology company,\n           and the Indian Council of Medical Research.
           It is a two-dose vaccine with an efficacy rate of 78%,according to interim phase 3 clinical data.
           Covaxin, also known as BBV152, is a type of whole-virus vaccine called an inactivated vaccine.\n           An inactivated vaccine incorporates a modified or dead version of the virus,\n           in this case SARS-CoV-2, which cannot replicate and so cannot cause disease.
Side Effects:-
           1.fever
           2.headaches
           3.irritability
           4.pain, swelling, or both at the site of injection

2.Covishield:-
           The Covishield vaccine is a vaccine that aims to protect against COVID-19.
           It is developed by Oxford University and AstraZeneca.
           It is given by Intramuscular Injection,using as a vector the modified chimpanzee Adenovirus ChAdOx1.
Side Effects:-
           1.Pain or tenderness at the injection site
           2.Headache
           3.Tiredness
           4.Muscle or joint aches
           5.Fever
           6.Chills
           7.Nausea

3.Sputnik-V:
            Sputnik V is a two-dose Covid-19 vaccine, which has an efficacy of\n            over 91 per cent, according to a publication in scientific journal The Lancet.
            Made by the Gamaleya Research Institute of Epidemiology and Microbiology in Moscow.
            However, unlike Covishield, which uses a weakened common cold\n           “adenovirus” that affects chimpanzees, Sputnik V makes use of two different human adenoviruses.
Side Effects:
            1.flu-like illness
            2.headache
            3.fatigue
            4.injection-site reactions


***Type "Menu" to go to the home page or say "Thank you" to quit from the bot***''')
            q=input()
            if q=="Menu":
                print(greeting("hii"))
                wish=input()
                for i in range(1):
                    return(vaccine_locator(wish))
            elif q=='Thank you':
                print("You are always welcome")
vaccine_locator(select)