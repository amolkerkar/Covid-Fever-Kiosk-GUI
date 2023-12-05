import tkinter as tk 
from tkinter import ttk 
from PIL import ImageTk,Image


LARGEFONT =("Verdana", 35) 

class tkinterApp(tk.Tk): 
	
	# __init__ function for class tkinterApp 
	def __init__(self, *args, **kwargs): 
		
		# __init__ function for class Tk 
		tk.Tk.__init__(self, *args, **kwargs) 
		tk.Tk.minsize(self,700 ,400)
		tk.Tk.geometry(self,"630x500")
		
		# creating a container 
		container = tk.Frame(self) 
		container.pack(side = "top", fill = "both", expand = True) 


		container.grid_rowconfigure(0, weight = 1) 
		container.grid_columnconfigure(0, weight = 1) 

		# initializing frames to an empty array 
		self.frames = {} 

		# iterating through a tuple consisting 
		# of the different page layouts 
		for F in (StartPage, e1, e2,e3,ep1,ep2,ep3,ep4,ep5,ep6,rmfinger,suspect,process
		,h1,h2,h3,hp1,hp2,hp3,hp4,hp5,hp6,hrmfinger,hsuspect,hprocess,m1,m2,m3,mp1): 

			frame = F(container, self) 

			# initializing frame of that object from 
			# startpage, page1, page2 respectively with 
			# for loop 
			self.frames[F] = frame 

			frame.grid(row = 0, column = 0, sticky ="nsew") 

		self.show_frame(StartPage) 

	# to display the current frame passed as 
	# parameter 
	def show_frame(self, cont): 
		frame = self.frames[cont] 
		frame.tkraise() 


# ----------------------------------------------------------------------------------------------------------------------------

class StartPage(tk.Frame): 
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent,background="black") 
		
		# label of frame Layout 2 
		label1 = ttk.Label(self, text ="PLEASE SELECT A LANGUAGE",foreground="white",background="black",font='GALVJI 20').place(relx=0.5, rely=0.1, anchor='c')
		label2 = ttk.Label(self, text ="कृपया भाषा चुनें",foreground="white",background="black",font='GALVJI 20').place(relx=0.5, rely=0.2, anchor="c")
		label3 = ttk.Label(self, text ="कृपया एखादी भाषा निवडा",foreground="white",background="black",font='GALVJI 20').place(relx=0.5, rely=0.3, anchor="c")
		

		button1 = tk.Button(self, text ="English",background="white",font='GALVJI 14',width=35,height=2,command = lambda : controller.show_frame(e1)).place(relx=0.5, rely=0.5, anchor="c")
		button2 = tk.Button(self, text ="हिन्दी",background="white",font='GALVJI 14',width=35,height=2,command = lambda : controller.show_frame(h1)).place(relx=0.5, rely=0.7, anchor="c")
		button3 = tk.Button(self, text ="मराठी",background="white",font='GALVJI 14',width=35,height=2,command = lambda : controller.show_frame(m1)).place(relx=0.5, rely=0.9, anchor="c")
	
# --------------------------------------------------------------------------------------------------------------------------------
# ENGLISH FRAMES 

class e1(tk.Frame): 
	
	def __init__(self, parent, controller): 
		
		tk.Frame.__init__(self, parent,background="black")
		
		# label
		label = ttk.Label(self, text ="PLEASE ENTER YOUR 10 DIGIT MOBILE NUMBER TO RECEIVE OTP VIA SMS",foreground="white",background="black",font='GALVJI 13').place(relx=0.5, rely=0.3, anchor='c') 
        # entrybox
		entrybox1=tk.Entry(self,background="white",font='GALVJI 14',width=35).place(relx=0.5, rely=0.4, anchor='c')
		
		# button to show frame 2 with text 
		# layout2 
		button1 = tk.Button(self, text ="SUBMIT",background="red",font='GALVJI 14',width=25,height=2, command = lambda : controller.show_frame(e2)).place(relx=0.5, rely=0.6, anchor='c')
	

class e2(tk.Frame): 
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent,background="black") 

		# label 
		# label = ttk.Label(self, text ="Thank You for using the Fever Kiosk. Your OTP is", font = LARGEFONT).grid(row = 0, column = 4, padx = 10, pady = 10)
		label = ttk.Label(self, text ="PLEASE ENTER OTP SENT TO YOUR MOBILE NUMBER VIA SMS",foreground="white",background="black",font='GALVJI 14').place(relx=0.5, rely=0.3, anchor='c')

		# entrybox 
		entrybox=tk.Entry(self,background="white",font='GALVJI 14',width=35).place(relx=0.5, rely=0.4, anchor='c')
		# button to show frame 2 with text 
		# layout2 
		button1 = tk.Button(self, text ="RESEND OTP",background="red",font='GALVJI 14',width=25,height=1,command = lambda : controller.show_frame(e3)).place(relx=0.2, rely=0.7, anchor='c')
		button2 = tk.Button(self, text ="SUBMIT",background="red",font='GALVJI 14',width=25,height=1, command = lambda : controller.show_frame(e3)).place(relx=0.8, rely=0.7, anchor='c')



class e3(tk.Frame):
	def __init__(self,parent,controller):

		tk.Frame.__init__(self,parent,background="black")
		# label 
		l1=ttk.Label(self,text="PLEASE ENTER YOUR PERSONAL DETAILS ",foreground="white",background="black",font='GALVJI 20').place(relx=0.5, rely=0.1, anchor='c')
		l1=ttk.Label(self,text="Name ",foreground="white",background="black",font='GALVJI 14').place(relx=0.3, rely=0.3, anchor='c')
		l1=ttk.Label(self,text="Surname",foreground="white",background="black",font='GALVJI 14').place(relx=0.3, rely=0.4, anchor='c')
		l1=ttk.Label(self,text="Age ",foreground="white",background="black",font='GALVJI 14').place(relx=0.3, rely=0.5, anchor='c')

		# entry boxes
		ee1=ttk.Entry(self).place(relx=0.5, rely=0.3, anchor='c')
		ee2=ttk.Entry(self).place(relx=0.5, rely=0.4, anchor='c')
		ee3=ttk.Entry(self).place(relx=0.5, rely=0.5, anchor='c')

		# buttons/
		bb1=tk.Button(self,text="SUBMIT",background="red",font='GALVJI 14',width=35,height=2,command= lambda:controller.show_frame(ep1)).place(relx=0.5, rely=0.7, anchor='c')

class ep1(tk.Frame):
	def __init__(self, parent,controller):

		tk.Frame.__init__(self, parent,background="black")

		ttk.Label(self,text="PAGE 1/6",foreground="white",background="black",font='GALVJI 14').place(relx=0.5, rely=0.05, anchor='c')
		tk.Label(self,text="1. PLEASE SELECT THE SYMPTOMS THAT YOU ARE EXPERIENCING OR HAVE EXPERIENCED IN",foreground="white",background="black",font='GALVJI 11').place(relx=0.5, rely=0.125, anchor='c')
		
		tk.Label(self,text="THE LAST 7 DAYS (IF ANY)",foreground="white",background="black",font='GALVJI 11').place(relx=0.5, rely=0.175, anchor='c')

		# variable 
		fever= int
		cough=int
		breath= int
		throat= int
		loose= int
		ns= int

		tk.Checkbutton(self,text="Fever",foreground="red",background="black",font='GALVJI 14',variable=fever,onvalue=0,offvalue=1).place(relx=0.5, rely=0.3, anchor='c')
		tk.Checkbutton(self,text="SHORTNESS OF BREATH \n (BREATHLESSNESS)",foreground="red",background="black",font='GALVJI 14',variable=breath,onvalue=0,offvalue=1).place(relx=0.5, rely=0.4, anchor='c')
		tk.Checkbutton(self,text="COUGH",foreground="red",background="black",font='GALVJI 14',variable=cough,onvalue=0,offvalue=1).place(relx=0.5, rely=0.5, anchor='c')
		tk.Checkbutton(self,text="SORE THROAT",foreground="red",background="black",font='GALVJI 14',variable=throat,onvalue=0,offvalue=1).place(relx=0.5, rely=0.6, anchor='c')
		tk.Checkbutton(self,text="LOOSE MOTIONS",foreground="red",background="black",font='GALVJI 14',variable=loose,onvalue=0,offvalue=1).place(relx=0.5, rely=0.7, anchor='c')
		tk.Checkbutton(self,text="NO SYMPTOMS",foreground="red",background="black",font='GALVJI 14',variable=ns,onvalue=0,offvalue=1).place(relx=0.5, rely=0.8, anchor='c')

		ttk.Button(self,text="Next Page ->",command=lambda:controller.show_frame(ep2)).place(relx=0.5, rely=0.9, anchor='c')

class ep2(tk.Frame):
	def __init__(self, parent,controller):

		tk.Frame.__init__(self, parent,background="black")

		
		# variable 
		healthcare= tk.IntVar()
		woppe=tk.IntVar()
		# woppe= tk.StringVar


		h=tk.Radiobutton(self,text="yes",foreground="red",background="black",font='GALVJI 14',variable=healthcare,value=1).place(relx=0.5, rely=0.2, anchor='c')
		h=tk.Radiobutton(self,text="no",foreground="red",background="black",font='GALVJI 14',variable=healthcare,value=0).place(relx=0.5, rely=0.3, anchor='c')

		tk.Radiobutton(self,text="yes",foreground="red",background="black",font='GALVJI 14',variable=woppe,value=1).place(relx=0.5, rely=0.6, anchor='c')
		tk.Radiobutton(self,text="no",foreground="red",background="black",font='GALVJI 14',variable=woppe,value=0).place(relx=0.5, rely=0.7, anchor='c')


		ttk.Label(self,text="page 2/6",foreground="white",background="black",font='GALVJI 14').place(relx=0.5, rely=0.05, anchor='c')
		ttk.Label(self,text="2. ARE YOU A HEALTHCARE WORKER?",foreground="white",background="black",font='GALVJI 12').place(relx=0.5, rely=0.125, anchor='c')
		ttk.Label(self,text="3. HAVE YOU BEEN PROVIDING DIRECT CARE TO COVID-19 PATIENTS IN THE LAST 14 \n DAYS WITHOUT PERSONAL PROTECTIVE EQUIPMENT (PPE)?",foreground="white",background="black",font='GALVJI 12').place(relx=0.5, rely=0.5, anchor='c')

		tk.Button(self,text="previous",foreground="white",background="black",font='GALVJI 14',command=lambda:controller.show_frame(ep1)).place(relx=0.2, rely=0.8, anchor='c')
		tk.Button(self,text="next",foreground="white",background="black",font='GALVJI 14',command=lambda:controller.show_frame(ep3)).place(relx=0.8, rely=0.8, anchor='c')

class ep3(tk.Frame):
	def __init__(self, parent,controller):

		tk.Frame.__init__(self, parent,background="black")

		
		# variable 
		stay= tk.IntVar()
		travel=tk.IntVar()
		# woppe= tk.StringVar


		h=tk.Radiobutton(self,text="yes",foreground="red",background="black",font='GALVJI 14',variable=stay,value=1).place(relx=0.5, rely=0.2, anchor='c')
		h=tk.Radiobutton(self,text="no",foreground="red",background="black",font='GALVJI 14',variable=stay,value=0).place(relx=0.5, rely=0.3, anchor='c')

		tk.Radiobutton(self,text="yes",foreground="red",background="black",font='GALVJI 14',variable=travel,value=1).place(relx=0.5, rely=0.6, anchor='c')
		tk.Radiobutton(self,text="no",foreground="red",background="black",font='GALVJI 14',variable=travel,value=0).place(relx=0.5, rely=0.7, anchor='c')


		tk.Label(self,text="page 3/6",foreground="white",background="black",font='GALVJI 14').place(relx=0.5, rely=0.05, anchor='c')
		tk.Label(self,text="4. HAVE YOU BEEN STAYING IN THE SAME CLOSE ENVIRONMENT OF A COVID-19 POSITIVE \n PATIENT (EG. WORKPLACE, CLASSROOM, HOUSEHOLD, GATHERINGS) IN THE LAST 14 DAYS ?",foreground="white",background="black",font='GALVJI 11').place(relx=0.5, rely=0.125, anchor='c')
		tk.Label(self,text="5. HAVE YOU TRAVELLED IN CLOSE PROXIMITY (1 METER) WITH A SYMPTOMATIC PERSON WHO \n LATER TESTED POSITIVE FOR COVID-19 IN THE LAST 14 DAYS?",foreground="white",background="black",font='GALVJI 11').place(relx=0.5, rely=0.5, anchor='c')

		tk.Button(self,text="previous",foreground="white",background="black",font='GALVJI 14',command=lambda:controller.show_frame(ep2)).place(relx=0.2, rely=0.8, anchor='c')
		tk.Button(self,text="next",foreground="white",background="black",font='GALVJI 14',command=lambda:controller.show_frame(ep4)).place(relx=0.8, rely=0.8, anchor='c')

class ep4(tk.Frame):
	def __init__(self, parent,controller):

		tk.Frame.__init__(self, parent,background="black")

		
		# variable 
		conditionss= tk.IntVar()
		conditionss1= tk.IntVar()
		conditionss2= tk.IntVar()
		conditionss3= tk.IntVar()
		conditionss4= tk.IntVar()
		conditionss5= tk.IntVar()
		conditionss6= tk.IntVar()
		conditionss7= tk.IntVar()
		
		# woppe= tk.StringVar


		h=tk.Checkbutton(self,text="DIABETES (HIGH BLOOD SUGAR)",foreground="red",background="black",font='GALVJI 14',variable=conditionss,onvalue=1,offvalue=0).place(relx=0.5, rely=0.2, anchor='c')
		h=tk.Checkbutton(self,text="HYPERTENSION (HIGH BLOOD PRESSURE)",foreground="red",background="black",font='GALVJI 14',variable=conditionss1,onvalue=1,offvalue=0).place(relx=0.5, rely=0.275, anchor='c')
		h=tk.Checkbutton(self,text="ASTHMA",foreground="red",background="black",font='GALVJI 14',variable=conditionss2,onvalue=1,offvalue=0).place(relx=0.5, rely=0.35, anchor='c')
		h=tk.Checkbutton(self,text="STROKE",foreground="red",background="black",font='GALVJI 14',variable=conditionss3,onvalue=1,offvalue=0).place(relx=0.5, rely=0.425, anchor='c')
		h=tk.Checkbutton(self,text="HEART ATTACK/ OTHER HEART PROBLEMS",foreground="red",background="black",font='GALVJI 14',variable=conditionss4,onvalue=1,offvalue=0).place(relx=0.5, rely=0.525, anchor='c')
		h=tk.Checkbutton(self,text="CANCER",foreground="red",background="black",font='GALVJI 14',variable=conditionss5,onvalue=1,offvalue=0).place(relx=0.5, rely=0.6, anchor='c')
		h=tk.Checkbutton(self,text="PREGNANCY",foreground="red",background="black",font='GALVJI 14',variable=conditionss6,onvalue=1,offvalue=0).place(relx=0.5, rely=0.675, anchor='c')
		h=tk.Checkbutton(self,text="NONE OF THE ABOVE",foreground="red",background="black",font='GALVJI 14',variable=conditionss7,onvalue=1,offvalue=0).place(relx=0.5, rely=0.725, anchor='c')

		


		tk.Label(self,text="page 4/6",foreground="white",background="black",font='GALVJI 14').place(relx=0.5, rely=0.05, anchor='c')
		tk.Label(self,text="6. PLEASE SELECT THE CONDITIONS THAT YOU HAVE BEEN DIAGNOSED WITH (IF ANY) ",foreground="white",background="black",font='GALVJI 12').place(relx=0.5, rely=0.125, anchor='c')
		

		tk.Button(self,text="previous page",foreground="white",background="black",font='GALVJI 14',command=lambda:controller.show_frame(ep3)).place(relx=0.2, rely=0.9, anchor='c')
		tk.Button(self,text="SUBMIT",foreground="white",background="black",font='GALVJI 14',command=lambda:controller.show_frame(ep5)).place(relx=0.8, rely=0.9, anchor='c')

class ep5(tk.Frame):
	def __init__(self, parent,controller):

		tk.Frame.__init__(self, parent,background="black")

		
		# variable 
		oxyValue=90

		

	


		tk.Label(self,text="page 5/6",foreground="white",background="black",font='GALVJI 14').place(relx=0.5, rely=0.05, anchor='c')
		tk.Label(self,text=" PLEASE INSERT YOUR FINGER INTO THE PULSE OXIMETER TILL THE VALUE\n APPEARS ON THE SCREEN",foreground="white",background="black",font='GALVJI 12').place(relx=0.5, rely=0.2, anchor='c')
		tk.Label(self,text="OXYGEN SATURATION:",foreground="white",background="black",font='GALVJI 14').place(relx=0.4, rely=0.8, anchor='c')
		tk.Label(self,text=str(oxyValue),foreground="white",background="black",font='GALVJI 14').place(relx=0.6, rely=0.8, anchor='c')
		myimage=ImageTk.PhotoImage(Image.open(".\Images\Picture.png"))
		panel=tk.Label(self,image=myimage)
		panel.photo=myimage
		panel.place(relx=0.5, rely=0.5, anchor='c')
		tk.Button(self,text="next",command=lambda:controller.show_frame(rmfinger)).place(relx=0.5, rely=0.9, anchor='c')
		
class rmfinger(tk.Frame):
	def __init__(self, parent,controller):

		tk.Frame.__init__(self, parent,background="black")

		

		

	


		tk.Label(self,text="YOU MAY NOW WITHDRAW YOUR FINGER",foreground="white",background="black",font='GALVJI 14').place(relx=0.5, rely=0.1, anchor='c')

		myimage2=ImageTk.PhotoImage(Image.open(".\Images\tick.png"))
		panel=tk.Label(self,image=myimage2,background='black')
		panel.photo=myimage2
		panel.place(relx=0.5, rely=0.5, anchor='c')
		
		tk.Button(self,text="next",foreground="white",background="black",font='GALVJI 14',command=lambda:controller.show_frame(ep6)).place(relx=0.5, rely=0.9, anchor='c')
		
class ep6(tk.Frame):
	def __init__(self, parent,controller):

		tk.Frame.__init__(self, parent,background="black")

		# variabledd
		temperature= 104
		tk.Label(self,text="page 6/6",foreground="white",background="black",font='GALVJI 12').place(relx=0.5, rely=0.1, anchor='c')
		tk.Label(self,text=" PLEASE STAND IN THE YELLOW BOX IN FRONT OF THE TEMPERATURE SCANNER \n TILL THE VALUE APPEARS ON THE SCREEN",foreground="white",background="black",font='GALVJI 12').place(relx=0.5, rely=0.3, anchor='c')
		tk.Label(self,text="TEMPERATURE",foreground="white",background="black",font='GALVJI 13').place(relx=0.5, rely=0.42, anchor='c')
		tk.Label(self,text=temperature,foreground="BLACK",background="WHITE",font='GALVJI 16').place(relx=0.5, rely=0.5, anchor='c')
		if temperature>100:
			tk.Label(self,text='FEBRILE',foreground="white",background="RED",font='GALVJI 16').place(relx=0.5, rely=0.6, anchor='c')
		else:
			tk.Label(self,text='AFEBRILE',foreground="BLACK",background="GREEN",font='GALVJI 16').place(relx=0.5, rely=0.6, anchor='c')
			
          
		
		tk.Button(self,text="next",foreground="white",background="black",font='GALVJI 14',command=lambda:controller.show_frame(process)).place(relx=0.5, rely=0.9, anchor='c')

class process(tk.Frame):
	def __init__(self, parent,controller):

		tk.Frame.__init__(self, parent,background="black")

		# ttk.Label(self,text="PROCESSING RESULTS...",foreground="white",background="RED",font='GALVJI 16').place(relx=0.5, rely=0.6, anchor='c')
	    
		tk.Button(self,text="next",foreground="white",background="RED",font='GALVJI 16',command=lambda:controller.show_frame(suspect)).place(relx=0.5, rely=0.9, anchor='c')
		myimage3=ImageTk.PhotoImage(Image.open(".\Images\ok.png")) 
		panel=tk.Label(self,image=myimage3,background='black') 
		panel.photo=myimage3 
		panel.place(relx=0.5, rely=0.5, anchor='c')



class suspect(tk.Frame):
	def __init__(self, parent,controller):

		tk.Frame.__init__(self, parent,background="black")

		suspection="suspect"

		tk.Label(self,text="YOU ARE",foreground="white",background="BLACK",font='BodoniSvtyTwoOSITCTT-Book 13').place(relx=0.5, rely=0.125, anchor='c')
		tk.Label(self,text=suspection,foreground="white",background="RED",font='BodoniSvtyTwoOSITCTT-Book 14').place(relx=0.5, rely=0.2, anchor='c')
		tk.Label(self,text="FOR COVID-19. ",foreground="white",background="BLACK",font='BodoniSvtyTwoOSITCTT-Book 13').place(relx=0.5, rely=0.275, anchor='c')
		# tk.Button(self,text="next",foreground="white",background="RED",font='GALVJI 16',command=lambda:controller.show_frame(omk)).place(relx=0.5, rely=0.6, anchor='c')

		if suspection=="suspect":
			tk.Label(self,text="KINDLY GET YOURSELF TESTED FOR COVID-19 ",foreground="white",background="BLACK",font='BodoniSvtyTwoOSITCTT-Book 12').place(relx=0.5, rely=0.4, anchor='c')
			tk.Label(self,text="SHOULD YOU BE EXPERIENCING SEVERE SYMPTOMS, KINDLY CONSULT A PHYSICIAN IMMEDIATELY.  ",foreground="white",background="BLACK",font='BodoniSvtyTwoOSITCTT-Book 10').place(relx=0.5, rely=0.5, anchor='c')
			tk.Label(self,text="IN CASE OF ANY COVID RELATED QUERIES, KINDLY CONTACT THE BMC HELPLINE NUMBER 1916. ",foreground="white",background="BLACK",font='BodoniSvtyTwoOSITCTT-Book 10').place(relx=0.5, rely=0.6, anchor='c')
			tk.Label(self,text=" (You have been sent the result of your screening  via SMS on your Registered Mobile Number along with a list of the \nCOVID-19 Testing Facilities in Mumbai)  ",foreground="white",background="BLACK",font='BodoniSvtyTwoOSITCTT-Book 10').place(relx=0.5, rely=0.7, anchor='c')

			# send msg :" (You have been sent the result of your screening via SMS on your Registered Mobile Number along with a list of theCOVID-19 Testing Facilities in Mumbai) "
		else:
		 tk.Label(self,text="YOU MAY GET YOURSELF ASSESSED AGAIN IN CASE OF ANY SYMPTOMS. \nSHOULD YOU BE EXPERIENCING SEVERE SYMPTOMS, KINDLY CONSULT A PHYSICIAN IMMEDIATELY.",foreground="white",background="black",font='BodoniSvtyTwoOSITCTT-Book 10').place(relx=0.5, rely=0.4, anchor='c') 
		 tk.Label(self,text="IN CASE OF ANY SYMPTOMS OTHER THAN THE ONES MENTIONED,\n PLEASE CONSULT YOUR NEAREST PHYSICIAN.",foreground="white",background="black",font='BodoniSvtyTwoOSITCTT-Book 10').place(relx=0.5, rely=0.5, anchor='c')
		 tk.Label(self,text="IN CASE OF ANY COVID RELATED QUERIES, KINDLY CONTACT THE BMC HELPLINE NUMBER 1916.",foreground="white",background="black",font='BodoniSvtyTwoOSITCTT-Book 10').place(relx=0.5, rely=0.6, anchor='c')
		 tk.Label(self,text="(You have been sent the result of your screening via SMS on your Registered Mobile Number along with a list of \n the COVID-19 Testing Facilities in Mumbai) ",foreground="white",background="black",font='BodoniSvtyTwoOSITCTT-Book 10').place(relx=0.5, rely=0.7, anchor='c')
	     	# send msg :" (You have been sent the result of your screening via SMS on your Registered Mobile Number along with a list of \n the COVID-19 Testing Facilities in Mumbai) "

        



# ---------------------------------------------------------------------------------------------------------------------------------
# Hindi FRAMES 

class h1(tk.Frame): 
	
	def __init__(self, parent, controller): 
		
		tk.Frame.__init__(self, parent,background="black")
		
		# label
		label = ttk.Label(self, text ="SMS दारा OTP पानेके िलए कृ पया अपना मोबाइल नमर दजरकर",foreground="white",background="black",font='GALVJI 13').place(relx=0.5, rely=0.3, anchor='c') 
        # entrybox
		entrybox1=tk.Entry(self,background="white",font='GALVJI 14',width=35).place(relx=0.5, rely=0.4, anchor='c')

		# button to show frame 2 with text 
		# layout2 
		button1 = tk.Button(self, text ="SUBMIT",background="red",font='GALVJI 14',width=25,height=2, command = lambda : controller.show_frame(h2)).place(relx=0.5, rely=0.6, anchor='c')
	

class h2(tk.Frame): 
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent,background="black") 

		# label 
		# label = ttk.Label(self, text ="Thank You for using the Fever Kiosk. Your OTP is", font = LARGEFONT).grid(row = 0, column = 4, padx = 10, pady = 10)
		label = ttk.Label(self, text ="SMS दारा भेजा गया OTP नीचेिलिखए",foreground="white",background="black",font='GALVJI 14').place(relx=0.5, rely=0.3, anchor='c')

		# entrybox 
		entrybox=tk.Entry(self,background="white",font='GALVJI 14',width=35).place(relx=0.5, rely=0.4, anchor='c')
		# button to show frame 2 with text 
		# layout2 
		button1 = tk.Button(self, text ="OTP दोबारा भेिजए",background="red",font='GALVJI 14',width=25,height=1,command = lambda : controller.show_frame(e3)).place(relx=0.2, rely=0.7, anchor='c')
		button2 = tk.Button(self, text ="आग",background="red",font='GALVJI 14',width=25,height=1, command = lambda : controller.show_frame(h3)).place(relx=0.8, rely=0.7, anchor='c')



class h3(tk.Frame):
	def __init__(self,parent,controller):

		tk.Frame.__init__(self,parent,background="black")
		# label 
		l1=ttk.Label(self,text="कृ पया अपनी िनजी जानकारी दजरकीिजए ",foreground="white",background="black",font='GALVJI 20').place(relx=0.5, rely=0.1, anchor='c')
		l1=ttk.Label(self,text="नाम ",foreground="white",background="black",font='GALVJI 14').place(relx=0.3, rely=0.3, anchor='c')
		l1=ttk.Label(self,text="उपनाम (सरनेम)",foreground="white",background="black",font='GALVJI 14').place(relx=0.3, rely=0.4, anchor='c')
		l1=ttk.Label(self,text="ऊम ",foreground="white",background="black",font='GALVJI 14').place(relx=0.3, rely=0.5, anchor='c')

		# entry boxes
		ee1=ttk.Entry(self).place(relx=0.5, rely=0.3, anchor='c')
		ee2=ttk.Entry(self).place(relx=0.5, rely=0.4, anchor='c')
		ee3=ttk.Entry(self).place(relx=0.5, rely=0.5, anchor='c')

		# buttons/
		bb1=tk.Button(self,text="आग",background="red",font='GALVJI 14',width=35,height=2,command= lambda:controller.show_frame(hp1)).place(relx=0.5, rely=0.7, anchor='c')

class hp1(tk.Frame):
	def __init__(self, parent,controller):

		tk.Frame.__init__(self, parent,background="black")

		ttk.Label(self,text="PAGE 1/6",foreground="white",background="black",font='GALVJI 14').place(relx=0.5, rely=0.05, anchor='c')
		tk.Label(self,text="1. िदए गए लकणो मेसेजो लकण आप इस समय अनुभव कर रहेहै, ",foreground="white",background="black",font='GALVJI 11').place(relx=0.5, rely=0.125, anchor='c')
		
		tk.Label(self,text="या िजनका अनुभव आपको िपछले 7 िदनो मेहआ है; उन लकणो को चुिनए ।",foreground="white",background="black",font='GALVJI 11').place(relx=0.5, rely=0.175, anchor='c')

		# variable 
		fever= int
		cough=int
		breath= int
		throat= int
		loose= int
		ns= int

		tk.Checkbutton(self,text="बुख़ार",foreground="red",background="black",font='GALVJI 14',variable=fever,onvalue=0,offvalue=1).place(relx=0.5, rely=0.3, anchor='c')
		tk.Checkbutton(self,text="साँस लेनेमेिदकत \n(साँस फू लना)",foreground="red",background="black",font='GALVJI 14',variable=breath,onvalue=0,offvalue=1).place(relx=0.5, rely=0.4, anchor='c')
		tk.Checkbutton(self,text="खाँस",foreground="red",background="black",font='GALVJI 14',variable=cough,onvalue=0,offvalue=1).place(relx=0.5, rely=0.5, anchor='c')
		tk.Checkbutton(self,text="गलेमेख़राश",foreground="red",background="black",font='GALVJI 14',variable=throat,onvalue=0,offvalue=1).place(relx=0.5, rely=0.6, anchor='c')
		tk.Checkbutton(self,text="जुलाब",foreground="red",background="black",font='GALVJI 14',variable=loose,onvalue=0,offvalue=1).place(relx=0.5, rely=0.7, anchor='c')
		tk.Checkbutton(self,text="इनमेसेकोई भी नही",foreground="red",background="black",font='GALVJI 14',variable=ns,onvalue=0,offvalue=1).place(relx=0.5, rely=0.8, anchor='c')

		ttk.Button(self,text="आगे>>>",command=lambda:controller.show_frame(hp2)).place(relx=0.5, rely=0.9, anchor='c')

class hp2(tk.Frame):
	def __init__(self, parent,controller):

		tk.Frame.__init__(self, parent,background="black")

		
		# variable 
		healthcare= tk.IntVar()
		woppe=tk.IntVar()
		# woppe= tk.StringVar


		h=tk.Radiobutton(self,text="हाँ",foreground="red",background="black",font='GALVJI 14',variable=healthcare,value=1).place(relx=0.5, rely=0.2, anchor='c')
		h=tk.Radiobutton(self,text="नही",foreground="red",background="black",font='GALVJI 14',variable=healthcare,value=0).place(relx=0.5, rely=0.3, anchor='c')

		tk.Radiobutton(self,text="हाँ",foreground="red",background="black",font='GALVJI 14',variable=woppe,value=1).place(relx=0.5, rely=0.6, anchor='c')
		tk.Radiobutton(self,text="नही",foreground="red",background="black",font='GALVJI 14',variable=woppe,value=0).place(relx=0.5, rely=0.7, anchor='c')


		ttk.Label(self,text="page 2/6",foreground="white",background="black",font='GALVJI 14').place(relx=0.5, rely=0.05, anchor='c')
		ttk.Label(self,text="2. का आप सास कमरचारी (हॉिसटल मेकाम करनेवालेविक) है?",foreground="white",background="black",font='GALVJI 12').place(relx=0.5, rely=0.125, anchor='c')
		ttk.Label(self,text="3. का आपनेिपछले 14 िदनो मेिबना सुरका यंत के (PPE के बग़ैर)\n कोरोना (COVID-19) के मरीज़ो की देखभाल की थी ?",foreground="white",background="black",font='GALVJI 12').place(relx=0.5, rely=0.5, anchor='c')

		tk.Button(self,text="<<<पीछ",foreground="white",background="black",font='GALVJI 14',command=lambda:controller.show_frame(hp1)).place(relx=0.2, rely=0.8, anchor='c')
		tk.Button(self,text="आगे>>>",foreground="white",background="black",font='GALVJI 14',command=lambda:controller.show_frame(hp3)).place(relx=0.8, rely=0.8, anchor='c')

class hp3(tk.Frame):
	def __init__(self, parent,controller):

		tk.Frame.__init__(self, parent,background="black")

		
		# variable 
		stay= tk.IntVar()
		travel=tk.IntVar()
		# woppe= tk.StringVar


		h=tk.Radiobutton(self,text="हाँ",foreground="red",background="black",font='GALVJI 14',variable=stay,value=1).place(relx=0.5, rely=0.2, anchor='c')
		h=tk.Radiobutton(self,text="नही",foreground="red",background="black",font='GALVJI 14',variable=stay,value=0).place(relx=0.5, rely=0.3, anchor='c')

		tk.Radiobutton(self,text="हाँ",foreground="red",background="black",font='GALVJI 14',variable=travel,value=1).place(relx=0.5, rely=0.6, anchor='c')
		tk.Radiobutton(self,text="नही",foreground="red",background="black",font='GALVJI 14',variable=travel,value=0).place(relx=0.5, rely=0.7, anchor='c')


		tk.Label(self,text="page 3/6",foreground="white",background="black",font='GALVJI 14').place(relx=0.5, rely=0.05, anchor='c')
		tk.Label(self,text="4. का आप िपछले 14 िदनो मेिकसी COVID-19 पॉिजिटव रोगी के करीबी वातावरण मेरहेहै ? \n(जैसेकाम पर, कका मे, घर मे, यािकसी बड़ी सभा मे)",foreground="white",background="black",font='GALVJI 11').place(relx=0.5, rely=0.125, anchor='c')
		tk.Label(self,text="5. का आपनेिपछले 14 िदनो मेिकसी ऐसेविक के पास ( 1 मीटर सेकम दरी) बैठकर सफ़र िकया हैिजसको कोरोना के लकण थेऔर बाद मे COVID-19 पॉिजिटव पाया गया ?",foreground="white",background="black",font='GALVJI 11').place(relx=0.5, rely=0.5, anchor='c')

		tk.Button(self,text="<<<पीछ",foreground="white",background="black",font='GALVJI 14',command=lambda:controller.show_frame(hp2)).place(relx=0.2, rely=0.8, anchor='c')
		tk.Button(self,text="आगे>>>",foreground="white",background="black",font='GALVJI 14',command=lambda:controller.show_frame(hp4)).place(relx=0.8, rely=0.8, anchor='c')

class hp4(tk.Frame):
	def __init__(self, parent,controller):

		tk.Frame.__init__(self, parent,background="black")

		
		# variable 
		conditionss= tk.IntVar()
		conditionss1= tk.IntVar()
		conditionss2= tk.IntVar()
		conditionss3= tk.IntVar()
		conditionss4= tk.IntVar()
		conditionss5= tk.IntVar()
		conditionss6= tk.IntVar()
		conditionss7= tk.IntVar()
		
		# woppe= tk.StringVar


		h=tk.Checkbutton(self,text="डायिबटीज़ (शकर की बीमारी)",foreground="red",background="black",font='GALVJI 14',variable=conditionss,onvalue=1,offvalue=0).place(relx=0.5, rely=0.2, anchor='c')
		h=tk.Checkbutton(self,text="उच रकचाप (बी॰ पी॰ की बीमारी)",foreground="red",background="black",font='GALVJI 14',variable=conditionss1,onvalue=1,offvalue=0).place(relx=0.5, rely=0.275, anchor='c')
		h=tk.Checkbutton(self,text="दमा (असमा)",foreground="red",background="black",font='GALVJI 14',variable=conditionss2,onvalue=1,offvalue=0).place(relx=0.5, rely=0.35, anchor='c')
		h=tk.Checkbutton(self,text="लकवा",foreground="red",background="black",font='GALVJI 14',variable=conditionss3,onvalue=1,offvalue=0).place(relx=0.5, rely=0.425, anchor='c')
		h=tk.Checkbutton(self,text="हदय रोग (हाटरअटैक या िदल की कोई बीमारी )",foreground="red",background="black",font='GALVJI 14',variable=conditionss4,onvalue=1,offvalue=0).place(relx=0.5, rely=0.525, anchor='c')
		h=tk.Checkbutton(self,text="गभरवती",foreground="red",background="black",font='GALVJI 14',variable=conditionss5,onvalue=1,offvalue=0).place(relx=0.5, rely=0.6, anchor='c')
		h=tk.Checkbutton(self,text="ककर रोग (कै नर)",foreground="red",background="black",font='GALVJI 14',variable=conditionss6,onvalue=1,offvalue=0).place(relx=0.5, rely=0.675, anchor='c')
		h=tk.Checkbutton(self,text="इनमेसेकोई भी नही",foreground="red",background="black",font='GALVJI 14',variable=conditionss7,onvalue=1,offvalue=0).place(relx=0.5, rely=0.725, anchor='c')

		


		tk.Label(self,text="page 4/6",foreground="white",background="black",font='GALVJI 14').place(relx=0.5, rely=0.05, anchor='c')
		tk.Label(self,text="6. नीचेिलख़ी गई बीमािरयो मेसेआपको जो बीमािरयाँहई हैउनेचुिनये: ",foreground="white",background="black",font='GALVJI 12').place(relx=0.5, rely=0.125, anchor='c')
		

		tk.Button(self,text="<<<पीछ",foreground="white",background="black",font='GALVJI 14',command=lambda:controller.show_frame(hp3)).place(relx=0.2, rely=0.9, anchor='c')
		tk.Button(self,text="आगे",foreground="white",background="black",font='GALVJI 14',command=lambda:controller.show_frame(hp5)).place(relx=0.8, rely=0.9, anchor='c')

class hp5(tk.Frame):
	def __init__(self, parent,controller):

		tk.Frame.__init__(self, parent,background="black")

		
		# variable 
		oxyValue=90

		

	


		tk.Label(self,text="page 5/6",foreground="white",background="black",font='GALVJI 14').place(relx=0.5, rely=0.05, anchor='c')
		tk.Label(self,text="बाजूमेरखेगए PULSE OXIMETER (नीलेरंग का यंत) मेअपनी उँगली डािलए और सीन पर आँ कडेआनेकी पतीका कीिजए ।",foreground="white",background="black",font='GALVJI 12').place(relx=0.5, rely=0.2, anchor='c')
		tk.Label(self,text="OXYGEN SATURATION:",foreground="white",background="black",font='GALVJI 14').place(relx=0.4, rely=0.8, anchor='c')
		tk.Label(self,text=str(oxyValue),foreground="white",background="black",font='GALVJI 14').place(relx=0.6, rely=0.8, anchor='c')
		myimage=ImageTk.PhotoImage(Image.open(".\Images\Picture.png"))
		panel=tk.Label(self,image=myimage)
		panel.photo=myimage
		panel.place(relx=0.5, rely=0.5, anchor='c')
		tk.Button(self,text="previous",command=lambda:controller.show_frame(hrmfinger)).place(relx=0.5, rely=0.9, anchor='c')
		
class hrmfinger(tk.Frame):
	def __init__(self, parent,controller):

		tk.Frame.__init__(self, parent,background="black")

		

		

	


		tk.Label(self,text="अब आप अपनी उँगली िनकाल सकतेहै।",foreground="white",background="black",font='GALVJI 14').place(relx=0.5, rely=0.1, anchor='c')

		myimage2=ImageTk.PhotoImage(Image.open(".\Images\tick.png"))
		panel=tk.Label(self,image=myimage2,background='black')
		panel.photo=myimage2
		panel.place(relx=0.5, rely=0.5, anchor='c')
		
		tk.Button(self,text="previous",foreground="white",background="black",font='GALVJI 14',command=lambda:controller.show_frame(hp6)).place(relx=0.5, rely=0.9, anchor='c')
		
class hp6(tk.Frame):
	def __init__(self, parent,controller):

		tk.Frame.__init__(self, parent,background="black")

		# variabledd
		temperature= 104
		tk.Label(self,text="page 6/6",foreground="white",background="black",font='GALVJI 12').place(relx=0.5, rely=0.1, anchor='c')
		tk.Label(self,text=" कृ पया ज़मीन मेबनाए पीलेचौकोन मेखड़ेरहेऔर सीन पर आँ कड़ेआनेतक तापमान सनेर (TEMPERATURE SCANNER) \n की ओर देखतेरिहए",foreground="white",background="black",font='GALVJI 12').place(relx=0.5, rely=0.3, anchor='c')
		tk.Label(self,text="TEMPERATURE",foreground="white",background="black",font='GALVJI 13').place(relx=0.5, rely=0.42, anchor='c')
		tk.Label(self,text=temperature,foreground="BLACK",background="WHITE",font='GALVJI 16').place(relx=0.5, rely=0.5, anchor='c')
		if temperature>100:
			tk.Label(self,text='आपको बुख़ार ह',foreground="white",background="RED",font='GALVJI 16').place(relx=0.5, rely=0.6, anchor='c')
		else:
			tk.Label(self,text='आपको बुख़ार नही ह',foreground="BLACK",background="GREEN",font='GALVJI 16').place(relx=0.5, rely=0.6, anchor='c')
			
          
		
		tk.Button(self,text="previous",foreground="white",background="black",font='GALVJI 14',command=lambda:controller.show_frame(hprocess)).place(relx=0.5, rely=0.9, anchor='c')

class hprocess(tk.Frame):
	def __init__(self, parent,controller):

		tk.Frame.__init__(self, parent,background="black")

		# ttk.Label(self,text="PROCESSING RESULTS...",foreground="white",background="RED",font='GALVJI 16').place(relx=0.5, rely=0.6, anchor='c')
	    
		tk.Button(self,text="next",foreground="white",background="RED",font='GALVJI 16',command=lambda:controller.show_frame(hsuspect)).place(relx=0.5, rely=0.9, anchor='c')
		myimage3=ImageTk.PhotoImage(Image.open(".\Images\okh.png")) 
		panel=tk.Label(self,image=myimage3,background='black') 
		panel.photo=myimage3 
		panel.place(relx=0.5, rely=0.5, anchor='c')



class hsuspect(tk.Frame):
	def __init__(self, parent,controller):

		tk.Frame.__init__(self, parent,background="black")

		suspection="suspect"

		tk.Label(self,text="YOU ARE",foreground="white",background="BLACK",font='BodoniSvtyTwoOSITCTT-Book 13').place(relx=0.5, rely=0.125, anchor='c')
		tk.Label(self,text="आप कोरोना (COVID-19) संिदग (ससेक) नही ह",foreground="white",background="RED",font='BodoniSvtyTwoOSITCTT-Book 14').place(relx=0.5, rely=0.2, anchor='c')
		tk.Label(self,text="FOR COVID-19. ",foreground="white",background="BLACK",font='BodoniSvtyTwoOSITCTT-Book 13').place(relx=0.5, rely=0.275, anchor='c') 

		# tk.Button(self,text="next",foreground="white",background="RED",font='GALVJI 16',command=lambda:controller.show_frame(omk)).place(relx=0.5, rely=0.6, anchor='c')

		if suspection=="SUSPECT":
			tk.Label(self,text="कृ पया अपनी कोरोना (COVID-19) जाँच करवाएँ । यिद लकण अतंत गंभीर हैया मरीज़ की जान ख़तरेमेमहसूस होती हैतो कृ पया अपने नज़दीकी डाकर सेसंपकर करे।",foreground="white",background="BLACK",font='BodoniSvtyTwoOSITCTT-Book 12').place(relx=0.5, rely=0.4, anchor='c')
			tk.Label(self,text="अिधक जानकारी केिलए आप BMC हेललाइन 1916 पर संपकर करे।",foreground="white",background="BLACK",font='BodoniSvtyTwoOSITCTT-Book 10').place(relx=0.5, rely=0.5, anchor='c')
			
			tk.Label(self,text=" इस जाँच केपिरणाम केसाथ शहर केसभी कोरोना (COVID-19) टिसग सेटर की सूिच आपको अपनेमोबाइल नंबर पर SMS दारा भेजागयी है। ",foreground="white",background="BLACK",font='BodoniSvtyTwoOSITCTT-Book 10').place(relx=0.5, rely=0.7, anchor='c')

			# send msg :" (You have been sent the result of your screening via SMS on your Registered Mobile Number along with a list of theCOVID-19 Testing Facilities in Mumbai) "
		else:
		 tk.Label(self,text="िद आपको COVID-19 सेजुड़ेिकसी भी लकण का अनुभव होता हैतो आप फ़ीवर कीआसमेअपनी जाँच पुनः कर सकतेहै। यिद लकण अतंत गंभीर हैया मरीज़ की जान ख़तरेमेमहसूस होती हैतो कृ पया अपनेनज़दीकी डाकर सेसंपकर करे।",foreground="white",background="RED",font='BodoniSvtyTwoOSITCTT-Book 16').place(relx=0.5, rely=0.4, anchor='c') 
		 tk.Label(self,text="अिधक जानकारी केिलए आप BMC हेललाइन 1916 पर संपकर करे।.",foreground="white",background="RED",font='BodoniSvtyTwoOSITCTT-Book 16').place(relx=0.5, rely=0.5, anchor='c')
		 tk.Label(self,text="IN CASE OF ANY COVID RELATED QUERIES, KINDLY CONTACT THE BMC HELPLINE NUMBER 1916.",foreground="white",background="RED",font='BodoniSvtyTwoOSITCTT-Book 16').place(relx=0.5, rely=0.6, anchor='c')
		 tk.Label(self,text="इस जाँच केपिरणाम केसाथ शहर केसभी कोरोना (COVID-19) टिसग सेटर की सूिच आपको अपनेमोबाइल नंबर पर SMS दारा भेजागयी है। ",foreground="white",background="RED",font='BodoniSvtyTwoOSITCTT-Book 16').place(relx=0.5, rely=0.7, anchor='c')
	     	# send msg :" (You have been sent the result of your screening via SMS on your Registered Mobile Number along with a list of theCOVID-19 Testing Facilities in Mumbai) "


# Marathi FRAMES 

class m1(tk.Frame): 
	
	def __init__(self, parent, controller): 
		
		tk.Frame.__init__(self, parent)
		
		# label
		label = ttk.Label(self, text =" (marathi) PLEASE ENTER YOUR 10 DIGIT MOBILE NUMBER TO RECEIVE OTP VIA SMS").grid(row = 0, column = 4, padx = 10, pady = 10) 

        # entrybox
		entrybox1=ttk.Entry(self).grid(row =1, column =4 , padx=0,pady=10)

		# button to show frame 2 with text 
		# layout2 
		button1 = ttk.Button(self, text ="SUBMIT",command = lambda : controller.show_frame(m2)).grid(row = 2, column = 5, padx = 10, pady = 10) 
	

class m2(tk.Frame): 
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent) 

		# label 
		# label = ttk.Label(self, text ="Thank You for using the Fever Kiosk. Your OTP is", font = LARGEFONT).grid(row = 0, column = 4, padx = 10, pady = 10)
		label = ttk.Label(self, text =" (marathi) PLEASE ENTER OTP SENT TO YOUR MOBILE NUMBER VIA SMS", font = LARGEFONT).grid(row = 0, column = 4, padx = 10, pady = 10)

		# entrybox 
		entrybox=ttk.Entry(self).grid(row = 2, column = 4, padx = 10, pady = 10)
		# button to show frame 2 with text 
		# layout2 
		button1 = ttk.Button(self, text ="SUBMIT", command = lambda : controller.show_frame(m3)).grid(row = 2, column = 1, padx = 10, pady = 10) 


class m3(tk.Frame):
	def __init__(self,parent,controller):

		tk.Frame.__init__(self,parent)
		# label 
		l1=ttk.Label(self,text="(marathi)PLEASE ENTER YOUR PERSONAL DETAILS ").grid(row=0,column=0)
		l1=ttk.Label(self,text="m name ").grid(row=1,column=0)
		l1=ttk.Label(self,text="m surname").grid(row=2,column=0)
		l1=ttk.Label(self,text="m age ").grid(row=3,column=0)

		# entry boxes
		ee1=ttk.Entry(self).grid(row=1,column=1)
		ee2=ttk.Entry(self).grid(row=2,column=1)
		ee3=ttk.Entry(self).grid(row=3,column=1)

		# buttons/
		bb1=ttk.Button(self,text="SUBMIT",command= lambda:controller.show_frame(mp1)).grid(row=4,column=2)

	
class mp1(tk.Frame):
	def __init__(self, parent,controller):

		tk.Frame.__init__(self, parent)

		ttk.Label(self,text="m page 1/6").grid(row=0,column=0)
		ttk.Label(self,text="m 1. PLEASE SELECT THE SYMPTOMS THAT YOU ARE EXPERIENCING OR HAVE EXPERIENCED INTHE LAST 7 DAYS (IF ANY)").grid(row=1,column=5)
		
		# variable 
		fever= bool
		cough= bool
		breath= bool
		throat= bool
		loose= bool
		ns= bool

		ttk.Checkbutton(self,text="Fever",variable=fever).grid(row=3,column=0)
		ttk.Checkbutton(self,text="SHORTNESS OF BREATH (BREATHLESSNESS)",variable=cough).grid(row=4,column=0)
		ttk.Checkbutton(self,text="COUGH",variable=breath).grid(row=5,column=0)
		ttk.Checkbutton(self,text="SORE THROAT",variable=throat).grid(row=6,column=0)
		ttk.Checkbutton(self,text="LOOSE MOTIONS",variable=loose).grid(row=7,column=0)
		ttk.Checkbutton(self,text="NO SYMPTOMS",variable=ns).grid(row=8,column=0)

		ttk.Button(self,text="Next Page ->>",command=lambda:controller.show_frame(mp2)).grid(row=9,column=0)

# Driver Code 
app = tkinterApp() 
app.mainloop() 
