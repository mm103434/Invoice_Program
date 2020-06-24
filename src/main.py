import os, csv
from MyInvoiceHandler import MyInvoiceHandler


# Set paths to input and output
#from src.MyInvoiceHandler import MyInvoiceHandler

final_product = MyInvoiceHandler()
number = 1
input_dir = '..//input'
output_dir = '..//output'

my_boolean = os.path.isdir(input_dir)
my_boolean2 = os.path.isdir(output_dir)

if not my_boolean:
    if not my_boolean2:
        os.mkdir(output_dir)

    os.mkdir(input_dir)
    exit(1)

for filename in os.listdir(input_dir):
    if filename.endswith(".txt"):
        invoice_loc = input_dir + "//" + filename
        #invoice_file = ""
        #for path in invoice_loc.iterdir():
         # only process if it is a file
         #   if path.is_file():
            # convert path to string and pass to function
        invoice_file = str(invoice_loc)



    # included columns.
        inc_cols = [2, 14, 15, 47, 46, 56]


        with open(invoice_loc, newline='') as textfile:
            my_reader = csv.reader(textfile, delimiter='\t', quotechar='|')
            count = 0
            for row in my_reader:
                new_text = list(row[i] for i in inc_cols)
                if count == 1:
                    final_product.setInvNum(row[0])
                    final_product.setInvAmt(row[14])
                    final_product.setDate(row[2])
                    final_product.setShortAmt(row[13])
                    final_product.setAmtPayable()
                    final_product.setDept(row[4])

                if count > 0:
                    final_product.compare_list(arrayrow=new_text)

                count += 1
                #print(new_text)

        final_product.invRound()
        final_product.showInvObject()
        final_product.writetoWord(number)
        final_product.addNew()
        number += 1

