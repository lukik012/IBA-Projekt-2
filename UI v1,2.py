import customtkinter as c

def change_content_beregner(): # funktion kalde calculator layout 
    for widget in frame.winfo_children():
        widget.grid_forget()

   #kald de funktioner og knapper som er relevante 
  
    o_label2.grid (row= 0, column = 2, padx=(20,0))
    p_label1.grid (row= 0, column = 3, padx=20)
    calc_label.grid (row= 0, column = 4)

    dropdown_mats.grid(row= 1, column = 1, padx=(20,0))
    dropdown_printere.grid(row= 2, column = 1, padx=(20,0))

    calc_E1.grid(row= 3, column = 1, padx=(20,0))
    calc_E2.grid(row= 4, column = 1, padx=(20,0))
    calc_E3.grid(row= 5, column = 1, padx=(20,0))
    calc_E4.grid(row= 6, column = 1, padx=(20,0))
    calc_E5.grid(row= 7, column = 1, padx=(20,0))

    calc_reset_BTN.grid(row= 8, column = 1, padx=(20,0))
    calc_save_BTN.grid(row= 8, column = 2, padx=(20,0))
    
    return_button.grid(row= 8, column=3 )


def change_content_database(): # funktion til at kalde DB frame layout
    for widget in frame.winfo_children():
        widget.grid_forget()

    #kald de funktioner og knapper som er relevante 
    o_label2.grid (row= 0, column = 0, padx=(5,0))
    db_label.grid (row= 0, column = 1)
    db_seBTN.grid(row= 1, column =0)
    db_redigerBTN.grid (row= 2, column =0, padx=20)
    db_removeBTN.grid(row= 3, column =0, padx=20)

    frame2.grid(row= 2, column=1)

    
    return_button.grid(row= 4, column=4 )



def change_content_users(): # funktion til at kalde users frame layout frem
    for widget in frame.winfo_children():
        widget.grid_forget()

  #kald de funktioner og knapper som er relevante 
    o_label2.grid(row= 0, column = 0, padx=(5,0))
    p_label1.grid(row= 0, column = 1, padx=(10))
    u_label.grid (row= 0, column = 2)

    add_user.grid(row= 3, column = 1 , padx=(10))
    remove_user.grid(row= 3, column = 2)

    return_button.grid(row= 4, column=4 )
   

def show_original_content():
    # tøm nuværende frame 
    for widget in frame.winfo_children():
        widget.grid_forget()

    # tilføj tilbage fra main menu 

    o_label1.grid(row= 1, column=2 )
    o_label2.grid(row= 1, column=3 )
    calc_button.grid(row= 2, column=1 )
    db_button.grid(row= 2, column=2 )
    user_button.grid(row= 2, column=3 )

    

    ## makør

# lav et vindu
master = c.CTk()
master.title("Dynamic Content Example")
master.geometry("700x500")

# lav en frame til at holde widgets
frame = c.CTkFrame(master, 
                   width= 650,
                   height=450,
                   fg_color="#757575" )
frame.pack(padx=10, pady=10, fill="both", expand=True)

frame2 = c.CTkFrame(frame, 
                   width= 250,
                   height=250,
                   fg_color="#000000" )



# labels
o_label1 = c.CTkLabel(frame,
                    text="NextPrint",
                    font= ("Tuffy",64))

o_label2 = c.CTkLabel(frame, 
                      text="Easy", 
                        text_color="#228B22", 
                        font=("Tuffy", 64))

calc_label = u_label =  c.CTkLabel(frame,
                    text="beregner",
                    font= ("Tuffy",64))

u_label =  c.CTkLabel(frame,
                    text="Users",
                    font= ("Tuffy",64))

db_label =  c.CTkLabel(frame,
                    text="DataBase",
                    font= ("Tuffy",64)) 

p_label1 = c.CTkLabel(frame,
                    text="Print",
                    font= ("Tuffy",64)) 


# main knapper
calc_button=c.CTkButton(frame, text = "Beregner",  #udregner knap
                       height = 200, 
                       width = 200,
                       font = ("helvetica", 24),
                       fg_color= 'green',
                       hover_color = "Blue",
                       corner_radius= 50, 
                       border_width= 2,
                       border_color= "black",
                       command=change_content_beregner)


db_button=c.CTkButton(frame, text = "Database",  #database knap
                       height = 200, 
                       width = 200,
                       font = ("helvetica", 24),
                       fg_color= 'green',
                       hover_color = "dark grey",
                       corner_radius= 50, 
                       border_width= 2,
                       border_color= "black",command=change_content_database)


user_button=c.CTkButton(frame, text = "users",  #user knap
                       height = 200, 
                       width = 200,
                       font = ("helvetica", 24),
                       fg_color= 'green',
                       hover_color = "dark grey",
                       corner_radius= 50, 
                       border_width= 2,
                       border_color= "black",command= change_content_users)

return_button=c.CTkButton(frame, text = "exit",  #til hovedmenu knap
                       height = 50, 
                       width = 50,
                       font = ("helvetica", 24),
                       fg_color= 'red',
                       hover_color = "dark red",
                       corner_radius= 50, 
                       border_width= 2,
                       border_color= "black",command=show_original_content)

##calc knapper
calc_save_BTN=c.CTkButton(frame, text = "Gem til DB og print",  #til hovedmenu knap
                       height = 50, 
                       width = 50,
                       font = ("helvetica", 24),
                       fg_color= 'green',
                       hover_color = "dark green",
                       corner_radius= 50, 
                       border_width= 2,
                       border_color= "black",)

calc_reset_BTN=c.CTkButton(frame, text = "Reset ",  #til hovedmenu knap
                       height = 50, 
                       width = 50,
                       font = ("helvetica", 24),
                       fg_color= 'red',
                       hover_color = "dark red",
                       corner_radius= 50, 
                       border_width= 2,
                       border_color= "black",)


##user knapper 
add_user=c.CTkButton(frame, text = "add user",  #user knap
                       height = 100, 
                       width = 100,
                       font = ("helvetica", 24),
                       fg_color= 'green',
                       hover_color = "dark grey",
                       corner_radius= 50, 
                       border_width= 2,
                       border_color= "black",)

remove_user=c.CTkButton(frame, text = "remove user",  #user knap
                       height = 100, 
                       width = 100,
                       font = ("helvetica", 24),
                       fg_color= 'green',
                       hover_color = "dark grey",
                       corner_radius= 50, 
                       border_width= 2,
                       border_color= "black",)

## database knapper
db_seBTN=c.CTkButton(frame, text = "Se data", 
                       height = 50, 
                       width = 100,
                       font = ("helvetica", 24),
                       fg_color= 'green',
                       hover_color = "dark grey",
                       corner_radius= 50, 
                       border_width= 2,
                       border_color= "black",)

db_redigerBTN=c.CTkButton(frame, text = "Rediger databasen",  
                       height = 50, 
                       width = 100,
                       font = ("helvetica", 24),
                       fg_color= 'green',
                       hover_color = "dark grey",
                       corner_radius= 50, 
                       border_width= 2,
                       border_color= "black",)

db_removeBTN=c.CTkButton(frame, text = "Slet databasen",  
                       height = 50, 
                       width = 100,
                       font = ("helvetica", 24),
                       fg_color= 'green',
                       hover_color = "dark grey",
                       corner_radius= 50, 
                       border_width= 2,
                       border_color= "black",)



#entrie fields
calc_E1 = c.CTkEntry(frame,
                    placeholder_text= "fyldningsprocent",)

calc_E2 = c.CTkEntry(frame,
                    placeholder_text= "densitet", )

calc_E3 = c.CTkEntry(frame,
                    placeholder_text= "højde",)

calc_E4 = c.CTkEntry(frame,
                    placeholder_text= "bredde",)

calc_E5 = c.CTkEntry(frame,
                    placeholder_text= "længde",)


#dropdowns 
mats=['ABS','Ultem', 'Clear Resin','Dental Resin','Accura Xtreme','casting Resin','PA2200','PA12','Alumide','Ti6Al4V','SSL314','Problack 10']
dropdown_mats= c.CTkComboBox (frame, 
                           values= mats,)

printere=['Ultimaker 3','Fortus 360 mc', 'form 2','ProX 950','ESOINT P800','EOSm100','3D systems Fig']
dropdown_printere=c.CTkComboBox (frame, 
                           values= printere,)


#placeringer i grid 
o_label1.grid(row= 1, column=2 )
o_label2.grid(row=1, column = 3)
calc_button.grid(row= 2, column=1 , padx= (10,0) )
db_button.grid(row= 2, column=2 )
user_button.grid(row= 2, column=3 )

# Start loop
master.mainloop()
