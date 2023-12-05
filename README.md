# Covid-Fever-Kiosk-GUI
This is an implementation of a GUI for the project Fever kiosk which is basically a booth which asks user some questions and screens for the body temperature and finally indicates if the user is a suspect or not.

In the current pandemic situation, the screening of every individual was a terrible task. The workforce and infrastructure needed to be set up at many locations to carry out the testing and questioning of the people to know if they were possible suspects or not. This led to massive confusion and hard work in the maintenance of the data of the possible suspects and notifying them to get their tests done. We came up with an excellent idea where this questioning and preliminary tests could be carried out without interference from a dedicated workforce. This could be carried out by setting up kiosks in public places like gardens or streets. Such kiosks will have a simple questionnaire followed by wireless temperature scans and sanitized oxymeters scans. A screen with a designed GUI in three different languages for users to respond to these questions. The contact details will be inputted by the system and after evaluating the responses and the temperature and blood oxygen values the backend algorithm will decide whether the person is a possible COVID-19 suspect or not. These results will be sent to the central database and also to the person's phone number.

The front end of the screen which is the users’ interface is made using ‘Tkinter’ and ‘Pillow’ libraries in python. The GUI is made of 6 different screens. The first screen is the language selection for the users in the choice between three languages namely: English, Marathi, and Hindi. After selecting the desired language the further menus on the screen are reflected in the same language. On the second page, the users have to enter their mobile numbers after they enter their mobile numbers the data starts appending in the backend for the user data. After entering a correct phone number a random OTP is generated in the backend and sent to the phone numbers using the Twilio library. On the third screen, the users have to enter the OTP received by them on their phone numbers. There is a button for resending the OTP for the user. In the backend, the OTP generated and entered are compared, if they match the users are redirected to the next screen else the user gets 2 more tries to attempt the OTP verification. If failed they are redirected to the screen to enter the mobile number again. The third screen contains the personal details to be entered like the name, surname, and age and a submit button. After this, there is a set of questionnaires of 4 pages in which users select the radio buttons against the options available for them and press submit. The first questionnaire asks for the symptoms the user has been facing in the past 7 days. The 2nd page asks whether you're a healthcare worker and whether you've been taking care of a person affected by COVID-19 without a PPE kit in the last 2 weeks. The 3rd asks if you stay in a place that has covid affected patients and whether youtube traveled with the patient. The fourth page asks for any conditions you've been diagnosed with like asthma, heart attack, etc. After this Screen, the users are to insert their finger into a pulse oximeter which gets automatically sanitized after every use. The blood oxygen values are saved in the backend and also displayed for users to see it. The next screen has a request to stand in front of a contactless temperature sensor which after taking in the values displays it and indicated whether you're febrile or not febrile based on the threshold set. After answering all these questions, the following results are processed in the backend using a classifier algorithm. This algorithm classifies whether the user is a possible suspect of COVID-19 or not. In the end, it sends the result of this screening to the registered mobile number are sends a list of testing centers in Mumbai.

## Screenshots of GUI screens
![My Image](src/Screenshot%202023-12-04%20225352.png)

