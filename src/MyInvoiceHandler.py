from __future__ import print_function
import csv
from mailmerge import MailMerge
from PopupBox import PopupBox
from datetime import date


class MyInvoiceHandler:

    def __init__(self):
        self.final_invoice = "..//RESOURCES//Invoice_Form.docx"
        self.brand_new_items = []
        self.ref_sheet = ref_sheet = '..//RESOURCES//guide.txt'
        self.categories = ['CS', 'DB', 'D', 'DG', 'F', 'FC', 'M', 'N', 'P', 'PR', 'S']
        self.date = ""
        self.supplier = "US Foods"
        self.inv_num = ""
        self.inv_amt = 5950.03
        self.dynamic_amt = self.inv_amt
        self.short_amt = ""
        self.amt_payable = ""
        self.dept = ""
        self.chem = 0
        self.dairy_bread = 0
        self.drink = 0
        self.dry_goods = 0
        self.freight = 0
        self.frozen_cooler = 0
        self.meat = 0
        self.novelty = 0
        self.paper = 0
        self.produce = 0
        self.snacks = 0
        #self.cat_vars = [self.chem, self.dairy_bread, self.drink, self.dry_goods, self.freight, self.frozen_cooler, self.meat, self.novelty, self.paper, self.produce, self.snacks]

    def compare_list(self, arrayrow):
        amt = arrayrow[5]
        product_num = arrayrow[4]
        #print("Product number " + product_num + " costs $" + amt + " dollars.")
        with open(self.ref_sheet, newline='') as textfile:
            reader = csv.reader(textfile, delimiter='\t', quotechar='|')
            for row in reader:
                #print(row)
                new_text = list(row[i] for i in range(len(row)))
                if len(new_text) > 1:
                    if (new_text[1] == product_num) or (new_text[1] == arrayrow[3]):
                        self.categorizeArr(arrayrow, new_text)
                        return

                if len(new_text) < 3:
                    pass
                    #self.inv_num =


        print("Failed to find a match.")
        user_input = PopupBox()
        user_cat = user_input.makeWindow(arrayrow[3])
        user_cat = user_cat.upper()
        self.categorizeInt(arrayrow, user_cat)
        if user_cat != "":
            self.brand_new_items.append([arrayrow[3], product_num, user_cat])
        #print(user_cat)
        #print(self.brand_new_items)


    def categorizeArr(self, array1, array2):
        #print(array2[0] + " is " + array2[2])

        if array2[2] == "CS":
            self.chem += float(array1[5])
            self.dynamic_amt -= float(array1[5])
        elif array2[2] == "DB":
            self.dairy_bread += float(array1[5])
            self.dynamic_amt -= float(array1[5])
        elif array2[2] == "D":
            self.drink += float(array1[5])
            self.dynamic_amt -= float(array1[5])
        elif array2[2] == "DG":
            self.dry_goods += float(array1[5])
            self.dynamic_amt -= float(array1[5])
        elif array2[2] == "F":
            self.freight += float(array1[5])
            self.dynamic_amt -= float(array1[5])
        elif array2[2] == "FC":
            self.frozen_cooler += float(array1[5])
            self.dynamic_amt -= float(array1[5])
        elif array2[2] == "M":
            self.meat += float(array1[5])
            self.dynamic_amt -= float(array1[5])
        elif array2[2] == "N":
            self.novelty += float(array1[5])
            self.dynamic_amt -= float(array1[5])
        elif array2[2] == "P":
            self.paper += float(array1[5])
            self.dynamic_amt -= float(array1[5])
        elif array2[2] == "PR":
            self.produce += float(array1[5])
            self.dynamic_amt -= float(array1[5])
        elif array2[2] == "S":
            self.snacks += float(array1[5])
            self.dynamic_amt -= float(array1[5])
        else:
            #self.getUserInput()
            print("You are a failure.")
            self.dynamic_amt -= float(array1[5])
        print("Found Match")

    def categorizeInt(self, array, cat):
        if cat == "CS":
            self.chem += float(array[5])
            self.dynamic_amt -= float(array[5])
        elif cat == "DB":
            self.dairy_bread += float(array[5])
            self.dynamic_amt -= float(array[5])
        elif cat == "D":
            self.drink += float(array[5])
            self.dynamic_amt -= float(array[5])
        elif cat == "DG":
            self.dry_goods += float(array[5])
            self.dynamic_amt -= float(array[5])
        elif cat == "F":
            self.freight += float(array[5])
            self.dynamic_amt -= float(array[5])
        elif cat == "FC":
            self.frozen_cooler += float(array[5])
            self.dynamic_amt -= float(array[5])
        elif cat == "M":
            self.meat += float(array[5])
            self.dynamic_amt -= float(array[5])
        elif cat == "N":
            self.novelty += float(array[5])
            self.dynamic_amt -= float(array[5])
        elif cat == "P":
            self.paper += float(array[5])
            self.dynamic_amt -= float(array[5])
        elif cat == "PR":
            self.produce += float(array[5])
            self.dynamic_amt -= float(array[5])
        elif cat == "S":
            self.snacks += float(array[5])
            self.dynamic_amt -= float(array[5])
        else:
            #self.getUserInput()
            print("You are a failure.")
            self.dynamic_amt -= float(array[5])

    def showInvObject(self):
        print("Categories:")
        print("Chem/Suppl: $" + str(self.chem))
        print("Dairy/Bread: $" + str(self.dairy_bread))
        print("Drinks: $" + str(self.drink))
        print("Dry Goods: $" + str(self.dry_goods))
        print("Freight: $" + str(self.freight))
        print("Frozen/Cooler: $" + str(self.frozen_cooler))
        print("Meat: $" + str(self.meat))
        print("Novelty: $" + str(self.novelty))
        print("Paper: $" + str(self.paper))
        print("Produce: $" + str(self.produce))
        print("Snacks: $" + str(self.snacks))
        print("")
        print("The total inconsistency is " + str(self.dynamic_amt))


    def invRound(self):
        self.chem = round(self.chem, 2)
        self.dairy_bread = round(self.dairy_bread, 2)
        self.drink = round(self.drink, 2)
        self.dry_goods = round(self.dry_goods, 2)
        self.freight = round(self.freight, 2)
        self.frozen_cooler = round(self.frozen_cooler, 2)
        self.meat = round(self.meat, 2)
        self.novelty = round(self.novelty, 2)
        self.paper = round(self.paper, 2)
        self.produce = round(self.produce, 2)
        self.snacks = round(self.snacks, 2)
        self.dynamic_amt = round(self.dynamic_amt, 2)

    def addNew(self):
        new_text = []
        new_file = []
        with open(self.ref_sheet, newline='') as textfile:
            my_reader = csv.reader(textfile, delimiter='\t', quotechar='|')
            for row in my_reader:
                if row != []:
                    new_text = list(row[i] for i in [0, 1, 2])
                    new_file.append(new_text)

        for i in range(len(self.brand_new_items)):
            new_text = list(self.brand_new_items[i])
            new_file.append(new_text)

        with open(self.ref_sheet, 'w') as myfile:
            wr = csv.writer(myfile, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for i in range(len(new_file)):
                wr.writerow(new_file[i])

    def writetoWord(self, number):
        num = number
        document = MailMerge(self.final_invoice)
        print(document.get_merge_fields())
        document.merge(
            inv_date = self.date,
            supplier_name = self.supplier,
            inv_num = self.inv_num,
            inv_amt = "$" + self.inv_amt,
            short_amt = "$" + self.short_amt,
            amt_to_supplier = "$" + self.amt_payable,
            dept_charged = self.dept,
            chem = "$" + str(self.chem),
            dairy_bread = "$" + str(self.dairy_bread),
            drinks = "$" + str(self.drink),
            dry_goods = "$" + str(self.dry_goods),
            freight = "$" + str(self.freight),
            frozen_cooler = "$" + str(self.frozen_cooler),
            meat = "$" + str(self.meat),
            novelties = "$" + str(self.novelty),
            paper = "$" + str(self.paper),
            produce = "$" + str(self.produce),
            snacks = "$" + str(self.snacks),
            total_amt = "$" + str(self.amt_payable)
        )
        document.write(f"..//output//Invoice{num}.docx")


    def setInvNum(self, num):
        self.inv_num = num

    def setInvAmt(self, num):
        self.inv_amt = num
        self.dynamic_amt = round(float(num), 2)

    def setDate(self, date):
        self.date = date

    def setShortAmt(self, num):
        self.short_amt = num

    def setAmtPayable(self):
        self.amt_payable = str(round(float(self.inv_amt) - float(self.short_amt), 2))

    def setDept(self, dept):
        self.dept = dept










