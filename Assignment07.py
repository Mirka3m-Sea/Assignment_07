#------------------------------------------#
# Title: Assignment07.py
# Desc: Starting with Assig06, 
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
#Miroslava Meza, 2022-Mar-06, Included classes and functions
#Miroslava Meza, 2022-Mar-06, Eliminated TODO marks, pass, and redundant code lines
#Miroslava Meza, 2022-Mar-12, Corrected from HW6, clearing any previously saved inventory txt by using append.
#Miroslava Meza, 2022-Mar-13, Modified lines for user input to include error handling, and data storage on binary type
#------------------------------------------#

# -- DATA -- #
strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {}  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object
cdData =[None, None, None] # Saving data in memory as a list, starts with no values.
dicRow= {'ID': None, 'Title':None, 'Artist':None} #start the dictionary with no values

#Importing module
import pickle
# -- PROCESSING -- #

class DataProcessor:
    #"""
    # Action-1 add functions for processing here
    #using the functions identified in the starter code as:
    #    3.3.2, 3.5.2, 3.6.2.1
    def add_data():
        """
        Add and save data entries
        Using the list type variable named 'cdData' 
        variable names were already in dicRow
        
        Args: intID, strTitle, stArtist, IO.cdData, IO.show_inventory, lstable, dicRow
        Returns: inventory list with new entry.
        
        Note: read and write functions are on the next class.
        """
        intID, strTitle,stArtist =IO.data_input()
        dicRow = {'ID': intID, 'Title': strTitle, 'Artist': stArtist}
        lstTbl.append(dicRow)
        IO.show_inventory(lstTbl)
        
        
    def delete_data(intIDDel): 
        """
        This function allows to erase a data entry.
        Args: lstTbl, intIDDel, intRowNr
        IO.show_inventory
        
        ASSIGNMENT 07- If the ID provided by user is invalid or not Int type.
        Substituted the previous option of "else:"l
        
        """
        intRowNr = -1
        blnCDRemoved = False
        for row in lstTbl:
            intRowNr += 1
            if row['ID'] == intIDDel:
                del lstTbl[intRowNr]
                blnCDRemoved = True
                break
        if blnCDRemoved:
            print('The CD was removed\n')
        try:
            if blnCDRemoved == True:
                print('CD removed\n')
            if blnCDRemoved == False:
                raise Exception
        except Exception:
            print('CD not found \nGoing to main menu\n ')
            return intIDDel
        IO.show_inventory(lstTbl)

        
class FileProcessor:
    """Processing the data to and from text file
    ASSIGNMENT 07-  Storing the information into binary data
    """

    @staticmethod
    def read_file(file_name, table):
        """Function to manage data ingestion from file to a list of dictionaries

         Reads the data from file identified by file_name=strFileName into a 2D table
         (list of dicts) table one line in the file represents one dictionary row in table.
         Args:
             strFileName (string): name of file used to read the data from
             table (list of dict): 2D data structure (list of dicts) that holds the data during runtime
         Returns: None.
        *** file_name will be tied to the variable strFileName
        
        ASSIGNMENT 07: Store inventory into binary data type. Use Picking module

        """
        objFile = open(file_name, 'ab') # It did not work if I used 'rb'
        pickle.dump(table, objFile) # pickle.dump(obj, file, protocol=None, *, fix_imports=True, buffer_callback=None) 
        #                           #Return the pickled representation of the object obj as a bytes object, instead of writing it to a file.
        print('You have a new binary file ready to work.\n') 
        objFile.close()

            
    @staticmethod
    def write_file(file_name, table):
        """
        
        Parameters
            file_name (String) : destination file.
                table (List): Inventory data appended through out the script
        Returns: None 
        #-----------------Assignment 07 ----------------#
        #First I corrected my missuse of a global variable within the function. Followed
        #Laura's feedback to Assignment 06
        ASSIGNMENT 07: Modified this function to store/write data into a binary type.

        """
        objFile = open(file_name, 'wb') # Writing on a binary data type file.  #@Laura, I corrected my error from HW6
        pickle.dump(table, objFile) ### @Laura: I made the mistake of adding file_name instead of objFile and corrected!
        objFile.close() # Closing as fast as possible.
        print('Inventory saved\n')


# -- PRESENTATION (Input/Output) -- #

class IO:
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] Load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] Delete CD from Inventory\n[s] Save Inventory to file\n[x] Exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table
        Args:table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.
        Returns:  None.
        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')
        
    def data_input() :
        """
        This function request the user to input data for each CD.
        Arg: strID, intID, strTitle, stArtist. All of these entries are held
        in the internal memory of this function. THey are no global variables.
        Returns: None
        
        ASSIGNMENT 07: User Input Error Handling for ID, when user adds a non numerical ID.
         Used the following operators: while, try, break
        """
        while True:
            strID = input('Enter ID: ').strip()
            try:
                intID= int(strID)
                break
            except ValueError:
                print('Invalid ID entry, type a number\t')
        strTitle = input('What is the CD\'s title? ').strip()
        stArtist = input('What is the Artist\'s name? ').strip()
        return  [intID, strTitle, stArtist]
    
# 1. When program starts, read in the currently saved Inventory
"""
The script did not run without creating the file to store data. To avoid issues, I will start by
ensuring CDInventory.txt exists.
"""
file_name2=open('CDInventory.txt', 'a') #@Laura: I fixed this as you recommended, thanks!.
file_name2.close()

#Script starts


# 2. start main loop
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break
    # 3.2 process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled\t')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            FileProcessor.read_file(strFileName, lstTbl)
            IO.show_inventory(lstTbl)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.3 process add a CD
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist
# DONE move IO code into function, Calling the add data function from DataProcessor
        DataProcessor.add_data()
        continue # start loop back at top.
    # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.5 process delete a CD
    elif strChoice == 'd':
        # 3.5.1 get Userinput for which CD to delete
        # 3.5.1.1 display Inventory to user
        IO.show_inventory(lstTbl)
        # 3.5.1.2 ask user which ID to remove
        intIDDel = int(input('Which ID would you like to delete? ').strip())
        # 3.5.2 search thru table and delete CD
# DONE moved processing code into function
        DataProcessor.delete_data(intIDDel)
        continue  # start loop back at top.
    # 3.6 process save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstTbl)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
# DONE Called the function write_file from the Class "FileProcessor"
            FileProcessor.write_file(strFileName, lstTbl) # 3.6.2.1 save data
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')