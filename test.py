from tkinter import *
 
class Window(Frame):

    state = ""
    incometaxrate = 0
    salestaxrate = 0
    propertytaxrate = 0
    msg = ""
    

    def __init__(self, window, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        self.window = window
        self.window.geometry("680x500")
        
        self.window.title('Tax Calculator')
 
        # creating a frame for the listbox
        self.listbox_frame = Frame(self.window)

        lab = Label(self.listbox_frame, text="Select a state:")
        lab.pack()
 
        # creating scroll bar 
        sb = Scrollbar(self.listbox_frame, orient=VERTICAL)

 
        # creating listbox      
        self.listbox = Listbox(self.listbox_frame, exportselection=0, yscrollcommand=sb.set, 
                               width=30, height=27, selectmode=SINGLE)
        
 
        # set binding on item select in listbox
        self.listbox.bind('<<ListboxSelect>>', lambda event: self.when_clicked())
        self.listbox.pack(side=LEFT, fill=Y)
       
        sb.config(command=self.listbox.yview)
        sb.pack(side=LEFT, fill=Y)
 
        # grid listbox_frame to window
        self.listbox_frame.grid(row=0, column=0)
 
        # add items to listbox
        self.listbox.insert(1, "Alabama")
        self.listbox.insert(2, "Alaska")
        self.listbox.insert(3, "Arizona")
        self.listbox.insert(4, "Arkansas")
        self.listbox.insert(5, "California")
        self.listbox.insert(6, "Colorado")
        self.listbox.insert(7, "Connecticut")
        self.listbox.insert(8, "Delaware")
        self.listbox.insert(9, "Florida")
        self.listbox.insert(10, "Georgia")
        self.listbox.insert(11, "Hawaii")
        self.listbox.insert(12, "Idaho")
        self.listbox.insert(13, "Illinois")
        self.listbox.insert(14, "Indiana")
        self.listbox.insert(15, "Iowa")
        self.listbox.insert(16, "Kansas")
        self.listbox.insert(17, "Kentucky")
        self.listbox.insert(18, "Louisiana")
        self.listbox.insert(19, "Maine")
        self.listbox.insert(20, "Maryland")
        self.listbox.insert(21, "Massachusetts")
        self.listbox.insert(22, "Michigan")
        self.listbox.insert(23, "Minnesota")
        self.listbox.insert(24, "Mississippi")
        self.listbox.insert(25, "Missouri")
        self.listbox.insert(26, "Montana")
        self.listbox.insert(27, "Nebraska")
        self.listbox.insert(28, "Nevada")
        self.listbox.insert(29, "New Hampshire")
        self.listbox.insert(30, "New Jersey")
        self.listbox.insert(31, "New Mexico")
        self.listbox.insert(32, "New York")
        self.listbox.insert(33, "North Carolina")
        self.listbox.insert(34, "North Dakota")
        self.listbox.insert(35, "Ohio")
        self.listbox.insert(36, "Oklahoma")
        self.listbox.insert(37, "Oregon")
        self.listbox.insert(38, "Pennsylvania")
        self.listbox.insert(39, "Rhode Island")
        self.listbox.insert(40, "South Carolina")
        self.listbox.insert(41, "South Dakota")
        self.listbox.insert(42, "Tennessee")
        self.listbox.insert(43, "Texas")
        self.listbox.insert(44, "Utah")
        self.listbox.insert(45, "Vermont")
        self.listbox.insert(46, "Virginia")
        self.listbox.insert(47, "Washington")
        self.listbox.insert(48, "West Virginia")
        self.listbox.insert(49, "Wisconsin")
        self.listbox.insert(50, "Wyoming")

 
       #what occurs when an item from the listbox is clicked
    def when_clicked(self):
        selection = self.listbox.curselection()
        #selecting states
        if selection[0] == 0:
            state = "Alabama"
        if selection[0] == 1:
            state = "Alaska"
        if selection[0] == 2:
            state = "Arizona"
        if selection[0] == 3:
            state = "Arkansas"
        if selection[0] == 4:
            state = "California"
        if selection[0] == 5:
            state = "Colorado"
        if selection[0] == 6:
            state = "Connecticut"
        if selection[0] == 7:
            state = "Delaware"
        if selection[0] == 8:
            state = "Florida"
        if selection[0] == 9:
            state = "Georgia"
        if selection[0] == 10:
            state = "Hawaii"
        if selection[0] == 11:
            state = "Idaho"
        if selection[0] == 12:
            state = "Illinois"
        if selection[0] == 13:
            state = "Indiana"
        if selection[0] == 14:
            state = "Iowa"
        if selection[0] == 15:
            state = "Kansas"
        if selection[0] == 16:
            state = "Kentucky"
        if selection[0] == 17:
            state = "Louisiana"
        if selection[0] == 18:
            state = "Maine"
        if selection[0] == 19:
            state = "Maryland"
        if selection[0] == 20:
            state = "Massachusetts"
        if selection[0] == 21:
            state = "Michigan"
        if selection[0] == 22:
            state = "Minnesota"
        if selection[0] == 23:
            state = "Mississippi"
        if selection[0] == 24:
            state = "Missouri"
        if selection[0] == 25:
            state = "Montana"
        if selection[0] == 26:
            state = "Nebraska"
        if selection[0] == 27:
            state = "Nevada"
        if selection[0] == 28:
            state = "New Hampshire"
        if selection[0] == 29:
            state = "New Jersey"
        if selection[0] == 30:
            state = "New Mexico"
        if selection[0] == 31:
            state = "New York"
        if selection[0] == 32:
            state = "North Carolina"
        if selection[0] == 33:
            state = "North Dakota"
        if selection[0] == 34:
            state = "Ohio"
        if selection[0] == 35:
            state = "Oklahoma"
        if selection[0] == 36:
            state = "Oregon"
        if selection[0] == 37:
            state = "Pennsylvania"
        if selection[0] == 38:
            state = "Rhode Island"
        if selection[0] == 39:
            state = "South Carolina"
        if selection[0] == 40:
            state = "South Dakota"
        if selection[0] == 41:
            state = "Tennessee"
        if selection[0] == 42:
            state = "Texas"
        if selection[0] == 43:
            state = "Utah"
        if selection[0] == 44:
            state = "Vermont"
        if selection[0] == 45:
            state = "Virginia"
        if selection[0] == 46:
            state = "Washington"
        if selection[0] == 47:
            state = "West Virginia"
        if selection[0] == 48:
            state = "Wisconsin"
        if selection[0] == 49:
            state = "Wyoming"

       
                
            #income tax rates per state
        if state == "Alabama" :
            incometaxrate = 0.05
        elif state == "Alaska" :
            incometaxrate = 0
        elif state == "Arizona":
            incometaxrate = 0.0454
        elif state =="Arkansas":
            incometaxrate = 0.069
        elif state == "California":
            incometaxrate = 0.133
        elif state == "Colorado":
            incometaxrate = 0.0463
        elif state == "Connecticut":
            incometaxrate = 0.0699
        elif state == "Delaware":
            incometaxrate = 0.066
        elif state == "Florida":
            incometaxrate = 0
        elif state == "Georgia":
            incometaxrate = 0.0575
        elif state == "Hawaii":
            incometaxrate = 0.11
        elif state == "Idaho":
            incometaxrate = 0.0693
        elif state == "Illinois":
            incometaxrate = 0.0495
        elif state == "Indiana":
            incometaxrate = 0.0323
        elif state == "Iowa":
            incometaxrate = 0.0853
        elif state == "Kansas" :
            incometaxrate = 0.0570
        elif state == "Kentucky":
            incometaxrate = 0.05
        elif state =="Louisiana":
            incometaxrate = 0.06
        elif state == "Maine":
            incometaxrate = 0.0715
        elif state == "Maryland":
            incometaxrate = 0.0575
        elif state == "Massachusetts":
            incometaxrate = 0.0505
        elif state == "Michigan":
            incometaxrate = 0.0425
        elif state == "Minnesota":
            incometaxrate = 0.0985
        elif state == "Mississippi":
            incometaxrate = 0.05
        elif state == "Missouri":
            incometaxrate = 0.054
        elif state == "Montana":
            incometaxrate = 0.0690
        elif state == "Nebraska":
            incometaxrate = 0.0684
        elif state == "Nevada":
            incometaxrate = 0
        elif state == "New Hampshire":
            incometaxrate = 0.05
        elif state == "New Jersey" :
            incometaxrate = 0.1075
        elif state == "New Mexico":
            incometaxrate = 0.0490
        elif state =="New York":
            incometaxrate = 0.0882
        elif state == "North Carolina":
            incometaxrate = 0.0525
        elif state == "North Dakota":
            incometaxrate = 0.0290
        elif state == "Ohio":
            incometaxrate = 0.050
        elif state == "Oklahoma":
            incometaxrate = 0.050
        elif state == "Oregon":
            incometaxrate = 0.0990
        elif state == "Pennsylvania":
            incometaxrate = 0.0307
        elif state == "Rhode Island":
            incometaxrate = 0.0599
        elif state == "South Carolina":
            incometaxrate = 0.07
        elif state == "South Dakota":
            incometaxrate = 0
        elif state == "Tennessee":
            incometaxrate = 0.02
        elif state == "Texas":
            incometaxrate = 0
        elif state == "Utah":
            incometaxrate = 0.0495
        elif state == "Vermont":
            incometaxrate = 0.0875
        elif state == "Virginia":
            incometaxrate = 0.0575
        elif state == "Washington":
            incometaxrate = 0
        elif state == "West Virginia":
            incometaxrate = 0.065
        elif state == "Wisconsin":
            incometaxrate = 0.0765
        elif state == "Wyoming":
            incometaxrate = 0

        #sales tax rate per state
        if state == "Alabama":
            salestaxrate = 0.0914
        elif state == "Alaska":
            salestaxrate = 0.0143
        elif state == "Arizona":
            salestaxrate =  0.0837
        elif state == "Arkansas":
            salestaxrate = 0.0943
        elif state == "California":
            salestaxrate = 0.0856
        elif state == "Colorado":
            salestaxrate = 0.0763
        elif state == "Connecticut":
            salestaxrate = 0.0635
        elif state == "Delaware":
            salestaxrate = 0
        elif state == "Florida":
            salestaxrate = 0.0705
        elif state == "Georgia":
            salestaxrate = 0.0729
        elif state == "Hawaii":
            salestaxrate = 0.0441
        elif state == "Idaho":
            salestaxrate = 0.0603
        elif state == "Illinois":
            salestaxrate = 0.0874
        elif state == "Indiana":
            salestaxrate = 0.0700
        elif state == "Iowa":
            salestaxrate = 0.0682
        elif state == "Kansas":
            salestaxrate = 0.0867
        elif state == "Kentucky":
            salestaxrate = 0.0600
        elif state == "Louisiana":
            salestaxrate = 0.0945
        elif state == "Maine":
            salestaxrate = 0.0550
        elif state == "Maryland":
            salestaxrate = 0.0600
        elif state == "Massachusetts":
            salestaxrate = 0.0625
        elif state == "Michigan":
            salestaxrate = 0.0600
        elif state == "Minnesota":
            salestaxrate = 0.0743
        elif state == "Mississippi":
            salestaxrate = 0.0707
        elif state == "Missouri":
            salestaxrate = 0.0813
        elif state == "Montana":
            salestaxrate = 0
        elif state == "Nebraska":
            salestaxrate = 0.0685
        elif state == "Nevada":
            salestaxrate = 0.0814
        elif state == "New Hampshire":
            salestaxrate = 0
        elif state == "New Jersey":
            salestaxrate = 0.0660
        elif state == "New Mexico":
            salestaxrate = 0.0782
        elif state == "New York":
            salestaxrate = 0.0849
        elif state == "North Carolina":
            salestaxrate = 0.0697
        elif state == "North Dakota":
            salestaxrate = 0.0685
        elif state == "Ohio":
            salestaxrate = 0.0717
        elif state == "Oklahoma":
            salestaxrate = 0.0892
        elif state == "Oregon":
            salestaxrate = 0
        elif state == "Pennsylvania":
            salestaxrate = 0.0634
        elif state == "Rhode Island":
            salestaxrate = 0.0700
        elif state == "South Carolina":
            salestaxrate = 0.0743
        elif state == "South Dakota":
            salestaxrate = 0.0640
        elif state == "Tennessee":
            salestaxrate = 0.0947
        elif state == "Texas":
            salestaxrate = 0.0819
        elif state == "Utah":
            salestaxrate = 0.0694
        elif state == "Vermont":
            salestaxrate = 0.0618
        elif state == "Virginia":
            salestaxrate = 0.0565
        elif state == "Washington":
            salestaxrate = 0.0917
        elif state == "West Virginia":
            salestaxrate = 0.0639
        elif state == "Wisconsin":
            salestaxrate = 0.0544
        elif state == "Wyoming":
            salestaxrate = 0.0536 

        #property tax rate per state
        if state == "Alabama" :
            propertytaxrate = 0.004
        elif state == "Alaska" :
            propertytaxrate = 0.0101
        elif state == "Arizona":
            propertytaxrate = 0.0066
        elif state =="Arkansas":
            propertytaxrate = 0.0064
        elif state == "California":
            propertytaxrate = 0.0073
        elif state == "Colorado":
            propertytaxrate = 0.0059
        elif state == "Connecticut":
            propertytaxrate = 0.0153
        elif state == "Delaware":
            propertytaxrate = 0.0055
        elif state == "Florida":
            propertytaxrate = 0.0098
        elif state == "Georgia":
            propertytaxrate = 0.0091
        elif state == "Hawaii":
            propertytaxrate = 0.0028
        elif state == "Idaho":
            propertytaxrate = 0.0073
        elif state == "Illinois":
            propertytaxrate = 0.0198
        elif state == "Indiana":
            propertytaxrate = 0.0086
        elif state == "Iowa":
            propertytaxrate = 0.0142
        elif state == "Kansas" :
            propertytaxrate = 0.0130
        elif state == "Kentucky":
            propertytaxrate = 0.0080
        elif state =="Louisiana":
            propertytaxrate = 0.0050
        elif state == "Maine":
            propertytaxrate = 0.0120
        elif state == "Maryland":
            propertytaxrate = 0.0100
        elif state == "Massachusetts":
            propertytaxrate = 0.0111
        elif state == "Michigan":
            propertytaxrate = 0.0146
        elif state == "Minnesota":
            propertytaxrate = 0.0109
        elif state == "Mississippi":
            propertytaxrate = 0.0065
        elif state == "Missouri":
            propertytaxrate = 0.0100
        elif state == "Montana":
            propertytaxrate = 0.0075
        elif state == "Nebraska":
            propertytaxrate = 0.0165
        elif state == "Nevada":
            propertytaxrate = 0.0071
        elif state == "New Hampshire":
            propertytaxrate = 0.0199
        elif state == "New Jersey" :
            propertytaxrate = 0.0211
        elif state == "New Mexico":
            propertytaxrate = 0.0066
        elif state =="New York":
            propertytaxrate = 0.0138
        elif state == "North Carolina":
            propertytaxrate = 0.0084
        elif state == "North Dakota":
            propertytaxrate = 0.0095
        elif state == "Ohio":
            propertytaxrate = 0.0158
        elif state == "Oklahoma":
            propertytaxrate = 0.0085
        elif state == "Oregon":
            propertytaxrate = 0.0101
        elif state == "Pennsylvania":
            propertytaxrate = 0.0146
        elif state == "Rhode Island":
            propertytaxrate = 0.0146
        elif state == "South Carolina":
            propertytaxrate = 0.0055
        elif state == "South Dakota":
            propertytaxrate = 0.0122
        elif state == "Tennessee":
            propertytaxrate = 0.0075
        elif state == "Texas":
            propertytaxrate = 0.0167
        elif state == "Utah":
            propertytaxrate = 0.0063
        elif state == "Vermont":
            propertytaxrate = 0.0170
        elif state == "Virginia":
            propertytaxrate = 0.0081
        elif state == "Washington":
            propertytaxrate = 0.0094
        elif state == "West Virginia":
            propertytaxrate = 0.0053
        elif state == "Wisconsin":
            propertytaxrate = 0.0174
        elif state == "Wyoming":
            propertytaxrate = 0.0051          


            #message to show what state has been chosen
        msg = "You've chosen " + state + "!"
        self.messageVar = Message(self.listbox_frame, text = msg, width = 700, aspect = 250) 
        self.messageVar.config(bg='lightblue') 
        self.messageVar.pack()

            #calculating sales tax
        def calculate_sales():
            amount_of_purchase = float(entry_1.get())
            total1 = salestaxrate*amount_of_purchase
            string_to_display = "Tax to be paid is " + str(round(total1,2))
            self.message = Message(self.listbox_frame, text = string_to_display, width = 200)
            self.message.pack()
            button55.pack()

            #calculating income tax
        def calculate_income():
            amount_of_income = float(entry_2.get())
            total2 = incometaxrate*amount_of_income
            string_to_display = "Tax on income to be paid is " + str(round(total2,2))
            self.message = Message(self.listbox_frame, text = string_to_display, width = 200)
            self.message.pack()
            button55.pack()

            #calculating property tax
        def calculate_property():
            amount_of_property = float(entry_3.get())
            total3 = propertytaxrate*amount_of_property
            string_to_display = "Tax on property to be paid is " + str(round(total3,2))
            self.message = Message(self.listbox_frame, text = string_to_display, width = 200)
            self.message.pack()
            button55.pack()


        #allows user to enter salary, purchase amount, etc
        def show_sales_when_clicked():
            Label_1.pack()
            entry_1.pack()
            button_1.pack()

        def show_income_when_clicked():
            Label_2.pack()
            entry_2.pack()
            button_2.pack()
            
        def show_property_when_clicked():
            Label_3.pack()
            entry_3.pack()
            button_3.pack()
            
        Label_1 = Label(self.listbox_frame, text = "Enter your amount of purchase")
        entry_1 = Entry(self.listbox_frame)
        button_1 = Button(self.listbox_frame, text = "Calculate your sales tax", command = calculate_sales)

        Label_2 = Label(self.listbox_frame, text = "Enter your annual salary")
        entry_2 = Entry(self.listbox_frame)
        button_2 = Button(self.listbox_frame, text = "Calculate your income tax", command = calculate_income)

        Label_3 = Label(self.listbox_frame, text = "Enter your property value")
        entry_3 = Entry(self.listbox_frame)
        button_3 = Button(self.listbox_frame, text = "Calculate your property tax", command = calculate_property)


        #options of which tax to calculate
        button1 = Button(self.listbox_frame, text = "Calculate income tax", command = show_income_when_clicked)
        button1.pack()
        button2 = Button(self.listbox_frame, text = "Calculate property tax", command = show_property_when_clicked)
        button2.pack()
        button3 = Button(self.listbox_frame, text = "Calculate sales tax", command = show_sales_when_clicked)
        button3.pack()


        #opens up when "done" is clicked
        def toplevel():
            top = Toplevel()
            top.title("Expenses")

            if len(entry_1.get()) != 0:
                amount_of_purchase = float(entry_1.get())
                total1 = salestaxrate*amount_of_purchase
                purchase_string = "Budget for an extra " + str(round(total1,2)) + " you might need to spend on sales tax" 
                pmessage = Message(top, text = purchase_string, width = 400)
                pmessage.pack()

            if len(entry_2.get()) != 0:
                amount_of_income = float(entry_2.get())
                total2 = incometaxrate*amount_of_income
                income_tosave = total2/12
                income_string = "Save " + str(round(income_tosave,2)) + " of your income per month towards your income tax." 
                imessage = Message(top, text = income_string, width = 400)
                imessage.pack()

            if len(entry_3.get()) != 0:
                amount_of_property = float(entry_3.get())
                total3 = propertytaxrate*amount_of_property
                property_tosave = total3/12
                property_string = "Save " + str(round(property_tosave,2)) + " per month towards your property tax." 
                prmessage = Message(top, text = property_string, width = 400)
                prmessage.pack()

            
        button55 = Button(self.listbox_frame, text="Done", command=toplevel)
        
       
        
    
        
 
if __name__ == "__main__":
    root = Tk()
    App = Window(root)
    root.mainloop()


