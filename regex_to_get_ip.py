#! /usr/bin/env python3

import os

try:
   import re
except:
   input_1 = input("re module is missing. Do you want to install [Y/N]:")
   input_1 = input_1.upper()
   if input_1 == "Y":
      try:
         try:
            os.system("pip install regex")
         except:
            os.system("pip3 install regex")
      except:
         print("Please install regex package manually")
   else:
      print("Retuen and type \"y\" to install") #escape characters


txt = """Shared-Dev-APP-Subnet-AZ3
subnet-0a965d7b23a54953b	Available	vpc-02692e9b805ebabc4 | us-west-2-shared-dev-vpc	10.155.236.0/22	–	821	us-west-2c	usw2-az3	us-west-2	rtb-074ca8b5433cea054	acl-0313e9e5e51c48acf	No	No	No	-	No	299029076690 (shared)
Shared-Dev-DMZ-Subnet-AZ2
subnet-0ec3a2ac57c0a95c1	Available	vpc-02692e9b805ebabc4 | us-west-2-shared-dev-vpc	10.172.232.0/22	2600:1f14:375:52e8::/64	984	us-west-2a	usw2-az2	us-west-2	rtb-056bc497f4b3811f5	acl-04bbc2e35eaef7716	No	No	No	-	No	299029076690 (shared)
Shared-Dev-DMZ-Subnet-AZ3
subnet-0647a9c93d2d182d7	Available	vpc-02692e9b805ebabc4 | us-west-2-shared-dev-vpc	10.172.236.0/22	2600:1f14:375:52ec::/64	990	us-west-2c	usw2-az3	us-west-2	rtb-056bc497f4b3811f5	acl-04bbc2e35eaef7716	No	No	No	-	No	299029076690 (shared)
Shared-Dev-DMZ-Subnet-AZ1
subnet-09d6257945db133c9	Available	vpc-02692e9b805ebabc4 | us-west-2-shared-dev-vpc	10.172.228.0/22	2600:1f14:375:52e4::/64	983	us-west-2b	usw2-az1	us-west-2	rtb-056bc497f4b3811f5	acl-04bbc2e35eaef7716	No	No	No	-	No	299029076690 (shared)
Shared-Dev-APP-Subnet-AZ2
subnet-08cfb617298ecd3f0	Available	vpc-02692e9b805ebabc4 | us-west-2-shared-dev-vpc	10.155.232.0/22	–	796	us-west-2a	usw2-az2	us-west-2	rtb-05f7a778572531f65	acl-0313e9e5e51c48acf	No	No	No	-	No	299029076690 (shared)
Shared-Dev-APP-Subnet-AZ1
subnet-0f65f31aafc9bc086	Available	vpc-02692e9b805ebabc4 | us-west-2-shared-dev-vpc	10.155.228.0/22
    """

x = re.findall("1\w[\w./]+", txt)
#print(x)
y=[]

for i in range((len(x))):
    a=x[i]
    if a[-3] == "/":
       y.append(x[i])
print("This is the IP address from the string:" ,y)
print("Length of the output:", len(y))