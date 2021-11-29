# eggOS
Easy Giftcard Generate Operating System (eggOS)

![Sample](eggOS_image.jpeg)

# Intro
eggOS stand for Easy Giftcard Generate Operating System, wriiten in Python 3, eggOS is a complete and straightforward unique code generating application, suitable for marketing code, gift card, redemption code, promo code, software serial number, etc.  
eggOS is built to create massive volume unique code (i.e. 100000+ codes) efficiently and prevent repeat codes and easy to confuse characters (i.e. L,I,1,J,O,0,V,U,etc) at the same time.  
The program supports generating additional codes from previous projects and comes with step-by-step command-line interface.

# Usage
eggOS can run in three different ways:  
1.	Direct executing  
2.	Import to another python application  
3.	Use directly via Python Interactive Shell   

When eggOS runs direct mode, eggOS will provide a simple step-by-step command-line interface to help the user use this application without any programming skills.

When running in an interactive shell or import to another python application, the developer can start creating code set by executing:  
> new_event = Code("New Event", "PFX", 9) 

while the number is the length of code.  
Common commands include:  
> new_event.create(10) #create 10 new codes  
> new_event.save() #save as txt file  
> new_event.check_unique() #check if the code set have any repeated codes  
> new_event.reload() #reload the code from file without saving  
> new_event.count() #count the qty of codes  
> new_event.name() #name of the event  
> print(new_event) #show the codes  

# Open Source License
This project is developed stand-alone by Nova Altesse for the term project of CS-521 MSc-InfoSec, Boston University and decided to open source after the course.  
This project is under the GPL License.
